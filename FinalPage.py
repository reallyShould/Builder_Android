import flet as ft
import requests
import json

domain = "https://reallys.pythonanywhere.com"

class FinalPage:
    def __init__(self, page: ft.Page, build: dict):
        self.page = page
        self.build = build

    def get_view(self):
        out = json.loads(self.get_curl())

        ####### CPU #######
        cpu = out["cpu"]
        cpu_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("CPU", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        ft.Text(cpu["name"], size=24, color="Black", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Socket: {cpu['socket']}", size=16, color="Black"),
                        ft.Text(f"Cores: {cpu['cores']}", size=16, color="Black"),
                        ft.Text(f"TDP: {cpu['tdp']} W", size=16, color="Black"),
                        ft.Text(f"BenchMark: {cpu['bench']}", size=16, color="Black"),
                        ft.Text(f"Price: {cpu['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD),
                    ],
                    spacing=5
                ),
                padding=10,
                bgcolor="#F5F5F5",
                border_radius=8
            ),
            width=self.page.width
        )

        ####### GPU #######
        gpu = out["gpu"]
        gpu_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("GPU", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        ft.Text(gpu["name"], size=24, color="Black", weight=ft.FontWeight.BOLD),
                        ft.Text(f"BenchMark3D: {gpu['bench3d']}", size=16, color="Black"),
                        ft.Text(f"BenchMark2D: {gpu['bench2d']}", size=16, color="Black"),
                        ft.Text(f"TDP: {gpu['tdp']} W", size=16, color="Black"),
                        ft.Text(f"Price: {gpu['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD),
                    ],
                    spacing=5
                ),
                padding=10,
                bgcolor="#F5F5F5",
                border_radius=8
            ),
            width=self.page.width
        )

        ####### Motherboard #######
        mb = out["motherboard"]
        mb_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Motherboard", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        ft.Text(mb["name"], size=24, color="Black", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Chipset: {mb['chipset']}", size=16, color="Black"),
                        ft.Text(f"Socket: {mb['socket']}", size=16, color="Black"),
                        ft.Text(f"Max RAM: {mb['maxRam']} GB", size=16, color="Black"),
                        ft.Text(f"Price: {mb['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD),
                    ],
                    spacing=5
                ),
                padding=10,
                bgcolor="#F5F5F5",
                border_radius=8
            ),
            width=self.page.width
        )

        ####### RAM #######
        ram = out["ram"]
        ram_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("RAM", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        ft.Text(ram["name"], size=24, color="Black", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Type: {ram['type']}", size=16, color="Black"),
                        ft.Text(f"Capacity: {ram['capacity']} GB x {ram['count']}", size=16, color="Black"),
                        ft.Text(f"Frequency: {ram['freq']} MHz", size=16, color="Black"),
                        ft.Text(f"Price: {ram['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD),
                    ],
                    spacing=5
                ),
                padding=10,
                bgcolor="#F5F5F5",
                border_radius=8
            ),
            width=self.page.width
        )

        ####### ROM #######
        rom = out["rom"]
        rom_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Storage (ROM)", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        ft.Text(rom["name"], size=24, color="Black", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Type: {rom['type']}", size=16, color="Black"),
                        ft.Text(f"Capacity: {rom['capacity']} GB", size=16, color="Black"),
                        ft.Text(f"BenchMark: {rom['bench']}", size=16, color="Black"),
                        ft.Text(f"Price: {rom['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD),
                    ],
                    spacing=5
                ),
                padding=10,
                bgcolor="#F5F5F5",
                border_radius=8
            ),
            width=self.page.width
        )

        ####### PSU #######
        psu = out["psu"]
        psu_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Power Supply (PSU)", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        ft.Text(psu["name"], size=24, color="Black", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Power: {psu['power']} W", size=16, color="Black"),
                        ft.Text(f"Fan: {psu['fan']} mm", size=16, color="Black"),
                        ft.Text(f"Price: {psu['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD),
                    ],
                    spacing=5
                ),
                padding=10,
                bgcolor="#F5F5F5",
                border_radius=8
            ),
            width=self.page.width
        )

        ####### Layout #######
        col = ft.Column(
            controls=[
                cpu_card,
                gpu_card,
                mb_card,
                ram_card,
                rom_card,
                psu_card,
                ft.ElevatedButton(
                    text="Back to Main",
                    on_click=lambda e: self.page.go("/"),
                    bgcolor="Blue",
                    color="White",
                )
            ],
            spacing=20,
            horizontal_alignment="center"
        )

        return ft.View("/final", controls=[col], bgcolor="#FFFFFF")

    def get_curl(self):
        headers = {}

        json_data = {
            "price": self.build["price"],
            "cfg": self.build["cfg"],
        }
        return requests.get(f'{domain}/build', headers=headers, json=json_data).content
