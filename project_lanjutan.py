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
    dash.title("Dashboard")
    tk.Label(dash, text=f"Selamat datang, {username}!", font=("Arial", 14)).pack(pady=20)
    tk.Button(dash, text="Logout", command=dash.destroy).pack(pady=10)
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
