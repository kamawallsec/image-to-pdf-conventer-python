import os
import tkinter as tk
from tkinter import filedialog


class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.select_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.ui_initializer()

    def ui_initializer(self):
        title = tk.Label(self.root, text="Image to Pdf Converter", font=("Rale way", 20, "bold"))
        title.pack(pady=10)


def main():
    root = tk.Tk()
    root.title("Image to Pdf")
    root.geometry("800x1000")
    root.mainloop()


if __name__ == "main":
    main()
# test