import tkinter as tk
from tkinter import messagebox
from functools import partial

# Declaration variable "celsius"
temp_Val = "Celsius"


# getting drop down value
def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp


# Conversion of temperature
def call_convert(label1, input_num):
    temp = input_num.get()

    if temp_Val == 'Celsius':
        # Conversion from celsius to temperature
        f = float((float(temp) * 9 / 5) + 32)
        label1.config(text="%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Fahrenheit ")

    if temp_Val == 'Fahrenheit':
        # Conversion from fahrenheit to degrees celsius
        c = float((float(temp) - 32) * 5 / 9)
        label1.config(text="%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Celsius ")
    return


# creating Tk window
window = tk.Tk()

# setting geometry of the window
window.geometry('900x300')

# Using title() to display a message in the
# dialogue box of the message in the title bar
window.title('Temperature Converter')
window.configure(bg="blue")
# Lay out widgets
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

inputNumber = tk.StringVar()
var = tk.StringVar()

# label and entry field
input_label = tk.Label(window, text="Enter temperature", fg="black")
entry_label = tk.Entry(window, textvariable=inputNumber, )
input_label.grid(row=1)
entry_label.grid(row=1, column=1)
result_label = tk.Label(window, fg="Black", bg="White", borderwidth=2, relief="sunken")
result_label.grid(row=2, columnspan=4,)

# drop down setup
dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(window, var, *dropDownList,
                          command=store_temp)
var.set(dropDownList[0])
drop_down.grid(row=1, column=2)


# button widget
call_convert = partial(call_convert, result_label,
                       inputNumber)
result_button = tk.Button(window, text="Convert",
                          command=call_convert)
result_button.grid(row=5, columnspan=2)

# created a LOOP so that the program can run
window.mainloop()
