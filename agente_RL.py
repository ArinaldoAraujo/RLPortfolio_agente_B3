import warnings
warnings.filterwarnings("ignore", message=" Could not initialize NNPACK!")

import pandas as pd
import sys
sys.path.append("..")

from rlportfolio.environment import PortfolioOptimizationEnv
from rlportfolio.algorithm import PolicyGradient, EpisodicPolicyGradient
from rlportfolio.policy import EI3


# dataframe with training data (market price time series)
df_train = pd.read_csv("dados_historicos_final.csv")
print("Colunas Disponiveis:", df_train.columns.tolist() )
df_train['date'] = pd.to_datetime(df_train['date'], errors='coerce')
df_train = df_train.sort_values('date') #ordenar por data
print(df_train.head())

# dataframe with testing data (market price time series)
df_test = pd.read_csv("dados_historicos_final_teste.csv")
df_test['date'] = pd.to_datetime(df_test['date'], errors='coerce')
df_test = df_test.sort_values('date') #ordenar por data


print ("INDEX")
print (df_train.index)

#ambiente de treinamento
environment = PortfolioOptimizationEnv(
        df_train, # dataframe com a serie temporal
        initial_amount=100000,  # valor inicial do portfolio    
        state_normalization = "by_last_value",
	     comission_fee_pct= 0.0025, #custo da transação                     
        time_window = 50, # observa os ultimos x dias 
        
              
       
        features=["close", "high", "low"],
     
        plot_graphs=True, 
        cwd="./resultados_treino"
        
        
   
   )

print("Numero de elementos no dataframe treinamento: ")
num_= len(df_train["date"].unique())
print(num_)

print("Ambiente criado com sucesso!")

print("### FAZENDO ALGUNS TESTES ###")

print("Numero de ações no portfólio")
print(environment.portfolio_size)

print("Tamanho do episodio")
print(environment.episode_length)

print("Espaço de ação")
print(environment.action_space)

print("Espaço de observação")
print(environment.observation_space)

obs = environment.reset()
print("Estado inicial:", obs)

action = environment.action_space.sample()
print("Ação aleatória:", action)


print("### FIM DOS TESTES ###")

#ambiente de teste
environment_test = PortfolioOptimizationEnv(
        df_test, # data to be used
        initial_amount=100000,  # valor inicial do portfolio                 
        time_window = 50, # observa os ultimos x dias       
        comission_fee_pct= 0.0025, #custo da transação
        features=["close", "high", "low"],
    )

print("Numero de elementos no dataframe teste: ")
num = len(df_test["date"].unique())
print (num)


from rlportfolio.algorithm import PolicyGradient
from rlportfolio.policy import EI3

#algorithm = PolicyGradient(environment, policy=EI3)
algorithm = EpisodicPolicyGradient(
			environment,
			policy=EI3,
			sample_bias=0.001,
   		batch_size=200,
		   lr=5e-5,
    		action_noise="dirichlet",
    		action_epsilon=0.2,
		   action_alpha=0.01,
		   use_tensorboard=True,
		 #  device=device
)


#train the algorithm for 120 steps
#algorithm.train(10)

algorithm.train(episodes=3, val_period=10, val_gradient_steps=30, val_env=environment_test)
#algorithm.train(episodes=3, val_period=10, val_gradient_steps=30, val_env=environment)

print("ATE AQUI RODOU")

# test the agent in the test environment
print("ALGORITMO DE TESTE")
algorithm.test(environment_test)
