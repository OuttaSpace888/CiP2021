import tkinter as tk
from tkinter import ttk
from tkmacosx import Button as button
from io import BytesIO
from PIL import Image, ImageTk
from py_edamam import PyEdamam
import requests
import webbrowser
import math


WINDOW_TITLE = "Dialysis Nutrition Information By Yihan Ye"
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300
MAIN_WINDOW_SIZE = "900x900"
MAIN_WINDOW_COLOR = "#bedddc"
MAIN_FRAME_COLOR = "#f4efeb"
GOOD_FOOD_COLOR = "#9be281"
BAD_FOOD_COLOR = "#f9a08b"
BTN_COLOR = "#e5c5c8"


class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

    def show(self):
        self.lift()


class Intro(Page):
    intro_text = (
        "Here you can find recommended foods to eat for dialysis patients as well as which foods to avoid. You can also find nutrition information for individual food items of your choice with the built in API!\n"
        "\nUse the calculator to determine your daily energy and protein intake for a balanced diet.\n"
        "\nCheck out the other tabs for additional useful information that can help you consume your favorite foods in a safe way!"
    )

    def __init__(self):
        Page.__init__(self)
        label = tk.Label(
            self,
            text="Welcome to the Dialysis Nutrition App!",
            bg=MAIN_FRAME_COLOR,
            font=("Arial", 24, "bold"),
        )
        label.pack(pady=30)

        border_frame = tk.LabelFrame(self, bg=MAIN_FRAME_COLOR)
        border_frame.pack()
        message = tk.Message(
            border_frame,
            text=Intro.intro_text,
            font=("Arial", 18),
            bg=MAIN_FRAME_COLOR,
        )
        message.pack(pady=20)


class Calculator(Page):
    # def __init__(self):
    #     Page.__init__(self)
    #     label = tk.Label(self, text="This is page 2")
    #     label.pack(side="top", fill="both", expand=True)
    pass


class Nutrients(Page):
    # def __init__(self):
    #     Page.__init__(self)
    #     label = tk.Label(self, text="This is page 3")
    #     label.pack(side="top", fill="both", expand=True)
    pass


class Information(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(
            self,
            text="Important Things to Note",
            font=("Arial", 24, "bold"),
            bg=MAIN_FRAME_COLOR,
        )
        label.pack(pady=30)

        border_frame = tk.LabelFrame(self, bg="yellow")
        border_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)


class Recipe(Page):
    # def __init__(self):
    #     Page.__init__(self)
    #     label = tk.Label(self, text="This is page 3")
    #     label.pack(side="top", fill="both", expand=True)
    pass


class MenuButton(object):
    def __init__(self, frame, btn_text, raise_content):
        btn = button(
            frame,
            text=btn_text,
            height=100,
            background=BTN_COLOR,
            activebackground="orange",
            # activeforeground="black",
            font=("Arial", 24),
            command=raise_content,
        )
        btn.pack(fill="both")


class MainWindow(tk.Frame):
    def __init__(self, frame) -> None:
        tk.Frame.__init__(self, frame)
        intro = Intro()
        calculator = Calculator()
        nutrients = Nutrients()
        info = Information()
        recipe = Recipe()

        self.frame = frame
        self.header = tk.Label(
            self.frame,
            text="Dialysis Nutrition Information",
            justify="center",
            bg=MAIN_WINDOW_COLOR,
            font=("Arial", 32, "bold"),
        )
        self.header.place(relx=0.42, rely=0.1)

        button_frame = tk.Frame(self.frame)
        button_frame.place(relx=0.025, rely=0.2, relwidth=0.2, relheight=0.65)
        content_frame = tk.Frame(self.frame, bg="orange")
        content_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

        intro.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
        info.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)

        intro_btn = MenuButton(button_frame, "Intro", intro.show)
        calculator_btn = MenuButton(button_frame, "Calculator", calculator.show)
        nutrients_btn = MenuButton(button_frame, "Nutrients", nutrients.show)
        info_btn = MenuButton(button_frame, "Tips & Tricks", info.show)
        recipe_btn = MenuButton(button_frame, "Recipe", recipe.show)


if __name__ == "__main__":
    window = tk.Tk()
    window.title(WINDOW_TITLE)
    window.configure(bg=MAIN_WINDOW_COLOR)
    main = MainWindow(window)
    main.pack()
    window.wm_geometry(MAIN_WINDOW_SIZE)
    window.mainloop()
