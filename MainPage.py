import flet as ft

class MainPage:
    def __init__(self, page: ft.Page, build:dict):
        self.page = page
        self.build = build

    def get_view(self):
        navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Auto", selected_icon=ft.icons.EXPLORE),
                ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Custom"),
            ]
        )

        self.label = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Builder", size=30, color="Black", weight=ft.FontWeight.BOLD, font_family="Verdana"),
                    ft.Text("by reallyShould", size=16, color="Black", font_family="Verdana"),
                ],
                spacing=1
            ), 
            padding=10
        )

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

        self.start_btn = ft.CupertinoButton(
            content=ft.Text("Start", color="white", font_family="Verdana"),
            bgcolor="black",
            border_radius=ft.border_radius.all(3),
            opacity_on_click=0.5,
            on_click=lambda e: self.route(),
            width=self.page.width,
        )

        col = ft.Column(
            controls=[
                self.label,
                self.price_field,
                self.configDD,
                self.cpuDD,
                self.gpuDD,
                self.start_btn,
            ],
        )

        return ft.View("/", controls=[col], bgcolor="white", appbar=navigation_bar)
    
    def route(self):
        self.build["price"] = self.price_field.value
        self.build["cfg"] = self.configDD.value
        self.page.go("/final")
