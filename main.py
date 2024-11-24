import flet as ft
from MainPage import MainPage
from FinalPage import FinalPage

build = {}

def main(page: ft.Page):
    page.title = "PC Builder"
    page.padding = 20

    main_page = MainPage(page, build)
    final_page = FinalPage(page, build)

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(main_page.get_view())
        elif page.route == "/final":
            page.views.append(final_page.get_view())
        page.update()

    page.on_route_change = route_change

    page.go("/")

ft.app(main)
