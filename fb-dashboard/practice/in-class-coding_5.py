#### In-class Coding 5 ####

## Sobre o Programa a ser criado:
# Programa de cadastro e gestão dos usuários e livros da
# biblioteca da Faculdade Belavista

## PARTE 1 - Validação de Dados do Usuário ##

# (a) Adicione uma validação para o e-mail do usuário. 
#     O e-mail deve terminar com "@faculdadebelavista.edu.br". 
#     Se não terminar, peça ao usuário para inserir um e-mail válido.

def validar_email(email):
    return email.endswith("@faculdadebelavista.edu.br")

def registra_usuario():
    ## Obtendo os três inputs necessários
    nome_completo = input('Insira seu nome completo: ').title()
    email_aluno = input('Insira seu email: ')
    data_nasc = input('Insira sua data de nascimento: ')
    
    ## Devolvendo os inputs corretos ao usuário
    # Output 1
    primeiro_nome = nome_completo.split(' ')[0]
    print(f'Olá, {primeiro_nome}, seja bem-vindo à biblioteca da Belavista')

    # Output 2
    if validar_email(email_aluno):
        email_biblioteca = email_aluno.replace('faculdadebelavista',
                                               'bibliotecafb')
    
    print(f'Seu e-mail biblioteca é: {email_biblioteca}')

    # Output 3
    print(f'Sua senha temporária é: {primeiro_nome[0:2]}_{data_nasc[3:5]}_fb2024')
    
    ## LOOP

registra_usuario()

## PARTE 2 - Confirmação de Cadastro ##

# (b) Após cadastrar um livro ou usuário, pergunte ao usuário
#     se ele deseja realizar outro cadastro.
#     Se sim, repita o processo; se não, encerre o programa.



## PARTE 3 - Atualização da Validação de Gênero ##

# (c) Modifique a validação do gênero do livro para garantir
#     que ele esteja dentro de uma lista pré-definida de gêneros
#     aceitáveis. Se não estiver, atribua um gênero padrão 'Geral'

def registrar_livro():

    ## Inputs do usuário
    nome_livro = input('Insira o nome do livro: ')
    autor_livro = input('Insira o autor do livro: ')
    genero_livro = input('Insira o gênero do livro: ')
    
    ## Checagem da validade do gênero inserido
    generos_validos = ['Romance', 'Ficção Científica', 'Mistério', 'Fantasia', 'Biografia']
    if genero_livro not in generos_validos:
        genero_livro = 'Geral'

    print(f'O livro inserido é: {nome_livro.title()}')
    print(f'O autor do livro inserido é: {autor_livro.upper()}')
    print(f'O gênero do livro inserido é: {genero_livro}')
    print('O código único do livro é: 0001')

registrar_livro()
