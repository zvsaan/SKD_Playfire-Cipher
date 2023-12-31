#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Inisialisasi variabel a dan b untuk digunakan dalam rekursi dalam mengisi karakter lainnya
a = b = 0

# Minta pengguna untuk memasukkan kunci untuk digunakan dalam pembuatan matriks 5x5
kunci = input("Masukkan kunci: ")
kunci = kunci.replace(" ", "")  # Hapus spasi dari kunci
kunci = kunci.upper()  # Konversi kunci menjadi huruf kapital

# Minta pengguna untuk memasukkan teks sandi yang akan didekripsi
teks_sandi = input("Teks sandi: ")
teks_sandi = teks_sandi.replace(" ", "")  # Hapus spasi dari teks sandi
teks_sandi = teks_sandi.upper()  # Konversi teks sandi menjadi huruf kapital

# Fungsi matriks untuk membuat daftar bersarang secara rekursif.
def matriks(x, y, awal):
    return [[awal for _ in range(x)] for _ in range(y)]

# Fungsi indexlocator untuk mencari indeks suatu karakter dalam matriks sandi
def indexlocator(x):
    if x == 'J':
        x = 'I'
    for i, j in enumerate(matriks_sandi):
        for k, l in enumerate(j):
            if x == l:
                return [i, k]

# Membuat matriks sandi dengan menggunakan fungsi matriks
matriks_sandi = matriks(5, 5, 0)
key_ke_matriks = []

for c in kunci:
    if c not in key_ke_matriks:
        if c == 'J':
            key_ke_matriks.append('I')
        else:
            key_ke_matriks.append(c)

for i in range(65, 91):
    if chr(i) not in key_ke_matriks:
        if i == 73 and chr(74) not in key_ke_matriks:
            key_ke_matriks.append("I")
            a = 1
        elif a == 0 and (i == 73 or i == 74):
            pass
        else:
            key_ke_matriks.append(chr(i))

# Mengisi matriks sandi dengan karakter dari daftar key_ke_matriks
b = 0
for i in range(5):
    for j in range(5):
        matriks_sandi[i][j] = key_ke_matriks[b]
        b += 1 if b < len(key_ke_matriks) - 1 else 0

# Fungsi dekripsi untuk mendekripsi teks sandi Playfair
def dekripsi(teks):
    i = 0
    while i < len(teks):
        lst = indexlocator(teks[i])
        lon = indexlocator(teks[i + 1])
        if lst[1] == lon[1]:
            print(f"{matriks_sandi[(lst[0] - 1) % 5][lst[1]]}{matriks_sandi[(lon[0] - 1) % 5][lon[1]]}", end=' ')
        elif lst[0] == lon[0]:
            print(f"{matriks_sandi[lst[0]][(lst[1] - 1) % 5]}{matriks_sandi[lon[0]][(lon[1] - 1) % 5]}", end=' ')
        else:
            print(f"{matriks_sandi[lst[0]][lon[1]]}{matriks_sandi[lon[0]][lst[1]]}", end=' ')
        i += 2

# Panggil fungsi dekripsi dengan teks sandi yang diberikan
dekripsi(teks_sandi)


# In[ ]:




