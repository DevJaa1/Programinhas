import flet as ft
import pandas as pd
import datetime


tchau = pd.read_excel('C:/Users/joaom/OneDrive/Área de Trabalho/pp/cadastro.xlsx', engine='openpyxl')


def main(page: ft.Page):

    page.window_width = 500
    page.window_height = 1000
    page.update()

    def info (e):        

        t.value = {nome.value}, {Datanas.value}, {sex.value}, {estadocivil.value}, {telefone.value},{cpf.value}, {idade.value}
        page.update()


    def savedados(e):

        datafdeletados = {
            'Nome': nome.value,
            'Data de Nascimento':Datanas.value,
            'Gênero': sex.value,
            'Telefone': telefone.value,
            'Estado Civil': estadocivil.value,
            'Idade': idade.value,
            'CPF': cpf.value,
         
        }
        df_nova = pd.DataFrame([datafdeletados])
        
        global tchau
        tchau = pd.concat([tchau,df_nova], ignore_index=True)
        tchau.to_excel('C:/Users/joaom/OneDrive/Área de Trabalho/pp/cadastro.xlsx',index=False)
      
        nome.value = ''
        Datanas.value = ''
        sex.value = None
        telefone.value = ''
        estadocivil.value = None
        idade.value = ''
        cpf.value = ''
        page.update()       
 

    
    t = ft.Text()
    nome = ft.TextField(label='Nome Completo', 
                        width=400)
    Datanas = ft.TextField(label='Data de Nascimento',
                           width=200)        
    
    sex = ft.Dropdown(label='Gênero',
                      width=220,options=[
        ft.dropdown.Option('Masculino'),
        ft.dropdown.Option('Feminino'),
        ft.dropdown.Option('Outros')
    ])

    estadocivil = ft.Dropdown(
        label='Estado Civil',
        width=220,
        options=[
                ft.dropdown.Option('Solteiro(a)'),
                ft.dropdown.Option('Casado(a)'),
                ft.dropdown.Option('Viúvo(a)'),
                ft.dropdown.Option('Divorciado(a)'),
                ft.dropdown.Option('Separado(a)'),                            
                              ])
    telefone = ft.TextField(label='Telefone de contato',
                            width=190)
    cpf = ft.TextField(label='CPF',
                       width=200)
    idade = ft.TextField(label='Idade',
                         width=80)

    btCad = ft.ElevatedButton(text='Cadastrar', on_click=savedados)    


    page.add(nome,Datanas,sex,telefone,estadocivil,idade,cpf,btCad,t)
    page.add()
ft.app(target=main)