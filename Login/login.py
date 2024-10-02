import flet as ft
import pandas as pd


#chau = pd.read_excel('C:/Users/joaom/OneDrive/Área de Trabalho/pp/cadastro.xlsx', engine='openpyxl') (por algum motivo esta com erro informando que nao esta instalado a biblioteca OpenPy ENT N SEI OQ TA ACONTECENDO )


def main(page: ft.Page):

    page.window_width = 600
    page.window_height = 1000
    page.update()


    login = ft.Column([
        ft.Container(
            bgcolor=ft.colors.BLACK45,
            width=page.window_width - 10,
            height=page.window_height - 60,
            border_radius=10,
        

            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE60,
                    width=320,
                    height=400,
                    border_radius=10,

                    content=ft.Column([
                        ft.Text(
                            value='Portal Login',
                            weight='italic',
                            size=40,
                            font_family='Cream Cake',
                            color=ft.colors.BLACK
                        ),
                        

                        ft.TextField(
                        hint_text='Usuário',
                        width=270,
                        height=45,
                        border_radius=40,
                        prefix_icon= ft.icons.PERSON,
                        text_vertical_align=1,
                
                        ),
                        
                        ft.TextField(
                        hint_text='Senha',
                        width=270,
                        height=45,
                        border_radius=40,
                        prefix_icon= ft.icons.LOCK_OUTLINE,
                        text_vertical_align=1,
                        password=True,
                        can_reveal_password=True,
                        keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                        ),

                        
                        ft.ElevatedButton(text='Entrar',
                                              color=ft.colors.GREEN,
                                              width=270,
                                              height=30),

                        ft.Row([
                            ft.TextButton('Cadastrar',
                                          ),
                            ft.TextButton('Recuperar conta'),


                    ],width=300,
                    alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.IconButton(icon=ft.icons.EMAIL,
                                      icon_color='black'),
                        ft.IconButton(icon=ft.icons.TELEGRAM,
                                      icon_color='black'),
                        ft.IconButton(icon=ft.icons.FACEBOOK,
                                      icon_color=ft.colors.BLACK)
                    ], alignment=ft.MainAxisAlignment.CENTER)
                        

                    ],spacing=20, horizontal_alignment='center')
),

            ],horizontal_alignment ='center',alignment='center')

        )
    ])
    
    page.add(login)

ft.app(target=main)