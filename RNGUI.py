import tkinter as tk
from tkinter import messagebox
from typing import Union
from RomanNumerals import RomanNumeralConverter


class RomanNumeralConverterGUI:
    """
    A GUI program for converting integers to Roman numerals and vice versa.
    """

    def __init__(self):
        self.converter = RomanNumeralConverter()
        self.window = tk.Tk()
        self.window.title("Roman Numeral Converter")
        self.window.geometry("400x350")
        
        # Initialize conversion type variable.
        self.conversion_type = tk.StringVar()

        # Create a label for the conversion type.
        self.conversion_label = tk.Label(self.window, text="Conversion type:")
        self.conversion_label.grid(column=0, row=0, pady=10)

        # Create a radio button for converting to Roman numeral.
        self.to_roman_button = tk.Radiobutton(self.window, text="To Roman Numeral", value="to_roman", variable=self.conversion_type)
        self.to_roman_button.grid(column=1, row=0)

        # Create a radio button for converting to integer.
        self.to_integer_button = tk.Radiobutton(self.window, text="To Integer", value="to_integer", variable=self.conversion_type)
        self.to_integer_button.grid(column=2, row=0)

        # Create a label for the input.
        self.input_label = tk.Label(self.window, text="Enter the input:")
        self.input_label.grid(column=0, row=1, pady=10)

        # Create an entry box for the input.
        self.input_entry = tk.Entry(self.window)
        self.input_entry.grid(column=1, row=1, columnspan=2)
        self.input_entry.focus()

        # Create a button for conversion.
        self.convert_button = tk.Button(self.window, text="Convert", command=self.convert)
        self.convert_button.grid(column=1, row=2, pady=10)
        self.window.bind('<Return>', lambda event: self.convert())  # bind enter key to convert button

        # Create a label for the output.
        self.output_label = tk.Label(self.window, text="Output:")
        self.output_label.grid(column=0, row=3)

        # Create a text box for the output.
        self.output_text = tk.Text(self.window, height=5, width=30)
        self.output_text.grid(column=1, row=3, columnspan=2)

        # Create a button to copy output to clipboard.
        self.copy_button = tk.Button(self.window, text="Copy", command=self.copy_to_clipboard)
        self.copy_button.grid(column=1, row=4, pady=10)

        # Create a button to clear output.
        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear_output)
        self.clear_button.grid(column=2, row=4, pady=10)

        self.window.mainloop()

    def convert(self):
        input_value = self.input_entry.get()
        conversion_type = self.conversion_type.get()

        try:
            if conversion_type == "to_roman":
                result = self.converter.to_roman(int(input_value))
                self.output_text.delete('1.0', tk.END)  # clear previous output
                self.output_text.insert(tk.END, result)
            elif conversion_type == "to_integer":
                result = self.converter.from_roman(input_value.upper())
                self.output_text.delete('1.0', tk.END)  # clear previous output
                self.output_text.insert(tk.END, result)
            else:
                raise ValueError("Invalid conversion type.")
        except ValueError:
            self.output_text.delete('1.0', tk.END)


    def copy_to_clipboard(self):
        output_value = self.output_text.get('1.0', tk.END)
        self.window.clipboard_clear()
        self.window.clipboard_append(output_value)
        messagebox.showinfo("Copy to Clipboard", "Output copied to clipboard!")
        
    def clear_output(self):
        self.output_text.delete('1.0', tk.END)

if __name__ == '__main__':
    app = RomanNumeralConverterGUI()
