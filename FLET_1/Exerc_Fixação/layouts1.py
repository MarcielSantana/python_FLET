import flet as ft


def main(page: ft.Page):
    texto1 = ft.Text('Texto à esquerda')
    texto2 = ft.Text('Texto à direita')
    linha = ft.Row(
        controls=[texto1, texto2],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    page.add(linha)


ft.app(target=main)
