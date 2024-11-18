import flet as ft


def main(page: ft.Page):
    def botao_clicado(event):
        texto_click = ft.Text('Você clicou no botão')
        page.add(texto_click)

    texto = ft.Text('Olá Mundo')
    botao = ft.ElevatedButton('Clique aqui', on_click=botao_clicado)
    campo_digitar = ft.TextField(label='Digite aqui')
    concordar = ft.Checkbox('Concordo com os termos do documento')
    deslizar = ft.Slider(min=0, max=100, value=20)

    lista_suspensa = ft.Dropdown(
        options=[
            ft.dropdown.Option('Opção 1'),
            ft.dropdown.Option('Opção 2'),
            ft.dropdown.Option('Opção 3')
        ]
    )

    radios = ft.RadioGroup(content=ft.Column([
        ft.Radio(value='Vermelho', label='Vermelho'),
        ft.Radio(value='Azul', label='Azul'),
        ft.Radio(value='Verde', label='Verde'),
        ft.Radio(value='Preto', label='Preto')]))

    page.add(texto, botao, campo_digitar, concordar, deslizar,
             lista_suspensa, radios)


ft.app(target=main)
