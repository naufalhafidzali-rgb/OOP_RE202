# Kecepatan awal
kecepatan = 0

while True:
    print("\n=== MENU KENDARAAN ===")
    print("1. Tambah kecepatan")
    print("2. Kurangi kecepatan")
    print("3. Lihat status kendaraan")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        kecepatan += 10
        if kecepatan > 120:
            kecepatan = 120
            print("Kecepatan sudah maksimal (120 km/jam)")
        else:
            print("Kecepatan bertambah menjadi", kecepatan, "km/jam")

    elif pilihan == "2":
        kecepatan -= 10
        if kecepatan < 0:
            kecepatan = 0
        print("Kecepatan berkurang menjadi", kecepatan, "km/jam")

    elif pilihan == "3":
        print("Kecepatan saat ini:", kecepatan, "km/jam")
        if kecepatan == 0:
            print("Kendaraan berhenti")
        else:
            print("Kendaraan berjalan")

    elif pilihan == "4":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")