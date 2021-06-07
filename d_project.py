import tkinter as tk
from tkinter import ttk
from tkmacosx import Button as button
import math


MAIN_FRAME_COLOR = "#f4efeb"


def main():
    window = tk.Tk()
    window.title("Dialysis Nutrition Information By Yihan Ye")
    window.geometry("900x900")
    window.configure(bg="#bedddc")

    # Generating header and placing it into main window
    header = tk.Label(
        window,
        text="Dialysis Nutrition Information",
        justify="center",
        bg="#bedddc",
        font=("Arial", 32, "bold"),
    )
    header.place(relx=0.35, rely=0.1)

    # Frame for each button category
    calc_frame = tk.Frame(window, bg=MAIN_FRAME_COLOR)
    calc_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    nutr_frame = tk.Frame(window, bg=MAIN_FRAME_COLOR)
    nutr_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    tips_frame = tk.Frame(window, bg=MAIN_FRAME_COLOR)
    tips_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    slides_frame = tk.Frame(window, bg="yellow")
    slides_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    intro_frame = tk.Frame(window, bg=MAIN_FRAME_COLOR)
    intro_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    # Button frame containing all buttons
    button_frame = tk.Frame(window, bg=MAIN_FRAME_COLOR)
    button_frame.place(relx=0.025, rely=0.2, relwidth=0.2, relheight=0.65)

    intro_content(intro_frame)
    calculator_content(calc_frame)
    nutrition_tabs(nutr_frame)
    tips_content(tips_frame)
    slides_content(slides_frame)
    # Creating buttons with butt() and naming them
    butt("Intro", button_frame, intro_frame)
    butt("Calculator", button_frame, calc_frame)
    butt("Nutrition", button_frame, nutr_frame)
    butt("Tips & Tricks", button_frame, tips_frame)
    butt("Slides", button_frame, slides_frame)

    window.resizable(True, True)
    window.mainloop()


# Rounds number > = 0.5 up, else down
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def swap_frames(frame):
    frame.tkraise()


# Creating buttons for each category. Buttons are lined up one on the side.
def butt(btn_text, frame, raise_frame):
    btn = button(
        frame,
        text=btn_text,
        height=100,
        background="#e5c5c8",
        activebackground="orange",
        # activeforeground="black",
        font=("Arial", 24),
        relief="raised",
        command=lambda: swap_frames(raise_frame),
    )
    btn.pack(fill="both")


def intro_content(frame):
    title = tk.Label(
        frame,
        text="Welcome to the Dialysis Nutrition App!",
        bg=MAIN_FRAME_COLOR,
        font=("Arial", 24, "bold"),
    ).pack(pady=30)

    intro_text = (
        "Here you can find recommended foods to eat for dialysis patients as well as which foods to avoid. You can also find nutrition information for individual food items of your choice with the built in API!\n"
        "\nUse the calculator to determine your daily energy and protein intake for a balanced diet.\n"
        "\nCheck out the other tabs for additional useful information that can help you consume your favorite foods in a safe way!"
    )
    message = tk.Message(
        frame,
        text=intro_text,
        font=("Arial", 18),
        bg=MAIN_FRAME_COLOR,
    ).pack(pady=20)


# Calculates daily intakes and displays them on the screen
def calculating_weight(frame, weight):
    # Converts weight into float for accurate calculation, rounds the number and return as integer
    daily_calories = int(round_half_up(float(weight.strip().strip("kg")) * 30))
    calories_result = f"Calories per day: {daily_calories}"

    daily_protein = int(round_half_up(float(weight.strip().strip("kg")) * 1.2))
    protein_result = f"Protein per day: {daily_protein}"

    display_calories = tk.Label(
        frame, text=calories_result, bg=MAIN_FRAME_COLOR, font=("Arial", 18)
    )
    display_calories.pack(pady=25)

    display_protein = tk.Label(
        frame, text=protein_result, bg=MAIN_FRAME_COLOR, font=("Arial", 18)
    )
    display_protein.pack()


# Generates label, entry box and submit button for weight input
def calculator_content(calc_frame):
    # Instructions Label
    instructions = tk.Label(
        calc_frame,
        text="Calculate your daily energy and protein intake requirements.",
        font=("Arial", 20),
        bg=MAIN_FRAME_COLOR,
    )
    instructions.pack(pady=25)

    # Enter weight, label
    weight_label = tk.Label(
        calc_frame,
        text="Enter your weight in kg:",
        font=("Arial", 18),
        bg=MAIN_FRAME_COLOR,
    )
    weight_label.pack(pady=10)

    # Weight entry box
    weight_entry = tk.Entry(calc_frame)
    weight_entry.pack(pady=10)

    # Weight submit button
    weight_btn = button(
        calc_frame,
        text="Submit",
        bg="#5ddeef",
        activebackground="#4285f4",
        font=("Arial", 14),
        command=lambda: calculating_weight(calc_frame, weight_entry.get()),
    )
    weight_btn.pack(pady=10)

    # additional information
    note = tk.Label(
        calc_frame,
        text="*All numbers are rounded to the nearest ones place",
        bg=MAIN_FRAME_COLOR,
    )
    note.place(relx=0.05, rely=0.9)


