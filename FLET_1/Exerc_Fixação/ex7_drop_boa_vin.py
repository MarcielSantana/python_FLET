import flet as ft


def main(page: ft.Page):
    def mostrar_saudacao(event):
        saudacao = lista_suspensa.value
        texto_saudacao.value = saudacao
        page.update()

    lista_suspensa = ft.Dropdown(
        options=[
            ft.dropdown.Option("Bom dia"),
            ft.dropdown.Option("Boa tarde"),
            ft.dropdown.Option("Boa noite")],
        label='Escolha uma saudação'
    )

    btn_saudacao = ft.ElevatedButton(text='Mostrar Saudação',
                                     on_click=mostrar_saudacao)

    texto_saudacao = ft.Text('')

    page.add(lista_suspensa, btn_saudacao, texto_saudacao)


ft.app(target=main)
