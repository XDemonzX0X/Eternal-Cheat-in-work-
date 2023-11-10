import tkinter as tk
from PIL import Image, ImageTk
import io
import requests

class TransparentWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window attributes
        self.title("Transparent Window")
        self.configure(bg="systemTransparent")
        self.overrideredirect(True)
        self.geometry("400x300")

        # Load custom image from URL
        image_url = "https://example.com/your-image.jpg"  # Replace with your image URL
        image_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_data))
        self.custom_image = ImageTk.PhotoImage(image)

        # Create a label for the image
        image_label = tk.Label(self, image=self.custom_image, bg="systemTransparent")
        image_label.pack(pady=10)

        # Add buttons
        button1 = tk.Button(self, text="Button 1", command=self.button1_click)
        button1.pack(pady=5)

        button2 = tk.Button(self, text="Button 2", command=self.button2_click)
        button2.pack(pady=5)

        # Close button
        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.pack(pady=10)

    def button1_click(self):
        print("Button 1 clicked")

    def button2_click(self):
        print("Button 2 clicked")

if __name__ == "__main__":
    app = TransparentWindow()
    app.mainloop()
