#### Operações Clássicas com DataFrame (ii) ####

## Importando nossa biblioteca
import pandas as pd

## Dataset
gapminder = pd.read_csv('gapminder.csv')

## DESAFIO 1 ##

## Qual é a expectativa de vida média por continente em 2007?
gapminder_2007 = gapminder[gapminder['year'] == 2007]
avg_life_exp_by_continent = gapminder_2007.groupby('continent')['lifeExp'].mean()







## Como o PIB per capita mudou ao longo do tempo para os
#  países do BRICS (Brasil, Rússia, Índia, China, África do Sul)?

brics_countries = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
brics_data = gapminder[gapminder['country'].isin(brics_countries)]

# Cria um gráfico de linha do PIB per capita ao longo do tempo para cada país
import matplotlib.pyplot as plt

for country in brics_countries:
    country_data = brics_data[brics_data['country'] == country]
    plt.plot(country_data['year'], country_data['gdpPercap'], label=country)

plt.xlabel('Year')
plt.ylabel('GDP per capita')
plt.title('GDP Per Capita Over Time for BRICS Countries')
plt.legend()
plt.show()







## Qual país teve a maior variação no PIB per capita entre 1952 e 2007?
# PIB per capita inicial e final
gdp_start = gapminder[gapminder['year'] == 1952].set_index('country')['gdpPercap']
gdp_end = gapminder[gapminder['year'] == 2007].set_index('country')['gdpPercap']

# Calcula a diferença
gdp_change = (gdp_end - gdp_start).dropna()
max_gdp_change_country = gdp_change.idxmax()
max_gdp_change_value = gdp_change.max()



## Qual continente teve o maior crescimento populacional médio entre os anos disponíveis?
# Calcula o crescimento populacional médio por continente
avg_population_growth = gapminder.groupby('continent').apply(
    lambda x: (x['pop'].iloc[-1] - x['pop'].iloc[0]) / x['pop'].iloc[0]
)
max_growth_continent = avg_population_growth.idxmax()
max_growth_value = avg_population_growth.max()

print(f"Continent with the highest average population growth: {max_growth_continent} with a growth of {max_growth_value}")





## Quais países possuem uma "alta" expectativa de vida mas um PIB per capita abaixo da média mundial em 2007?
data_2007 = gapminder[gapminder['year'] == 2007]

# Média mundial do PIB per capita para 2007
global_gdp_avg = data_2007['gdpPercap'].mean()

# "alta" expectativa de vida como acima da mediana
median_life_exp = data_2007['lifeExp'].median()

# Filtra os países com alta expectativa de vida e PIB per capita abaixo da média mundial
high_life_low_gdp = data_2007[(data_2007['lifeExp'] > median_life_exp) & (data_2007['gdpPercap'] < global_gdp_avg)]
print(high_life_low_gdp[['country', 'lifeExp', 'gdpPercap']])







## Quais são os top 5 países em termos de expectativa de vida em 2007?
top_5_life_exp = gapminder_2007.sort_values(by='lifeExp', ascending=False).head(5)
print(top_5_life_exp[['country', 'lifeExp']])







## Quais países apresentaram uma redução na expectativa de vida de um ano para o outro?
country_life_exp = gapminder.pivot_table(index='year', columns='country', values='lifeExp')

# Calcula a diferença anual na expectativa de vida
life_exp_diff = country_life_exp.diff()

# Encontra os anos e países onde houve redução na expectativa de vida
life_exp_reduction = life_exp_diff[life_exp_diff < 0].stack()
print(life_exp_reduction)







## Agrupe os países em categorias de PIB per capita (baixo, médio, alto)
# e analise a média da expectativa de vida em cada categoria para 2007.


## DESAFIO 2 ##

# Melhorando nosso dataset!


## DESAFIO 3 - R! ##

## Questões de Gráfico:
## (1) Existe uma correlação entre PIB per capita e expectativa de vida em 2007?

## (2) Como a distribuição da expectativa de vida mudou de 1952 a 2007?