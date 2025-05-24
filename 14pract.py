import tkinter as tk

class IceCreamGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ice Cream Stand")

        self.label = tk.Label(root, text="Добро пожаловать в кафе!")
        self.label.pack()

        self.flavor_entry = tk.Entry(root)
        self.flavor_entry.pack()

        self.add_flavor_button = tk.Button(root, text="Добавить вкус", command=self.add_flavor)
        self.add_flavor_button.pack()

        self.remove_flavor_button = tk.Button(root, text="Без добавок вкусов", command=self.remove_flavor)
        self.remove_flavor_button.pack()

    def add_flavor(self):
        flavor = self.flavor_entry.get()
        iceCreamCafe.add_flavor(flavor)

    def remove_flavor(self):
        flavor = self.flavor_entry.get()
        iceCreamCafe.remove_flavor(flavor)

root = tk.Tk()
app = IceCreamGUI(root)
root.mainloop()