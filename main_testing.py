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
MAIN_WINDOW_SIZE = "1000x1000"
MAIN_WINDOW_COLOR = "#bedddc"
MAIN_FRAME_COLOR = "#f4efeb"
GOOD_FOOD_COLOR = "#9be281"
BAD_FOOD_COLOR = "#f9a08b"
BTN_COLOR = "#e5c5c8"
# Nutrition Tab Content Lists
DAILY_NUTR_LEFT = ["Calories", "Protein", "Liquid", "Salt", "Potassium", "Phosphorous"]
DAILY_NUTR_RIGHT = [
    "30cal/kg per day",
    "1,2g/kg per day",
    "500ml + residual excretion/24h",
    "5-6g salt per day",
    "2000-2500mg per day",
    "1000-1400mg per day",
]
GOOD_LIST_LEFT = [
    "Zucchini, Cucumbers",
    "Lemons, Lime",
    "Blueberries",
    "Apple, Pears",
    "Salads",
    "Couscous",
    "Lean Meat",
    "Most Fish",
    "Cauliflower",
    "Olive Oil, Butter",
    "Mushrooms",
]
GOOD_LIST_RIGHT = [
    "Radish, Celery",
    "Green Pepper",
    "Strawberries",
    "Carrots, Green Beans",
    "Cream",
    "Mozzarella",
    "Onion, Garlic",
    "Honey, Jam",
    "Eggs",
    "Watermelon",
    "Cooked Rice, Pasta",
]
BAD_LIST_LEFT = [
    "Offal, Sausages, Salmon",
    "Smoked Fish or Meat",
    "Processed Foods",
    "Potatoes",
    "Ketchup, Mayonnaise",
    "Canned Tomato Products/Juice",
    "Olives, Pickles, Relish",
    "Tzatziki",
    "Canned Fish, Meat, Beans",
    "Saturated Fat",
    "Avocados",
]
BAD_LIST_RIGHT = [
    "Chocolate",
    "Dried Fruits",
    "Marzipan",
    "Undiluted Fruit Juice",
    "Vegetable Juice",
    "Tee, Cola",
    "Bananas, Kiwis",
    "Dates, Figs",
    "Feta, Parmesan, Cheddar etc.",
    "Most Dairy Products",
    "Coconuts, Nuts",
]
SALT_CONTENT = [
    "- Season food after it's\n  cooked for more control",
    "- Don't use salt substitute!\n  Use alternatives instead",
    "- Alternatives are:\n  Basil, Cilantro, Garlic\n  Oregano, Mint, Chives\n  Lemon, Parsley, Sage",
]
PHOSPHOROUS_CONTENT = [
    "- Throw out cooking water\n  & change while cooking",
    "- Throw away canned\n  vegetables & meat juice",
    "- Soak diced vegetables\n  in  water before cooking",
    "- Dice or shred vegetables\n  with high  phosphorous\n  content",
]
ADDITIONAL_CONTENT = [
    "- Avoid eating animal skin\n  (poultry)",
    "- Try not to eat egss more\n  than 3x per week",
    "- Pre-fill your water bottle\n  for the entire day",
    "- Don't forget food contains\n  water as well!\n  (fruits, soup, ice cream)",
]


class Page(tk.Frame):
    # Main content frame
    def __init__(self):
        tk.Frame.__init__(self, bg=MAIN_FRAME_COLOR)

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

        # Border around text body and message generation
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
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(
            self,
            text="Calculate your daily energy and protein intake requirements.",
            font=("Arial", 20),
            bg=MAIN_FRAME_COLOR,
        )
        label.pack(pady=25)


