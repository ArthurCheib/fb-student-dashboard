## IN-CLASS CODING 15 ##

## Libraries
library(tidyverse)
library(nycflights13)

## Data
data(flights)

## Exercise 1
# Selecione aleatoriamente 100 voos do conjunto de dados `flights`, 
# e calcule a média do atraso na chegada (`arr_delay`) para cada companhia aérea (`carrier`).
# Observação: rode o código ao menos 3x e repare na diferença entre os resultados
flights |> 
  slice_sample(n = 3336) |> 
  group_by(carrier) |> 
  summarize(mean_delay = mean(arr_delay, na.rm = TRUE)) |> 
  left_join(flights |> 
              group_by(carrier) |> 
              summarize(mean_delay = mean(arr_delay, na.rm = TRUE)),
            by = 'carrier')

## Exercise 2
# Encontre os 5 destinos (`dest`) com o maior número de voos distintos (`flight`), 
# e para esses destinos, calcule a média do tempo de voo (`air_time`).
flights |> 
  group_by(dest) |> 
  summarize(total_voos = n_distinct(flight),
            avg_air_time = mean(air_time, na.rm = TRUE)) |> 
  slice_max(total_voos, n = 5)

## Exercise 3
# Preencha valores ausentes na coluna `dep_delay` com o valor 0, 
# e calcule a média do atraso na partida (`dep_delay`) para cada mês (`month`).


## Método 1
flights |> 
  select(dep_delay)

## Método 2
flights |> 
  pull(dep_delay)

## Método
flights$dep_delay
flights[ ,c(1,2)]

## Exercise 4
# Detecte a presença da letra 'A' na coluna `dest`, 
# e crie uma nova coluna `contains_A` que armazene TRUE ou FALSE. 
# Em seguida, filtre para manter apenas os voos onde `contains_A` é TRUE.


## Exercise 5
# Conte o número de voos por companhia aérea (`carrier`) usando a função `count`
# e crie um gráfico de barras simples mostrando o número de voos por companhia, para todas
# aquelas companhias que fizeram mais de 15k voos em 2013.
