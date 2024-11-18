import flet


def main(page: flet.Page):
    campo = flet.TextField(label='Escreva aqui', max_length=10)

    def mostra_texto(event):
        texto_campo = flet.Text(campo.value)
        page.add(texto_campo)

    btn_troca_texto = flet.ElevatedButton('Mostra Texto',
                                          on_click=mostra_texto)
    page.add(campo, btn_troca_texto)


flet.app(target=main)
