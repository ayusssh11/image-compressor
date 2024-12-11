from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def compress_image(input_image_path, output_image_path, quality=85):
    # Open the original image
    with Image.open(input_image_path) as img:
        # Print original size
        print(f"Original size: {os.path.getsize(input_image_path) / 1024:.2f} KB")
        
        # Save the image with reduced quality
        img.save(output_image_path, "JPEG", quality=quality)
        
        # Print new size
        print(f"Compressed size: {os.path.getsize(output_image_path) / 1024:.2f} KB")

def select_image():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select an image
    input_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    
    if input_path:
        # Ask for output path and filename
        output_path = filedialog.asksaveasfilename(
            title="Save Compressed Image As",
            defaultextension=".jpg",
            filetypes=[("JPEG Files", "*.jpg;*.jpeg"), ("PNG Files", "*.png"), ("All Files", "*.*")]
        )
        
        if output_path:
            # Ask for compression quality
            quality = simpledialog.askinteger("Compression Quality",
                                                "Enter compression quality (1-100):",
                                                minvalue=1, maxvalue=100,
                                                initialvalue=85)
            if quality is not None: 
                compress_image(input_path, output_path, quality)

if __name__ == "__main__":
    select_image()
