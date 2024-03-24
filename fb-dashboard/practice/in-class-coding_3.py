#### In-class Coding 3.0 ####
## Sobre o Programa a ser criado:
# Programa de cadastro e gestão dos usuários da
# biblioteca da Faculdade Belavista
    

## PARTE 1 ##

# INPUTS:

# (a) Faça um programa que obtenha três informações
#     do novo usuário da biblioteca: 
    
#       (i) nome completo do aluno   
#       (ii) e-mail belavista do aluno
#       (iii) data de nascimento do aluno


## Obtendo o nome do usuário
nome_completo = input('Insira seu nome: ')
email_aluno = input('Insira seu e-mail Belavista: ')
data_nasc = input('Insira sua data de nascimento: ')


# OUTPUTS:

# (b) Continue codando seu programa - faça com que ele
#     retorne uma mensagem de boas-vindas que contenha:
    
#      (i) Saudação que utilize o primeiro nome do aluno

#      (ii) Informação do email de biblioteca do aluno,
#           que é igual ao email belavista, mas substituindo-se
#           o @belavista.edu.org por @bibliotecafb.edu.org

#      (iii) Senha inicial do aluno - a senha deve conter
#            dois caracteres do nome do aluno, o mês de
#            nascimento do aluno e deve terminar com '_fb2024'         

## Output (i)
primeiro_nome = nome_completo.split(' ')
print(f'Olá, {primeiro_nome}, seja bem-vindo à biblioteca da Belavista')

## Output (ii)
email_biblioteca = email_aluno.replace('belavista',
                                       'bibliotecafb')
print('Seu e-mail biblioteca é: {email_biblioteca}')

## Output (iii)
print(f'Sua senha temporária é: {primeiro_nome[0:2]}_{data_nasc[3:5]}_fb2024')


## PARTE 2 ##

# TORNE O CÓDIGO UMA FUNÇÃO

def registra_usuario(nome, email, data):
    
    ## Obtendo os três inputs necessários
    nome_completo = nome
    email_aluno = email
    data_nasc = data
    
    ## Devolvendo os inputs corretos ao usuário
    # Output 1
    primeiro_nome = nome_completo.split(' ')[0]
    print(f'Olá, {primeiro_nome}, seja bem-vindo à biblioteca da Belavista')

    # Output 2
    email_biblioteca = email_aluno.replace('faculdadebelavista',
                                           'bibliotecafb')
    
    print(f'Seu e-mail biblioteca é: {email_biblioteca}')

    # Output 3
    print(f'Sua senha temporária é: {primeiro_nome[0:2]}_{data_nasc[3:5]}_fb2024')


registra_usuario(nome = 'Arthur Cheib',
                 email = 'arthur.cheib@faculdadebelavista.edu.br',
                 data = '22/08/1992')
