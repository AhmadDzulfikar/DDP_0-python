#form input
print("Welcome to Dek Depe`s Name Store!")
print(36*'-')

nama = input("Nama: ")
tanggalLahir = input("Tanggal lahir: ")
jurusan = input("Jurusan: ")
motto = input('Motto Hidup: ')
panjang = float(input('Masukkan panjang (cm): '))
lebar = float(input('Masukkan lebar (cm): '))
luas = panjang * lebar
harga = luas * 100



# Hasil
print(36*'-')
print("halo", nama, "dari ", jurusan,".""\nLahir pada", 
        tanggalLahir, 'dengan motto','"',motto,'!"',
        '\nLuas name tag', nama,':', luas, 'cm^2',
        '\nHarga name tag ', nama,': Rp. ', harga)
print(36*'-')
print('Terima kasih sudah berbelanja di Dek Depe`s Name Tag Store!')