# Project-task--Steganography-Tool-for-Image-File-Hiding
#  Image Steganography Tool 

A Python-based GUI tool that lets you **hide secret text messages inside images** using LSB (Least Significant Bit) steganography.


##  Table of Contents

- [About](#about)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Recommended Image Formats](#recommended-image-formats)
- [Project Structure](#project-structure)
- [License](#license)



##  About

This project demonstrates how steganography can be used to hide text messages within images using the least significant bits of pixel values. It includes a **simple Tkinter-based GUI** for selecting images, entering/extracting messages, and saving output.



##  Features

 Embed and extract secret messages from `.png` and `.bmp` images
 Uses lossless formats to retain hidden data accurately
 GUI for selecting image, entering message, and saving output
 Optional logo support (not required to run)
 No prior knowledge of steganography needed



##  How It Works

1. **Message Encoding:**
   - Converts the secret message into binary.
   - Embeds the bits into the least significant bits of the image’s RGB pixel values.
   - Appends a unique delimiter (`#####END#####`) to mark message end.

2. **Message Extraction:**
   - Reads pixel LSBs and reconstructs binary data.
   - Stops at the delimiter and converts the binary to readable text.


##  Installation

### 1. Clone the Repository
bash
git clone https://github.com/yourusername/image-steganography-tool.git
cd image-steganography-tool
