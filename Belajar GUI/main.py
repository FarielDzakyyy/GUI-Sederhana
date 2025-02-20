import tkinter as tk
from tkinter import messagebox

class StockInvestmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Investasi Saham")
        self.root.geometry("700x300")
        self.root.configure(bg="black")  # Warna latar belakang

        # Judul Aplikasi
        self.title_label = tk.Label(
            root,
            text="Aplikasi Investasi Saham",
            font=("Helvetica", 17, "bold"),
            bg="red",
            fg="white"
        )
        self.title_label.pack(pady=10)

        # Frame Input
        self.input_frame = tk.Frame(root, bg="white")
        self.input_frame.pack(pady=10)

        # Label dan Entry untuk Nama Saham
        self.stock_name_label = tk.Label(
            self.input_frame,
            text="Nama Saham:",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg="black"
        )
        self.stock_name_label.grid(row=0, column=0, padx=5, pady=5)
        self.stock_name_entry = tk.Entry(self.input_frame, font=("Helvetica", 12))
        self.stock_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label dan Entry untuk Harga Beli
        self.buy_price_label = tk.Label(
            self.input_frame,
            text="Harga Beli:",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg="black"
        )
        self.buy_price_label.grid(row=1, column=0, padx=5, pady=5)
        self.buy_price_entry = tk.Entry(self.input_frame, font=("Helvetica", 12))
        self.buy_price_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label dan Entry untuk Jumlah Lot
        self.lot_label = tk.Label(
            self.input_frame,
            text="Jumlah Lot:",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg="black"
        )
        self.lot_label.grid(row=2, column=0, padx=5, pady=5)
        self.lot_entry = tk.Entry(self.input_frame, font=("Helvetica", 12))
        self.lot_entry.grid(row=2, column=1, padx=5, pady=5)

        # Tombol Simpan
        self.save_button = tk.Button(
            root,
            text="Simpan Investasi",
            font=("Helvetica", 12, "bold"),
            bg="green",
            fg="white",
            command=self.save_investment
        )
        self.save_button.pack(pady=10)

        # Frame Hasil
        self.result_frame = tk.Frame(root, bg="blue")
        self.result_frame.pack(pady=10)

        # Label Hasil
        self.result_label = tk.Label(
            self.result_frame,
            text="Portofolio Investasi",
            font=("Helvetica", 14, "bold"),
            bg="yellow",
            fg="black"
        )
        self.result_label.grid(row=0, column=0, columnspan=2, pady=5)

        # Text Widget untuk Menampilkan Hasil
        self.result_text = tk.Text(
            self.result_frame,
            height=19,
            width=70,
            font=("Helvetica", 12),
            bg="purple",
            fg="white"
        )
        self.result_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Inisialisasi Data Portofolio
        self.portfolio = []

    def save_investment(self):
        # Ambil data dari input
        stock_name = self.stock_name_entry.get()
        buy_price = self.buy_price_entry.get()
        lot = self.lot_entry.get()

        # Validasi input
        if not stock_name or not buy_price or not lot:
            messagebox.showwarning("Peringatan", "Harap isi semua field!")
            return

        try:
            buy_price = float(buy_price)
            lot = int(lot)
        except ValueError:
            messagebox.showwarning("Peringatan", "Harga beli dan jumlah lot harus berupa angka!")
            return

        # Simpan data ke portofolio
        self.portfolio.append({
            "stock_name": stock_name,
            "buy_price": buy_price,
            "lot": lot
        })

        # Bersihkan input
        self.stock_name_entry.delete(0, tk.END)
        self.buy_price_entry.delete(0, tk.END)
        self.lot_entry.delete(0, tk.END)

        # Update hasil
        self.update_result()

    def update_result(self):
        # Bersihkan text widget
        self.result_text.delete(1.0, tk.END)

        # Tampilkan data portofolio
        for investment in self.portfolio:
            self.result_text.insert(tk.END, f"Saham: {investment['stock_name']}\n")
            self.result_text.insert(tk.END, f"Harga Beli: Rp {investment['buy_price']:,}\n")
            self.result_text.insert(tk.END, f"Jumlah Lot: {investment['lot']}\n")
            self.result_text.insert(tk.END, "-" * 50 + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockInvestmentApp(root)
    root.mainloop()