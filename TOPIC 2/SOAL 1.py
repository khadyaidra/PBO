def calculate_average(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input harus berupa list angka.")
        
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("Semua elemen dalam list harus berupa angka.")
        
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except (TypeError, ValueError) as e:
        return f"Terjadi kesalahan: {e}"

print(calculate_average([5, 5, 7, 8]))  # Input benar

# Contoh input salah
print(calculate_average("5, 5, 7, 8"))  # Input salah (string)
print(calculate_average(123))  # Input salah (integer)
print(calculate_average([5, "tujuh", 8]))  # Input salah (elemen bukan angka)