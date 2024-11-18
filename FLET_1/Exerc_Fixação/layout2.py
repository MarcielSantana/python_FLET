import flet as ft


def main(page: ft.Page):
    texto1 = ft.TextField(label='Digite aqui')
    btn_enviar = ft.ElevatedButton('Enviar')
    linha = ft.Row(
        controls=[texto1, btn_enviar],
        alignment=ft.MainAxisAlignment.START
    )

    page.add(linha)


ft.app(target=main)
