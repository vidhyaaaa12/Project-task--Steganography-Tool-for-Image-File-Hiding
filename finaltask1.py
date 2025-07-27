import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# --- Binary conversion helpers ---
def to_bin(data):
    return ''.join(format(ord(c), '08b') for c in data)

def from_bin(bin_data):
    chars = [chr(int(bin_data[i:i+8], 2)) for i in range(0, len(bin_data), 8)]
    return ''.join(chars)

# --- Embedding function ---
def embed_message(image_path, message, output_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    encoded = img.copy()
    width, height = img.size
    max_capacity = width * height * 3 // 8

    message += "#####END#####"
    binary_message = to_bin(message)

    if len(binary_message) > width * height * 3:
        raise ValueError("Message too large to embed in this image.")

    data_index = 0
    pixels = encoded.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if data_index < len(binary_message):
                r = (r & ~1) | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                g = (g & ~1) | int(binary_message[data_index])
                data_index += 1
            if data_index < len(binary_message):
                b = (b & ~1) | int(binary_message[data_index])
                data_index += 1
            pixels[x, y] = (r, g, b)
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded.save(output_path)

# --- Extraction function ---
def extract_message(image_path):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    binary_data = ''
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ''
    for byte in all_bytes:
        decoded += chr(int(byte, 2))
        if decoded.endswith("#####END#####"):
            break

    return decoded[:-12]  # remove the END delimiter

# --- GUI Functions ---
def select_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.bmp")])
    image_entry.delete(0, tk.END)
    image_entry.insert(0, path)

def embed_gui():
    image = image_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    if not image or not message:
        messagebox.showwarning("Input Error", "Please select an image and enter a message.")
        return
    default_name = os.path.splitext(os.path.basename(image))[0] + "_encoded.png"
    output = filedialog.asksaveasfilename(defaultextension=".png", initialfile=default_name, filetypes=[("PNG Image", "*.png")])
    if output:
        try:
            embed_message(image, message, output)
            messagebox.showinfo("Success", f"Message embedded and saved to:\n{output}")
        except Exception as e:
            messagebox.showerror("Error", f"Embedding failed: {e}")

def extract_gui():
    image = image_entry.get()
    if not image:
        messagebox.showwarning("Input Error", "Please select an image to extract from.")
        return
    try:
        extracted = extract_message(image)
        message_text.delete("1.0", tk.END)
        message_text.insert(tk.END, extracted)
    except Exception as e:
        messagebox.showerror("Error", f"Extraction failed: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("500x550")
root.resizable(False, False)

# --- Logo (optional) ---
try:
    logo_img = Image.open("logo.png")  # Using your uploaded image
    logo_img = logo_img.resize((200, 50))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.image = logo_photo
    logo_label.pack(pady=10)
except Exception as e:
    print("Logo image could not be loaded:", e)

# --- Widgets ---
tk.Label(root, text="Image Path:").pack(pady=5)
image_entry = tk.Entry(root, width=60)
image_entry.pack()
tk.Button(root, text="Browse", command=select_image).pack(pady=5)

tk.Label(root, text="Secret Message:").pack(pady=5)
message_text = tk.Text(root, height=10, width=60)
message_text.pack(pady=5)

tk.Button(root, text="Embed Message", command=embed_gui, width=20).pack(pady=10)
tk.Button(root, text="Extract Message", command=extract_gui, width=20).pack(pady=5)

# --- Footer ---
tk.Label(root, text="2025 © Steganography Tool", fg="gray").pack(side=tk.BOTTOM, pady=10)

root.mainloop()
