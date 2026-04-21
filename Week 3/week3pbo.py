# mendefinisikan kelas untuk membangun objek untuk mobil
class car :
    car_type = 'sports car'
    color = 'biru'

print(f"aku punya mobil tipenya : {car.car_type}, warna mobilku warnanya : {car.color}")

# Buat objek berupa "mobil_ayah" dari kelas mobil
mobil_ayah = car()

# print untuk melihat spesifikasi mobil_ayah
print("--- Informasi Mobil Ayah ---")
print("Jenis mobil ayah :", mobil_ayah.car_type)
print("Warna mobil ayah :", mobil_ayah.color)