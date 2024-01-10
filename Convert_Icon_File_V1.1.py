# /******************************************************************************
#  * Project Title: [Icon Converter w Resolution]
#  * Version: [1.2]
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


def convert_to_icon(input_image_path, output_icon_path, resolution):
    # Open the image to convert
    img = Image.open(input_image_path)

    # Save the image as ICO with the specified resolution
    img.save(output_icon_path, format="ICO", sizes=[(resolution, resolution)])


def select_input_file():
    root = Tk()  # Create a Tkinter object
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select Input Image",
                                           filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    return file_path # returns the filepath


def select_output_file():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.asksaveasfilename(title="Save ICO File", defaultextension=".ico",
                                             filetypes=[("ICO files", "*.ico")])
    return file_path # Define where to save converted icon to


def define_output_resolution():
    root = Tk()
    root.withdraw()  # Hide the main window

    resolution = simpledialog.askinteger("Resolution", "Enter the output resolution for the ICO file:", initialvalue=32) # Dialogue box for setting resolution

    return resolution # Return the resolution for the converted output


input_image_path = select_input_file()
output_icon_path = select_output_file()

if input_image_path and output_icon_path:
    resolution = define_output_resolution()

    if resolution:  # Check if a resolution has been provided
        convert_to_icon(input_image_path, output_icon_path, resolution)
        print(f"Conversion Complete. File saved at: {output_ico_path}")
    else:
        print("Resolution invalid. Conversion to icon Cancelled: ")
else:
    print("Invalid, Conversion Cancelled: ")
