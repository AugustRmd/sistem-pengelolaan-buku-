class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = True

    def info(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul:<30} {self.penulis:<20} {status}"

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def kembalikan(self):
        self.tersedia = True