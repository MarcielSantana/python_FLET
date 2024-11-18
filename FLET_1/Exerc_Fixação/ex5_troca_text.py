import flet


def main(page: flet.Page):
    texto1 = flet.Text('Primeiro texto')

    def troca_texto(event):
        texto1.value = 'Texto Alterado'
        page.update()

    btn_troca_texto = flet.ElevatedButton('Muda Texto', on_click=troca_texto)
    page.add(texto1, btn_troca_texto)


flet.app(target=main)
