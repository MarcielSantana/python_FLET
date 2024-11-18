import flet as ft


def main(page: ft.Page):
    texto = ft.TextField(label='Digite seu nome')

    def mostrar_mensagem(event):
        nome = texto.value
        texto_result = ft.Text(f'Olá {nome}!')
        page.add(texto_result)

    botao = ft.ElevatedButton('Enviar', on_click=mostrar_mensagem)

    page.add(texto, botao)


ft.app(target=main)
