class View:
    @staticmethod
    def tampilkan_header():
        print("\n=== Sistem Perpustakaan ===")
        print("(T)ambah Buku")
        print("(L)ihat Buku")
        print("(P)injam Buku")
        print("(K)embalikan Buku")
        print("(E)xit")

    @staticmethod
    def tampilkan_buku(daftar_buku):
        try:
            if not daftar_buku:
                print("\nPerpustakaan kosong.")
            else:
                print("\nDaftar Buku:")
                print(f"{'Judul':<30} {'Penulis':<20} {'Status'}")
                print("-" * 60)
                for buku in daftar_buku:
                    print(buku.info())
        except Exception as e:
            print(f"Error saat menampilkan buku: {e}")

    @staticmethod
    def tampilkan_pesan(pesan):
        print(f"\n{pesan}")