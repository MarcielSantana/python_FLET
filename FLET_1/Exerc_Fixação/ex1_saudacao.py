import flet


def main(page: flet.Page):
    texto = flet.Text('Olá Mundo')

    page.add(texto)


flet.app(target=main)
