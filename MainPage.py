# MainPage.py
import flet as ft

class MainPage:
    def __init__(self, page: ft.Page, build:dict):
        self.page = page
        self.build = build

    def get_view(self):
        self.main_label = ft.Text("Builder", size=30, color="Black", weight=ft.FontWeight.BOLD)
        self.additional_label = ft.Text("by reallyShould", size=16, color="Black")

        self.price_field = ft.TextField(
            label="Price",
            keyboard_type=ft.KeyboardType.NUMBER,
            color="white",
            bgcolor="gray",
        )

        self.configDD = ft.Dropdown(
            options=[
                ft.dropdown.Option("Gaming"),
                ft.dropdown.Option("Working"),
                ft.dropdown.Option("Graphics"),
            ],
            label="Config",
            color="white",
            bgcolor="gray",
        )

        self.cpuDD = ft.Dropdown(
            options=[
                ft.dropdown.Option("INTEL"),
                ft.dropdown.Option("AMD"),
            ],
            label="CPU",
            color="white",
            bgcolor="gray",
        )

        self.gpuDD = ft.Dropdown(
            options=[
                ft.dropdown.Option("NVIDIA"),
                ft.dropdown.Option("AMD"),
            ],
            label="GPU",
            color="white",
            bgcolor="gray",
        )

        self.start_btn = ft.CupertinoFilledButton(
            content=ft.Text("Start"),
            opacity_on_click=0.3,
            on_click=lambda e: self.route()
        )

        col = ft.Column(
            controls=[
                self.main_label,
                self.additional_label,
                self.price_field,
                self.configDD,
                self.cpuDD,
                self.gpuDD,
                self.start_btn,
            ],
        )

        return ft.View("/", controls=[col], bgcolor="white")
    
    def route(self):
        self.build["price"] = self.price_field.value
        self.build["cfg"] = self.configDD.value
        self.page.go("/final")