import tkinter as tk
from tkinter import ttk # Combobox
import tkinter.font as font # Button fonts

euro_currency = {
    # Dollar convert
    "dollar": 0.85, # 1$ -> 0,85€
    "euro": 1.17, # 1€ -> 1,17$

    # Rouble convert
    "rouble": 0.012, # 1 rouble -> 0,012€
    "euro_rouble": 86.18, # 1€ -> 86,18 rouble

    # Sterling convert
    "sterling": 1.17, # 1 sterling -> 1,17€
    "euro_sterling": 0.85, # 1€ -> 0,85 sterling

    # Yen convert
    "yen": 0.0078, # 1 yen -> 0,0078€
    "euro_yen": 128.32, # 1€ -> 128,32 yen

    # Yuan convert
    "yuan": 0.13, # 1 yuan -> 0,13€
    "euro_yuan": 7.60, # 1€ -> 7,60 yuan

    # Zloty convert
    "zloty": 0.22, # 1 zloty -> 0,22€
    "euro_zloty": 4.56 # 1€ -> 4,56 zloty
}

dollar_currency = {
    # Rouble convert
    "rouble": 0.014, # 1 rouble -> 0,014$
    "dollar_rouble": 73.59, # 1$ -> 73,59 rouble

    # Sterling convert
    "sterling": 1.37, # 1 sterling -> 1,37$
    "dollar_sterling": 0.73, # 1$ -> 0,73 sterling

    # Yen convert
    "yen": 0.0091, # 1 yen -> 0,0091$
    "dollar_yen": 109.58, # 1$ -> 109,58 yen

    # Yuan convert
    "yuan": 0.15, # 1 yuan -> 0,15$
    "dollar_yuan": 6.49, # 1$ -> 6,49 yuan

    # Zloty convert
    "zloty": 0.26, # 1 zloty -> 0,26$
    "dollar_zloty": 3.90 # 1$ -> 3,90 zloty
}

rouble_currency = {
    # Sterling convert
    "sterling": 101.09, # 1 sterling -> 101,09 rouble
    "rouble_sterling": 0.0099, # 1 rouble -> 0.0099 sterling

    # Yen convert
    "yen": 0.67, # 1 yen -> 0,67 rouble
    "rouble_yen": 1.49, # 1 rouble -> 1,49 yen

    # Yuan convert
    "yuan": 11.34, # 1 yuan -> 11,34 rouble
    "rouble_yuan": 0.088, # 1 rouble -> 0,088 yuan

    # Zloty convert
    "zloty": 18.88, # 1 zloty -> 18,88 rouble
    "rouble_zloty": 0.053 # 1 rouble -> 0,053 zloty
}

sterling_currency = {
    # Yen convert
    "yen": 0.0066, # 1 yen -> 0,0066 terling
    "sterling_yen": 150.53, # 1 sterling -> 150,53 yen

    # Yuan convert
    "yuan": 0.11, # 1 yuan -> 0,11 sterling
    "sterling_yuan": 8.91, # 1 sterling -> 8,91 yuan

    # Zloty convert
    "zloty": 0.19, # 1 zloty -> 0,19 sterling
    "sterling_zloty": 5.35 # 1 sterling -> 5,35 zloty
}

yen_currency = {
    # Yuan convert
    "yuan": 16.89, # 1 yuan -> 16,89 yen
    "yen_yuan": 0.059, # 1 yen -> 0,059 yuan

    # Zloty convert
    "zloty": 28.12, # 1 zloty -> 28,12 yen
    "yen_zloty": 0.036 # 1 yen -> 0,036 zloty
}

yuan_currency = {
    # Zloty convert
    "zloty": 1.66, # 1 zloty -> 1,66 yuan
    "yuan_zloty": 0.60 # 1 yuan -> 0,60 zloty
}

# GUI

window = tk.Tk()

window.title("Currency converter")

window.geometry("280x250")

# First currency option
entry = tk.Entry(window)

entry.grid(column=0, row=0)

currency_options_1 = ttk.Combobox(window)

