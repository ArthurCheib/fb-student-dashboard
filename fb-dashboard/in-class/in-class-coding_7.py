#### In-class Coding 7 ####

## Sobre o Programa a ser criado:
# Programa de cadastro e gestão dos usuários e livros da
# biblioteca da Faculdade Belavista

# Até aqui, é necessário que todos tenham ao menos duas funções:
# (i) Uma função para registrar usuários
# (ii) Uma função para registrar livros

## PARTE 1 - Upgrading da função que registra usuários ##

# (a) Adicione um loop que siga requisitando o email do
#     usuário enquanto um e-mail correto não for compartilhado

# (b) Após cadastrar usuário, pergunte ao usuário
#     se ele deseja realizar outro cadastro.
#     Se sim, repita o processo; se não, encerre o programa.












## PARTE 2 - Upgrading da função que registra livros ##

# (a) Adicione um loop que siga requisitando o gênero do livro
#     usuário enquanto ele não fornecer um tipo válido.

# (b) Após cadastrar um livro, pergunte ao usuário
#     se ele deseja realizar outro cadastro.
#     Se sim, repita o processo; se não, encerre o programa.


    
    

    nome_livro = input('Insira o nome do livro: ')
    autor_livro = input('Insira o autor do livro: ')
    genero_livro = input('Insira o gênero do livro: ')
    
    generos_validos = ['Romance', 'Ficção Científica', 'Mistério', 'Fantasia', 'Biografia']
    if genero_livro not in generos_validos:
        genero_livro = 'Geral'

    print(f'O livro inserido é: {nome_livro.title()}')
    print(f'O autor do livro inserido é: {autor_livro.upper()}')
    print(f'O gênero do livro inserido é: {genero_livro}')
    print('O código único do livro é: 0001')

registrar_livro()