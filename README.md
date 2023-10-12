# annotate_draw_image
# Annotate and Draw Image

This is a simple web application built with Flask and OpenCV that allows users to upload an image, select a region of interest (ROI) by specifying coordinates, and annotate the selected region by drawing a black rectangle on the image.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Upload an image.
- Specify coordinates (x, y, width, height) to define a region of interest (ROI).
- Annotate the selected ROI by drawing a black rectangle on the image.
- Save the annotated image.

## Getting Started

### Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.x
- Flask
- OpenCV (opencv-python-headless)
- Werkzeug

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/thanhhuytran919/annotate_draw_image.git
   cd annotate_draw_image
2. Install the required packages:
   ```bash
   pip install -r requirements.txt

### Usage

1. Run the Flask application:
   ```bash
   python app.py
2. Access the application in your web browser by navigating to http://localhost:5000.
3. Follow the instructions on the web page to upload an image, specify coordinates, and annotate the selected region. Images test in folder Test_img.
4. The annotated image will be displayed on the web page.
5. You can also find the annotated image in the static directory of the project.

### Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request. Your contributions are greatly appreciated.
