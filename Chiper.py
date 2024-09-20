import tkinter as tk
from tkinter import filedialog
import numpy as np

# Vigenere Cipher
def vigenere_encrypt(plain_text, key):
    key = key.upper()
    plain_text = plain_text.upper().replace(" ", "")
    cipher_text = ""
    for i in range(len(plain_text)):
        p = ord(plain_text[i]) - 65
        k = ord(key[i % len(key)]) - 65
        cipher_text += chr((p + k) % 26 + 65)
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    key = key.upper()
    cipher_text = cipher_text.upper().replace(" ", "")
    plain_text = ""
    for i in range(len(cipher_text)):
        c = ord(cipher_text[i]) - 65
        k = ord(key[i % len(key)]) - 65
        plain_text += chr((c - k) % 26 + 65)
    return plain_text

# Playfair Cipher
def create_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        if char in matrix[i]:
            return i, matrix[i].index(char)

def playfair_encrypt(plain_text, key):
    matrix = create_playfair_matrix(key)
    plain_text = plain_text.upper().replace('J', 'I').replace(" ", "")
    if len(plain_text) % 2 != 0:
        plain_text += 'X'
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        row1, col1 = find_position(matrix, plain_text[i])
        row2, col2 = find_position(matrix, plain_text[i+1])
        if row1 == row2:
            cipher_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    return cipher_text

def playfair_decrypt(cipher_text, key):
    matrix = create_playfair_matrix(key)
    cipher_text = cipher_text.upper().replace(" ", "")
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        row1, col1 = find_position(matrix, cipher_text[i])
        row2, col2 = find_position(matrix, cipher_text[i+1])
        if row1 == row2:
            plain_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plain_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            plain_text += matrix[row1][col2] + matrix[row2][col1]
    return plain_text

# Hill Cipher
def hill_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % 2 != 0:
        plain_text += 'X'
    key_matrix = np.array(key).reshape(2, 2)
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        vector = np.array([ord(plain_text[i])-65, ord(plain_text[i+1])-65])
        result = np.dot(key_matrix, vector) % 26
        cipher_text += chr(result[0]+65) + chr(result[1]+65)
    return cipher_text

def hill_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper().replace(" ", "")
    key_matrix = np.array(key).reshape(2, 2)
    inv_key_matrix = np.linalg.inv(key_matrix).astype(int) % 26
    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        vector = np.array([ord(cipher_text[i])-65, ord(cipher_text[i+1])-65])
        result = np.dot(inv_key_matrix, vector) % 26
        plain_text += chr(result[0]+65) + chr(result[1]+65)
    return plain_text

# Fungsi untuk membuka file
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_input_box.delete("1.0", tk.END)
            text_input_box.insert(tk.END, file.read())

# Fungsi untuk memproses teks (enkripsi atau dekripsi)
def process_text(mode="encrypt"):
    text = text_input_box.get("1.0", tk.END).strip()
    key = key_input.get().strip()
    cipher = cipher_choice.get()

    if len(key) < 12 and cipher != "Hill":
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Panjang kunci minimal 12 karakter!")
        return

    if cipher == "Hill":
        key_matrix = [int(i) for i in key.split()]

    if mode == "encrypt":
        if cipher == "Vigenere":
            processed_text = vigenere_encrypt(text, key)
        elif cipher == "Playfair":
            processed_text = playfair_encrypt(text, key)
        elif cipher == "Hill":
            processed_text = hill_encrypt(text, key_matrix)
    else:
        if cipher == "Vigenere":
            processed_text = vigenere_decrypt(text, key)
        elif cipher == "Playfair":
            processed_text = playfair_decrypt(text, key)
        elif cipher == "Hill":
            processed_text = hill_decrypt(text, key_matrix)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, processed_text)

# Fungsi untuk enkripsi
def encrypt_message():
    process_text("encrypt")

# Fungsi untuk dekripsi
def decrypt_message():
    process_text("decrypt")

# Setup GUI
window = tk.Tk()
window.title("Program Enkripsi dan Dekripsi")
window.geometry("550x400")  

# Warna background
window.configure(bg="#f4f4f4")  

# Membuat frame untuk input
input_frame = tk.Frame(window, bg="#f4f4f4") 
input_frame.pack(pady=10)

# Input Teks
input_label = tk.Label(input_frame, text="Teks Input:", bg="#f4f4f4", fg="#333333", font=("Helvetica", 10))
input_label.grid(row=0, column=0, padx=5, pady=5)

text_input_box = tk.Text(input_frame, height=5, width=50, bg="#ffffff", fg="#333333", bd=2, relief="solid")
text_input_box.grid(row=0, column=1, padx=5, pady=5)

# Tombol untuk membuka file
open_file_button = tk.Button(input_frame, text="Buka File", command=load_file, bg="#007bff", fg="#ffffff", relief="flat", padx=10)
open_file_button.grid(row=0, column=2, padx=5, pady=5)

# Input Kunci
key_label = tk.Label(input_frame, text="Kunci:", bg="#f4f4f4", fg="#333333", font=("Helvetica", 10))
key_label.grid(row=1, column=0, padx=5, pady=5)

key_input = tk.Entry(input_frame, width=50, bg="#ffffff", fg="#333333", bd=2, relief="solid")
key_input.grid(row=1, column=1, padx=5, pady=5)

# Pilihan Cipher
cipher_label = tk.Label(input_frame, text="Pilih Cipher:", bg="#f4f4f4", fg="#333333", font=("Helvetica", 10))
cipher_label.grid(row=2, column=0, padx=5, pady=5)

cipher_choice = tk.StringVar(window)
vigenere_radio = tk.Radiobutton(input_frame, text="Vigenere", variable=cipher_choice, value="Vigenere", bg="#f4f4f4", fg="#333333", font=("Helvetica", 9))
vigenere_radio.grid(row=2, column=1, sticky='w')

playfair_radio = tk.Radiobutton(input_frame, text="Playfair", variable=cipher_choice, value="Playfair", bg="#f4f4f4", fg="#333333", font=("Helvetica", 9))
playfair_radio.grid(row=2, column=1, padx=80, sticky='w')

hill_radio = tk.Radiobutton(input_frame, text="Hill", variable=cipher_choice, value="Hill", bg="#f4f4f4", fg="#333333", font=("Helvetica", 9))
hill_radio.grid(row=2, column=1, padx=160, sticky='w')

# Frame untuk tombol
button_frame = tk.Frame(window, bg="#f4f4f4")
button_frame.pack(pady=10)

# Tombol Enkripsi dan Dekripsi
encrypt_button = tk.Button(button_frame, text="Enkripsi", command=encrypt_message, bg="#28a745", fg="#ffffff", relief="flat", padx=10)
encrypt_button.pack(side=tk.LEFT, padx=10)

decrypt_button = tk.Button(button_frame, text="Dekripsi", command=decrypt_message, bg="#dc3545", fg="#ffffff", relief="flat", padx=10)
decrypt_button.pack(side=tk.LEFT, padx=10)

# Output
output_frame = tk.Frame(window, bg="#f4f4f4")
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="Hasil:", bg="#f4f4f4", fg="#333333", font=("Helvetica", 10))
output_label.pack()

output_box = tk.Text(output_frame, height=5, width=60, bg="#ffffff", fg="#333333", bd=2, relief="solid")
output_box.pack()

window.mainloop()
