import tkinter as tk
from tkinter import messagebox

akun = {}

def register_window():
    reg_win = tk.Toplevel()
    reg_win.title("Register")
    
    tk.Label(reg_win, text="Username").pack()
    entry_reg_user = tk.Entry(reg_win)
    entry_reg_user.pack()
    
    tk.Label(reg_win, text="Password").pack()
    entry_reg_pw = tk.Entry(reg_win, show="*")
    entry_reg_pw.pack()
    
    def register():
        user = entry_reg_user.get()
        pw = entry_reg_pw.get()
        if user in akun:
            messagebox.showwarning("Error", "Username sudah ada!")
        elif user == "" or pw == "":
            messagebox.showwarning("Error", "Username dan password tidak boleh kosong!")
        else:
            akun[user] = pw
            messagebox.showinfo("Sukses", "Akun berhasil dibuat!")
            reg_win.destroy()  # tutup window register

    tk.Button(reg_win, text="Register", command=register).pack(pady=5)

def login():
    user = entry_login_user.get()
    pw = entry_login_pw.get()
    if user in akun and akun[user] == pw:
        messagebox.showinfo("Sukses", f"Selamat datang, {user}!")
        login_window.destroy()
        dashboard(user)
    else:
        messagebox.showerror("Error", "Username atau password salah!")

def dashboard(username):
    dash = tk.Tk()
    dash.title("Dashboard Sidebar")
    dash.geometry("600x400")
    
    # Warna latar utama
    dash.config(bg="#f0f8ff")
    
    # Sidebar
    sidebar = tk.Frame(dash, width=150, bg="#1e90ff", height=400, relief="sunken")
    sidebar.pack(expand=False, fill='y', side='left', anchor='nw')
    
    # Tombol sidebar
    tk.Button(sidebar, text="Dashboard", bg="#1e90ff", fg="white", bd=0, font=("Arial", 12, "bold")).pack(pady=10, fill='x')
    tk.Button(sidebar, text="Profil", bg="#1e90ff", fg="white", bd=0, font=("Arial", 12, "bold")).pack(pady=10, fill='x')
    tk.Button(sidebar, text="Logout", bg="#ff4d4d", fg="white", bd=0, font=("Arial", 12, "bold"), command=dash.destroy).pack(pady=10, fill='x')
    
    # Area konten utama
    main_area = tk.Frame(dash, bg="#f0f8ff")
    main_area.pack(expand=True, fill='both', side='right')
    
    tk.Label(main_area, text=f"Selamat datang, {username}!", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333").pack(pady=20)
    tk.Label(main_area, text="Ini adalah area konten dashboard.", font=("Arial", 12), bg="#f0f8ff", fg="#555").pack(pady=10)
    
    dash.mainloop()

# GUI Login
login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Username").pack()
entry_login_user = tk.Entry(login_window)
entry_login_user.pack()
tk.Label(login_window, text="Password").pack()
entry_login_pw = tk.Entry(login_window, show="*")
entry_login_pw.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=5)
tk.Button(login_window, text="Register", command=register_window).pack(pady=5)

login_window.mainloop()
