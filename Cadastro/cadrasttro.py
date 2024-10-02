import pandas as pd



dataf = pd.read_excel('dadosP.xlsx', engine='openpyxl')


def mostrar_menu():

    print(50*'*')
    print(5*'*','Sistema de cadastro ultilizando pandas', 5*'*')
    print('Digite 1 para CADASTRO: ')
    print('Digite 2 para BUSCAR USUÁRIO: ')
    print('Digite 3 para ENCERRAR O SISTEMA: ')
    print(50*'*')


def user (usuario):

    nome = input('Nome completo: ')
    Datanas = input('Data de Nascimento: ')
    sex = input('Sexo: ')
    estadocivil = input('Estado Civil: ')
    telefone = input('Telefone: ')
    cpf = input('CPF: ')
    es_cidade = input('Estado/Cidade: ')
    idade = input('Idade: ')

    dados = {

    'nome': nome,
    'Datanas': Datanas,
    'sex': sex, 
    'estadocivil': estadocivil, 
    'telefone': telefone,
    'cpf': cpf,
    'es_cidade':es_cidade, 
    'idade': idade,

    }
    usuario.append(dados)
    print('Usuário cadastrado com sucesso!')

def list_user (usuario):

    if len(usuario) == 0:
        print('Nenhum usuário encontrado!')
    else:
        for i, dados in enumerate(usuario):
            print(f'Usuário {i+1}:')
            print(f'Nome: {dados['nome']}')
            print(f'Data: {dados['Datanas']}')
            print(f'Genêro: {dados['sex']}')
            print(f'Estado Civil: {dados['estadocivil']}')
            print(f'Telefone: {dados['telefone']}')
            print(f'CPF: {dados['cpf']}')
            print(f'Estado/Cidade: {dados['estadocivil']}')
            print(f'Idade: {dados['idade']}')
            print()
def sis ():

    usua = []

    while True:
        mostrar_menu()
        op = input('Insira a opção desejada: ')

        if op == '1':
            user(usua)
        elif op == '2':
            list_user(usua)
        elif op == '3':
            print('Encerrando programa!')
            break
    
    if usua:
        novos_dados = pd.DataFrame (usua)
        novo_dado = pd.concat ([dataf, novos_dados],ignore_index=True)
        novo_dado.to_excel('dadosP.xlsx', index=False)
        print('Dados salvos no arquivo (DADOSP.XLSX) com sucesso! ')

sis()

