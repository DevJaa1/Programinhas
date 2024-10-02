import random    # IMPORTA O SISTEMA DE ESCOLHAS ALEATORIAS
import flet as ft  # IMPORTA A BIBLIOTECA DE INTERFACE GRÁFICA
import pandas as pd # IMPORTA A BIBLIOTECA DE BANCO DE DADOS ULTILIZADA NESSE CÓDIGO
 

# Carrega os dados do Excel
dataf = pd.read_excel('C:/Users/joaom/OneDrive/Área de Trabalho/pp/DBFILMES.xlsx', engine='openpyxl')

# FUNÇÃO QUE FAZ O SORTEIO DOS FILMES QUE FOREM ADICIONADOS NO ARQUIVO EXCEL

def sorteio(e): # FUNÇÃO DE SORTEIO
    if not dataf.empty: # SE O DATAFRAME NÃO ESTIVER VAZIO SIGINIFICA QUE ELE PODE SORTEAR O QUE TEM DENTRO 
        escolhido = random.choice(dataf['filme'].tolist()) # SORTEAR O QUE TEM DENTRO DO DATAFRAME
        resultado.value = f'O filme escolhido foi o: {escolhido}' # MOSTRA O QUE FOI SORTEADO DENTRO DO DATAFRAME
        resultado.update() # ATUALIZA A VARIAVEL RESULTADO
    else:
        resultado.value = 'Nenhum filme disponível para sorteio' # CASO CONTRATIO SE O DATAFRAME ESTIVER VAZIO INFORMAR QUE NÃO EXISTE FILME PARA SER SORTEADO
        resultado.update()
# -------------------------------------------------------------------------


def adcfilme(e): # FUNÇÃO PARA ADIOCIONAR FILME
    global dataf # CHAMA A VARIAVEL DATAF (O DATAFRAME) PARA A FUNÇÃO ADCFILME
    filmenovo = input_filme.value #
    if filmenovo:
        novo_filme = pd.DataFrame({'filme': [filmenovo]})
        dataf = pd.concat([dataf, novo_filme], ignore_index=True)
        dataf.to_excel('DBFILMES.xlsx', index=False)
        input_filme.value = ''
        input_filme.update()
        atualizarlista()

def deletar_filmes(e):
    global dataf
    filmes_a_deletar = [cb.label for cb in checkboxes if cb.value]
    if filmes_a_deletar:
        
        dataf = dataf[~dataf['filme'].isin(filmes_a_deletar)]
        dataf.to_excel('DBFILMES.xlsx', index=False)
        atualizarlista()


def atualizarlista():
    global checkboxes
    lista_filmes.controls.clear()
    checkboxes = []
    for i in dataf['filme']:
        checkbox = ft.Checkbox(label=i)
        checkboxes.append(checkbox)
        lista_filmes.controls.append(checkbox)
    
    lista_filmes.update()

def janela(page: ft.Page):
    global resultado, input_filme, lista_filmes, dataf, checkboxes, deletados

    page.appbar = ft.AppBar(
        title=ft.Text(
            "R O L E T A  D O  F I L M E",
            style=ft.TextStyle(
                font_family='Berlin Sans FB',
                size=30,
                weight='w400',
            ),
        ),
        center_title=True,
        bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
    )

    input_filme = ft.TextField(label='Novo Filme')
    bot_adc = ft.ElevatedButton(text='Adicionar Filme', on_click=adcfilme)

    input_container = ft.Container(
        content=ft.Column([input_filme, bot_adc]),
        alignment=ft.alignment.center,
        padding=50
    )

    lista_filmes = ft.Column()

    resultado = ft.Text('')

    page.title = 'Sorteador de Filmes'
    page.window_width = 400
    page.window_height = 1025

    botsort = ft.ElevatedButton(text='Sortear Filme', on_click=sorteio)
    bot_del = ft.ElevatedButton(text='Deletar Filme', on_click=deletar_filmes)

    caixadobot = ft.Container(
        content=ft.Column([botsort, bot_del]),
        alignment=ft.alignment.center,
        padding=50
    )


    page.add(input_container)
    page.add(lista_filmes)
    page.add(caixadobot)
    page.add(resultado)

    atualizarlista()

ft.app(target=janela)
