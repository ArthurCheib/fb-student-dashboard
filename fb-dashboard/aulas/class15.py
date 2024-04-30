#### Operações Clássicas com DataFrame (i) ####

## Importando nossa biblioteca
import pandas as pd

## Lendo nossos dados
gapminder = pd.read_csv('gapminder.csv')

#### (1) Criando Colunas ####

# Método 1
gapminder['total_gdp'] = gapminder['gdpPercap'] * gapminder['pop']

# Método 2: aplicando uma função em cada elemento da coluna
def categorize_life_exp(life_exp):
    if life_exp < 50:
        return 'Baixa'
    elif life_exp < 70:
        return 'Média'
    else:
        return 'Alta'

# Uma função que podemos criar
gapminder['lifeExp_cat'] = gapminder['lifeExp'].apply(categorize_life_exp)

# Uma função existente
import numpy as np
gapminder['gdpPercap'].apply(np.log)

#### (2) Ordenando o DataFrame ####
gapminder_recent = gapminder.sort_values('year', ascending=False)
gapminder_recent

# Método 1: somente expectativa de vida alta
gapminder[gapminder['lifeExp_cat'] == 'Alta']
