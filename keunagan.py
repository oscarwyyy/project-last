import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Fungsi untuk menambahkan pengeluaran
def tambah_pengeluaran():
    try:
        kategori = entry_kategori_pengeluaran.get()
        jumlah = float(entry_jumlah_pengeluaran.get())
        
        # Menambah data pengeluaran
        pengeluaran.append((kategori, jumlah))
        listbox_pengeluaran.insert(tk.END, f"{kategori}: Rp {jumlah:.2f}")
        
        # Menghitung ulang total pengeluaran
        hitung_total_pengeluaran()
    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan jumlah yang valid.")

# Fungsi untuk menambahkan pendapatan
def tambah_pendapatan():
    try:
        jumlah_pendapatan = float(entry_jumlah_pendapatan.get())
        
        # Menambah pendapatan
        pendapatan.append(jumlah_pendapatan)
        listbox_pendapatan.insert(tk.END, f"Rp {jumlah_pendapatan:.2f}")
        
        # Menghitung ulang total pendapatan
        hitung_total_pendapatan()
    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan jumlah yang valid.")

# Fungsi untuk menghitung total pengeluaran
def hitung_total_pengeluaran():
    total = sum(jumlah for kategori, jumlah in pengeluaran)
    label_total_pengeluaran.config(text=f"Total Pengeluaran: Rp {total:.2f}")
    return total

# Fungsi untuk menghitung total pendapatan
def hitung_total_pendapatan():
    total = sum(pendapatan)
    label_total_pendapatan.config(text=f"Total Pendapatan: Rp {total:.2f}")
    return total

# Fungsi untuk menghitung saldo
def hitung_saldo():
    total_pengeluaran = hitung_total_pengeluaran()
    total_pendapatan = hitung_total_pendapatan()
    saldo = total_pendapatan - total_pengeluaran
    label_saldo.config(text=f"Saldo: Rp {saldo:.2f}")
    return saldo

# Fungsi untuk menampilkan grafik pengeluaran vs pendapatan
def tampilkan_grafik():
    total_pengeluaran = hitung_total_pengeluaran()
    total_pendapatan = hitung_total_pendapatan()
    
    # Membuat grafik perbandingan pengeluaran dan pendapatan
    plt.bar(['Pendapatan', 'Pengeluaran'], [total_pendapatan, total_pengeluaran], color=['green', 'red'])
    plt.title('Pendapatan vs Pengeluaran')
    plt.ylabel('Jumlah (Rp)')
    plt.show()

# Menyiapkan data awal
pengeluaran = []
pendapatan = []

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Keuangan Pribadi")

# Input Pengeluaran
label_kategori_pengeluaran = tk.Label(root, text="Kategori Pengeluaran:")
label_kategori_pengeluaran.pack()
entry_kategori_pengeluaran = tk.Entry(root)
entry_kategori_pengeluaran.pack()

label_jumlah_pengeluaran = tk.Label(root, text="Jumlah Pengeluaran (Rp):")
label_jumlah_pengeluaran.pack()
entry_jumlah_pengeluaran = tk.Entry(root)
entry_jumlah_pengeluaran.pack()

button_tambah_pengeluaran = tk.Button(root, text="Tambah Pengeluaran", command=tambah_pengeluaran)
button_tambah_pengeluaran.pack()

# Menampilkan daftar pengeluaran
listbox_pengeluaran = tk.Listbox(root)
listbox_pengeluaran.pack()

label_total_pengeluaran = tk.Label(root, text="Total Pengeluaran: Rp 0.00")
label_total_pengeluaran.pack()

# Input Pendapatan
label_jumlah_pendapatan = tk.Label(root, text="Jumlah Pendapatan (Rp):")
label_jumlah_pendapatan.pack()
entry_jumlah_pendapatan = tk.Entry(root)
entry_jumlah_pendapatan.pack()

button_tambah_pendapatan = tk.Button(root, text="Tambah Pendapatan", command=tambah_pendapatan)
button_tambah_pendapatan.pack()

# Menampilkan daftar pendapatan
listbox_pendapatan = tk.Listbox(root)
listbox_pendapatan.pack()

label_total_pendapatan = tk.Label(root, text="Total Pendapatan: Rp 0.00")
label_total_pendapatan.pack()

# Menampilkan saldo
label_saldo = tk.Label(root, text="Saldo: Rp 0.00")
label_saldo.pack()

# Button untuk menghitung saldo
button_hitung_saldo = tk.Button(root, text="Hitung Saldo", command=hitung_saldo)
button_hitung_saldo.pack()

# Button untuk menampilkan grafik
button_grafik = tk.Button(root, text="Tampilkan Grafik", command=tampilkan_grafik)
button_grafik.pack()

# Menjalankan GUI
root.mainloop()

