import tkinter as tk
from tkinter import messagebox
from notifier import schedule_notification

def start_app():
    def set_notification():
        hour = int(hour_var.get())
        minute = int(minute_var.get())
        am_pm = ampm_var.get()

        # Convert to 24-hour format
        if am_pm == "PM" and hour != 12:
            hour += 12
        elif am_pm == "AM" and hour == 12:
            hour = 0

        time_str = f"{hour:02d}:{minute:02d}"
        title = title_entry.get()
        message = message_entry.get()
        repeat = repeat_var.get()

        if not title or not message:
            messagebox.showwarning("Warning", "Please enter title and message.")
            return

        schedule_notification(time_str, title, message, repeat)
        messagebox.showinfo("Scheduled", f"Notification set for {time_str} ({am_pm})")

    # --- GUI Layout ---
    root = tk.Tk()
    root.title("Daily Notifier")
    root.geometry("400x380")
    root.resizable(False, False)

    tk.Label(root, text="🕒 Notification Time", font=("Helvetica", 12, "bold")).pack(pady=10)
    frame_time = tk.Frame(root)
    frame_time.pack()

    hour_var = tk.StringVar(value="09")
    minute_var = tk.StringVar(value="00")
    ampm_var = tk.StringVar(value="AM")

    tk.Entry(frame_time, textvariable=hour_var, width=5, justify="center").pack(side="left", padx=5)
    tk.Label(frame_time, text=":").pack(side="left")
    tk.Entry(frame_time, textvariable=minute_var, width=5, justify="center").pack(side="left", padx=5)
    tk.OptionMenu(frame_time, ampm_var, "AM", "PM").pack(side="left", padx=5)

    tk.Label(root, text="📌 Title").pack(pady=5)
    title_entry = tk.Entry(root, width=40)
    title_entry.pack(pady=5)

    tk.Label(root, text="💬 Message").pack(pady=5)
    message_entry = tk.Entry(root, width=40)
    message_entry.pack(pady=5)

    repeat_var = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="Repeat Daily", variable=repeat_var).pack(pady=5)

    tk.Button(root, text="Set Notification", command=set_notification, bg="#0078D7", fg="white").pack(pady=15)

    tk.Label(root, text="Developed by ChatGPT 🧠", fg="gray").pack(side="bottom", pady=5)

    root.mainloop()

if __name__ == "__main__":
    start_app()
