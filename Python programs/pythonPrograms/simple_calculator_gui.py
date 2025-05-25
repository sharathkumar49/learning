# Simple Calculator with GUI (Tkinter)
import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", width=4, height=2)
        b.pack(side=tk.LEFT, padx=2, pady=2)
        b.bind('<Button-1>', on_click)

root.mainloop()
