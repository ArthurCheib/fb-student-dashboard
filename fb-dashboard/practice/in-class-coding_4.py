#### In-class Coding 4 ####

## Sobre o Programa a ser criado:
# Programa de cadastro e gestão de livros da
# biblioteca da Faculdade Belavista
    

## PARTE 1 ##

# INPUTS:

# (a) Faça um programa que obtenha três informações
#     sobre um livro a ser registrado na biblioteca: 
    
#       (i) nome completo do livro   
#       (ii) autor do livro
#       (iii) gênero do livro

nome_livro = input('Insira o nome do livro: ')
autor_livro = input('Insira o autor do livro: ')
genero_livro = input('Insira o gênero do livro: ')
            

# OUTPUTS:

# (b) Continue codando seu programa - faça com que ele
#     retorne uma mensagem contendo as seguintes infos do livro:
    
#      (i) Nome do livro (deve ser 'title-cased')

#      (ii) Nome do autor do livro (todo em caixa alta)

#      (iii) O genêro do livro. No entanto, substitua o gênero
#            do livro que foi inserido por um gênero padrão         

#      (iv) Um código numérico para o livro


# Output 1
print(f'O livro inserido é: {nome_livro.title()}')

# Output 2
print(f'O autor do livro inserido é: {autor_livro.upper()}')

# Output 3
genero_livro = genero_livro.replace('Amor', 'Romance')
genero_livro = genero_livro.replace('Paixão', 'Romance')
genero_livro = genero_livro.replace('Relacionamento', 'Romance')

genero_livro = genero_livro.replace('Sci-fi', 'Ficção Científica')
genero_livro = genero_livro.replace('Turismo', 'Ficção Científica')
genero_livro = genero_livro.replace('Tecnologia', 'Ficção Científica')

genero_livro = genero_livro.replace('Suspense', 'Mistério')
genero_livro = genero_livro.replace('Enigma', 'Mistério')
genero_livro = genero_livro.replace('Investigação', 'Mistério')

genero_livro = genero_livro.replace('Mágica', 'Fantasia')
genero_livro = genero_livro.replace('Sobrenatural', 'Fantasia')
genero_livro = genero_livro.replace('Aventura', 'Fantasia')

genero_livro = genero_livro.replace('Vida', 'Biografia')
genero_livro = genero_livro.replace('História Real', 'Biografia')
genero_livro = genero_livro.replace('Memórias', 'Biografia')

print(f'O gênero do livro inserido é: {genero_livro}')

# Output 4
print('O código único do livro é: 0001')

## PARTE 3 ##

# TRANSFORMANDO O PROGRAMA EM UMA FUNÇÃO

def registrar_livro(nome_livro, autor_livro, genero_livro):
    # Output 1
    print(f'O livro inserido é: {nome_livro.title()}')

    # Output 2
    print(f'O autor do livro inserido é: {autor_livro.upper()}')

    # Output 3
    genero_livro = genero_livro.replace('Amor', 'Romance')
    genero_livro = genero_livro.replace('Paixão', 'Romance')
    genero_livro = genero_livro.replace('Relacionamento', 'Romance')

    genero_livro = genero_livro.replace('Sci-fi', 'Ficção Científica')
    genero_livro = genero_livro.replace('Turismo', 'Ficção Científica')
    genero_livro = genero_livro.replace('Tecnologia', 'Ficção Científica')

    genero_livro = genero_livro.replace('Suspense', 'Mistério')
    genero_livro = genero_livro.replace('Enigma', 'Mistério')
    genero_livro = genero_livro.replace('Investigação', 'Mistério')

    genero_livro = genero_livro.replace('Mágica', 'Fantasia')
    genero_livro = genero_livro.replace('Sobrenatural', 'Fantasia')
    genero_livro = genero_livro.replace('Aventura', 'Fantasia')

    genero_livro = genero_livro.replace('Vida', 'Biografia')
    genero_livro = genero_livro.replace('História Real', 'Biografia')
    genero_livro = genero_livro.replace('Memórias', 'Biografia')

    print(f'O gênero do livro inserido é: {genero_livro}')

    # Output 4
    print('O código único do livro é: 0001')


