# webp_converter
Converts jpg and png image files to webp. Comes with a GUI written in CustomTkinter

`webp_converter` is a simple desktop application that converts JPG and PNG images to WebP format. This Python-based tool features a user-friendly GUI developed with `customtkinter` and utilizes `OpenCV` for efficient image processing.

## Features

- Convert JPG/PNG images to WebP format.
- Simple and intuitive graphical user interface.
- Uses OpenCV for high-performance image conversions.

## Screenshots

*Initial state of the GUI*

<img src="/imgs/img1.png" alt="Initial state of the application" width="60%" />

*GUI after conversion*

<img src="/imgs/img2.png" alt="State after the conversion" width="60%" />


## Prerequisites

Before you can run the `webp_converter`, make sure you have the following installed:
- Python 3.x
- OpenCV
- customtkinter

You can install the necessary Python libraries using pip:

```bash
pip install opencv-python customtkinter
```

## Installation
To use webp_converter, follow these steps:

Clone the repository:
```
git clone https://github.com/yourusername/webp_converter.git
```
Navigate to the cloned directory:
```
cd webp_converter
```

## Usage

To run the application, execute the following command in the terminal:
'''
python webp_converter.py
'''

The GUI will launch, allowing you to choose an image file for conversion. Once the file is selected, click the "Convert" button to start the conversion process. The converted file will be saved in the same location as the original image with the same name and a .webp extension


## License
This project is open source and available under the MIT License.


