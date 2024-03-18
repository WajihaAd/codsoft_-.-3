import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tqdm import tqdm
import time
import threading

class password1:
    def __init__(self,base):
        self.base = base
        base.geometry("400x200")
        base.title("Password Generator")
        base.resizable(False, False) 
        self.greeting=ttk.Label(base,text="Welcome To The Password Generator!")
        self.greeting.grid(row=0, column=0, columnspan=2, padx=100, pady=5)
        self.imp1 = ttk.Label(base,text="Enter the Length of Password: ")
        self.imp1.grid(row=1, column=0, padx=1, pady=5)
        self.imp = ttk.Entry(base)
        self.imp.grid(row=1, column=1, padx=5, pady=5)
        self.button = ttk.Button(base, text="Generate Password!!", command=self.Generator)
        self.button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.progress_bar = ttk.Progressbar(base, orient='horizontal', length=200, mode='indeterminate')
        self.progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.password_label = ttk.Label(base, text="Generated Password:")
        self.password_label.grid(row=4, column=0, padx=10, pady=5)

        self.password_display = ttk.Entry(base, state="readonly")
        self.password_display.grid(row=4, column=1, padx=10, pady=5)


        self.password_label.grid_remove()
        self.password_display.grid_remove()


    def Generator(self):
        try:
            length = int(self.imp.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer")

            self.progress_bar.start() 


            threading.Thread(target=self.Generator1, args=(length,)).start()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def Generator1(self,length):

        try:
            choice2 = []
            from passwordg import all_characters as ch
            for i in tqdm(range(length), desc="Generating Password", unit="chars", leave=False):
                choice1 = random.choice(ch)
                choice2.append(choice1)
                time.sleep(1) 
            result = ''.join(choice2)


            self.base.after(0, self.update_gui, result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_gui(self, result):

        self.progress_bar.stop()

        self.imp1.grid_remove()
        self.imp.grid_remove()
        self.button.grid_remove()
        # Show password label and display
        self.password_label.grid()
        self.password_display.grid()
        # Update password display
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, result)
        self.password_display.config(state="readonly")    

if __name__ == "__main__":
    base = tk.Tk()
    base1=password1(base)
    base.mainloop()