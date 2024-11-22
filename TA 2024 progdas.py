import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pastikan PIL sudah terinstal

def check_login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "oka" and password == "miau":
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror("Error", "Username atau password salah!")

def main_window():
    global main_app
    main_app = tk.Tk()
    main_app.title("StockTrack - Dashboard")
    main_app.geometry('800x600')
    main_app.resizable(True, True)
    
    tk.Label(main_app, text="StockTrack", font=("Arial", 20)).pack(pady=20)
    tk.Label(main_app, text="Pilih Fitur", font=("Arial", 14)).pack(pady=10)
    
    frame_main = tk.Frame(main_app)
    frame_main.pack(pady=20, expand=True)

    tk.Button(frame_main, text="Hitung Keuntungan/Kerugian", font=("Arial", 16), width=25, height=2, command=lambda: print("Fitur 1")).grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    tk.Button(frame_main, text="Simulasi Harga Jual", font=("Arial", 16), width=25, height=2, command=lambda: print("Fitur 2")).grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    tk.Button(frame_main, text="Hitung Dividen",  font=("Arial", 16), width=25, height=2, command=lambda: print("Fitur 3")).grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    
    frame_main.grid_columnconfigure(0, weight=1)
    main_app.mainloop()

login_window = tk.Tk()
login_window.title("StockTrack - Login")
login_window.geometry('400x300')  
login_window.resizable(True, True)

try:
    stock_image = Image.open("stocktrack.jpg")  # Nama file gambar di folder yang sama
    stock_image = stock_image.resize((400, 150), Image.ANTIALIAS)  # Resize gambar
    stock_photo = ImageTk.PhotoImage(stock_image)
    label_image = tk.Label(login_window, image=stock_photo)
    label_image.image = stock_photo  # Simpan referensi gambar
    label_image.pack(pady=5)
except Exception as e:
    messagebox.showwarning("Warning", f"Gambar tidak ditemukan: {e}")

tk.Label(login_window, text="StockTrack", font=("Arial", 20)).pack(pady=10)
tk.Label(login_window, text="Masukkan username dan password", font=("Arial", 14)).pack(pady=10)

frame_login = tk.Frame(login_window)
frame_login.pack(pady=10)

tk.Label(frame_login, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_username = tk.Entry(frame_login, font=("Arial", 12))
entry_username.grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame_login, text="Password:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_password = tk.Entry(frame_login, show="*", font=("Arial", 12))
entry_password.grid(row=1, column=1, padx=5, pady=5)

tk.Button(login_window, text="Login", command=check_login, width=15, height=2, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)

login_window.mainloop()
