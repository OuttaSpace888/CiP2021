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

    # Content frame for each category
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
    # Creating buttons with butt() and naming them
    butt("Intro", button_frame, intro_frame)
    butt("Calculator", button_frame, calc_frame)
    butt("Nutrition", button_frame, nutr_frame)
    butt("Tips & Tricks", button_frame, tips_frame)
    butt("Slides", button_frame, slides_frame)

    # Running all frames
    intro_content(intro_frame)
    calculator_content(calc_frame)
    nutrition_tabs(nutr_frame)
    tips_content(tips_frame)
    slides_content(slides_frame)

    window.resizable(True, True)
    window.mainloop()


# Rounds number > = 0.5 up, else down
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


# Raises frame according to which button is pressed
def swap_frames(frame):
    frame.tkraise()


# Creating menu buttons for each category, which are lined up one on the side.
# Including command for each button pressed
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
    # Welcome Header for App
    title = tk.Label(
        frame,
        text="Welcome to the Dialysis Nutrition App!",
        bg=MAIN_FRAME_COLOR,
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    # Introduction text created and packed into frame
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
    # Converts weight into float for accurate calculation with the help of round_half_up() function,
    # rounds the number and return as integer
    daily_calories = int(round_half_up(float(weight.strip().strip("kg")) * 30))
    calories_result = f"Calories per day: {daily_calories}"

    daily_protein = int(round_half_up(float(weight.strip().strip("kg")) * 1.2))
    protein_result = f"Protein per day: {daily_protein}"
    # Label that contains the results
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

    # additional note marked with '*'
    note = tk.Label(
        calc_frame,
        text="*All numbers are rounded to the nearest ones place",
        bg=MAIN_FRAME_COLOR,
    )
    note.place(relx=0.05, rely=0.9)


# Generating tabs to divide the diet section into 4 parts
# without adding more buttons and using more space
def nutrition_tabs(frame):
    # Creating notebook for tabs
    notebook = ttk.Notebook(frame)
    notebook.pack()

    # Creating frame for each tab
    intake_frame = tk.Frame(notebook, width=900, height=500, bg=MAIN_FRAME_COLOR)
    good_foods_frame = tk.Frame(notebook, width=900, height=500, bg="#5ece08")
    bad_foods_frame = tk.Frame(notebook, width=900, height=500, bg="#f9a08b")
    api_frame = tk.Frame(notebook, width=900, height=500, bg=MAIN_FRAME_COLOR)

    # Packing each tab frame into notebook frame and naming each tab
    frames = [intake_frame, good_foods_frame, bad_foods_frame, api_frame]
    tab_names = ["Daily Intake", "Recommended Foods", "Foods to Avoid", "Nutrition API"]
    i = 0
    for frame in frames:
        frame.pack(fill="both", expand=1)
        notebook.add(frame, text=tab_names[i])
        i += 1

    # Daily Intake Tab Section
    # Tab Label for Daily
    intake_title = tk.Label(
        intake_frame,
        text="Daily Nutrients Guideline",
        font=("Arial", 20),
        bg=MAIN_FRAME_COLOR,
    ).pack(pady=25)

    # Daily Frames Section
    left_frame = tk.Frame(intake_frame, bg=MAIN_FRAME_COLOR)
    left_frame.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.8)
    right_frame = tk.Frame(intake_frame, bg=MAIN_FRAME_COLOR)
    right_frame.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.8)

    # Nutrients dictionary for creating chart.
    # Key => left, Value => right
    daily_nutrients = {
        "Calories": "30cal/kg per day",
        "Protein": "1,2g/kg per day",
        "Liquid": "500ml + residual excretion/24h",
        "Salt": "5-6g salt per day",
        "Potassium": "2000-2500mg per day",
        "Phosphorous": "1000-1400mg per day"
    }
    l_y = 0.1
    for point in daily_nutrients:
        point = tk.Label(
            left_frame,
            text=point,
            font=("Arial", 18, 'bold'),
            justify="left",
            bg=MAIN_FRAME_COLOR,
        )
        point.place(relx=0.1, rely=l_y)
        l_y += 0.1

    r_y = 0.1
    for point in daily_nutrients:
        point = tk.Label(
            right_frame,
            text=daily_nutrients[point],
            font=("Arial", 18),
            justify="left",
            bg=MAIN_FRAME_COLOR,
        )
        point.place(relx=0.1, rely=r_y)
        r_y += 0.1

    # Recommended Foods Tab Section
    low_title = tk.Label(
        good_foods_frame,
        text="Low levels of phosphorous and potassium foods",
        font=("Arial", 18),
        bg="#5ece08",
    ).pack(pady=25)

    # Recommended food frames
    g_labels_frame_left = tk.Frame(good_foods_frame, bg='#5ece08')
    g_labels_frame_left.place(relx=0.1, rely=0.2, relwidth=0.4)
    g_labels_frame_right = tk.Frame(good_foods_frame, bg='#5ece08')
    g_labels_frame_right.place(relx=0.5, rely=0.2, relwidth=0.4)
    # Food to Avoid frames
    b_labels_frame_left = tk.Frame(bad_foods_frame, bg="#f9a08b")
    b_labels_frame_left.place(relx=0.1, rely=0.2, relwidth=0.4)
    b_labels_frame_right = tk.Frame(bad_foods_frame, bg="#f9a08b")
    b_labels_frame_right.place(relx=0.5, rely=0.2, relwidth=0.4)

    # g_list1 = [
    #     "Zucchini, Cucumbers",
    #     "Lemons, Lime",
    #     "Blueberries",
    #     "Apple, Pears",
    #     "Salads",
    #     "Couscous",
    #     "lean Meat",
    #     "most Fish",
    #     "Cauliflower",
    #     "Olive Oil, Butter",
    #     "Mushrooms",
    # ]
    
    for item in g_list1:
        g_food_left = tk.Label(
            g_labels_frame_left,
            text=item,
            font=("Arial", 16),
            bg="#5ece08",
            anchor="w",
        )
        g_food_left.pack()

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
            bg="#5ece08",
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
        "Coconuts, Nuts",
    ]
    for item in b_list1:
        b_food_left = tk.Label(
            b_labels_frame_left,
            text=item,
            font=("Arial", 16),
            bg="#f9a08b",
            anchor="w",
        )
        b_food_left.pack()

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
        "Dates, Figs",
        "Avocados",
    ]
    for item in b_list2:
        b_food_right = tk.Label(
            b_labels_frame_right,
            text=item,
            font=("Arial", 16),
            bg="#f9a08b",
            anchor="w",
        )
        b_food_right.pack()


