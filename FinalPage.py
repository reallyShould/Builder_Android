# MainPage.py
import flet as ft
import requests

class FinalPage:
    def __init__(self, page: ft.Page, build:dict):
        self.page = page
        self.build = build

    def get_view(self):
        test = ft.Text(self.get_curl(), size=16, color="Black")

        col = ft.Column(
            controls=[
                test
            ],
        )

        return ft.View("/final", controls=[col], bgcolor="white")

    def get_curl(self):
        headers = {
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
        }

        json_data = {
            "price": self.build["price"],
            "cfg": self.build["cfg"],
        }
        return requests.get('https://reallys.pythonanywhere.com/build', headers=headers, json=json_data).content