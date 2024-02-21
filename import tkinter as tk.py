import tkinter as tk

def enable_entry():
    entry_value.config(state="normal")

def convert_length():
    length_value = float(entry_value.get())
    length_convert = dropdown_conversion.get()

    if length_convert == "Centimeter to Feets":
        result_label.config(text="{} cm is equal to {:.2f} ft.".format(length_value, length_value / 30.48))
        result_label2.config(text="")
    elif length_convert == "Feets to inches":
        result_label.config(text="{} ft is equal to {:.2f} inches.".format(length_value, length_value * 12))
        result_label2.config(text="")
    elif length_convert == "sqft to sqmtrs":
        result_label.config(text="{} sqft is equal to {:.2f} sqmtrs.".format(length_value, length_value * 0.092903))
        result_label2.config(text="")
    elif length_convert == "sqft to Hectre/Acres":
        result_label.config(text="{} sqft is equal to {:.6f} Hectares.".format(length_value, length_value * 0.000009290304))
        result_label2.config(text="{} sqft is equal to {:.6f} acres.".format(length_value, length_value * 0.0000229568))
    else:
        result_label.config(text="Invalid conversion")
        result_label2.config(text="")

# Create main window
window = tk.Tk()
window.title("Unit Converter")

# Add labels and entry widgets
conversion_label = tk.Label(window, text="Select conversion:")
conversion_label.grid(row=0, column=0, padx=5, pady=5)

dropdown_conversion = tk.StringVar(window)
dropdown_conversion.set("Centimeter to Feets")
menu_conversion = tk.OptionMenu(window, dropdown_conversion, "Centimeter to Feets", "Feets to inches", "sqft to sqmtrs", "sqft to Hectre/Acres", command=enable_entry)
menu_conversion.grid(row=0, column=1, padx=5, pady=5)

value_label = tk.Label(window, text="Enter a number to convert:")
value_label.grid(row=1, column=0, padx=5, pady=5)

entry_value = tk.Entry(window)
entry_value.grid(row=1, column=1, padx=5, pady=5)

# Add button to trigger conversion
convert_button = tk.Button(window, text="Convert", command=convert_length)
convert_button.grid(row=2, columnspan=2, padx=5, pady=5)

# Add labels to display results
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label2 = tk.Label(window, text="")
result_label2.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run Tkinter event loop
window.mainloop()
