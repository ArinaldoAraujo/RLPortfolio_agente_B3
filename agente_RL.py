import pandas as pd
from rlportfolio.environment import PortfolioOptimizationEnv


# dataframe with training data (market price time series)
df_train = pd.read_csv("dados_historicos_final.csv")


#df_train.set_index('date') # redefinindo o index porque precisa ser uma data
#print ("INDEX")
#print (df_train.index)


environment = PortfolioOptimizationEnv(
        df_train, # data to be used
        100000    # initial value of the portfolio
    )


#from rlportfolio.algorithm import PolicyGradient
#from rlportfolio.policy import EI3

#algorithm = PolicyGradient(environment, policy=EI3)


# train the algorithm for 10000 steps
#algorithm.train(10000)
#print("ATE AQUI RODOU")

# dataframe with testing data (market price time series)
#df_test = pd.read_csv("trainTT_data.csv")

#environment_test = PortfolioOptimizationEnv(
#        df_test, # data to be used
#        100000   # initial value of the portfolio
#    )

# test the agent in the test environment
#algorithm.test(environment_test)
