import flet as ft

def main (page: ft.Page):

    res = ft.ResponsiveRow(
        ft.Column(col={"sm":6}, controls= [ft.Text("Coluna 1")]),
        ft.Column(col={"sm":6}, controls= [ft.Text("Coluna 2")])
        )
    pw = ft.Text(bottom=50, right=5, style='displaysmall')
    page.overlay.append(pw)

    
    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text('Coluna 1'),
                    padding=5,
                    bgcolor=ft.colors.DEEP_ORANGE,
                    col={'sm':6, 'md':4, 'xl':2},                    
                ),

                  ft.Container(
                    ft.Text('Coluna 1'),
                    padding=5,
                    bgcolor=ft.colors.RED_200,
                    col={'sm':6, 'md':4, 'xl':2},                    
                ),

                  ft.Container(
                    ft.Text('Coluna 1'),
                    padding=5,
                    bgcolor=ft.colors.GREEN_300,
                    col={'sm':6, 'md':4, 'xl':2},                    
                ),

                  ft.Container(
                    ft.Text('Coluna 1'),
                    padding=5,
                    bgcolor=ft.colors.DEEP_PURPLE_600,
                    col={'sm':6, 'md':4, 'xl':2},                    
                ),

            ]
        )
    )





ft.app(target=main)




