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
        self.CpuTitle = ft.Text(cpu["name"], size=24, color="Black", weight=ft.FontWeight.BOLD)
        self.CpuSocket = ft.Text(f"Socket: {cpu['socket']}", size=16, color="Black")
        self.CpuCores = ft.Text(f"Cores: {cpu['cores']}", size=16, color="Black")
        self.CpuTdp = ft.Text(f"TDP: {cpu['tdp']}", size=16, color="Black")
        self.CpuBench = ft.Text(f"BenchMark: {cpu['bench']}", size=16, color="Black")
        self.CpuPrice = ft.Text(f"Price: {cpu['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD)

        cpu_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("CPU", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        self.CpuTitle,
                        self.CpuSocket,
                        self.CpuCores,
                        self.CpuTdp,
                        self.CpuBench,
                        self.CpuPrice,
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
        self.GpuTitle = ft.Text(gpu["name"], size=24, color="Black", weight=ft.FontWeight.BOLD)
        self.GpuBench3d = ft.Text(f"BenchMark3D: {gpu['bench3d']}", size=16, color="Black")
        self.GpuBench2d = ft.Text(f"BenchMark2D: {gpu['bench2d']}", size=16, color="Black")
        self.GpuTdp = ft.Text(f"TDP: {gpu['tdp']}", size=16, color="Black")
        self.GpuPrice = ft.Text(f"Price: {gpu['price']}$", size=16, color="Green", weight=ft.FontWeight.BOLD)

        gpu_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("GPU", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        self.GpuTitle,
                        self.GpuBench3d,
                        self.GpuBench2d,
                        self.GpuTdp,
                        self.GpuPrice,
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
        self.MbTitle = ft.Text(mb["name"], size=24, color="Black", weight=ft.FontWeight.BOLD)
        self.MbChipset = ft.Text(f"Chipset: {mb['chipset']}", size=16, color="Black")
        self.MbSocket = ft.Text(f"Socket: {mb['socket']}", size=16, color="Black")

        mb_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Motherboard", size=18, color="Blue", weight=ft.FontWeight.BOLD),
                        self.MbTitle,
                        self.MbChipset,
                        self.MbSocket,
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
