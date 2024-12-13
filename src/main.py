import flet as ft
from mylocale.TR import tr

mysupported_locales = ["en", "de"]

tr_file = "src/assets/localisation.csv"


def main(page: ft.Page):
    page.fonts = {"Christmas": ""}
    audio = ft.Audio(src="assets/we-wish-you-a-merry-christmas.wav", autoplay=True)
    page.overlay.append(audio)

    def changelang(e):
        greeting.value = tr(
            target_key="MERRYCHRISTMAS", csv_file=tr_file, langcode=lang.value
        )
        greeting.update()

    lang = ft.Dropdown(
        value="en",
        options=[ft.dropdown.Option(locale) for locale in mysupported_locales],
        on_change=changelang,
    )
    greeting = ft.Text(
        tr(target_key="MERRYCHRISTMAS", csv_file=tr_file, langcode=lang.value),
        size=50,
        data=0,
    )

    # page.floating_action_button = ft.FloatingActionButton(
    #    icon=ft.Icons.ADD, on_click=increment_click
    # )
    page.add(
        ft.SafeArea(
            ft.Container(
                greeting,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                lang,
                alignment=ft.alignment.center,
                expand=True,
            ),
        ),
    )


ft.app(main)