def tips_content(frame):
    prep_title = tk.Label(
        frame,
        text="Important Things to Note",
        font=("Arial", 24, "bold"),
        bg=MAIN_FRAME_COLOR,
    ).pack(pady=30)

    prep_tips_frame = tk.Frame(frame, bg=MAIN_FRAME_COLOR)
    prep_tips_frame.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.7)
    seasoning_frame = tk.Frame(frame, bg=MAIN_FRAME_COLOR)
    seasoning_frame.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.7)
    other__info_frame = tk.Frame(frame, bg=MAIN_FRAME_COLOR)
    other__info_frame.place(relx=0.65, rely=0.2, relwidth=0.31, relheight=0.7)

    prep_header = tk.Label(
        prep_tips_frame,
        text="Decreasing phosphorous\nlevels in food",
        font=("Arial", 16, "bold"),
        bg=MAIN_FRAME_COLOR,
    ).pack(pady=10)
    seasoning_header = tk.Label(
        seasoning_frame,
        text="Salt & Pepper Substitute",
        font=("Arial", 16, "bold"),
        bg=MAIN_FRAME_COLOR,
    ).pack(pady=10)
    others_header = tk.Label(
        other__info_frame,
        text="Additional Insights",
        font=("Arial", 16, "bold"),
        bg=MAIN_FRAME_COLOR,
    ).pack(pady=10)

    prep_content = {
        "first": "- throw out cooking water\n  and change while cooking",
        "second": "- throw away canned\n  vegetables & meat juice",
        "third": "- soak diced vegetables in\n  water before cooking",
        "fourth": "- dice or shred vegetables\n  with high  phosphorous\n  content",
    }
    y = 0.2
    for point in prep_content:
        point = tk.Label(
            prep_tips_frame,
            text=prep_content[point],
            font=("Arial", 16),
            justify="left",
            bg=MAIN_FRAME_COLOR,
        )
        point.place(relx=0.1, rely=y)
        y += 0.2

    salt_content = {
        "first": "- Don't use salt substitute!\n  Use alternatives instead",
        "second": "- Season food after it's\n  cooked for more control",
        "third": "- Alternatives are:\n  Basil, Cilantro, Garlic\n  Oregano, Mint, Chives\n  Lemon, Parsley, Sage",
    }
    y = 0.2
    for point in salt_content:
        point = tk.Label(
            seasoning_frame,
            text=salt_content[point],
            font=("Arial", 16),
            justify="left",
            bg=MAIN_FRAME_COLOR,
        )
        point.place(relx=0.1, rely=y)
        y += 0.2

    more_tips_content = {
        "first": "- Avoid eating animal skin\n  (poultry)",
        "second": "- Try not to eat egss more\n   than 3x per week",
        "third": " - Pre-fill your water bottle\n    for the entire day",
        "fourth": " - Don't forget food contains\n    water as well!\n   (fruits, soup, ice cream)",
    }
    y = 0.2
    for point in more_tips_content:
        point = tk.Label(
            other__info_frame,
            text=more_tips_content[point],
            font=("Arial", 16),
            justify="left",
            bg=MAIN_FRAME_COLOR,
        )
        point.place(relx=0.1, rely=y)
        y += 0.2


def slides_content(frame):
    pass


if __name__ == "__main__":
    main()
