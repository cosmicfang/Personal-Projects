import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk


class QRApp:
    # Main Root
    def __init__(self, root):
        self.root = root
        self.title = self.root.title("QR Code Generation")
        self.geometry = self.root.geometry("400x300")
        self.configure = self.root.configure(bg="#f0f4f7")

        self.setup_styles()
        self.create_widgets()

    # 'Enter URL' label
    def create_widgets(self):
        self.label_url = ttk.Label(self.root, text="Enter URL: ", background="#f0f4f7")
        self.label_url.pack(pady=10)

        self.entry_url = ttk.Entry(self.root, font="Helvetica", width=12)
        self.entry_url.pack(pady=10)

        self.button_generate = ttk.Button(self.root, text="Generate QR Code", command=self.generate_qrcode, style="TButton")
        self.button_generate.pack(pady=10)

        self.label_result = ttk.Label(self.root, text="", font=("Helvetica", 14), background="#f0f4f7", foreground="#333")
        self.label_result.pack(pady=10)

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), padding=5)
        self.style.map("TButton",
                  background=[("active", "#0056b3"), ("!active", "#007bff")],
                  foreground=[("active", "black"), ("!active", "black")])

    def generate_qrcode(self):
        url = self.entry_url.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,
            border = 2
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("qrcode.png")

        image = Image.open("qrcode.png")
        image_tk = ImageTk.PhotoImage(image)

        self.qr_label = ttk.Label(self.root, image=image_tk)
        self.qr_label.image = image_tk
        self.qr_label.pack(pady=10)

        self.label_result.config(text="QR Code generated Successfully! ")

def main():
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()