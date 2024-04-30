#### Operações Clássicas com DataFrame (iv) ####

# Biblioteca
import pandas as pd 

# Leitura dos dados
pop_data = pd.read_csv('population_data.csv')
country_data = pd.read_csv('country_data.csv')
gdp_life_data = pd.read_csv('gdp_life_data.csv')

## Pivoteando o dataset
# Transforma as colunas em linhas, exceto a coluna 'country'
pop_data_longer = pop_data.melt(id_vars=['country'], var_name='year', value_name='population')

## Limpeza da coluna 'year'
# Removebdo o prefixo 'yr_' da coluna 'year' e convertendo toda a coluna para int
pop_data_longer['year'] = pop_data_longer['year'].str.replace('yr_', '').astype(int)

## Juntando os datasets
# Realizando um left join do gdp_life_data com pop_data_longer
gapminder = pd.merge(gdp_life_data, pop_data_longer, on=['country', 'year'], how='left')

# Realizando um left join do resultado anterior com country_data
gapminder = pd.merge(gapminder, country_data, on='country', how='left')
