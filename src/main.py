import flet as ft

mysupported_locales = ["en", "de"]


def main(page: ft.Page):
    audio = ft.Audio(src="assets/we-wish-you-a-merry-christmas.wav", autoplay=True)
    page.overlay.append(audio)
    counter = ft.Text("Merry Christmas", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    # page.floating_action_button = ft.FloatingActionButton(
    #    icon=ft.Icons.ADD, on_click=increment_click
    # )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Dropdown(
                    value="en",
                    options=[
                        ft.dropdown.Option(locale) for locale in mysupported_locales
                    ],
                ),
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
