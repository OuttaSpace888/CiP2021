import tkinter as tk
from tkinter import ttk
from tkmacosx import Button as button
import requests
import math

# No module named 'test_d'
# from test_d import dConsts as d
# from test_d import dConsts
# Attempted relative import with no known parent package
# from .dConsts import *
import dConsts


class Page(tk.Frame):
    # Main content frame
    def __init__(self):
        tk.Frame.__init__(self, bg=dConsts.MAIN_FRAME_COLOR)

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
            bg=dConsts.MAIN_FRAME_COLOR,
            font=("Arial", 24, "bold"),
        )
        label.pack(pady=30)

        # Border around text body and message generation
        border_frame = tk.LabelFrame(self, bg=dConsts.MAIN_FRAME_COLOR)
        border_frame.pack()
        message = tk.Message(
            border_frame,
            text=Intro.intro_text,
            font=("Arial", 18),
            bg=dConsts.MAIN_FRAME_COLOR,
        )
        message.pack(pady=20)


# TODO: Put Calculator and Nutrients together
class Calculator(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(
            self,
            text="Calculate your daily energy and protein intake requirements.",
            font=("Arial", 20),
            bg=dConsts.MAIN_FRAME_COLOR,
        )
        label.pack(pady=25)

        # Enter weight, label
        weight_label = tk.Label(
            self,
            text="Enter your weight in kg:",
            font=("Arial", 18),
            bg=dConsts.MAIN_FRAME_COLOR,
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
            command=lambda: self.calculating_weight(weight_entry.get()),
        )
        weight_btn.pack(pady=10)

        # additional note marked with '*'
        note = tk.Label(
            self,
            text="*All numbers are rounded to the nearest ones place",
            bg=dConsts.MAIN_FRAME_COLOR,
        )
        note.place(relx=0.05, rely=0.9)

    # Rounds number > = 0.5 up, else down
    def round_half_up(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier + 0.5) / multiplier

    # Calculates daily intakes and displays them on the screen
    def calculating_weight(self, weight):
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
            self, text=calories, font=("Arial", 18), bg=dConsts.MAIN_FRAME_COLOR
        )
        calories_result.place(relx=0.36, rely=0.5, relwidth=0.2, relheight=0.1)

        protein_result = tk.Label(
            self, text=protein, font=("Arial", 18), bg=dConsts.MAIN_FRAME_COLOR
        )
        protein_result.place(relx=0.36, rely=0.6, relwidth=0.2, relheight=0.1)

        # Automatic self updating StringVar printed to the screen
        display_calories = tk.Label(
            self,
            textvariable=cal_number,
            bg=dConsts.MAIN_FRAME_COLOR,
            font=("Arial", 18),
        )
        display_calories.place(relx=0.56, rely=0.5, relwidth=0.1, relheight=0.1)

        display_protein = tk.Label(
            self,
            textvariable=prot_number,
            bg=dConsts.MAIN_FRAME_COLOR,
            font=("Arial", 18),
        )
        display_protein.place(relx=0.56, rely=0.6, relwidth=0.1, relheight=0.1)


