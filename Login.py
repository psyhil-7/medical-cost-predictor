import os
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import Tk, Label
from PIL import Image, ImageTk, ImageEnhance
#from datetime import datetime
import itertools
from tkinter import messagebox

from tkinter import font
import time
import math
#from datetime import datetime
#from patient_gui import open_patient_gui
import joblib
import csv 
from tkinter import messagebox
from tkinter import messagebox, filedialog

import platform
from itertools import cycle



from tkinter import Toplevel, Label, Frame
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg









def center_window(window, width, height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")




root = tk.Tk()
root.title("Login")
center_window(root, 400, 500)

root.configure(bg="#0d0d0d")
root.resizable(False, False)



bg_image = Image.open("img-bg/2.jpg") 
bg_image = bg_image.resize((400, 500))  # Resize to fit window
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

 # Cover entire window



frame = tk.Frame(root, bg="black", bd=2, relief="solid") # Background color to match theme
frame.place(relx=0.5, rely=0.4, anchor="center")

# Title Label (Place it AFTER the background image)
# Title Label (Over Background Image)

# Load and display an icon above the title
icon_image = Image.open("img-bg/hospital.png")  # Replace with your icon file
icon_image = icon_image.resize((50, 50))  # Resize as needed
icon_photo = ImageTk.PhotoImage(icon_image)
icon_label = tk.Label(root, image=icon_photo, bg="black")  # Match the background color
icon_label.image = icon_photo  # Keep a reference
icon_label.place(relx=0.5, rely=0.08, anchor="center")  # Adjust position

custom_font = ("Orbitron", 16, "bold")
title_label = tk.Label(root, text="Medical Insurance Predictor", 
                       font=custom_font, fg="#00ffcc", bg="black", padx=10, pady=5) 
title_label.place(relx=0.5, rely=0.16, anchor="center")  # Moved slightly downward




#username
username_label = tk.Label(frame, text="Enter Username:", fg="white", bg="black", font=("Arial", 12))
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

username_entry = tk.Entry(frame, font=("Arial", 12), width=18, bg="#222", fg="white", insertbackground="white")
username_entry.grid(row=0, column=1, padx=10, pady=10)
#password
password_label = tk.Label(frame, text="Enter Password:", fg="white", bg="black", font=("Arial", 12))
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
password_entry = tk.Entry(frame, font=("Arial", 12), show="*", width=18, bg="#222", fg="white", insertbackground="white")
password_entry.grid(row=1, column=1, padx=10, pady=10)


import tkinter.ttk as ttk
def show_loading_then_main(username):
    splash = tk.Toplevel(root)
    splash.overrideredirect(True)
    splash.geometry("300x150+500+300")  # Adjust position
    splash.configure(bg="#0f0f0f")

    label = tk.Label(splash, text="Loading Dashboard...", fg="lightgreen", bg="#0f0f0f", font=("Orbitron", 14))
    label.pack(expand=True, pady=20)

    progress = ttk.Progressbar(splash, mode="indeterminate", length=200)
    progress.pack(pady=10)
    progress.start()



    def launch_main():
        splash.destroy()
        open_dashboard(username)

    splash.after(3000, launch_main)

#function
def login ():
  
     username = username_entry.get()
     password = password_entry.get()

     if username == "admin" and password == "password":
        result_label.config(text="Login is Successful", fg="lime")
        root.after(1000, lambda: show_loading_then_main(username))
     else:
        result_label.config(text="Invalid Username or Password. Please try again.", fg="red")


#login_button
def on_enter(e):
    login_button.config(bg="#00ffcc", fg="black")

def on_leave(e):
    login_button.config(bg="#008080", fg="white")

login_button = tk.Button(root, text="Login", font=("Arial", 12, "bold"), 
                         bg="#008080", fg="white", relief="flat", command=login)
login_button.place(relx=0.5, rely=0.55, anchor="center")
login_button.bind("<Enter>", on_enter)
login_button.bind("<Leave>", on_leave)



# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#0d0d0d", fg="white")
result_label.place(relx=0.5, rely=0.65, anchor="center")


 


def update_time():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')  # Fix: Use datetime.datetime
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Fix: Use datetime.datetime

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    dashboard.after(1000, update_time)  # Call every second



from tkinter import Button

def open_dashboard(username):
    root.withdraw()
    global dashboard
    dashboard = tk.Toplevel()
    dashboard.title("Medical Prediction Dashboard")
    #dashboard.geometry("800x500")
   
    # Center Dashboard Window
    window_width = 800
    window_height = 500

    screen_width = dashboard.winfo_screenwidth()  # Get screen width
    screen_height = dashboard.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)  # Calculate top position
    position_left = int(screen_width / 2 - window_width / 2) 

    dashboard.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')



    
   




    


   # check_icon = load_icon("user.png")  # Adjust the filename

