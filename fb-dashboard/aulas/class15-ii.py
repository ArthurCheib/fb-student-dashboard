#### Operações Clássicas com DataFrame (iii) ####


## Importando nossa biblioteca
import pandas as pd

## Lendo nossos dados
gapminder = pd.read_csv('gapminder.csv')

## (4) Joining/Merging Data

# Dados adicionais
data = {
    'country': ['Brazil', 'Argentina', 'Uruguay'],
    'copas': [5, 3, 2],
}
additional_data = pd.DataFrame(data)

# Joining/Merging o gapminder com o novo DataFrame, additional_data
merged_df = pd.merge(gapminder, additional_data,
                     on='country',
                     how='left')


## (5) Concatenando Tabelas

# Criando algumas tabelas fictícias

df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
})

df3 = pd.DataFrame({
    'A': [9, 10],
    'C': [11, 12]
})

# Concatenando df1, df2, df3
concat_df = pd.concat([df1, df2, df3], ignore_index=True)


