from flask import Flask, render_template, request

# Membuat objek Flask, ini adalah aplikasi web kita
app = Flask(__name__)

# Membuat route untuk URL root ('/') yang menerima metode GET dan POST
@app.route('/', methods=['GET', 'POST'])
def kalkulator():
    hasil = None  # Inisialisasi variabel hasil, nantinya akan menyimpan hasil perhitungan

    # Jika form dikirim dengan metode POST (misal tombol submit ditekan)
    if request.method == 'POST':
        # Ambil data dari form dengan nama 'ekspresi'
        # Jika tidak ada data, maka gunakan string kosong sebagai default
        ekspresi = request.form.get('ekspresi', '')  

        try:
            # Evaluasi ekspresi matematika yang dimasukkan pengguna secara dinamis
            # Hati-hati menggunakan eval karena bisa mengeksekusi kode berbahaya jika input tidak aman
            hasil = eval(ekspresi)  
        except Exception as e:
            # Jika ada error saat evaluasi ekspresi, tampilkan pesan error
            hasil = 'Error: ' + str(e)

    # Render template HTML 'kalkulator.html' dan kirim variabel hasil ke template tersebut
    return render_template('kalkulator.html', hasil=hasil)

# Mengecek apakah file ini dijalankan langsung (bukan di-import)
if __name__ == '__main__':
    # Jalankan aplikasi Flask dalam mode debug agar mudah saat pengembangan
    app.run(debug=True)