# Create button with an icon
   # check_button = tk.Button(dashboard, text="Check Insurance", image=check_icon, compound="left", padx=10, pady=5)
   # check_button.place(relx=0.5, rely=0.6, anchor="center")

    #load image
    bg_image = Image.open("img-bg/background1.webp")  # Ensure the correct filename
    bg_image = bg_image.resize((800, 500))  # Resize to fit window
    bg_photo = ImageTk.PhotoImage(bg_image)

    enhancer = ImageEnhance.Brightness(bg_image)
    bg_image = enhancer.enhance(0.20)

    bg_photo = ImageTk.PhotoImage(bg_image)

    dashboard.bg_photo = bg_photo
    
    


    # Set background image using a Label
    bg_label = tk.Label(dashboard, image=dashboard.bg_photo)
    bg_label.place(relwidth=1, relheight=1)  # Cover entire window

    welcome_label = tk.Label(dashboard, text=f"Welcome, Admin !", font=("Arial", 14, "bold"), fg="white", bg="#1E272E")
    welcome_label.place(relx=0.5, rely=0.1, anchor = "center")

   # date time label
    global time_label, date_label
    time_label = tk.Label(dashboard, font=("Arial", 12), fg="White", bg="#1E272E")
    time_label.place(relx=0.02, rely=0.02, anchor="nw")
    
    date_label = tk.Label(dashboard, font=('Arial', 12), fg="White", bg = "#1E272E")
    date_label.place(relx=0.02, rely=0.06, anchor="nw")

  
    dashboard.after(1000, update_time)  

    #inurance button
    check_insurance_button = tk.Button(dashboard, text="Check Insurance", font=("Arial", 12), bg="#3498DB", fg="white", padx=10, pady=5, command=open_patient_gui)
    check_insurance_button.place(relx=0.5, rely=0.3, anchor="center")

    view_data_button = tk.Button(
        dashboard,
        text="View Patient Data",
        font=("Segoe UI", 12),
        bg="#1f1f1f",
        fg="white",
        padx=10,
        pady=5,
        command=view_all_patients
    )
    view_data_button.place(relx=0.5, rely=0.45, anchor="center")

    

    

        # FAQ function
    def show_faq():
        faq_window = tk.Toplevel(dashboard)
        faq_window.title("FAQ - Help")
        faq_window.geometry("400x300")
        faq_window.configure(bg="#f5f5f5")

        faq_title = tk.Label(faq_window, text="Frequently Asked Questions", font=("Helvetica", 14, "bold"), bg="#f5f5f5", fg="#333")
        faq_title.pack(pady=10)

        faqs = [
            "Q1: How do I check insurance cost?\nA: Click on 'Check Insurance' and fill the form.",
            "Q2: Where is patient data stored?\nA: In the 'insurance.csv' file.",
            "Q3: Can I download receipts?\nA: Yes, from the receipt window after prediction.",
            "Q4: Who can access the dashboard?\nA: Only authorized users via login."
        ]

        for faq in faqs:
            tk.Label(faq_window, text=faq, wraplength=350, justify="left", bg="#f5f5f5", fg="#000", font=("Arial", 10)).pack(anchor="w", padx=15, pady=5)

    # Function to start the image carousel
  
   



        


        



        # Logout function to close dashboard and return to login
    def logout():
        if messagebox.askyesno("Logout", "Do you want to logout?"):
            dashboard.destroy()


    # Logout Button
    logout_button = tk.Button(dashboard, text="Logout", font=("Orbitron", 12),
                              bg="#FF5555", fg="white", padx=10, pady=5,
                              command=logout, relief="flat", activebackground="#FF8C00")
    logout_button.place(relx=0.95, rely=0.95, anchor="se")

    faq_button = tk.Button(dashboard, text="FAQ", font=("Orbitron", 11),
                       bg="#4B7BEC", fg="white", padx=8, pady=3,
                       command=show_faq, relief="flat", activebackground="#5F9DF7")
    faq_button.place(relx=0.985, rely=0.01, anchor="ne")



