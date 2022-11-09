import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

data = BeautifulSoup(open('gasolina.csv', mode='r', encoding='utf8'))

data_df = pd.read_csv('gasolina.csv')

grafico_gasolina = sns.lineplot(data=data_df, x='dia', y='venda', palette='pastel1')
grafico_gasolina.set(title='Preço médio de venda por dia', xlabel='Dia', ylabel='Valor R$');
plt.savefig('grafico_gasolina.png')
!touch gasolina.py