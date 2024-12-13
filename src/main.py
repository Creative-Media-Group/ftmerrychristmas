import flet as ft
from mylocale.TR import tr

mysupported_locales = ["en", "de"]

tr_file = "src/assets/localisation.csv"


def main(page: ft.Page):
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage("src/assets/menuescreen.png")
    )
    lang = ft.Dropdown(
        value="en",
        options=[ft.dropdown.Option(locale) for locale in mysupported_locales],
    )
    lang.on_change = lambda _: changelang(lang.value)
    text = ft.Text(
        tr(target_key="MERRYCHRISTMAS", csv_file=tr_file, langcode=lang.value)
    )
    page.appbar = ft.AppBar(title=text)
    page.fonts = {"Christmas": "src/assets/fonts/QTMerryScript.otf"}
    page.theme = ft.Theme(font_family="Christmas")
    audio = ft.Audio(src="assets/we-wish-you-a-merry-christmas.mp3", autoplay=True)
    page.overlay.append(audio)

    def changelang(mylang):
        greeting.value = tr(
            target_key="MERRYCHRISTMAS", csv_file=tr_file, langcode=mylang
        )
        text.value = tr(target_key="MERRYCHRISTMAS", csv_file=tr_file, langcode=mylang)
        greeting.update()
        page.appbar.update()

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
