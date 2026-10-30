
import tkinter as tk
from tkinter import messagebox

remaining = 0
timer_id = None
running = False

def update_display():
    hours = remaining // 3600
    minutes = (remaining % 3600) // 60
    seconds = remaining % 60

    timer_label.config(
        text=f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    )

def countdown():
    global remaining, timer_id, running

    if remaining > 0:
        remaining -= 1
        update_display()
        timer_id = root.after(1000, countdown)
    else:
        running = False
        timer_id = None
        messagebox.showinfo("Timer", "Time is up!")

def start_timer():
    global remaining, running

    if running:
        return

    if remaining == 0:
        try:
            remaining = int(time_entry.get())

            if remaining <= 0:
                messagebox.showwarning(
                    "Invalid Time",
                    "Please enter a time greater than zero."
                )
                remaining = 0
                return

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number of seconds."
            )
            return

    running = True
    countdown()

def pause_timer():
    global timer_id, running

    if running:
        root.after_cancel(timer_id)
        timer_id = None
        running = False

def reset_timer():
    global remaining, timer_id, running

    if timer_id is not None:
        root.after_cancel(timer_id)

    timer_id = None
    running = False

    try:
        remaining = int(time_entry.get())

        if remaining < 0:
            raise ValueError

        update_display()

    except ValueError:
        remaining = 0
        update_display()
        messagebox.showwarning(
            "Invalid Input",
            "Enter a valid positive number of seconds."
        )

# Main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("450x500")
root.configure(bg="#eaf2f8")

# Heading
heading = tk.Label(
    root,
    text="COUNTDOWN TIMER",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
heading.pack(pady=25)

# Instruction
tk.Label(
    root,
    text="Enter time in seconds:",
    font=("Arial", 13),
    bg="#eaf2f8"
).pack(pady=5)

# Time input
time_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=15,
    justify="center"
)
time_entry.pack(pady=10)

# Timer display
timer_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 38, "bold"),
    bg="#eaf2f8",
    fg="#2874a6"
)
timer_label.pack(pady=30)

# Start button
tk.Button(
    root,
    text="START",
    command=start_timer,
    font=("Arial", 12, "bold"),
    bg="#239b56",
    fg="white",
    width=15
).pack(pady=7)

# Pause button
tk.Button(
    root,
    text="PAUSE",
    command=pause_timer,
    font=("Arial", 12, "bold"),
    bg="#d68910",
    fg="white",
    width=15
).pack(pady=7)

# Reset button
tk.Button(
    root,
    text="RESET",
    command=reset_timer,
    font=("Arial", 12, "bold"),
    bg="#c0392b",
    fg="white",
    width=15
).pack(pady=7)

# Run application
root.mainloop()
