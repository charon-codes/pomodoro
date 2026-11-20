import tkinter as tk

root = tk.Tk()
root.title("Pomodoro")
root.geometry("300x200")

label = tk.Label(root, text="25:00", font=("Segoe UI", 40))
label.pack(pady=20)

button = tk.Button(root, text="Start")
button.pack()

root.mainloop()