import flet as ft
import flet_audio as fta
from mylocale.TR import TR

mysupported_locales = ["en", "de"]

tr_file = "src/assets/localisation.csv"


def main(page: ft.Page):
    tr = TR(langcode="en", csv_file=tr_file)
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage("src/assets/menuescreen.png")
    )
    lang = ft.Dropdown(
        value="en",
        options=[ft.dropdown.Option(locale) for locale in mysupported_locales],
    )
    text = ft.Text(tr.tr(target_key="MERRYCHRISTMAS", langcode="en"))
    page.appbar = ft.AppBar(title=text)
    # page.fonts = {"Christmas": "src/assets/fonts/QTMerryScript.otf"}
    # page.theme = ft.Theme(font_family="Christmas")
    audio = fta.Audio(src="/we-wish-you-a-merry-christmas.mp3", autoplay=True)
    page.overlay.append(audio)

    greeting = ft.Text(
        tr.tr(target_key="MERRYCHRISTMAS", langcode="en"),
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
                alignment=ft.Alignment.CENTER,
            ),
            expand=True,
        )
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                lang,
                alignment=ft.Alignment.CENTER,
                expand=True,
            ),
        ),
    )


ft.run(main)
