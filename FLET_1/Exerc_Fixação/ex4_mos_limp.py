import flet as ft


def main(page: ft.Page):
    texto = ft.Text('Mensagem exibida com sucesso!', visible=False)

    def mostrar(event):
        texto.visible = True
        page.add(texto)

    def ocultar(event):
        texto.visible = False
        page.add(texto)

    btn_mostrar = ft.ElevatedButton('Mostrar', on_click=mostrar)

    btn_ocultar = ft.ElevatedButton('Ocultar', on_click=ocultar)

    page.add(btn_mostrar, btn_ocultar)


ft.app(target=main)
