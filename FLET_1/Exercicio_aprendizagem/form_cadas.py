import flet as ft


def main(page: ft.Page):

    def cadastro(event):
        nome = campo_nome.value
        email = campo_email.value
        idade = campo_idade.value

        if not nome or not email or not idade:
            resultado.value = 'Todos os campos devem ser preenchidos'
        elif not idade.isdigit() or int(idade) < 0:
            resultado.value = 'Idade inválida. Insira um número positivo'
        else:
            resultado.value = f'''Cadastro efetuado com sucesso! Nome: {nome},
            Email: {email}, Idade: {idade}'''

        page.update()

    campo_nome = ft.TextField(label='Nome')
    campo_email = ft.TextField(label='email')
    campo_idade = ft.TextField(label='idade')

    btn_cadastrar = ft.ElevatedButton('Cadastrar', on_click=cadastro)
    resultado = ft.Text('')

    page.add(campo_nome, campo_email, campo_idade, btn_cadastrar, resultado)


ft.app(target=main)
