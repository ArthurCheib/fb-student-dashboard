#### Exercícios de Treinamento - 1 ####



## Exercício 1

# Peça ao usuário para inserir dois números. 
# Em seguida, crie uma função que realize e imprima a soma,
# subtração, multiplicação e divisão desses números.




## Exercício 2

# Solicite ao usuário que insira dois números.
# Compare os números e imprima:
# - "O primeiro número é maior" se o primeiro número for maior que o segundo.
# - "O segundo número é maior" se o segundo número for maior que o primeiro.
# - "Os números são iguais" se os números forem iguais.
# Utilize os operadores de comparação para realizar essa tarefa.




## Exercício 3

# Solicite ao usuário sua idade e converta esse valor para um inteiro.
# Verifique se a idade inserida é maior do que 18 e imprima uma mensagem indicando se o usuário é maior de idade.




## Exercício 4

# Peça ao usuário para inserir um nome e um número inteiro.
# Utilize a formatação de strings para imprimir a frase:
# "[nome] tem [número] anos de idade!", substituindo [nome] e [número] pelos valores inseridos.
# Exemplo: Se o usuário inserir "João" e 30, o programa deve imprimir "João tem 30 anos de idade!".
# Utilize f-strings para realizar a formatação.




## Exercício 5

# Peça ao usuário para inserir uma palavra.
# Se a palavra tiver mais de 5 letras, imprima "Sua palavra tem mais de 5 letras".
# Se a palavra tiver 5 letras ou menos, imprima "Sua palavra tem 5 letras ou menos".
# Utilize a função len() para determinar o comprimento da palavra.




## Exercício 6

# Crie uma função chamada classifica_aluno que recebe uma nota (inteiro ou float) como argumento.
# Dentro da função, use condicionais para classificar a nota do aluno conforme os seguintes critérios:
# - Nota maior ou igual a 70: "Aprovado"
# - Nota entre 50 e 69: "Recuperação"
# - Nota abaixo de 50: "Reprovado"
# A função deve retornar a classificação correspondente à nota.
# Teste sua função com diferentes valores de notas.




## Exercício 7

# Crie uma função chamada verifica_permissao que receba três argumentos:
    # idade;
    # tem_autorizacao_dos_pais
    # destino_viagem.
    
# A função deve verificar se uma pessoa tem permissão para
# participar de uma viagem escolar considerando o destino da viagem.

# A lógica para permissão é a seguinte:
# - Se a idade for maior ou igual a 18, a pessoa tem permissão para qualquer destino.
# - Se a idade for menor que 18 e tem_autorizacao_dos_pais for True, a pessoa tem permissão, exceto para destinos internacionais.
# - Para destinos internacionais, a pessoa deve ter mais de 15 anos, mesmo com autorização dos pais.
# - Caso contrário, a pessoa não tem permissão para participar.

# A função deve retornar "Permissão concedida" ou "Permissão negada" com base nos critérios acima.
# Teste sua função com diferentes valores e destinos.