import flet as ft


def main(page: ft.Page):
    contador = ft.Text('0')

    def incrementa(event):
        contador.value = str(int(contador.value) + 1)
        contador.update()

    def decrementa(event):
        contador.value = str(int(contador.value) - 1)
        contador.update()

    btn_incrementa = ft.ElevatedButton('Aumentar', on_click=incrementa)

    btn_DEcrementa = ft.ElevatedButton('Diminuir', on_click=decrementa)

    page.add(contador, btn_incrementa, btn_DEcrementa)


ft.app(target=main)
