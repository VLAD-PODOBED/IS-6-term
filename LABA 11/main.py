import tkinter as tk
import time
import datetime
from hashlib import sha256

class App:
    def __init__(self, master):
        self.master = master
        master.title("Хеширование SHA256")
        master.geometry("500x200")

        self.label = tk.Label(master, text="Введите сообщение:")
        self.label.pack()

        self.textbox = tk.Text(master, height=5, width=50)
        self.textbox.pack()

        self.button = tk.Button(master, text="Хешировать", command=self.hash_message)
        self.button.pack()

        self.result = tk.Label(master, text="")
        self.result.pack()

        self.time_label = tk.Label(master, text="")
        self.time_label.pack()

    def hash_message(self):
        message = self.textbox.get("1.0", "end-1c")
        start_time = datetime.datetime.now()
        hashed = sha256(message.encode()).hexdigest()
        self.result.config(text="Хеш: " + hashed)
        end_time = datetime.datetime.now()
        self.time_label.config(
            text="Время выполнения: {:.6f} миллисекунд".format((end_time - start_time).total_seconds() * 1000))

root = tk.Tk()
app = App(root)
root.mainloop()
