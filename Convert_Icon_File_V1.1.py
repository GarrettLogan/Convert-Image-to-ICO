# /******************************************************************************
#  * Project Title: [Icon Converter w Resolution]
#  * Version: [1.1]
#  * Description: [A Open source icon converter to convert images to icon(.ico) files for use with programs]
#  * Author: [Garrett Logan]
#  * License: [Open Source License]
#  * Contact: [garrettloganwork@gmail.com]
#  * Contact: Please contact me at [garrettloganwork@gmail.com] with any bugs or concerns
#  *
#  * This software is open source and freely available for modification and
#  * distribution under the terms of the specified license. Feel free to
#  * contribute, report issues, or use it in your projects. Visit the repository
#  * for more information and updates.
#  *****************************************************************************/

from PIL import Image
from tkinter import Tk, filedialog, simpledialog


def convert_to_ico(input_image_path, output_ico_path, resolution):
    # Open the image to convert
    img = Image.open(input_image_path)

    # Save the image as ICO with the specified resolution
    img.save(output_ico_path, format="ICO", sizes=[(resolution, resolution)])


def select_input_file():
    root = Tk()  # Create a Tkinter object
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select Input Image",
                                           filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    return file_path
    # Define the image to be used in the conversion


def select_output_file():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.asksaveasfilename(title="Save ICO File", defaultextension=".ico",
                                             filetypes=[("ICO files", "*.ico")])
    return file_path
    # Define where to save converted icon to


def select_resolution():
    root = Tk()
    root.withdraw()  # Hide the main window

    resolution = simpledialog.askinteger("Resolution", "Enter the resolution for the ICO file:", initialvalue=32)

    return resolution
    # Define the resolution for the output image


input_image_path = select_input_file()
output_ico_path = select_output_file()

if input_image_path and output_ico_path:
    resolution = select_resolution()

    if resolution:  # Check if a resolution has been provided
        convert_to_ico(input_image_path, output_ico_path, resolution)
        print(f"Conversion Complete. ICO file saved at: {output_ico_path}")
    else:
        print("Resolution not provided or invalid. Conversion Cancelled: ")
else:
    print("Conversion Cancelled: ")
