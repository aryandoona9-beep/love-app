import tkinter as tk

def show_message():
    msg_label.config(text="I LOVE YOU ❤️\nYou're amazing!")

root = tk.Tk()
root.title("Surprise App")
root.geometry("300x200")
root.configure(bg="pink")

tk.Label(root, text="Hey Babe!", font=("Comic Sans MS", 24, "bold"), bg="pink", fg="red").pack(pady=20)

msg_label = tk.Label(root, text="", font=("Arial", 14), bg="pink", fg="darkred")
msg_label.pack(pady=10)

btn = tk.Button(root, text="Open Your Surprise", command=show_message, bg="red", fg="white")
btn.pack(pady=20)

root.mainloop()
