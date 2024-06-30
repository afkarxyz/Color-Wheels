import customtkinter as ctk
from PIL import Image
import pyperclip
import os
import threading
import time

class ColorWheelsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Color Wheels")
        self.geometry("935x590")

        # Set custom icon
        icon_path = os.path.join(os.path.dirname(__file__), "rgb.ico")
        self.iconbitmap(icon_path)

        # Attempt to load the Color Wheel image
        image_path = os.path.join(os.path.dirname(__file__), "Color_Wheels.png")
        try:
            self.color_wheel = ctk.CTkImage(Image.open(image_path), size=(550, 550))
            self.color_wheel_label = ctk.CTkLabel(self, image=self.color_wheel, text="")
            self.color_wheel_label.grid(row=0, column=0, padx=20, pady=20)
        except FileNotFoundError:
            print(f"Warning: Image file not found at {image_path}")
            self.color_wheel_label = ctk.CTkLabel(self, text="Color Wheel Image Not Found", width=550, height=550)
            self.color_wheel_label.grid(row=0, column=0, padx=20, pady=20)

        # Color information
        colors = [
            ("FF0000", "Red"), ("FF7F00", "Orange"), ("FFFF00", "Yellow"),
            ("7FFF00", "Chartreuse"), ("00FF00", "Green"), ("00FF7F", "Spring Green"),
            ("00FFFF", "Cyan"), ("007FFF", "Azure"), ("0000FF", "Blue"),
            ("7F00FF", "Violet"), ("FF00FF", "Magenta"), ("FF007F", "Rose")
        ]

        color_frame = ctk.CTkFrame(self)
        color_frame.grid(row=0, column=1, padx=20, pady=20, sticky="ns")

        # Add title "Basic Color Wheels"
        title_label = ctk.CTkLabel(color_frame, text="Basic Color Wheels", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(10, 10))

        self.copy_buttons = {}  # Store copy buttons for later access

        for i, (color_code, color_name) in enumerate(colors, start=1):
            # Color sample button
            color_button = ctk.CTkButton(color_frame, text="", width=25, height=25, fg_color=f"#{color_code}", hover_color=f"#{color_code}")
            color_button.grid(row=i, column=0, padx=(10, 5), pady=5)

            # Color name textbox
            name_textbox = ctk.CTkTextbox(color_frame, width=90, height=25)
            name_textbox.insert("1.0", color_name)
            name_textbox.configure(state="disabled")
            name_textbox.grid(row=i, column=1, padx=5, pady=5)

            # Color code textbox
            code_textbox = ctk.CTkTextbox(color_frame, width=90, height=25)
            code_textbox.insert("1.0", color_code)
            code_textbox.configure(state="disabled")
            code_textbox.grid(row=i, column=2, padx=5, pady=5)

            # Copy button
            copy_button = ctk.CTkButton(color_frame, text="Copy", width=50, height=25, command=lambda c=color_code, b=i: self.copy_color(c, b))
            copy_button.grid(row=i, column=3, padx=(5, 10), pady=5)
            self.copy_buttons[i] = copy_button

    def copy_color(self, color_code, button_index):
        pyperclip.copy(color_code)
        print(f"Copied color code: {color_code}")
        
        # Change button text to "Copied"
        self.copy_buttons[button_index].configure(text="Copied")
        
        # Start a timer to reset the button text after 2 seconds
        threading.Timer(2.0, self.reset_button_text, args=[button_index]).start()

    def reset_button_text(self, button_index):
        self.copy_buttons[button_index].configure(text="Copy")

if __name__ == "__main__":
    app = ColorWheelsApp()
    app.mainloop()
