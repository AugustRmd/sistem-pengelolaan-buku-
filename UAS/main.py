from data.process import Process
from view.buku import View

def validasi_input_str(prompt):
    while True:
        try:
            pilihan = input(prompt).strip().upper()
            if pilihan in ['T', 'L', 'P', 'K', 'E']:
                return pilihan
            raise ValueError("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    perpustakaan = Process()
    view = View()

    while True:
        view.tampilkan_header()
        pilihan = validasi_input_str("Pilih opsi (T/L/P/K/E): ")

        if pilihan == 'T':
            try:
                judul = input("Masukkan judul buku: ").strip()
                penulis = input("Masukkan penulis buku: ").strip()
                if not judul or not penulis:
                    raise ValueError("Judul dan penulis tidak boleh kosong.")
                pesan = perpustakaan.tambah_buku(judul, penulis)
                view.tampilkan_pesan(pesan)
            except ValueError as e:
                view.tampilkan_pesan(f"Error: {e}")

        elif pilihan == 'L':
            try:
                daftar_buku = perpustakaan.lihat_buku()
                view.tampilkan_buku(daftar_buku)
            except Exception as e:
                view.tampilkan_pesan(f"Error: {e}")

        elif pilihan == 'P':
            try:
                judul = input("Masukkan judul buku yang ingin dipinjam: ").strip()
                if not judul:
                    raise ValueError("Judul buku tidak boleh kosong.")
                pesan = perpustakaan.pinjam_buku(judul)
                view.tampilkan_pesan(pesan)
            except ValueError as e:
                view.tampilkan_pesan(f"Error: {e}")

        elif pilihan == 'K':
            try:
                judul = input("Masukkan judul buku yang ingin dikembalikan: ").strip()
                if not judul:
                    raise ValueError("Judul buku tidak boleh kosong.")
                pesan = perpustakaan.kembalikan_buku(judul)
                view.tampilkan_pesan(pesan)
            except ValueError as e:
                view.tampilkan_pesan(f"Error: {e}")

        elif pilihan == 'E':
            view.tampilkan_pesan("Keluar dari program.")
            break

if __name__ == "__main__":
    main()
