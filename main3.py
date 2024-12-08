import tkinter as tk

def on_button_click(value):
    current = display.get()
    if value == "=":
        try:
            result = str(eval(current))
            history_list.insert(tk.END, current + " = " + result)
        except Exception as e:
            result = "Error"
            display.delete(0, tk.END)
            display.insert(0, result)
            root.after(1000, lambda: display.delete(0, tk.END))
        else:
            display.delete(0, tk.END)
            display.insert(0, result)
    elif value == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, value)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="grey")

# Create display
display = tk.Entry(root, font=("Arial", 18), bd=10, insertwidth=2, width=22, borderwidth=4, relief="solid", highlightthickness=2, highlightbackground="black", bg="lightgrey")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create history list
history_frame = tk.Frame(root, bd=2, relief="solid", bg="grey")
history_frame.grid(row=0, column=5, rowspan=6, padx=10, pady=10)
history_label = tk.Label(history_frame, text="History", font=("Arial", 12), bg="grey")
history_label.pack(padx=5, pady=5)
history_list = tk.Listbox(history_frame, width=25, height=20, font=("Arial", 12), bd=2, relief="solid", highlightthickness=2, highlightbackground="black")
history_list.pack(padx=5, pady=5)

# Button layout
buttons = [
    '(', ')', '.', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '=', 'C'
]

# Create buttons with borders and even spacing
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
              relief="solid", borderwidth=2, highlightthickness=1, highlightbackground="black",
              command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
