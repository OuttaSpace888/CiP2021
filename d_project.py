import tkinter as tk
from tkinter import ttk
from tkmacosx import Button as button


def main():
    window = tk.Tk()
    window.title("Dialysis Diet Assistant By Yihan Ye")
    window.geometry("900x900")
    window.configure(bg="#bedddc")

    # Generating header and placing it into main window
    header_frame = tk.Frame(window, bg="#bedddc")
    header_frame.place(relx=0.22, rely=0.08, relwidth=0.75, relheight=0.15)
    header = tk.Label(
        header_frame,
        text="Dialysis Nutrition Information",
        justify="center",
        bg="#bedddc",
        font=("Arial", 32, "bold"),
    )
    header.place(relx=0.17, rely=0.25)

    # Main frame where all information appear in
    frame = tk.Frame(window, bg="#f4efeb")
    frame.place(relx=0.22, rely=0.2, relwidth=0.74, relheight=0.65)
    # Button frame containing all buttons
    button_frame = tk.Frame(window, bg="green")
    button_frame.place(relx=0.025, rely=0.2, relwidth=0.2, relheight=0.65)

    # diet_tabs(frame)
    calculator_frame(frame)
    # Creating buttons with butt() and naming them
    btn_names = ["Calculator", "Nutrition", "Tips & Tricks", "Slides"]
    for name in btn_names:
        butt(name, button_frame)

    # btn_calc = butt('Calculator', button_frame, calculator_frame(frame))
    # btn_nutr = butt("Nutrition", button_frame, diet_tabs(frame))

    window.resizable(True, True)
    window.mainloop()

def weight_calc(weight):
    daily_calories = float(weight) * 30
    print("Your daily energy requirement is", daily_calories, "!")



def calculator_frame(frame):
    weight_label = tk.Label(
        frame,
        text="Enter your weight in kg:",
        font=("Arial", 18),
        bg="#f4efeb",
    )
    weight_label.place(relx=0.1, rely=0.15)

    weight_entry = tk.Entry(frame)
    weight_entry.place(relx=0.1, rely=0.25, relwidth=0.3)

    weight_btn = button(
        frame, text="Submit", bg='#5ddeef', activebackground="#4285f4", font=("Arial", 14), command=lambda:weight_calc(weight_entry.get())
    )
    weight_btn.place(relx=0.42, rely=0.25)


# Generating tabs to divide the diet section into 3 parts
# without adding more buttons and using more space
def diet_tabs(frame):
    notebook = ttk.Notebook(frame)
    notebook.pack()

    # Creating frame for each tab
    good_foods_frame = tk.Frame(notebook, width=900, height=500, bg="olive")
    bad_foods_frame = tk.Frame(notebook, width=900, height=500, bg="red")
    nutrition_frame = tk.Frame(notebook, width=900, height=500, bg="orange")

    # Packing each frame into notebook frame and naming each tab
    frames = [good_foods_frame, bad_foods_frame, nutrition_frame]
    tab_names = ["Recommended Foods", "Foods to Avoid", "Nutrition"]
    i = 0
    for frame in frames:
        frame.pack(fill="both", expand=1)
        notebook.add(frame, text=tab_names[i])
        i += 1


# Creating buttons for each category. Buttons are lined up one on the side.
def butt(btn_text, frame):
    btn = button(
        frame,
        text=btn_text,
        height=125,
        background="#e5c5c8",
        activebackground="orange",
        # activeforeground="black",
        font=("Arial", 24),
        relief="raised",
        # command=func
    )
    btn.pack(fill="x")


if __name__ == "__main__":
    main()
