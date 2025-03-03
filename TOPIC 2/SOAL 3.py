class Cashier:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices

    def calculate_total(self, selected_items):
        total = 0
        for item in selected_items:
            if item not in self.items:  # Check if item is not available
                raise ValueError(f"Item '{item}' tidak tersedia.")  # Raise error if item not found
            index = self.items.index(item)
            price = self.prices[index]
            total += price
        return total

# Daftar barang dan harga
items = ["apel", "pisang", "jeruk"]
prices = [2500, 1500, 3000]

# Membuat objek kasir
cashier = Cashier(items, prices)

# Meminta input dari pengguna
selected_items = input("Masukkan item yang dibeli (pisahkan dengan koma): ").lower().split(",")

# Menghapus spasi dari setiap item
selected_items = [item.strip() for item in selected_items]

try:
    # Menghitung total belanja
    total_price = cashier.calculate_total(selected_items)
    print("Total belanja:", total_price)
except ValueError as e:
    print(e)  # Menampilkan pesan error jika ada item yang tidak tersedia