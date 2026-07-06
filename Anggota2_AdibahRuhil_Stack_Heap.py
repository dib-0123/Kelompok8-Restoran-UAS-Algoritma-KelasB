# ==========================================================
# UAS ALGORITMA DAN STRUKTUR DATA - KELOMPOK 8
# Program Studi S1 Pendidikan Teknik Informatika dan Komputer
#
# Anggota 2  : Adibah Ruhil
# NIM        : K3525044
# Fokus      : Stack & Binary Heap
#
# Studi Kasus: Sistem Antrean dan Pemesanan Restoran
#
# CATATAN: kode di bawah ini SAMA PERSIS dengan yang ada di
# UAS__ALGORITMA_Kel_8_Restoran_StrukturData.ipynb (cell 4 dan 8),
# hanya ditambah komentar penjelasan + unit test standalone.
# ==========================================================


# ==========================================================
# 1. STACK (Riwayat Transaksi) - Implementasi Linked List
# ==========================================================

class NodeStack:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    Stack LIFO (Last In First Out) berbasis Linked List.

    Digunakan untuk mencatat riwayat transaksi (pesanan yang sudah
    selesai diproses dapur), sehingga transaksi PALING AKHIR selalu
    di posisi teratas dan bisa dibatalkan (undo) lewat operasi pop
    tanpa perlu menelusuri seluruh riwayat.

    Kompleksitas: push/pop/peek = O(1), display = O(n)
    """

    def __init__(self):
        self.top = None
        self._jumlah = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        """Menambahkan data baru ke puncak stack. O(1)"""
        node_baru = NodeStack(data)
        node_baru.next = self.top
        self.top = node_baru
        self._jumlah += 1

    def pop(self):
        """Mengambil & menghapus data dari puncak stack. O(1)"""
        if self.is_empty():
            return None
        node_teratas = self.top
        self.top = self.top.next
        self._jumlah -= 1
        return node_teratas.data

    def peek(self):
        """Melihat data paling atas tanpa menghapus. O(1)"""
        if self.is_empty():
            return None
        return self.top.data

    def jumlah(self):
        """Jumlah elemen dalam stack saat ini. O(1)"""
        return self._jumlah

    def display(self):
        """Menampilkan seluruh isi stack, paling baru di atas. O(n)"""
        if self.is_empty():
            print("Riwayat transaksi kosong.")
            return
        temp = self.top
        no = 1
        print("--- Riwayat Transaksi (paling baru di atas) ---")
        while temp is not None:
            print(f"{no}. {temp.data}")
            temp = temp.next
            no += 1


# ==========================================================
# 2. BINARY HEAP (Prioritas Dapur) - Implementasi Array (list biasa)
# ==========================================================

class BinaryHeap:
    """
    Min-Heap berbasis array (list Python murni, BUKAN modul heapq).

    Elemen yang disimpan adalah objek Pesanan itu sendiri. Perbandingan
    prioritas dilakukan lewat atribut `pesanan.priority_score`
    (semakin KECIL priority_score, semakin dulu diproses dapur).

    priority_score dihitung di kelas Pesanan sbb:
        priority_score = waktu_masuk - bonus_prioritas
        bonus_prioritas = 1000 jika jenis == "Take Away Express", else 0

    Jadi pesanan Take Away Express otomatis dapat priority_score jauh
    lebih kecil dibanding Dine In manapun (selisih 1000 jauh lebih besar
    dari selisih waktu_masuk yang realistis), sehingga SELALU diproses
    lebih dulu -- sekaligus tetap FIFO di antara sesama jenis yang sama
    (karena waktu_masuk tetap ikut menentukan urutan).

    Kompleksitas: insert/delete_root = O(log n), peek = O(1)
    """

    def __init__(self):
        self.heap = []  # list Python dipakai murni sebagai array, BUKAN heapq

    def is_empty(self):
        return len(self.heap) == 0

    def _parent(self, i):
        return (i - 1) // 2

    def _kiri(self, i):
        return 2 * i + 1

    def _kanan(self, i):
        return 2 * i + 2

    def insert(self, pesanan):
        """Menyisipkan objek Pesanan baru ke heap. O(log n)"""
        self.heap.append(pesanan)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        """Menaikkan elemen index i selama priority_score-nya lebih
        kecil (lebih prioritas) dibanding parent-nya."""
        while i > 0:
            idx_induk = self._parent(i)
            if self.heap[i].priority_score < self.heap[idx_induk].priority_score:
                self.heap[i], self.heap[idx_induk] = self.heap[idx_induk], self.heap[i]
                i = idx_induk
            else:
                break

    def delete_root(self):
        """Hapus & kembalikan pesanan dengan prioritas tertinggi (akar). O(log n)"""
        if self.is_empty():
            return None
        akar = self.heap[0]
        elemen_terakhir = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = elemen_terakhir
            self._heapify_down(0)
        return akar

    def _heapify_down(self, i):
        """Menurunkan elemen index i sampai kedua anaknya (kalau ada)
        sudah tidak lebih prioritas lagi."""
        n = len(self.heap)
        while True:
            kiri = self._kiri(i)
            kanan = self._kanan(i)
            terkecil = i
            if kiri < n and self.heap[kiri].priority_score < self.heap[terkecil].priority_score:
                terkecil = kiri
            if kanan < n and self.heap[kanan].priority_score < self.heap[terkecil].priority_score:
                terkecil = kanan
            if terkecil == i:
                break
            self.heap[i], self.heap[terkecil] = self.heap[terkecil], self.heap[i]
            i = terkecil

    def peek(self):
        """Melihat pesanan prioritas tertinggi tanpa menghapus. O(1)"""
        if self.is_empty():
            return None
        return self.heap[0]

    def display(self):
        """Menampilkan seluruh isi heap (urutan array). O(n)"""
        if self.is_empty():
            print("Antrean prioritas dapur kosong.")
            return
        print("--- Antrean Prioritas Dapur (Binary Heap) ---")
        for i, p in enumerate(self.heap):
            print(f"{i}. {p}")


# ==========================================================
# UNIT TEST STANDALONE (jalankan file ini langsung: python nama_file.py)
# Menggunakan kelas Pesanan yang sama seperti di kontrak data kelompok
# ==========================================================

if __name__ == "__main__":

    class Pesanan:
        """Disalin dari cell 'KELAS PESANAN' di notebook utama,
        supaya file ini bisa dites berdiri sendiri."""
        def __init__(self, id_pesanan, nama_pelanggan, no_meja, jenis, daftar_menu, waktu_masuk):
            self.id_pesanan = id_pesanan
            self.nama_pelanggan = nama_pelanggan
            self.no_meja = no_meja
            self.jenis = jenis
            self.daftar_menu = daftar_menu
            self.waktu_masuk = waktu_masuk
            self.status = "Menunggu diproses"
            self.total_harga = sum(harga for _, harga in daftar_menu)
            bonus_prioritas = 1000 if jenis == "Take Away Express" else 0
            self.priority_score = waktu_masuk - bonus_prioritas

        def __str__(self):
            menu_str = ", ".join(nama for nama, _ in self.daftar_menu)
            return (f"ID {self.id_pesanan} | {self.nama_pelanggan} | {self.jenis} | "
                    f"Menu: {menu_str} | Status: {self.status}")

    def section(judul):
        print("\n" + "#" * 55)
        print("#", judul)
        print("#" * 55)

    # ---------------- TEST STACK ----------------
    section("TEST 1: Stack kosong di awal")
    s = Stack()
    print("is_empty():", s.is_empty())          # True
    print("jumlah():", s.jumlah())                # 0
    print("pop() saat kosong:", s.pop())          # None
    print("peek() saat kosong:", s.peek())        # None

    section("TEST 2: Push riwayat transaksi & cek urutan LIFO")
    s.push("Transaksi#1 - Andi")
    s.push("Transaksi#2 - Budi")
    s.push("Transaksi#3 - Citra")
    print("jumlah() setelah 3x push:", s.jumlah())   # 3
    print("peek() -> harus Transaksi#3 (paling akhir masuk):", s.peek())
    s.display()

    section("TEST 3: Pop -> simulasi undo transaksi terakhir")
    print("pop():", s.pop())                       # Transaksi#3
    print("peek() sekarang:", s.peek())             # Transaksi#2
    s.display()

    # ---------------- TEST HEAP ----------------
    section("TEST 4: Heap kosong di awal")
    h = BinaryHeap()
    print("is_empty():", h.is_empty())            # True
    print("peek() saat kosong:", h.peek())          # None
    print("delete_root() saat kosong:", h.delete_root())  # None

    section("TEST 5: Skenario Take Away Express vs Dine In")
    p1 = Pesanan(1, "Andi", "A1", "Dine In", [("Nasi Goreng", 20000)], waktu_masuk=1)
    p2 = Pesanan(2, "Budi", "A2", "Dine In", [("Mie Ayam", 15000)], waktu_masuk=2)
    p3 = Pesanan(3, "Citra", None, "Take Away Express", [("Ayam Bakar", 25000)], waktu_masuk=3)
    p4 = Pesanan(4, "Dedi", "A3", "Dine In", [("Soto", 18000)], waktu_masuk=4)
    p5 = Pesanan(5, "Euis", None, "Take Away Express", [("Bakso", 15000)], waktu_masuk=5)

    for p in [p1, p2, p3, p4, p5]:
        h.insert(p)
        print(f"  insert -> {p.nama_pelanggan} ({p.jenis}), priority_score={p.priority_score}")

    print("\nEkspektasi: Citra & Euis (Take Away) diproses duluan drpd semua Dine In,")
    print("dan di antara keduanya, Citra duluan (waktu_masuk lebih kecil).\n")

    urutan = []
    while not h.is_empty():
        p = h.delete_root()
        urutan.append(p.nama_pelanggan)
        print(f"  diproses -> {p.nama_pelanggan} ({p.jenis})")

    print("\nUrutan hasil:", urutan)
    sesuai = urutan == ["Citra", "Euis", "Andi", "Budi", "Dedi"]
    print("Sesuai ekspektasi bisnis?", "YA" if sesuai else "TIDAK -- ADA BUG!")
    assert sesuai

    section("TEST 6: peek() tidak mengubah isi heap")
    h.insert(p1)
    h.insert(p3)
    print("peek():", h.peek().nama_pelanggan, "-- harus Citra (Take Away)")
    print("ukuran heap tetap 2?", len(h.heap) == 2)

    print("\n\nSEMUA UNIT TEST STACK & HEAP SELESAI TANPA ERROR.")
