from data.buku import Buku

class Process:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis):
        try:
            buku = Buku(judul, penulis)
            self.daftar_buku.append(buku)
            return f"Buku '{judul}' berhasil ditambahkan ke perpustakaan."
        except Exception as e:
            return f"Error saat menambah buku: {e}"

    def lihat_buku(self):
        return self.daftar_buku

    def pinjam_buku(self, judul):
        try:
            for buku in self.daftar_buku:
                if buku.judul.lower() == judul.lower():
                    if buku.pinjam():
                        return f"Buku '{judul}' berhasil dipinjam."
                    else:
                        return f"Buku '{judul}' sedang tidak tersedia."
            return f"Buku '{judul}' tidak ditemukan di perpustakaan."
        except Exception as e:
            return f"Error saat meminjam buku: {e}"

    def kembalikan_buku(self, judul):
        try:
            for buku in self.daftar_buku:
                if buku.judul.lower() == judul.lower():
                    buku.kembalikan()
                    return f"Buku '{judul}' berhasil dikembalikan."
            return f"Buku '{judul}' tidak ditemukan di perpustakaan."
        except Exception as e:
            return f"Error saat mengembalikan buku: {e}"