import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def view_all_patients():
    file_path = "insurance.csv"
    if os.path.exists(file_path):
        try:
            if platform.system() == "Windows":
                os.startfile(file_path)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{file_path}'")
            else:  # Linux
                os.system(f"xdg-open '{file_path}'")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

    else:
        messagebox.showerror("File Not Found", "No patient data found.")








def open_patient_gui():
    global entries, smoker_var, region_var, patient_root, sex_var, result_label

    entries = []
    region_var = tk.StringVar()
    sex_var = tk.StringVar()
    smoker_var = tk.StringVar()

    patient_root = tk.Toplevel()
    patient_root.title("Patient Form")
    #patient_root.geometry("800x500")

    width, height = 800, 500
    screen_width = patient_root.winfo_screenwidth()
    screen_height = patient_root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window geometry to be centered on the screen
    patient_root.geometry(f"{width}x{height}+{x}+{y}")

    

    # Load background image
    bg_image = Image.open("img-bg/formgui.jpg")
    bg_image = bg_image.resize((800, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(patient_root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
    patient_root.bg_photo = bg_photo  # Keep reference

    tk.Label(patient_root, text="PATIENT FORM", font=("Orbitron", 22, "bold"), fg="#00FFFF", bg="#0A192F").pack(pady=10)

    # Frame for Form Layout
    form_frame = tk.Frame(patient_root, bg="#0A192F")
    form_frame.place(relx=0.5, rely=0.45, anchor="center")

    # Labels and Entry Fields
    labels = ["Patient Name:", "Age:", "BMI:", "Children:", "Smoker:", "Region:", "Sex:"]
    for i, label in enumerate(labels):
        tk.Label(form_frame, text=label, font=("Orbitron", 12), fg="#00FFFF", bg="#0A192F").grid(row=i, column=0, padx=10, pady=5, sticky="w")

        if label == "Smoker:":
            entry = tk.OptionMenu(form_frame, smoker_var, "Yes", "No")
            entry.config(font=("Orbitron", 12), width=22, bg="#001F3F", fg="#00FFFF")
        elif label == "Region:":
            entry = tk.OptionMenu(form_frame, region_var, "Northwest", "Northeast", "Southwest", "Southeast")
            entry.config(font=("Orbitron", 12), width=22, bg="#001F3F", fg="#00FFFF")
        elif label == "Sex:":
            entry = tk.OptionMenu(form_frame, sex_var, "male", "female")
            entry.config(font=("Orbitron", 12), width=22, bg="#001F3F", fg="#00FFFF")
        else:
            entry = tk.Entry(form_frame, font=("Orbitron", 12), width=25, bg="#001F3F", fg="#00FFFF",
                             insertbackground="#00FFFF", relief="flat")

        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    # Submit Button
    submit_button = tk.Button(patient_root, text="Submit", font=("Orbitron", 12),
                              bg="#00FFFF", fg="#000", padx=10, pady=5,
                              command=submit_form, relief="flat", activebackground="#00CCCC")
    submit_button.place(relx=0.4, rely=0.9, anchor="center")

    # Exit Button
    exit_button = tk.Button(patient_root, text="Exit", font=("Orbitron", 12), bg="#FF5555",
                            fg="white", padx=10, pady=5, command=confirm_exit, relief="flat")
    exit_button.place(relx=0.6, rely=0.9, anchor="center")

    # Result Label
    result_label = tk.Label(patient_root, text="", font=("Orbitron", 14, "bold"),
                            fg="#00FF00", bg="#0A192F")
    result_label.place(relx=0.5, rely=0.95, anchor="center")


def confirm_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        patient_root.destroy()

def fake_loading_then_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge):
    loading_win = tk.Toplevel()
    loading_win.title("Processing...")
    loading_win.geometry("400x150")
    loading_win.configure(bg="#0d0d0d")
    loading_win.resizable(False, False)

    label = tk.Label(loading_win, text="Predicting Insurance Cost...", font=("Orbitron", 12), bg="#0d0d0d", fg="cyan")
    label.pack(pady=10)

    progress_var = tk.IntVar()
    progress = ttk.Progressbar(loading_win, variable=progress_var, maximum=100, length=300)
    progress.pack(pady=10)

    percent_label = tk.Label(loading_win, text="0%", font=("Orbitron", 10), bg="#0d0d0d", fg="white")
    percent_label.pack()

    def update_progress(i=0):
        if i <= 100:
            progress_var.set(i)
            percent_label.config(text=f"{i}%")
            loading_win.after(60, update_progress, i + 1)
        else:
            loading_win.destroy()
            show_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge)

    update_progress()

 
       

import pandas as pd   
def submit_form():
    try:
        name = entries[0].get().strip()
        age = entries[1].get().strip()
        bmi = entries[2].get().strip()
        smoker = smoker_var.get()
        children = entries[3].get().strip()
        region = region_var.get()
        sex = sex_var.get()

        # Validation
        if not name or not age or not bmi or not children or not smoker or not region or not sex:
            messagebox.showwarning("Missing Fields", "Please fill out all fields.")
            return

        if not age.isdigit() or int(age) <= 0:
            messagebox.showerror("Invalid Input", "Age must be a positive number.")
            return

        if not bmi.replace('.', '', 1).isdigit() or float(bmi) <= 0:
            messagebox.showerror("Invalid Input", "BMI must be a positive number.")
            return

        if not children.isdigit() or int(children) < 0:
            messagebox.showerror("Invalid Input", "Children must be a non-negative number.")
            return

        # Convert inputs
        age = int(age)
        bmi = float(bmi)
        children = int(children)

        sex_male = 1 if sex.lower() == "male" else 0
        smoker_yes = 1 if smoker.lower() == "yes" else 0
        region_northeast = 1 if region.lower() == "northeast" else 0
        region_northwest = 1 if region.lower() == "northwest" else 0
        region_southeast = 1 if region.lower() == "southeast" else 0

        input_data = [[
            age, bmi, children, sex_male, smoker_yes,
            region_northeast, region_northwest, region_southeast
        ]]

        # Load and Predict
        model = joblib.load("saved_models/model.pkl")
        predicted_charge = model.predict(input_data)[0]

        # Save to CSV
        file_name = "insurance.csv"
        file_exists = os.path.exists(file_name)

        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, sex, bmi, children, smoker, region, f"{predicted_charge:.2f}"])
             # Show Prediction Message
            #messagebox.showinfo("Prediction", f"Predicted Insurance Charges: ₹{predicted_charge:,.2f}")

        # Show Result
        #result_label.config(text=f"Predicted Insurance Charges: ₹{predicted_charge:.2f}")
        #messagebox.showinfo("Prediction", f"Predicted Insurance Charges: ₹{predicted_charge:,.2f}")
        #messagebox.showinfo("Success", "Patient data saved successfully!")
        fake_loading_then_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge)





    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
            # Save to CSV, get predicted_charge, etc.
    
    # Call the fake loading screen, then show receipt
    


    #ake_loading_then_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge)
   
    
