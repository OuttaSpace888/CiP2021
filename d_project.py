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

    tips_frame = tk.Frame(window, bg='light blue')
    tips_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    slides_frame = tk.Frame(window, bg='yellow')
    slides_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    intro_frame = tk.Frame(window, bg='olive')
    intro_frame.place(relx=0.225, rely=0.2, relwidth=0.75, relheight=0.65)

    # Button frame containing all buttons
    button_frame = tk.Frame(window, bg=MAIN_FRAME_COLOR)
    button_frame.place(relx=0.025, rely=0.2, relwidth=0.2, relheight=0.65)

    calculator_site_content(calc_frame)
    diet_tabs(nutr_frame)
    # Creating buttons with butt() and naming them
    butt("Intro", button_frame, intro_frame)
    butt("Calculator", button_frame, calc_frame)
    butt("Nutrition", button_frame, nutr_frame)
    butt("Tips & Tricks", button_frame, tips_frame)
    butt("Slides", button_frame, slides_frame)

    window.resizable(True, True)
    window.mainloop()


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


# Rounds number > = 0.5 up, else down
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def swap_frames(frame):
    frame.tkraise()


# Calculates daily intakes and displays them on the screen
def weight_calc(frame, weight):
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
def calculator_site_content(calc_frame):
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
        command=lambda: weight_calc(calc_frame, weight_entry.get()),
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
def diet_tabs(frame):
    notebook = ttk.Notebook(frame)
    notebook.pack()

    # Creating frame for each tab
    good_foods_frame = tk.Frame(notebook, width=900, height=500, bg='#26c96f')
    bad_foods_frame = tk.Frame(notebook, width=900, height=500, bg='#f9a08b')
    nutrition_frame = tk.Frame(notebook, width=900, height=500, bg="orange")

    # Packing each frame into notebook frame and naming each tab
    frames = [good_foods_frame, bad_foods_frame, nutrition_frame]
    tab_names = ["Recommended Foods", "Foods to Avoid", "Nutrition"]
    i = 0
    for frame in frames:
        frame.pack(fill="both", expand=1)
        notebook.add(frame, text=tab_names[i])
        i += 1
    # Recommended Foods Tab
    title = tk.Label(
        good_foods_frame,
        text="Low levels of phosphorous and potassium foods",
        font=("Arial", 18),
        bg='#26c96f',
    ).pack(pady=25)

    g_labels_frame_left = tk.Frame(good_foods_frame, bg=MAIN_FRAME_COLOR)
    g_labels_frame_left.place(relx=0.1, rely=0.2, relwidth=0.4)

    g_list1 = [
        "Zucchini",
        "Cucumbers",
        "Blueberries",
        "Apple",
        "Salads",
        "Couscous",
        "lean Meat",
        "most Fish",
        "Cauliflower",
        'Olive Oil',
        "Butter",
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
        "Radish",
        "green Pepper",
        "Strawberries",
        "Orange",
        "Cream",
        "Mozzarella",
        "Onion",
        "Garlic",
        "Eggs",
        "Watermelon",
        "Honey"
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
    title = tk.Label(
        bad_foods_frame,
        text="High levels of phosphorous and potassium foods",
        font=("Arial", 18),
        bg='#f9a08b',
    ).pack(pady=25)

    b_labels_frame_left = tk.Frame(bad_foods_frame, bg=MAIN_FRAME_COLOR)
    b_labels_frame_left.place(relx=0.1, rely=0.2, relwidth=0.4)

    b_list1 = [
        "Feta, Parmesan, Cheddar etc.",
        "Milk",
        "Sausages",
        "Smoked Fish or Meat",
        "Processed Foods",
        "Potatoes",
        "Offal",
        "Salmon",
        "Canned Fish",
        'Saturated Fat',
        "Nuts",
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
        "Nougat",
        "Marzipan",
        "Undiluted Fruit Juice",
        "Vegetable Juice",
        "Ketchup",
        "Mayonnaise",
        "Tzatziki",
        "Curry",
        "Aubergine",
        "Salt, Pepper"
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


if __name__ == "__main__":
    main()
