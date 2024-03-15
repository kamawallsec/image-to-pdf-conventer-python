import os
import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image


class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.select_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.ui_initializer()

    def ui_initializer(self):
        title = tk.Label(self.root, text="Image to PDF Converter", font=("Rale way", 20, "bold"))
        title.pack(pady=10)

        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images,
                                         font=("Rale way", 8, "normal"))
        select_images_button.pack(pady=(0, 10))

        self.select_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter PDF file name: ")
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=60, justify="center")
        pdf_name_entry.pack()

        convert_to_pdf_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf,
                                          font=("Rale way", 8, "normal"))
        convert_to_pdf_button.pack(pady=(20, 40))

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.png;*.jpg"
                                                                                                         ";*.jpeg")])

        self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        self.select_images_listbox.delete(0, tk.END)

        for image_path in self.image_paths:
            _, image_path = os.path.split(image_path)
            self.select_images_listbox.insert(tk.END, image_path)

    def convert_images_to_pdf(self):
        if not self.image_paths:
            return

        output_pdf_path = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "output.pdf"

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))


def main():
    root = tk.Tk()
    root.title("Image to Pdf")
    converter = ImageToPdfConverter(root)
    root.geometry("700x500")
    root.mainloop()


if __name__ == "__main__":
    main()
