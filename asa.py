# Calculator (Tkinter) — + - × ÷
import tkinter as tk

def press(val):
    if val == "C":
        display.delete(0, tk.END)
        return
    display.insert(tk.END, val)

def evaluate():
    expr = display.get().replace("×", "*").replace("÷", "/")
    try:
        result = str(eval(expr))
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "خطأ")

root = tk.Tk()
root.title("آلة حاسبة")

display = tk.Entry(root, font=("Arial", 24), justify="right", bd=8, relief=tk.FLAT)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    [("7","7"), ("8","8"), ("9","9"), ("÷","÷")],
    [("4","4"), ("5","5"), ("6","6"), ("×","×")],
    [("1","1"), ("2","2"), ("3","3"), ("-","-")],
    [("C","C"), ("0","0"), (".","."), ("+","+")],
]

for r, row in enumerate(buttons, start=1):
    for c, (label, val) in enumerate(row):
        tk.Button(
            root, text=label, command=lambda v=val: press(v),
            font=("Arial", 18), width=4, height=2, bd=1, relief=tk.RAISED
        ).grid(row=r, column=c, padx=6, pady=6, sticky="nsew")

tk.Button(
    root, text="=", command=evaluate, font=("Arial", 18), bd=1, relief=tk.RAISED, height=2
).grid(row=5, column=0, columnspan=4, padx=6, pady=6, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
