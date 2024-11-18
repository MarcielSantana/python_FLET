import flet


def main(page: flet.Page):
    texto = flet.TextField(label='Digite seu nome aqui')

    def mostrar_nome(event):
        nome = texto.value
        mensagem = flet.Text(f'Olá {nome}')
        page.add(mensagem)

    botao_enviar = flet.ElevatedButton('Enviar', on_click=mostrar_nome)

    page.add(texto, botao_enviar)


flet.app(target=main)
