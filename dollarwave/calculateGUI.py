import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk 

__all__ = ['InflationCalculatorApp']


class InflationCalculatorApp(tk.Tk):
    def __init__(self, calculator):
        super().__init__()
        self.calculator = calculator
        self.withdraw()

    def initialize(self):
        self.title("Inflation Calculator")
        self.deiconify()

        # Set the window icon using an absolute path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, 'assets','icon.ico')
        self.iconbitmap(icon_path)

        # Set the initial size of the window
        self.geometry("600x500") 
        self.minsize(600, 500)

        # Load the logo image
        logo_path = os.path.join(script_dir, 'assets','icon.png')
        self.logo_image = Image.open(logo_path)

        # Desired width while maintaining aspect ratio
        new_width = 160
        original_width, original_height = self.logo_image.size
        aspect_ratio = original_height / original_width
        new_height = int(new_width * aspect_ratio)

        # Resize the image with the new dimensions
        self.logo_image = self.logo_image.resize((new_width, new_height), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Create a Label widget to display the logo
        self.logo_label = tk.Label(self, image=self.logo_photo)
        self.logo_label.pack(pady=10)

        # Create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        # Add tabs
        self.create_adjustment_tab()
        self.create_current_year_tab()
        self.create_comparison_tab()

        # Bind the tab change event
        self.notebook.bind("<<NotebookTabChanged>>", self.clear_other_tabs)

    def create_adjustment_tab(self):
        self.adjustment_frame = ttk.Frame(self.notebook, width=400, height=300)
        self.adjustment_frame.pack(fill='both', expand=True)

        # Amount Label and Entry
        ttk.Label(self.adjustment_frame, text="Dollar Amount:").grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = ttk.Entry(self.adjustment_frame)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Original Year Label and Entry
        ttk.Label(self.adjustment_frame, text="Original Year:").grid(row=1, column=0, padx=10, pady=10)
        self.original_year_entry = ttk.Entry(self.adjustment_frame)
        self.original_year_entry.grid(row=1, column=1, padx=10, pady=10)

        # Target Year Label and Entry
        ttk.Label(self.adjustment_frame, text="Target Year:").grid(row=2, column=0, padx=10, pady=10)
        self.target_year_entry = ttk.Entry(self.adjustment_frame)
        self.target_year_entry.grid(row=2, column=1, padx=10, pady=10)

        # Calculate Button
        self.calculate_button = ttk.Button(self.adjustment_frame, text="Calculate", command=self.calculate_inflation)
        self.calculate_button.grid(row=3, columnspan=2, pady=10)

        # Result Label
        self.result_label = ttk.Label(self.adjustment_frame, text="")
        self.result_label.grid(row=4, columnspan=2, pady=10)

        self.notebook.add(self.adjustment_frame, text='Adjusted Value')

    def create_current_year_tab(self):
        self.current_year_frame = ttk.Frame(self.notebook, width=400, height=300)
        self.current_year_frame.pack(fill='both', expand=True)

        # Amount Label and Entry
        ttk.Label(self.current_year_frame, text="Dollar Amount:").grid(row=0, column=0, padx=10, pady=10)
        self.amount_current_entry = ttk.Entry(self.current_year_frame)
        self.amount_current_entry.grid(row=0, column=1, padx=10, pady=10)

        # Calculate Button
        self.current_year_button = ttk.Button(self.current_year_frame, text="Calculate", command=self.current_year_change)
        self.current_year_button.grid(row=1, columnspan=2, pady=10)

        # Result Label
        self.current_year_result_label = ttk.Label(self.current_year_frame, text="")
        self.current_year_result_label.grid(row=2, columnspan=2, pady=10)

        self.notebook.add(self.current_year_frame, text='Current Year Change')

    def create_comparison_tab(self):
        self.comparison_frame = ttk.Frame(self.notebook, width=400, height=300)
        self.comparison_frame.pack(fill='both', expand=True)

        # Amount Label and Entry
        ttk.Label(self.comparison_frame, text="Dollar Amount:").grid(row=0, column=0, padx=10, pady=10)
        self.amount_comparison_entry = ttk.Entry(self.comparison_frame)
        self.amount_comparison_entry.grid(row=0, column=1, padx=10, pady=10)

        # Number of Years Label and Entry
        ttk.Label(self.comparison_frame, text="Number of Years:").grid(row=1, column=0, padx=10, pady=10)
        self.n_years_entry = ttk.Entry(self.comparison_frame)
        self.n_years_entry.grid(row=1, column=1, padx=10, pady=10)

        # Calculate Button
        self.comparison_button = ttk.Button(self.comparison_frame, text="Calculate", command=self.comparison)
        self.comparison_button.grid(row=2, columnspan=2, pady=10)

        # Result Label
        self.comparison_result_label = ttk.Label(self.comparison_frame, text="")
        self.comparison_result_label.grid(row=3, columnspan=2, pady=10)

        self.notebook.add(self.comparison_frame, text='Dollar Comparison')

    def clear_other_tabs(self, event):
        selected_tab = self.notebook.index(self.notebook.select())
        if selected_tab != 0:
            self.amount_entry.delete(0, tk.END)
            self.original_year_entry.delete(0, tk.END)
            self.target_year_entry.delete(0, tk.END)
            self.result_label.config(text="")
        if selected_tab != 1:
            self.amount_current_entry.delete(0, tk.END)
            self.current_year_result_label.config(text="")
        if selected_tab != 2:
            self.amount_comparison_entry.delete(0, tk.END)
            self.n_years_entry.delete(0, tk.END)
            self.comparison_result_label.config(text="")

    def calculate_inflation(self):
        try:
            # Get input values
            amount = float(self.amount_entry.get())
            original_year = int(self.original_year_entry.get())
            target_year = int(self.target_year_entry.get())

            # Perform calculation
            adjusted_value = self.calculator.adjusted_value(amount, original_year, target_year)

            if adjusted_value is not None:
                result_text = f"${amount:.2f} from {original_year} is equivalent to ${adjusted_value:.2f} in {target_year}."
                self.result_label.config(text=result_text)
            else:
                self.result_label.config(text="Calculation failed. Check the input values.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for amount, original year, and target year.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def current_year_change(self):
        try:
            # Get input value
            amount = float(self.amount_current_entry.get())

            # Perform calculation
            results = self.calculator.current_year_change(amount, plot=False)

            if results:
                result_text = "\n".join([f"{month}: ${value:.2f}" for month, value in results.items()])
                self.current_year_result_label.config(text=result_text)
            else:
                self.current_year_result_label.config(text="Calculation failed. Check the input values.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for amount.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def comparison(self):
        try:
            # Get input values
            amount = float(self.amount_comparison_entry.get())
            n_years = int(self.n_years_entry.get())

            # Perform calculation
            results = self.calculator.comparison(amount, n_years, plot=False)

            if results:
                result_text = "\n".join([f"{year}: ${value:.2f}" for year, value in results.items()])
                self.comparison_result_label.config(text=result_text)
            else:
                self.comparison_result_label.config(text="Calculation failed. Check the input values.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for amount and number of years.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def run(self):
        self.initialize()
        self.mainloop()

    def __dir__(self):
        return ['run']
