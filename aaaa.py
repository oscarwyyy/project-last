import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

def tambah_pengeluaran():
    try:
        kategori = entry_kategori_pengeluaran.get()
        jumlah = float(entry_jumlah_pengeluaran.get().replace('.', '').replace('Rp', '').strip())
        
        pengeluaran.append((kategori, jumlah))
        listbox_pengeluaran.insert(tk.END, f"{kategori}: {locale.currency(jumlah, grouping=True)}")
        
        hitung_total_pengeluaran()
        entry_jumlah_pengeluaran.delete(0, tk.END)
        entry_kategori_pengeluaran.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan jumlah yang valid.")

def tambah_pendapatan():
    try:
        jumlah_pendapatan = float(entry_jumlah_pendapatan.get().replace('.', '').replace('Rp', '').strip())
        
        pendapatan.append(jumlah_pendapatan)
        listbox_pendapatan.insert(tk.END, f"{locale.currency(jumlah_pendapatan, grouping=True)}")
        
        hitung_total_pendapatan()
        entry_jumlah_pendapatan.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan jumlah yang valid.")

def hitung_total_pengeluaran():
    total = sum(jumlah for kategori, jumlah in pengeluaran)
    label_total_pengeluaran.config(text=f"Total Pengeluaran: {locale.currency(total, grouping=True)}")
    return total

def hitung_total_pendapatan():
    total = sum(pendapatan)
    label_total_pendapatan.config(text=f"Total Pendapatan: {locale.currency(total, grouping=True)}")
    return total

def hitung_saldo():
    total_pengeluaran = hitung_total_pengeluaran()
    total_pendapatan = hitung_total_pendapatan()
    saldo = total_pendapatan - total_pengeluaran
    label_saldo.config(text=f"Saldo: {locale.currency(saldo, grouping=True)}")
    return saldo

def tampilkan_grafik():
    total_pengeluaran = hitung_total_pengeluaran()
    total_pendapatan = hitung_total_pendapatan()
    
    plt.bar(['Pendapatan', 'Pengeluaran'], [total_pendapatan, total_pengeluaran], color=['green', 'red'])
    plt.title('Pendapatan vs Pengeluaran')
    plt.ylabel('Jumlah (Rp)')
    plt.show()

def reset_data():
    global pengeluaran, pendapatan
    pengeluaran = []
    pendapatan = []
    listbox_pengeluaran.delete(0, tk.END)
    listbox_pendapatan.delete(0, tk.END)
    label_total_pengeluaran.config(text="Total Pengeluaran: Rp 0")
    label_total_pendapatan.config(text="Total Pendapatan: Rp 0")
    label_saldo.config(text="Saldo: Rp 0")

def hapus_pengeluaran():
    try:
        selected = listbox_pengeluaran.curselection()
        if selected:
            index = selected[0]
            pengeluaran.pop(index)
            listbox_pengeluaran.delete(index)
            hitung_total_pengeluaran()
    except Exception as e:
        messagebox.showerror("Hapus Error", "Terjadi kesalahan saat menghapus data pengeluaran.")

def hapus_pendapatan():
    try:
        selected = listbox_pendapatan.curselection()
        if selected:
            index = selected[0]
            pendapatan.pop(index)
            listbox_pendapatan.delete(index)
            hitung_total_pendapatan()
    except Exception as e:
        messagebox.showerror("Hapus Error", "Terjadi kesalahan saat menghapus data pendapatan.")

pengeluaran = []
pendapatan = []

root = tk.Tk()
root.title("Aplikasi Keuangan Pribadi")

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

button_hapus_pengeluaran = tk.Button(root, text="Hapus Pengeluaran Terpilih", command=hapus_pengeluaran)
button_hapus_pengeluaran.pack()

listbox_pengeluaran = tk.Listbox(root)
listbox_pengeluaran.pack()

label_total_pengeluaran = tk.Label(root, text="Total Pengeluaran: Rp 0")
label_total_pengeluaran.pack()

label_jumlah_pendapatan = tk.Label(root, text="Jumlah Pendapatan (Rp):")
label_jumlah_pendapatan.pack()
entry_jumlah_pendapatan = tk.Entry(root)
entry_jumlah_pendapatan.pack()

button_tambah_pendapatan = tk.Button(root, text="Tambah Pendapatan", command=tambah_pendapatan)
button_tambah_pendapatan.pack()

button_hapus_pendapatan = tk.Button(root, text="Hapus Pendapatan Terpilih", command=hapus_pendapatan)
button_hapus_pendapatan.pack()

listbox_pendapatan = tk.Listbox(root)
listbox_pendapatan.pack()

label_total_pendapatan = tk.Label(root, text="Total Pendapatan: Rp 0")
label_total_pendapatan.pack()

label_saldo = tk.Label(root, text="Saldo: Rp 0")
label_saldo.pack()

button_hitung_saldo = tk.Button(root, text="Hitung Saldo", command=hitung_saldo)
button_hitung_saldo.pack()

button_grafik = tk.Button(root, text="Tampilkan Grafik", command=tampilkan_grafik)
button_grafik.pack()

button_reset = tk.Button(root, text="Reset Data", command=reset_data)
button_reset.pack()

root.mainloop()