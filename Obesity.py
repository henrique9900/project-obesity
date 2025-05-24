import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#carregando o arquivo
df_obesity = pd.read_csv("obesity_cleaned.csv")

#convertendo os dados para to_numeric
df_obesity['Obesity (%)'] = pd.to_numeric(df_obesity['Obesity (%)'].str.split(' ').str[0], errors='coerce')


#- Qual o percentual médio de obesidade por sexo no mundo no ano de 2015?
df_2015 = df_obesity[df_obesity["Year"] == 2015] #fintrando primeiro os dados de 2015
df_2015.groupby("Sex")["Obesity (%)"].mean() # valores que quero extrair atraves do dataframe 2015 e usando o groupby


# Quais são os 5 países com a maior e a menor taxa de aumento nos índices de obesidade no período observado?
#filtrando por onde os dados devem começar usando o .index
df_obesity_start = df_obesity[df_obesity.index == 1975]
df_obesity_end = df_obesity[df_obesity.index == 2016]

df_obesity_start.set_index("Country", inplace=True)
df_obesity_end.set_index("Country", inplace=True)
df_obesity_ev = df_obesity_end[df_obesity_end["Sex"] == "Both sexes"["Obesity (%)"]]


# Quais os países com maiores e menores níveis percetuais de obesidade em 2015?

df_2015 = df_obesity[df_obesity["Year"] == 2015]
df_2015[df_2015["Obesity (%)"] == df_2015["Obesity (%)"].max()]

#Qual a diferença média percentual de obesidade entre sexos ao longo dos anos para o Brasil?
df_brazil = df_obesity[df_obesity["Country"] == "Brazil"]
female = df_brazil[df_brazil["Sex"] == "Female"]["Obesity (%)"].reset_index(drop=True)
male = df_brazil[df_brazil["Sex"] == "Male"]["Obesity (%)"].reset_index(drop=True)
(female - male).plot()

#Você conseguiria plotar um gráfico mostrando a evolução da obesidade para ambos sexos no mundo?
df_both = df_obesity[df_obesity["Sex"] == "Both sexes"]
df_both.groupby("Year")["Obesity (%)"].mean().plot()
df_both.plot()

