print("Welcome to Dek Depe's Name Tag Store!")
print(40*'-')

## Biodata
nama = input('Nama: ')
tanggal = input('Tanggal lahir: ')
jurusan = input('Jurusan: ')
motto = input('Motto Hidup: ')
nametag = int(input('Silahkan masukkan banyak name tag: '))
if nametag > 0:
    ## luas nametag
    print(40*'-')

    total_luas = 0
    for i in range(nametag):
        print(f'Name Tag {i + 1}:')
        bentuk = input('Silahkan masukkan bentuk name tag anda: ')
        if bentuk == 'segiempat':
            panjang = float(input('Masukkan panjang (cm): '))
            lebar = float(input('Masukkan lebar (cm): '))
        elif bentuk == 'segitiga':
            alas = float(input('Masukkan panjang alas (cm): '))
            tinggi = float(input('Masukkan tinggi (cm): '))
        else:
            print('maaf bentuk yang anda inginkan tidak valid')
        # Cari luas
        if bentuk == 'segiempat':
            luas = panjang * lebar
        elif bentuk == 'segitiga':
            luas = alas * tinggi / 2

        total_luas += luas
        total_luas = float(total_luas)
        total_harga = float(total_luas*100)
        # return total_harga
    
    # hasil 
    print(40*'-')
    print(f'Halo {nama} dari {jurusan}.\
        \nLahir pada {tanggal} dengan motto “{motto}”\
        \nTotal biaya untuk memproduksi ke-{nametag} name tag adalah : Rp{total_harga} ')
    ## penutup
    print(40*'-')
    print("Terima kasih sudah berbelanja di Dek Depe's Name Tag Store!")
else:
    print('Jumlah nametag yang anda masukkan tidak valid \n\
tolong masukkan jumlah yang benar!!!')




