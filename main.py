import tkinter as tk
from tkinter import filedialog
from PIL import Image
from reportlab.pdfgen import canvas

def convert_jpg_to_pdf(input_image_path, output_pdf_path):
    # Open the image using Pillow
    image = Image.open(input_image_path)

    # Create a PDF document
    pdf = canvas.Canvas(output_pdf_path, pagesize=image.size)

    # Draw the image on the PDF
    pdf.drawInlineImage(input_image_path, 0, 0, width=image.width, height=image.height)

    # Save the PDF
    pdf.save()

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if file_path:
        convert_jpg_to_pdf(file_path, "output.pdf")
        status_label.config(text="Conversion successful!")

# Create the main window
root = tk.Tk()
root.title("JPG to PDF Converter")

# Create and configure widgets
browse_button = tk.Button(root, text="Browse", command=browse_image)
status_label = tk.Label(root, text="")

# Pack widgets
browse_button.pack(pady=10)
status_label.pack()

# Start the Tkinter event loop
root.mainloop()
