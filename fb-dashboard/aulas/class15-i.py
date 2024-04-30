#### Operações Clássicas com DataFrame (ii) ####

## Importando nossa biblioteca
import pandas as pd

## Lendo nossos dados
gapminder = pd.read_csv('gapminder.csv')

## (3) Agrupando resultados

# split-apply-combine

# (i) split: quebre em grupos menores
# (ii) apply: aplique a função em cada grupo
# (iii) combine: recoloque os grupos no formato do DataFrame original

# Passo-a-passo

# Passo 1: split
grouped_gapminder1 = gapminder.groupby('continent')

# Outra possibilidade (mais de um grupo)
grouped_gapminder1 = gapminder.groupby(['continent', 'year'])

# Passo 2: apply (sintaxe diferente)
df_agrupado_e_calculado = grouped_gapminder1['lifeExp'].mean()

# Agrupando por continente e calculando a média de expectativa de vida
gapminder.groupby('continent')['lifeExp'].mean()

# Agrupando por continente e ano + calculando o PIB per capita médio
gapminder.groupby(['continent', 'year'])['gdpPercap'].mean()


