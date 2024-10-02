import random
import flet as ft
import pandas as pd
import os

# Verifica se o arquivo existe
caminho_arquivo = 'C:/Users/joaom/OneDrive/Documentos/pp/DBFILMES.xlsx'
if not os.path.exists(caminho_arquivo):
    print("O arquivo não foi encontrado.")
    dataf = pd.DataFrame(columns=['filme'])  # Cria um DataFrame vazio
else:
    try:
        dataf = pd.read_excel(caminho_arquivo, engine='openpyxl')
    except Exception as e:
        print(f"Erro ao carregar o arquivo Excel: {e}")
        dataf = pd.DataFrame(columns=['filme'])  # Inicializa um DataFrame vazio se houver erro

def sorteio(e):
    if not dataf.empty:
        escolhido = random.choice(dataf['filme'].tolist())
        resultado.value = f'O filme escolhido foi o: {escolhido}'
        resultado.update()
    else:
        resultado.value = 'Nenhum filme disponível para sorteio'
        resultado.update()

def adcfilme(e):
    global dataf
    filmenovo = input_filme.value
    if filmenovo:
        novo_filme = pd.DataFrame({'filme': [filmenovo]})
        dataf = pd.concat([dataf, novo_filme], ignore_index=True)
        dataf.to_excel(caminho_arquivo, index=False)  # Caminho completo
        input_filme.value = ''
        input_filme.update()
        atualizarlista()

def deletar_filmes(e):
    global dataf
    filmes_a_deletar = [cb.label for cb in checkboxes if cb.value]
    if filmes_a_deletar:
        dataf = dataf[~dataf['filme'].isin(filmes_a_deletar)]
        dataf.to_excel(caminho_arquivo, index=False)  # Caminho completo
        atualizarlista()
    else:
        print("Nenhum filme selecionado para deletar.")

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
    global resultado, input_filme, lista_filmes, checkboxes

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