def fake_loading_then_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge):
    splash_screen = tk.Toplevel()
    splash_screen.title("Processing")
    splash_screen.configure(bg="#001F3F")
    splash_screen.geometry("400x200")

    # Center it manually
    splash_screen.update_idletasks()
    screen_width = splash_screen.winfo_screenwidth()
    screen_height = splash_screen.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2)
    y = (screen_height // 2) - (200 // 2)
    splash_screen.geometry(f"400x200+{x}+{y}")

    
    label = tk.Label(splash_screen, text="Submitting Your Information..\n\nPlease wait while we process your data and generate the result.",
                     font=("Arial", 12), bg="white", wraplength=360, justify="center")
    label.pack(pady=30)

    progress_bar = ttk.Progressbar(splash_screen, length=300, mode='indeterminate')
    progress_bar.pack(pady=10)

    # Start the progress bar animation
    progress_bar.start()

    # Delay and then open receipt
    splash_screen.after(7000, lambda: (
        splash_screen.destroy(),
        messagebox.showinfo("Receipt Generated", "Your receipt is generated. Click OK to proceed."),
        show_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge)
    ))


       

        #display reciept
     #fake_loading_then_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge)


from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk
import os
import tempfile

def print_receipt(details):
    
    try:
        # Default filename suggestion
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"receipt_{details['Name'].replace(' ', '_')}_{timestamp}.txt"

        # Ask user where to save the file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile=default_filename,
            filetypes=[("Text Files", "*.txt")],
            title="Save Receipt As"
        )

        if not file_path:
            return  # User canceled

        with open(file_path, "w") as f:
            # Fancy header/logo line
            f.write("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★\n")
            f.write("    INSURANCE COST RECEIPT\n")
            f.write("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★\n\n")

            for label, value in details.items():
                f.write(f"{label}: {value}\n")

            f.write("\nThank you for choosing us!\n")
            f.write("Stay healthy and safe! 🏥\n")

        messagebox.showinfo("Saved", f"Receipt saved successfully at:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save receipt:\n{e}")

