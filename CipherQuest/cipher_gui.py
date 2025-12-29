import tkinter as tk
from tkinter import messagebox

def encrypt_caesar(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt_caesar(cipher, shift):
    return encrypt_caesar(cipher, -shift)

# --- UI Functions ---

def process_text(mode):
    try:
        text = text_input.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        
        if mode == "encrypt":
            output = encrypt_caesar(text, shift)
        else:
            output = decrypt_caesar(text, shift)
            
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, output)
        text_output.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the shift!")

# --- Setup Main Window ---
root = tk.Tk()
root.title("🔐 Cipher Quest - Secret Encoder")
root.geometry("450x550")
root.configure(bg="#2c3e50") # Dark theme color

# Header
header = tk.Label(root, text="CIPHER QUEST", font=("Courier", 24, "bold"), fg="#ecf0f1", bg="#2c3e50")
header.pack(pady=20)

# Input Section
tk.Label(root, text="Enter Message:", fg="#bdc3c7", bg="#2c3e50", font=("Arial", 10)).pack()
text_input = tk.Text(root, height=5, width=40, font=("Arial", 12))
text_input.pack(pady=5)

# Shift Selection
tk.Label(root, text="Shift Value (1-25):", fg="#bdc3c7", bg="#2c3e50", font=("Arial", 10)).pack()
shift_entry = tk.Entry(root, width=10, font=("Arial", 12), justify='center')
shift_entry.insert(0, "3") # Default shift
shift_entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=15)

encrypt_btn = tk.Button(btn_frame, text="Encrypt 🔒", command=lambda: process_text("encrypt"), 
                        bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=12)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(btn_frame, text="Decrypt 🔓", command=lambda: process_text("decrypt"), 
                        bg="#2980b9", fg="white", font=("Arial", 10, "bold"), width=12)
decrypt_btn.grid(row=0, column=1, padx=10)

# Output Section
tk.Label(root, text="Result:", fg="#bdc3c7", bg="#2c3e50", font=("Arial", 10)).pack()
text_output = tk.Text(root, height=5, width=40, font=("Arial", 12, "bold"), bg="#ecf0f1", state=tk.DISABLED)
text_output.pack(pady=5)

# Footer
tk.Label(root, text="Ready for a secret mission?", fg="#7f8c8d", bg="#2c3e50", font=("Arial", 8, "italic")).pack(side=tk.BOTTOM, pady=10)

root.mainloop()