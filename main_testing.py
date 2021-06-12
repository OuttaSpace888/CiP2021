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
    "Smoked Fish or Meat",
    "Offal, Sausages, Salmon",
    "Processed Foods",
    "Canned Fish, Meat, Beans",
    "Ketchup, Mayonnaise",
    "Saturated Fat",
    "Olives, Pickles, Relish",
    "Potatoes",
    "Tee, Cola",
    "Tzatziki",
    "Avocados",
]
BAD_LIST_RIGHT = [
    "Chocolate",
    "Dried Fruits",
    "Marzipan",
    "Undiluted Fruit Juice",
    "Vegetable Juice",
    "Canned Tomato Products/Juice",
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

        # Enter weight, label
        weight_label = tk.Label(
            self,
            text="Enter your weight in kg:",
            font=("Arial", 18),
            bg=MAIN_FRAME_COLOR,
        )
        weight_label.pack(pady=10)

        # Weight entry box
        weight_entry = tk.Entry(self)
        weight_entry.pack(pady=10)

        # Weight submit button
        weight_btn = button(
            self,
            text="Submit",
            bg="#5ddeef",
            activebackground="#4285f4",
            font=("Arial", 14),
            command=lambda: self.calculating_weight(self, weight_entry.get()),
        )
        weight_btn.pack(pady=10)

        # additional note marked with '*'
        note = tk.Label(
            self,
            text="*All numbers are rounded to the nearest ones place",
            bg=MAIN_FRAME_COLOR,
        )
        note.place(relx=0.05, rely=0.9)

    # Rounds number > = 0.5 up, else down
    def round_half_up(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier + 0.5) / multiplier

    # Calculates daily intakes and displays them on the screen
    def calculating_weight(self, frame, weight):
        # Converts weight into float for accurate calculation with the help of round_half_up() function,
        # rounds the number and return as integer
        daily_calories = int(self.round_half_up(float(weight.strip().strip("kg")) * 30))
        # Creates StringVar in order to update value with re-submission
        cal_number = tk.StringVar(value=daily_calories)
        cal_number.get()
        calories = "Calories per day:"

        daily_protein = int(self.round_half_up(float(weight.strip().strip("kg")) * 1.2))
        prot_number = tk.StringVar(value=daily_protein)
        prot_number.get()
        protein = "Protein per day:"

        # Calories and protein labels, excluding actual calculated value
        calories_result = tk.Label(
            frame, text=calories, font=("Arial", 18), bg=MAIN_FRAME_COLOR
        )
        calories_result.place(relx=0.36, rely=0.5, relwidth=0.2, relheight=0.1)

        protein_result = tk.Label(
            frame, text=protein, font=("Arial", 18), bg=MAIN_FRAME_COLOR
        )
        protein_result.place(relx=0.36, rely=0.6, relwidth=0.2, relheight=0.1)

        # Automatic self updating StringVar printed to the screen
        display_calories = tk.Label(
            frame, textvariable=cal_number, bg=MAIN_FRAME_COLOR, font=("Arial", 18)
        )
        display_calories.place(relx=0.56, rely=0.5, relwidth=0.1, relheight=0.1)

        display_protein = tk.Label(
            frame, textvariable=prot_number, bg=MAIN_FRAME_COLOR, font=("Arial", 18)
        )
        display_protein.place(relx=0.56, rely=0.6, relwidth=0.1, relheight=0.1)


class Nutrients(Page):
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
        bad_foods_title = self.tab_titles(
            bad_foods_frame,
            "High levels of phosphorous and potassium foods",
            BAD_FOOD_COLOR,
        )
        # api_title = self.tab_titles(api_frame, "Nutrition Search Engine")

        # All Tab Inside Content Frames
        # Daily Intake Tab Frames
        tab1_left = tk.Frame(intake_frame, bg=MAIN_FRAME_COLOR)
        tab1_left.place(relx=0.25, rely=0.25, relwidth=0.2, relheight=0.6)
        tab1_right = tk.Frame(intake_frame, bg=MAIN_FRAME_COLOR)
        tab1_right.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.6)

        # Recommended Foods Frames
        tab2_left = self.tab_content_foods(good_foods_frame, GOOD_FOOD_COLOR)
        tab2_right = self.tab_content_foods(good_foods_frame, GOOD_FOOD_COLOR, 0.5)
        # Foods to Avoid Frames
        avoid_left = self.tab_content_foods(bad_foods_frame, BAD_FOOD_COLOR)
        avoid_right = self.tab_content_foods(bad_foods_frame, BAD_FOOD_COLOR, 0.5)

        # Defining Actual Tab Contents

        daily_left = self.daily_nutr_text(
            tab1_left, DAILY_NUTR_LEFT, MAIN_FRAME_COLOR, "bold"
        )
        daily_right = self.daily_nutr_text(
            tab1_right, DAILY_NUTR_RIGHT, MAIN_FRAME_COLOR
        )

        good_left = self.tab_body(tab2_left, GOOD_LIST_LEFT, GOOD_FOOD_COLOR)
        good_right = self.tab_body(tab2_right, GOOD_LIST_RIGHT, GOOD_FOOD_COLOR)

        bad_left = self.tab_body(avoid_left, BAD_LIST_LEFT, BAD_FOOD_COLOR)
        bad_right = self.tab_body(avoid_right, BAD_LIST_RIGHT, BAD_FOOD_COLOR)

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
    def tab_content_foods(self, frame, color, x=0.1):
        content_frame = tk.Frame(frame, bg=color)
        content_frame.place(relx=x, rely=0.2, relwidth=0.4)
        return content_frame

    # Generates all tab contents
    def tab_body(self, frame, content, color):
        labels = []
        for text in content:
            label = tk.Label(frame, text=text, font=("Arial", 18), bg=color)
            label.pack()
            labels.append(label)
        return labels

    def daily_nutr_text(self, frame, content, color, bold=""):
        y = 0.1
        labels = []
        for text in content:
            label = tk.Label(frame, text=text, font=("Arial", 18, bold), bg=color)
            label.place(relx=0.1, rely=y)
            y += 0.1
            labels.append(label)
        return labels

    # TODO: Try re-writing it with class method later
    # def tab_frames(self):
    #     tabs = tk.Frame(self.notebook, width=900, height=500, bg="black")
    #     tabs.pack(fill="both", expand=1)


class TabHeader(Page):
    pass


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
