import flet as ft


def main(page: ft.Page):
    pergunta = 'Qual é a capital do Brasil'
    resposta_certa = 'Brasília'
    alternativas = ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Recife']

    def verifica_resposta(event):
        if event.control.text == resposta_certa:
            resultado.value = 'Resposta Certa!'
        else:
            resultado.value = 'Resposta Incorreta!'
        page.update()

    texto_pergunta = ft.Text(pergunta)
    resultado = ft.Text('')

    botoes_alternativas = []
    for resposta in alternativas:
        botao = ft.ElevatedButton(resposta, on_click=verifica_resposta)
        botoes_alternativas.append(botao)

    page.add(texto_pergunta, *botoes_alternativas, resultado)


ft.app(target=main)
