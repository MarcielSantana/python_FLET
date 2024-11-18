import flet
import asyncio


def main(page: flet.Page):
    exibe_contador = flet.Text()
    page.add(exibe_contador)

    async def contador(event):
        for i in range(10, 0, -1):
            exibe_contador.value = (i)
            page.update()
            await asyncio.sleep(1)
        exibe_contador.value = 'Tempo esgotado'
        page.update()

    btn_cont_regressiva = flet.ElevatedButton('Contagem Regressiva',
                                              on_click=contador)
    page.add(btn_cont_regressiva)


flet.app(target=main)
