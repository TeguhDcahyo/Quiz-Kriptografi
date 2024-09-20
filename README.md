Program ini merupakan aplikasi berbasis GUI (Tkinter) untuk mengenkripsi dan mendekripsi pesan menggunakan
tiga algoritma chiper: Vigenere, Playfair, dan Hill. Pengguna dapat memasukkan teks untuk dilakukan enkripsi dan dekripsi
kemudian memilih metode chiper, serta memberikan kunci untuk proses enkripsi atau dekripsi.

Fitur utama
1. Vigenere Chiper: Metode subatituasi polialfabetik yang menggunakan kunci untuk menggeser huruf pada teks.
2. Playfair Chiper: Metode enkripsi pasangan huruf menggunakan matriks 5x5 yang dibuat berdasarkan kunci.
3. Hill Chiper: Metode enkripsi berbasis matriks yang menggunakan aritmatika modulo 26 dan matriks kunci untuk memproses teks dalalm blok

Cara Penggunaan
1. Proggram inni ditulis dalam Python, pastikan Anda sudah menginstall Python
2. Diperlukan juga beberapa pustakak Python seperti tkinter dan numpy
3. Pada jendela aplikasi, masukkan teks yang ingin dilakukan enkripsi dan dekripsi
4. Anda juga dapat memuat teks dari file dengan mengklik tombol Buka File dan memilih file teks (*.txt) dari komputer
5. masukkan kunci yang akan digunakan untuk enkripsi atau dekripsi dengan minimal panjang kunci adalah 12 karakter
6. pilih jenis chiper yang ingin digunakan: Vigenere, Playfair, atau Hill
7. Klik tombol Enkripsi untuk mengenkripsi pesan atau tombol Dekripsi untuk mendekripsi pesan yang telah dienkripsi
8. Hasil enkripsi atau dekripsi akan muncul di kotak teks bagian bawah
