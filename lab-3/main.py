list_nametag = None # TODO: lengkapi jenis struktur data yang akan digunakan untuk <list_nametag>
jenis_kertas = {
    "HVS": 100,
    "Karton": 150,
    "Buffalo": 170,
    "Art Paper": 190
}

def print_menu():
    """Fungsi yang mencetak menu yang tersedia"""
    print("Welcome to Dek Depe's Name Tag Store!")
    print("----------------------------------------")
    print("(1) Buat name tag")
    print("(2) Lihat pesanan name tag")
    print("(3) Exit\n")

def print_list_harga():
    """Fungsi yang mencetak bahan-bahan name tag yang tersedia"""
    print("Bahan kertas name tag yang tersedia:")
    # Melakukan iterasi setiap objek di dictionary jenis kertas
    for i, j in jenis_kertas.items():
        print(f"> {i}: Rp{j}/cm^2")

# Method-method untuk menghitung luas setiap bentuk

def hitung_segiempat(panjang, lebar):
    # TODO: implementasikan fungsi yang mengembalikan luas segiempat
    pass # hapus baris ini setelah fungsi ini selesai diimplementasi

def hitung_segitiga(alas, tinggi):
    # TODO: implementasikan fungsi yang mengembalikan luas segitiga
    pass # hapus baris ini setelah fungsi ini selesai diimplementasi

def hitung_lingkaran(diameter):
    # TODO: implementasikan fungsi yang mengembalikan luas lingkaran
    pass # hapus baris ini setelah fungsi ini selesai diimplementasi

def buat_nametag(counter):
    """Fungsi untuk menjalankan fitur buat pesanan"""
    # print("----------------------------------------")

    # Meminta input jumlah pelanggan
    jumlah_orang = int(input("Masukkan jumlah pelanggan: "))
    for i in range(jumlah_orang):
        print(f'====== PELANGGAN {i + 1}')
        input(f'Masukkan nama pelanggan ke-{i + 1}: ')
        jmlh_nametag = int(input('Masukkan jumlah nametag yang ingin dibuat: '))
        for j in range(jmlh_nametag):
            bentuk = input(f'\nBentuk nametag ke-{j + 1} (segiempat/segitiga/lingkaran/random): ')
            if bentuk == 'segiempat':
                int(input('Masukkan panjang (cm): '))
                int(input('Masukkan lebar (cm): '))
                print('Bahan kertas name tag yang tersedia:')
                print('> HVS: Rp100/cm^2')
                print('> Karton: Rp150/cm^2')
                print('> Buffalo: Rp170/cm^2')
                print('> Art Paper: Rp190/cm^2')
                input('Masukkan jenis kertas yang ingin digunakan: ')
    print()

    # TODO: iterasi permintaan setiap pelanggan beserta name tag yang ingin dibuat
    # HINT: manfaatkan variabel <counter>

def cetak_summary(nomor_antrian):
    # TODO: implementasikan fungsi yang mencetak summary pesanan sesuai nomor antrian yang di-pass ke parameter"""
    pass # hapus baris ini setelah fungsi ini selesai diimplementasi

"""Fungsi utama untuk menjalankan program"""
running = True
counter = 0
while running:
    print_menu()
    choice = int(input("Pilih fitur yang ingin Anda gunakan: "))
    print("----------------------------------------")
    # Fitur 1: Buat pesanan
    if choice == 1:
        buat_nametag(counter)
        print("----------------------------------------")
    # Fitur 2: Lihat pesanan
    elif choice == 2:
        # TODO: Mencetak summary name tag sesuai nomor antrian yang diinput
        pass # hapus baris ini setelah fungsi ini selesai diimplementasi
    # Exit
    else:
        print("----------------------------------------")
        print("Terima kasih sudah berbelanja di Dek Depe's Name Tags Store!")
        exit()