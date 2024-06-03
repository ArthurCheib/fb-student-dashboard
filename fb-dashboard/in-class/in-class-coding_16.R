## IN-CLASS CODING 16-17 ##

## Libraries
library(tidyverse)

## Dados
veiculos <- read_csv('vehicles.csv')
pessoas <- read_csv('people.csv')
acidentes <- read_csv('crashes.csv')

# Questão 1
# Calcule o número médio de passageiros envolvidos em acidentes para cada tipo de veículo (VEHICLE_TYPE)
# e visualize os resultados usando um gráfico de barras.

# Questão 2
# Descubra quais as condições climáticas (WEATHER_CONDITION) mais comumente associadas
# a acidentes graves e visualize a frequência usando um gráfico de barras.

# Questão 3
# Analise a relação entre os limites de velocidade postados (POSTED_SPEED_LIMIT)
# e a frequência de acidentes. Crie um gráfico de dispersão para visualizar essa relação.

# Questão 4
# Visualize a distribuição etária dos motoristas (AGE)
# envolvidos em acidentes usando um histograma.

# Questão 5
# Volvo vs. Jaguar vs. Tesla: motoristas de quais marcas de carros estão mais envolvidos em acidentes? Qual a faixa etária média dos motoristas de cada marca?

# Questão 6
# Em quais condiçõees climáticas, em 2023, acidentes envolvendo bicicletas normalmente acontecem?

## Questão 7
# Qual o pior lado da rua para ciclistas?
# Dica: a coluna FIRST_CONTACT_POINT indica o primeiro ponto de contato do veículo com o ciclista.

# Questão 8
# Realize uma análise temporal do número de acidentes ao longo dos anos. Crie um gráfico de linhas mostrando a tendência dos acidentes por ano.