currency_options_1["values"]= ("Euro", "Dollar", "Roubles", "Sterling", "Yen", "Yuan", "Zloty")

# Show the the second element (First is 0)
currency_options_1.current(1)

currency_options_1.grid(column=1, row=0)

# Second currency option
show_text = tk.StringVar()
show = tk.Entry(window, textvariable=show_text)

show.grid(column=0, row=1)

currency_options_2 = ttk.Combobox(window)

currency_options_2["values"]= ("Euro", "Dollar", "Roubles", "Sterling", "Yen", "Yuan", "Zloty")

currency_options_2.current(1)

currency_options_2.grid(column=1, row=1)


def currency_conversion():
    '''Convert currency options'''

    # Get choosed element
    first_selected = currency_options_1.get()
    second_selected = currency_options_2.get()

    def euro_currency_convertion():

        if first_selected == "Euro" and second_selected == "Dollar":
            result = float(entry.get()) * euro_currency.get("euro")

            show_text.set(result)

        elif first_selected == "Dollar" and second_selected == "Euro":
            result = float(entry.get()) * euro_currency.get("dollar")

            show_text.set(result)

        elif first_selected == "Roubles" and second_selected == "Euro":
            result = float(entry.get()) * euro_currency.get("rouble")

            show_text.set(result)

        elif first_selected == "Euro" and second_selected == "Roubles":
            result = float(entry.get()) * euro_currency.get("euro_rouble")

            show_text.set(result)

        elif first_selected == "Sterling" and second_selected == "Euro":
            result = float(entry.get()) * euro_currency.get("sterling")

            show_text.set(result)

        elif first_selected == "Euro" and second_selected == "Sterling":
            result = float(entry.get()) * euro_currency.get("euro_sterling")

            show_text.set(result)

        elif first_selected == "Yen" and second_selected == "Euro":
            result = float(entry.get()) * euro_currency.get("yen")

            show_text.set(result)

        elif first_selected == "Euro" and second_selected == "Yen":
            result = float(entry.get()) * euro_currency.get("euro_yen")

            show_text.set(result)

        elif first_selected == "Yuan" and second_selected == "Euro":
            result = float(entry.get()) * euro_currency.get("yuan")

            show_text.set(result)

        elif first_selected == "Euro" and second_selected == "Yuan":
            result = float(entry.get()) * euro_currency.get("euro_yuan")

            show_text.set(result)

        elif first_selected == "Zloty" and second_selected == "Euro":
            result = float(entry.get()) * euro_currency.get("zloty")

            show_text.set(result)

        elif first_selected == "Euro" and second_selected == "Zloty":
            result = float(entry.get()) * euro_currency.get("euro_zloty")

            show_text.set(result)


    def dollar_currency_convertion():

        if first_selected == "Roubles" and second_selected == "Dollar":
            result = float(entry.get()) * dollar_currency.get("rouble")

            show_text.set(result)

        elif first_selected == "Dollar" and second_selected == "Roubles":
            result = float(entry.get()) * dollar_currency.get("dollar_rouble")

            show_text.set(result)

        elif first_selected == "Sterling" and second_selected == "Dollar":
            result = float(entry.get()) * dollar_currency.get("sterling")

            show_text.set(result)

        elif first_selected == "Dollar" and second_selected == "Sterling":
            result = float(entry.get()) * dollar_currency.get("dollar_sterling")

            show_text.set(result)

        elif first_selected == "Yen" and second_selected == "Dollar":
            result = float(entry.get()) * dollar_currency.get("yen")

            show_text.set(result)

        elif first_selected == "Dollar" and second_selected == "Yen":
            result = float(entry.get()) * dollar_currency.get("dollar_yen")

            show_text.set(result)

        elif first_selected == "Yuan" and second_selected == "Dollar":
            result = float(entry.get()) * dollar_currency.get("yuan")

            show_text.set(result)

        elif first_selected == "Dollar" and second_selected == "Yuan":
            result = float(entry.get()) * dollar_currency.get("dollar_yuan")

            show_text.set(result)

        elif first_selected == "Zloty" and second_selected == "Dollar":
            result = float(entry.get()) * dollar_currency.get("zloty")

            show_text.set(result)

        elif first_selected == "Dollar" and second_selected == "Zloty":
            result = float(entry.get()) * dollar_currency.get("dollar_zloty")

            show_text.set(result)
            
    def rouble_currency_convertion():
        
        if first_selected == "Sterling" and second_selected == "Roubles":
            result = float(entry.get()) * rouble_currency.get("sterling")

            show_text.set(result)

        elif first_selected == "Roubles" and second_selected == "Sterling":
            result = float(entry.get()) * rouble_currency.get("rouble_sterling")

            show_text.set(result)

        elif first_selected == "Yen" and second_selected == "Roubles":
            result = float(entry.get()) * rouble_currency.get("yen")

            show_text.set(result)

        elif first_selected == "Roubles" and second_selected == "Yen":
            result = float(entry.get()) * rouble_currency.get("rouble_yen")

            show_text.set(result)

        elif first_selected == "Yuan" and second_selected == "Roubles":
            result = float(entry.get()) * rouble_currency.get("yuan")

            show_text.set(result)

        elif first_selected == "Roubles" and second_selected == "Yuan":
            result = float(entry.get()) * rouble_currency.get("rouble_yuan")

            show_text.set(result)

        elif first_selected == "Zloty" and second_selected == "Roubles":
            result = float(entry.get()) * rouble_currency.get("zloty")

            show_text.set(result)

        elif first_selected == "Roubles" and second_selected == "Zloty":
            result = float(entry.get()) * rouble_currency.get("rouble_zloty")

            show_text.set(result)

    def sterling_currency_convertion():

        if first_selected == "Yen" and second_selected == "Sterling":
            result = float(entry.get()) * sterling_currency.get("yen")

            show_text.set(result)

        elif first_selected == "Sterling" and second_selected == "Yen":
            result = float(entry.get()) * sterling_currency.get("sterling_yen")

            show_text.set(result)

        elif first_selected == "Yuan" and second_selected == "Sterling":
            result = float(entry.get()) * sterling_currency.get("yuan")

            show_text.set(result)

        elif first_selected == "Sterling" and second_selected == "Yuan":
            result = float(entry.get()) * sterling_currency.get("sterling_yuan")

            show_text.set(result)

        elif first_selected == "Zloty" and second_selected == "Sterling":
            result = float(entry.get()) * sterling_currency.get("zloty")

            show_text.set(result)

        elif first_selected == "Sterling" and second_selected == "Zloty":
            result = float(entry.get()) * sterling_currency.get("sterling_zloty")

            show_text.set(result)

    def yen_currency_convertion():

        if first_selected == "Yuan" and second_selected == "Yen":
            result = float(entry.get()) * yen_currency.get("yuan")

            show_text.set(result)

        elif first_selected == "Yen" and second_selected == "Yuan":
            result = float(entry.get()) * yen_currency.get("yen_yuan")

            show_text.set(result)

        elif first_selected == "Zloty" and second_selected == "Yen":
            result = float(entry.get()) * yen_currency.get("zloty")

            show_text.set(result)

        elif first_selected == "Yen" and second_selected == "Zloty":
            result = float(entry.get()) * yen_currency.get("yen_zloty")

            show_text.set(result)
            
    def yuan_currency_convertion():
        
        if first_selected == "Zloty" and second_selected == "Yuan":
            result = float(entry.get()) * yuan_currency.get("zloty")

            show_text.set(result)

        elif first_selected == "Yuan" and second_selected == "Zloty":
            result = float(entry.get()) * yuan_currency.get("yuan_zloty")

            show_text.set(result)

    return euro_currency_convertion(), dollar_currency_convertion(), rouble_currency_convertion(), sterling_currency_convertion(), yen_currency_convertion(), yuan_currency_convertion()


button_font = font.Font(family="Helvetica", size=12, weight='bold')
convert_button = tk.Button(window, text="Convert", bg="purple", fg="white", font=button_font, command=currency_conversion, padx=15, pady=15)
convert_button.grid(column=1, row=3)

window.mainloop()
