def sistem_kasir():
    item = []
    total_barang = 0

    print("sistem kasir fikri")
    print("ketik 'selesai' untuk menghentikan input barang.")

    while True:
        nama_barang = input("Masukkan nama barang: ")
    if nama_barang.lower() == 'selesai':
        break
    if nama_barang.strip() == "":
        print("Nama barang harus diisi. Silakan masukkan nama barang.")
        continue

    try:
        harga_barang = int(input(f"harga {nama_barang}: "))
        jumlah_barang = int(input(f"jumlah {nama_barang}: "))
    except ValueError:
        print("angka tidak valid. Silakan masukkan harga dan jumlah barang dalam bentuk angka.")
        continue
    if harga_barang <= 0 or jumlah_barang <= 0:
        print("Harga dan jumlah barang harus lebih dari 0. Silakan masukkan harga dan jumlah yang benar.")
        continue

subtotal = harga_barang * jumlah_barang
item.append({
    "nama": nama_barang,
    "harga": harga_barang,
    "jumlah": jumlah_barang,
    "subtotal": subtotal
})
total_barang += subtotal
print(f"-> {nama_barang} x {jumlah_barang} = Rp{subtotal}")

is_member = input("apakah anda member ya/tidak: ").strip().lower() == "y"

diskon_persen = 0
if total_barang >= 100000:
    diskon_persen = 10
if is_member:
    diskon_persen += 5
else:
    if is_member:
        diskon_persen += 3

nilai_diskon = total_barang * diskon_persen // 100
total_akhir = total_barang - nilai_diskon

print("Struk Belanja")
for i in item:
    print(f"{it['nama']} x {it['jumlah']} = Rp{it['subtotal']}")
print(f"Total: Rp{total_barang}")
print(f"Diskon: Rp{nilai_diskon}")
print(f"Total Akhir: Rp{total_akhir}")
print("Terima kasih telah berbelanja")
