import flet as ft
from MainPage import MainPage
from FinalPage import FinalPage

build = {}

def main(page: ft.Page):
    page.title = "PC Builder"
    page.padding = 20

    # Создаем объекты для каждой страницы
    main_page = MainPage(page, build)
    final_page = FinalPage(page, build)

    # Обработчик изменения маршрута
    def route_change(route):
        page.views.clear()  # Очистка текущих окон
        if page.route == "/":
            page.views.append(main_page.get_view())
        elif page.route == "/final":
            page.views.append(final_page.get_view())
        page.update()

    # Указываем обработчик маршрутов
    page.on_route_change = route_change

    # Устанавливаем стартовый маршрут
    page.go("/")

ft.app(main)