class Guidelines(Page):
    def __init__(self):
        Page.__init__(self)
        notebook = ttk.Notebook(self, width=1000, height=500)
        notebook.pack()

        # Creating each tab frame
        intake_frame = tk.Frame(
            notebook, width=900, height=500, bg=dConsts.MAIN_FRAME_COLOR
        )
        good_foods_frame = tk.Frame(
            notebook, width=900, height=500, bg=dConsts.GOOD_FOOD_COLOR
        )
        bad_foods_frame = tk.Frame(
            notebook, width=900, height=500, bg=dConsts.BAD_FOOD_COLOR
        )
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
        intake_title = self.tab_titles(intake_frame, "Daily Nutrition Guideline")
        good_foods_title = self.tab_titles(
            good_foods_frame,
            "Low levels of phosphorous and potassium foods",
            dConsts.GOOD_FOOD_COLOR,
        )
        bad_foods_title = self.tab_titles(
            bad_foods_frame,
            "High levels of phosphorous and potassium foods",
            dConsts.BAD_FOOD_COLOR,
        )
        # api_title = self.tab_titles(api_frame, "Nutrition Search Engine")

        # All Tab Inside Content Frames
        # Daily Intake Tab Frames
        tab1_left = tk.Frame(intake_frame, bg=dConsts.MAIN_FRAME_COLOR)
        tab1_left.place(relx=0.25, rely=0.25, relwidth=0.2, relheight=0.6)
        tab1_right = tk.Frame(intake_frame, bg=dConsts.MAIN_FRAME_COLOR)
        tab1_right.place(relx=0.45, rely=0.25, relwidth=0.45, relheight=0.6)

        # Recommended Foods Frames
        tab2_left = self.tab_content_foods(good_foods_frame, dConsts.GOOD_FOOD_COLOR)
        tab2_right = self.tab_content_foods(
            good_foods_frame, dConsts.GOOD_FOOD_COLOR, 0.5
        )
        # Foods to Avoid Frames
        avoid_left = self.tab_content_foods(bad_foods_frame, dConsts.BAD_FOOD_COLOR)
        avoid_right = self.tab_content_foods(
            bad_foods_frame, dConsts.BAD_FOOD_COLOR, 0.5
        )

        # Defining Actual Tab Contents

        daily_left = self.daily_nutr_text(
            tab1_left, dConsts.DAILY_NUTR_LEFT, dConsts.MAIN_FRAME_COLOR, "bold"
        )
        daily_right = self.daily_nutr_text(
            tab1_right, dConsts.DAILY_NUTR_RIGHT, dConsts.MAIN_FRAME_COLOR
        )

        good_left = self.tab_body(
            tab2_left, dConsts.GOOD_LIST_LEFT, dConsts.GOOD_FOOD_COLOR
        )
        good_right = self.tab_body(
            tab2_right, dConsts.GOOD_LIST_RIGHT, dConsts.GOOD_FOOD_COLOR
        )

        bad_left = self.tab_body(
            avoid_left, dConsts.BAD_LIST_LEFT, dConsts.BAD_FOOD_COLOR
        )
        bad_right = self.tab_body(
            avoid_right, dConsts.BAD_LIST_RIGHT, dConsts.BAD_FOOD_COLOR
        )

    # Method for creating all tab content headers
    def tab_titles(self, frame, text, color=dConsts.MAIN_FRAME_COLOR):
        title = tk.Label(
            frame,
            text=text,
            font=("Arial", 20, "bold"),
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


class Information(Page):
    def __init__(self):
        # Main Content Frame
        Page.__init__(self)
        label = tk.Label(
            self,
            text="Important Things to Note",
            font=("Arial", 24, "bold"),
            bg=dConsts.MAIN_FRAME_COLOR,
        )
        label.pack(pady=30)

        # Generates the border around the text body => box frame
        border_frame = tk.LabelFrame(self, bg=dConsts.MAIN_FRAME_COLOR)
        border_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        # Creating frame for each information column/section => The 3 small frames!
        left_frame = self.sections(border_frame, 0.03)
        middle_frame = self.sections(border_frame, 0.35)
        right_frame = self.sections(border_frame, 0.67)

        # Creating labels for each section/column
        left_header = self.headers(left_frame, "Salt & Pepper Substitute")
        middle_header = self.headers(
            middle_frame, "Decrease phosphorous\nlevels in food"
        )
        right_header = self.headers(right_frame, "Additional Insights")

        # Contents to fill each frame of each category
        left_content = self.frame_contents(left_frame, dConsts.SALT_CONTENT)
        middle_content = self.frame_contents(middle_frame, dConsts.PHOSPHOROUS_CONTENT)
        right_content = self.frame_contents(right_frame, dConsts.ADDITIONAL_CONTENT)

    # Method I used to create the 3 small frames
    def sections(self, frame, relx):
        section_frame = tk.Frame(frame, bg=dConsts.MAIN_FRAME_COLOR)
        section_frame.place(relx=relx, rely=0.08, relwidth=0.31, relheight=0.85)
        return section_frame

    # Header I used to create the header for each small frame
    def headers(self, frame, text):
        header = tk.Label(
            frame, text=text, font=("Arial", 16, "bold"), bg=dConsts.MAIN_FRAME_COLOR
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
                bg=dConsts.MAIN_FRAME_COLOR,
            )
            point.place(relx=0.1, rely=y)
            y += 0.2


# class InfoLeftFrame(Information):
#     def __init__(self):
#         Information.__init__(self)
#         frame = self.sections(, 0.03)


class Nutrients(Page):
    def __init__(self):
        Page.__init__(self)
        label = tk.Label(
            self,
            text="Food Item Nutrition Finder",
            font=("Arial", 20, "bold"),
            bg=dConsts.MAIN_FRAME_COLOR,
        )
        label.pack(pady=20)

        instructions = tk.Message(
            self,
            text="Enter a food item and find its nutrition information for calories, protein, potassium and phosphorous:",
            background=dConsts.MAIN_FRAME_COLOR,
            font=("Arial", 18),
            justify="center",
            aspect=800,
        )
        instructions.pack()

        # Food item entry box
        food_entry = tk.Entry(self)
        food_entry.pack(pady=20)

        # Submit button
        btn = button(
            self,
            text="Submit",
            bg="#5ddeef",
            activebackground="#4285f4",
            font=("Arial", 14),
            command=lambda: self.getting_api(food_entry.get()),
        )
        btn.pack(pady=10)

        second_note = self.note(
            "**All nutrients are based on a portion size of 100g incl. liquids", 0.95
        )
        first_note = self.note(
            "*Source: USDA FoodData Central API",
            0.91,
        )

    def note(self, text, y):
        # additional note marked with '*'
        note = tk.Label(
            self,
            text=text,
            font=10,
            bg=dConsts.MAIN_FRAME_COLOR,
        )
        note.place(relx=0.05, rely=y)
        return note

    def getting_api(self, food):
        API_KEY = "DEMO_KEY"
        # query = input("Enter food item: ")
        query = food
        url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query={query}&dataType=Foundation,Survey%20%28FNDDS%29&pageSize=1&pageNumber=1"
        response = requests.get(url).json()

        nutrient_values = {}
        i = 0
        try:
            for item in response["foods"][0]["foodNutrients"]:
                if (
                    i < len(dConsts.dConsts.NUTRIENT_NAME)
                    and item["nutrientName"] == dConsts.dConsts.NUTRIENT_NAME[i]
                ):
                    nutrient_values[item["value"]] = item["unitName"].lower()
                    i += 1

            nutrient_name_frame = tk.Frame(self, bg=dConsts.MAIN_FRAME_COLOR)
            nutrient_name_frame.place(relx=0.3, rely=0.47, relwidth=0.3, relheight=0.3)

            nutrient_value_frame = tk.Frame(self, bg=dConsts.MAIN_FRAME_COLOR)
            nutrient_value_frame.place(
                relx=0.55, rely=0.47, relwidth=0.08, relheight=0.3
            )

            nutrient_unit_frame = tk.Frame(self, bg=dConsts.MAIN_FRAME_COLOR)
            nutrient_unit_frame.place(
                relx=0.62, rely=0.47, relwidth=0.08, relheight=0.3
            )

            nutrient_lables = self.nutrient_label(
                nutrient_name_frame, dConsts.dConsts.NUTRIENT_NAME
            )

            display_values = self.nutrient_label(nutrient_value_frame, nutrient_values)

            y = 0.2
            for nutrient in nutrient_values:
                display_unit = tk.Label(
                    nutrient_unit_frame,
                    text=nutrient_values[nutrient],
                    font=("Arial", 18),
                    justify="left",
                    bg=dConsts.MAIN_FRAME_COLOR,
                )
                display_unit.place(relx=0.1, rely=y)
                y += 0.2
        except Exception as e:

            # nutrient_name_frame.destroy()
            # nutrient_unit_frame.destroy()
            # nutrient_value_frame.destroy()

            error_frame = tk.Frame(self, bg=dConsts.MAIN_FRAME_COLOR)
            error_frame.place(relx=0.3, rely=0.46, relwidth=0.4, relheight=0.3)

            error_label = tk.Label(
                error_frame,
                text="Item Not Found",
                font=("Arial", 18),
                bg=dConsts.MAIN_FRAME_COLOR,
            )
            error_label.place(relx=0.28, rely=0.3)

    def nutrient_label(self, frame, nutrient_list):
        y = 0.2
        for nutrient in nutrient_list:
            point = tk.Label(
                frame,
                text=nutrient,
                font=("Arial", 18),
                justify="left",
                bg=dConsts.MAIN_FRAME_COLOR,
            )
            point.place(relx=0.1, rely=y)
            y += 0.2


class MenuButton(object):
    def __init__(self, frame, btn_text, raise_content):
        btn = button(
            frame,
            text=btn_text,
            height=100,
            background=dConsts.BTN_COLOR,
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
        guidelines = Guidelines()
        info = Information()
        recipe = Nutrients()

        # App header placed into main window
        self.frame = frame
        self.header = tk.Label(
            self.frame,
            text="Dialysis Nutrition Information",
            justify="center",
            bg=dConsts.MAIN_WINDOW_COLOR,
            font=("Arial", 32, "bold"),
        )
        self.header.place(relx=0.42, rely=0.1)

        button_frame = tk.Frame(self.frame)
        button_frame.place(relx=0.025, rely=0.2, relwidth=0.2, relheight=0.65)
        content_frame = tk.Frame(self.frame)
        content_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

        intro.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
        calculator.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
        guidelines.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
        info.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)
        recipe.place(in_=content_frame, x=0, y=0, relwidth=1, relheight=1)

        intro_btn = MenuButton(button_frame, "Intro", intro.show)
        calculator_btn = MenuButton(button_frame, "Calculator", calculator.show)
        guidelines_btn = MenuButton(button_frame, "Guidelines", guidelines.show)
        info_btn = MenuButton(button_frame, "Tips & Tricks", info.show)
        recipe_btn = MenuButton(button_frame, "Nutrients", recipe.show)

        intro.show()


if __name__ == "__main__":
    window = tk.Tk()
    window.title(dConsts.WINDOW_TITLE)
    window.configure(bg=dConsts.MAIN_WINDOW_COLOR)
    main = MainWindow(window)
    main.pack()
    window.wm_geometry(dConsts.MAIN_WINDOW_SIZE)
    window.mainloop()
