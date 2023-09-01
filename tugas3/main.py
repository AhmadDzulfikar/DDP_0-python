import math as m
import random as r

# Function untuk menghitung luas setiap bentuk

def hitung_segiempat(panjang, lebar):
    luas = panjang * lebar
    return luas

def hitung_segitiga(alas, tinggi):
    luas = alas * tinggi /2
    return luas

def hitung_lingkaran(diameter):
    jari = diameter /2
    luas = m.pi * jari * jari
    return luas

def randomizer():
    isi = r.choice(['segiempat','segitiga','lingkaran'])
    return isi

# Main program
HARGA = 100 # Harga kertas per cm^2
print("Welcome to Dek Depe's Name Tag Store!")
jumlah_pelanggan = int(input("Masukkan jumlah pelanggan: ").strip())
print("----------------------------------------")

total_harga = 0

for i in range(1, jumlah_pelanggan + 1):
    print("======= PELANGGAN", i)
    nama_pelanggan = input("Masukkan nama pelanggan ke-" + str(i) + ": ")
    nametag = int(input('Masukkan jumlah name tag yang ingin dibuat: '))
    total_harga_pelanggan = 0 

    for j in range(nametag):
        bentuk = input(f'Bentuk name tag ke-{j + 1} (segiempat/segitiga/lingkaran/random): ')
        if bentuk.lower() == 'segiempat'.lower():
            panjang = float(input('Masukkan panjang (cm): '))
            lebar = float(input('Masukkan tinggi (cm): '))
            luas = hitung_segiempat(panjang, lebar)
        elif bentuk.lower() == 'segitiga'.lower():
            alas = float(input('Masukkan panjang alas (cm): '))
            tinggi = float(input('Masukkan tinggi (cm): '))
            luas = hitung_segitiga(alas,tinggi)
        elif bentuk.lower() == 'lingkaran'.lower():
            diameter = float(input('Masukkan diameter (cm): '))
            luas = hitung_lingkaran(diameter)
        else:
            bentuk == randomizer()
            luas = 0 

        bayar = luas * HARGA
        total_harga_pelanggan += bayar

    total_harga += total_harga_pelanggan
    print(f'Total harga kertas yang diperlukan untuk membuat {nametag} name tag untuk pelanggan atas nama {nama_pelanggan} adalah Rp{total_harga_pelanggan}')

print("----------------------------------------")
print("Terima kasih sudah berbelanja di Dek Depe's Name Tag Store!")