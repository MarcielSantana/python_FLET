import flet as ft


def main(page: ft.Page):
    number1 = ft.TextField(label='Número 1')
    number2 = ft.TextField(label='Número 2')
    text_result = ft.Text('')

    def somar(event):
        n1 = int(number1.value)
        n2 = int(number2.value)
        soma = n1 + n2
        text_result.value = soma
        page.update()

    def multiplicar(event):
        n1 = int(number1.value)
        n2 = int(number2.value)
        multiplca = n1 * n2
        text_result.value = multiplca
        page.update()

    def dividir(event):
        n1 = int(number1.value)
        n2 = int(number2.value)
        if n2 == 0:
            text_result.value = 'Não é posível dividisão por zero'
        else:
            dividi = n1 / n2
        text_result.value = dividi
        page.update()

    def subtracao(event):
        n1 = int(number1.value)
        n2 = int(number2.value)
        subtrai = n1 - n2
        text_result.value = subtrai
        page.update()

    btn_soma = ft.ElevatedButton('+', on_click=somar)
    btn_multiplicao = ft.ElevatedButton('*', on_click=multiplicar)
    btn_divisao = ft.ElevatedButton('/', on_click=dividir)
    btn_subtracao = ft.ElevatedButton('-', on_click=subtracao)

    page.add(number1, number2, text_result, btn_soma, btn_multiplicao,
             btn_divisao, btn_subtracao)


ft.app(target=main)