from tkinter import filedialog
from PIL import Image, ImageTk
import datetime

def show_receipt(name, age, sex, bmi, children, smoker, region, predicted_charge):
    receipt_window = tk.Toplevel()
    receipt_window.title("Insurance Cost Receipt")
    receipt_window.configure(bg="#000000")
    receipt_window.resizable(False, False)

    width, height = 450, 600
    screen_width = receipt_window.winfo_screenwidth()
    screen_height = receipt_window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    receipt_window.geometry(f"{width}x{height}+{x}+{y}")

    # Load and place the background
    try:
        bg_image = Image.open("img-bg/slip.png").resize((450, 600 ))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(receipt_window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Error loading background image:", e)

    # Details to show
    details = {
        "Name": name,
        "Age": age,
        "Sex": sex,
        "BMI": bmi,
        "Children": children,
        "Smoker": smoker,
        "Region": region,
        "Predicted Charges": f"₹{predicted_charge:,.2f}"
    }

    

    # Optional Heading (can comment this if not needed)
    # tk.Label(receipt_window, text="INSURANCE COST CHARGES", font=("Orbitron", 14, "bold"),
    #          fg="#00ffff", bg="#000000").place(relx=0.5, y=20, anchor="n")

    y_position = 200  # Increase downward movement (now more than 4 cm)

    for label, value in details.items():
        text = f"{label}: {value}"
        # Increase font size and set black text with transparent background
        tk.Label(receipt_window, text=text, font=("Orbitron", 12),
                 fg="black", anchor="w", width=40, wraplength=350).place(x=40, y=y_position)
        y_position += 30  # Increase spacing for the next line

    # Closing line
    tk.Label(receipt_window, text="Thank you for choosing us!",
             font=("Orbitron", 14, "bold"), fg="black").place(x=40, y=y_position + 10)

    # Load and place the download icon button (bottom-right)
    try:
        download_icon = Image.open("img-bg/db.png").resize((25, 25))
        download_icon = ImageTk.PhotoImage(download_icon)
        download_btn = Button(receipt_window, image=download_icon,
                              command=lambda: download_receipt_as_pdf(details),
                              bg="#000000", bd=0, activebackground="#000000")
        download_btn.image = download_icon
        download_btn.place(relx=0.9, rely=0.88)  # Bottom right corner
    except Exception as e:
        print("Error loading download icon:", e)


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog

def download_receipt_as_pdf(details):
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save Receipt As"
        )

        if not file_path:
            return

        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        # Hospital-style header
        c.setFont("Helvetica-Bold", 18)
        c.setFillColorRGB(0.2, 0.4, 0.6)
        c.drawCentredString(width / 2, height - 50, "HEALTHCARE MEDICAL CENTER")

        # Subheader
        c.setFont("Helvetica", 12)
        c.setFillColorRGB(0, 0, 0)
        c.drawCentredString(width / 2, height - 70, "INSURANCE COST RECEIPT")
        c.line(40, height - 80, width - 40, height - 80)

        # Patient details
        y = height - 110
        c.setFont("Helvetica", 11)
        for label, value in details.items():
            c.drawString(60, y, f"{label}:")
            c.drawRightString(width - 60, y, f"{value}")
            y -= 20

        # Footer
        c.setFont("Helvetica-Oblique", 10)
        y -= 30
        c.drawString(60, y, "Thank you for choosing Healthcare Medical Center.")
        c.drawString(60, y - 15, "Stay healthy and safe. 🌿")

        c.save()

        messagebox.showinfo("Saved", f"Receipt saved successfully at:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save receipt:\n{e}")


    

    

    





    
   





   
    def process_form(name_entry, age_entry, bmi_entry, smoker_var):
        patient_name = name_entry.get()
        age = age_entry.get()
        bmi = bmi_entry.get()
        smoker_status = smoker_var.get()


        print(f"patient: {patient_name}, Age: {age}, BMI: {bmi}, SMoker: {smoker_status}")

        

        messagebox.showinfo("form Submitted", "Patient details submitted successfully!")
     
   



root.mainloop()