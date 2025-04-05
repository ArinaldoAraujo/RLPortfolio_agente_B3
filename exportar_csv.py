import pandas as pd
import yfinance as yf

CARTEIRA_BRL = [
    "VALE3.SA", "PETR4.SA", "ITUB3.SA", "BBDC4.SA",
    "BBAS3.SA", "RENT3.SA", "LREN3.SA", "PRIO3.SA",
    "WEGE3.SA", "ABEV3.SA"
]

#dados_historicos2 =0

for i in range(10):
	acao = yf.Ticker(CARTEIRA_BRL[i])
	#dados_historicos = acao.history(start="2015-01-01" , end="2015-02-11")
	if i==0:
		dados_historicos = acao.history(start="2011-01-01" , end="2022-12-31")
	#	dados_historicos = acao.history(start="2011-01-01" , end="2011-01-31")
		dados_historicos['tic'] = CARTEIRA_BRL[i] #adiciona a coluna tic
	#	print(dados_historicos)
	else:
		dados_historicos2 = acao.history(start="2011-01-01" , end="2022-12-31")	
	#	dados_historicos2 = acao.history(start="2011-01-01" , end="2011-01-31")	
		dados_historicos2['tic'] = CARTEIRA_BRL[i]
	#dados_historicos['Date'].dt.date
	#dados_historicos['Date'] = dados_historicos['Date'].dt.date
	
		dados_historicos = dados_historicos._append(dados_historicos2, ignore_index=False) #adiciona um dataframe ao ja existente
	  # dados_historicos['tic'] = CARTEIRA_BRL[i]
	#	print(dados_historicos)
		#print(i)

dados_historicos = dados_historicos.drop(['Open', 'Volume', 'Dividends', 'Stock Splits'], axis = 1) # remove as colunas desnecessárias
#dados_historicos = dados_historicos.rename(columns={'Date': 'date','High': 'high','Low': 'low','Close': 'close' })# renomeia as colunas
#dados_historicos.columns =['date','high','low', 'close' ] # renomeia as colunas

	
	
#dados_historicos['Date'] = pd.to_datetime(dados_historicos['Date']).dt.normalize()
   
	
	#df['datetime_column'].dt.date
	
	
	#ticket = CARTEIRA_BRL[i]
	#pd_dados_historicos = pd.DataFrame(dados_historicos)
	#address = ['A', 'B', 'C','A', 'B', 'C']
#	dados_historicos['tic'] = CARTEIRA_BRL[i] # adiciona a coluna tic no dataframe
#	print(acao)
#print(dados_historicos)
	#dados_historicos2 = pd.concat([dados_historicos2,dados_historicos]) 
	
	#result = pd.concat([df1, df2])
	

#dados_historicos = ptr.history(period="max")

#dados_historicos.to_csv('test_data.csv')
print("Dados historicos")
print(dados_historicos)
print(dados_historicos.index)

# Para várias ações
#acoes = yf.download("VALE3.SA PETR4.SA ", start="2010-01-01" , end="2010-01-07")
#dados_historicos = acoes.history(period="max", group_by='Date')

dados_historicos.to_csv('dados_historicos_inicial.csv')
#dados_historicos.to_csv('dados_historicos_inicial.csv', index=None)

#df_train = pd.read_csv("dados_historicos_inicial.csv", sep = ',', parse_dates= ['Date'],encoding='utf-8-sig', usecols= ['Date'],)
df_train = pd.read_csv("dados_historicos_inicial.csv")

#df_train['Date'] = pd.to_datetime(df_train['Date']).dt.normalize()
df_train = df_train.rename(columns={'Date': 'date','High': 'high','Low': 'low','Close': 'close' })# renomeia as colunas


#df_train['date'].dt.date
#df_train['date'] = pd.to_datetime(df_train['date']).dt.date # transforma a data para o formato correto
df_train['date'] = pd.to_datetime(df_train['date'], utc=True) # transforma a data para o formato correto
df_train['date'] = df_train.date.dt.date

df_train.sort_values(by=['date'], inplace=True)

print("ATE AQUI RODOU")

#df_train.sort_values(by=['date'], inplace=True)

df_train.to_csv('dados_historicos_final.csv', index=None)

print ('Modificado')
print (df_train['date'])

print (df_train)


index_teste = pd.read_csv("dados_historicos_final.csv")
print ('INDEX')
print (index_teste.index)







#print(acoes)