class Nutrients(Page):
    y_step = 0.1

    def __init__(self):
        Page.__init__(self)
        notebook = ttk.Notebook(self, width=1000, height=500)
        notebook.pack()

        # Creating each tab frame
        intake_frame = tk.Frame(notebook, width=900, height=500, bg=MAIN_FRAME_COLOR)
        good_foods_frame = tk.Frame(notebook, width=900, height=500, bg=GOOD_FOOD_COLOR)
        bad_foods_frame = tk.Frame(notebook, width=900, height=500, bg=BAD_FOOD_COLOR)
        # api_frame = tk.Frame(notebook, width=900, height=500, bg="orange")

        # Naming each tab
        frames = [intake_frame, good_foods_frame, bad_foods_frame]  # , api_frame]
        tab_names = [
            "Daily Intake",
            "Recommended Foods",
            "Foods to Avoid",
            # "Nutrition API",
        ]
        i = 0
        for frame in frames:
            notebook.add(frame, text=tab_names[i])
            i += 1

        # Header for each tab section
        intake_title = self.tab_titles(intake_frame, "Daily Nutrients Guideline")
        good_foods_title = self.tab_titles(
            good_foods_frame,
            "Low levels of phosphorous and potassium foods",
            GOOD_FOOD_COLOR,
        )
        bad_foods_frame = self.tab_titles(
            bad_foods_frame,
            "High levels of phosphorous and potassium foods",
            BAD_FOOD_COLOR,
        )
        # api_title = self.tab_titles(api_frame, "Nutrition Search Engine")

        # All Tab Inside Content Frames
        # Daily Intake Tab Frames
        tab1_left = self.tab_content_frames(intake_frame, 0.1, 0.25, 0.8)
        tab1_right = self.tab_content_frames(intake_frame, 0.5, 0.5, 0.8)
        # Recommended Foods Frames
        tab2_left = self.tab_content_frames(good_foods_frame, 0.1, 0.4, 0.5)
        tab2_right = self.tab_content_frames(good_foods_frame, 0.3, 0.4, 0.5)
        # Foods to Avoid Frames
        tab3_left = self.tab_content_frames(bad_foods_frame, 0.1, 0.4, 0.5)
        tab3_right = self.tab_content_frames(bad_foods_frame, 0.3, 0.4, 0.5)

        # Defining Actual Tab Contents
        daily_left = self.tab_body(tab1_left, DAILY_NUTR_LEFT)
        daily_right = self.tab_body(tab1_right, DAILY_NUTR_RIGHT)

        good_left = self.tab_body(tab2_left, GOOD_LIST_LEFT)
        good_right = self.tab_body(tab2_right, GOOD_LIST_RIGHT)

        bad_left = self.tab_body(tab3_left, BAD_LIST_LEFT)
        bad_right = self.tab_body(tab3_right, BAD_LIST_RIGHT)

    # Method for creating all tab content headers
    def tab_titles(self, frame, text, color=MAIN_FRAME_COLOR):
        title = tk.Label(
            frame,
            text=text,
            font=("Arial", 20),
            bg=color,
        )
        title.pack(pady=25)

    # Tab content frames generator
    def tab_content_frames(self, frame, relx=0.1, width=0.4, height=0):
        content_frame = tk.Frame(frame, bg=MAIN_FRAME_COLOR)
        content_frame.place(relx=relx, rely=0.3, relwidth=width, relheight=height)
        return content_frame

    # Generates all tab contents
    def tab_body(self, frame, content):
        labels = []
        for text in content:
            label = tk.Label(frame, text=text, font=("Arial", 18), bg=MAIN_FRAME_COLOR)
            label.pack()
            labels.append(label)
        return labels

        # for point in content:
        #     point = tk.Label(
        #         frame,
        #         text=point,
        #         font=("Arial", 18, "bold"),
        #         bg=MAIN_FRAME_COLOR,
        #     )
        # point.pack()
        # return point

    # TODO: Try re-writing it with class method later
    # def tab_frames(self):
    #     tabs = tk.Frame(self.notebook, width=900, height=500, bg="black")
    #     tabs.pack(fill="both", expand=1)


class Information(Page):
    def __init__(self):
        # Main Content Frame
        Page.__init__(self)
        label = tk.Label(
            self,
            text="Important Things to Note",
            font=("Arial", 24, "bold"),
            bg=MAIN_FRAME_COLOR,
        )
        label.pack(pady=30)

        # Generates the border around the text body => box frame
        border_frame = tk.LabelFrame(self, bg=MAIN_FRAME_COLOR)
        border_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        # Creating frame for each information column/section => The 3 small frames!
        left_frame = self.sections(border_frame, 0.03)
        middle_frame = self.sections(border_frame, 0.35)
        right_frame = self.sections(border_frame, 0.67)

        # Creating labels for each section/column
        left_header = self.headers(
            left_frame, "Salt & Pepper Substitute"
        )  # Attaches as expected inside the box frame
        # Won't attach to the small frames, instead uses the root window
        middle_header = self.headers(
            middle_frame, "Decrease phosphorous\nlevels in food"
        )
        right_header = self.headers(right_frame, "Additional Insights")

        # Contents to fill each frame of each category
        left_content = self.frame_contents(
            left_frame, SALT_CONTENT
        )  # Once again works in box frame
        # And NOT in the 3 small frames.
        middle_content = self.frame_contents(middle_frame, PHOSPHOROUS_CONTENT)
        right_content = self.frame_contents(right_frame, ADDITIONAL_CONTENT)

    # Method I used to create the 3 small frames
    def sections(self, frame, relx):
        section_frame = tk.Frame(frame, bg=MAIN_FRAME_COLOR)
        section_frame.place(relx=relx, rely=0.08, relwidth=0.3, relheight=0.85)
        return section_frame

    # Header I used to create the header for each small frame
    def headers(self, frame, text):
        header = tk.Label(
            frame, text=text, font=("Arial", 16, "bold"), bg=MAIN_FRAME_COLOR
        )
        header.pack()  # place(relx=0.5, rely=0.02)

    # Generates the body content of each small frame
    def frame_contents(self, frame, content):
        y = 0.2
        for point in content:
            point = tk.Label(
                frame,
                text=point,
                font=("Arial", 16),
                justify="left",
                bg=MAIN_FRAME_COLOR,
            )
            point.place(relx=0.06, rely=y)
            y += 0.2


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

        # App header placed into main window
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
        content_frame = tk.Frame(self.frame)
        content_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

        intro.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
        calculator.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
        nutrients.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
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
