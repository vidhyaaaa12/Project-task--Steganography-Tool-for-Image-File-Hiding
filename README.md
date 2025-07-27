# Project-task--Steganography-Tool-for-Image-File-Hiding

 ## Objective: Hide text or files inside images using steganography.
 ### Tools: Python, PIL, stepic, tkinter
 Mini Guide:
 a.Convert message to binary and embed in image LSB.
 b.Allow uploading image + hidden message.
 c.Extract and decrypt (optional) from modified image.
 d.Add drag-and-drop GUI.
 e.Support image formats like PNG, BMP.
## Deliverables: GUI tool for embedding and extracting data from images.

#  Image Steganography Tool 

A Python-based GUI tool that lets you **hide secret text messages inside images** using LSB (Least Significant Bit) steganography.


##  About

This project hides and retrieves secret messages inside images by modifying the **least significant bits** of each pixel's RGB values. The GUI is built using **Tkinter**, and image processing is done using the **Pillow** library.



##  Features

- Hide and reveal messages inside `.png` or `.bmp` images
- Simple GUI using Tkinter
- Works with lossless image formats
- Optional logo display
- User-friendly for non-programmers


##  How the Code Works

### 1. Message Embedding Process

- **Step 1: Message Conversion**
  - The text message is converted into a binary format using 8-bit ASCII encoding.
  - A special delimiter `#####END#####` is added to indicate the end of the message.

- **Step 2: Image Processing**
  - The selected image is opened using the Pillow (`PIL`) library.
  - It is converted to RGB mode if not already.

- **Step 3: Embedding**
  - The binary message is embedded into the image’s pixels by modifying the **least significant bit** (LSB) of each R, G, and B value.
  - One bit of the message is placed in each color channel (R, G, B) of the image pixels.

- **Step 4: Saving the Image**
  - Once the message is fully embedded, the image is saved as a new file.

### 2. Message Extraction Process

- **Step 1: Load the Modified Image**
  - The user selects the modified image (with hidden message).

- **Step 2: Read Pixel Bits**
  - The tool reads each pixel and extracts the LSBs of the R, G, B channels.
  - All bits are collected and grouped into bytes.

- **Step 3: Convert to Text**
  - The bits are converted back into ASCII characters.
  - The process stops when it detects the delimiter `#####END#####`.