# Generating tabs to divide the diet section into 3 parts
# without adding more buttons and using more space
def nutrition_tabs(frame):
    notebook = ttk.Notebook(frame)
    notebook.pack()

    # Creating frame for each tab
    intake_frame = tk.Frame(notebook, width=900, height=500, bg=MAIN_FRAME_COLOR)
    good_foods_frame = tk.Frame(notebook, width=900, height=500, bg="#5ece08")
    bad_foods_frame = tk.Frame(notebook, width=900, height=500, bg="#f9a08b")
    api_frame = tk.Frame(notebook, width=900, height=500, bg="orange")

    # Packing each frame into notebook frame and naming each tab
    frames = [intake_frame, good_foods_frame, bad_foods_frame, api_frame]
    tab_names = ["Daily Intake", "Recommended Foods", "Foods to Avoid", "Nutrition API"]
    i = 0
    for frame in frames:
        frame.pack(fill="both", expand=1)
        notebook.add(frame, text=tab_names[i])
        i += 1

    # Daily Intake Tab
    intake_title = tk.Label(
        intake_frame,
        text="Daily Nutrients Guideline",
        font=("Arial", 18),
        bg=MAIN_FRAME_COLOR,
    ).pack(pady=25)

    # Recommended Foods Tab
    low_title = tk.Label(
        good_foods_frame,
        text="Low levels of phosphorous and potassium foods",
        font=("Arial", 18),
        bg="#5ece08",
    ).pack(pady=25)

    g_labels_frame_left = tk.Frame(good_foods_frame, bg=MAIN_FRAME_COLOR)
    g_labels_frame_left.place(relx=0.1, rely=0.2, relwidth=0.4)

    g_list1 = [
        "Zucchini, Cucumbers",
        "Lemons, Lime",
        "Blueberries",
        "Apple, Pears",
        "Salads",
        "Couscous",
        "lean Meat",
        "most Fish",
        "Cauliflower",
        "Olive Oil, Butter",
        "Mushrooms",
    ]
    for item in g_list1:
        g_food_left = tk.Label(
            g_labels_frame_left,
            text=item,
            font=("Arial", 16),
            bg=MAIN_FRAME_COLOR,
            anchor="w",
        )
        g_food_left.pack()

    g_labels_frame_right = tk.Frame(good_foods_frame, bg=MAIN_FRAME_COLOR)
    g_labels_frame_right.place(relx=0.5, rely=0.2, relwidth=0.4)

    g_list2 = [
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
    for item in g_list2:
        g_food_right = tk.Label(
            g_labels_frame_right,
            text=item,
            font=("Arial", 16),
            bg=MAIN_FRAME_COLOR,
            anchor="w",
        )
        g_food_right.pack()

    # Foods to Avoid Tab
    high_title = tk.Label(
        bad_foods_frame,
        text="High levels of phosphorous and potassium foods",
        font=("Arial", 18),
        bg="#f9a08b",
    ).pack(pady=25)

    b_labels_frame_left = tk.Frame(bad_foods_frame, bg=MAIN_FRAME_COLOR)
    b_labels_frame_left.place(relx=0.1, rely=0.2, relwidth=0.4)

    b_list1 = [
        "Feta, Parmesan, Cheddar etc.",
        "Most Dairy Products",
        "Offal, Sausages, Salmon",
        "Smoked Fish or Meat",
        "Processed Foods",
        "Potatoes",
        "Canned Tomato Products/Juice",
        "Olives,Pickles, Relish",
        "Canned Fish, Meat, Beans",
        "Saturated Fat",
        "Coconuts, Nuts, Dates",
    ]
    for item in b_list1:
        b_food_left = tk.Label(
            b_labels_frame_left,
            text=item,
            font=("Arial", 16),
            bg=MAIN_FRAME_COLOR,
            anchor="w",
        )
        b_food_left.pack()

    b_labels_frame_right = tk.Frame(bad_foods_frame, bg=MAIN_FRAME_COLOR)
    b_labels_frame_right.place(relx=0.5, rely=0.2, relwidth=0.4)

    b_list2 = [
        "Chocolate",
        "Dried Fruits",
        "Marzipan",
        "Undiluted Fruit Juice",
        "Vegetable Juice",
        "Ketchup, Mayonnaise",
        "Tee, Cola",
        "Tzatziki",
        "Bananas, Kiwis",
        "Aubergine",
        "Avocados",
    ]
    for item in b_list2:
        b_food_right = tk.Label(
            b_labels_frame_right,
            text=item,
            font=("Arial", 16),
            bg=MAIN_FRAME_COLOR,
            anchor="w",
        )
        b_food_right.pack()


def tips_content(frame):
    title = tk.Label(
        frame, text="Useful Insights", font=("Arial", 24, "bold"), bg=MAIN_FRAME_COLOR
    ).pack(pady=30)

    frame_names =['prep_tips_frame', 'seasoning_frame', 'other_info_frame']

    prep_tips_frame = tk.Frame(frame, bg='orange').place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.7)
    seasoning_frame = tk.Frame(frame, bg='yellow').place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.7)
    other__info_frame = tk.Frame(frame, bg='light blue').place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.7)



def slides_content(frame):
    pass


if __name__ == "__main__":
    main()
