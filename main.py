import tkinter as tk

WORK_SECONDS = 25 * 60
remaining = WORK_SECONDS
timer_id = None


def show_time():
    minutes, seconds = divmod(remaining, 60)
    label.config(text=f"{minutes:02d}:{seconds:02d}")


def tick():
    global remaining, timer_id
    remaining -= 1
    show_time()
    if remaining > 0:
        timer_id = root.after(1000, tick)
    else:
        timer_id = None
        button.config(text="Start")


def toggle():
    global remaining, timer_id
    if timer_id is None:  # not running -> start
        if remaining == 0:
            remaining = WORK_SECONDS
            show_time()
        timer_id = root.after(1000, tick)
        button.config(text="Pause")
    else:  # running -> pause
        root.after_cancel(timer_id)
        timer_id = None
        button.config(text="Start")


root = tk.Tk()
root.title("Pomodoro")
root.geometry("300x200")

label = tk.Label(root, text="25:00", font=("Segoe UI", 40))
label.pack(pady=20)

button = tk.Button(root, text="Start", command=toggle)
button.pack()

root.mainloop()