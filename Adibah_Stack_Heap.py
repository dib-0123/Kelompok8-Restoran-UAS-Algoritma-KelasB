# ==========================================================
# UAS ALGORITMA DAN STRUKTUR DATA
# Program Studi S1 Pendidikan Teknik Informatika dan Komputer
#
# Anggota 2  : Adibah
# NIM        : K3525044
# Fokus      : Stack & Binary Heap
#
# Studi Kasus: Sistem Manajemen Restoran "Warung Algoritma"
# ==========================================================


# ==========================================================
# 1. STACK (Riwayat Transaksi)
# Linked List, LIFO. push/pop/peek semuanya O(1).
# ==========================================================

class _NodeStack:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Stack LIFO berbasis Linked List. push/pop/peek O(1)."""

    def __init__(self):
        self._top = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def push(self, data):
        node = _NodeStack(data)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            return None
        return self._top.data

    def display(self):
        if self.is_empty():
            print("   (Riwayat kosong)")
            return
        current = self._top
        idx = 1
        while current is not None:
            print(f"   {idx}. {current.data}")
            current = current.next
            idx += 1


# ==========================================================
# 2. BINARY HEAP (Prioritas Dapur)
# Min-Heap berbasis array. Elemen: (prioritas, urutan_masuk, pesanan).
# Semakin KECIL prioritas, semakin dulu diproses.
# ==========================================================

class BinaryHeap:
    """
    Min-Heap berbasis array. Elemen: (prioritas, urutan_masuk, pesanan).
    Semakin KECIL prioritas, semakin dulu diproses.
    """

    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    @staticmethod
    def _parent(i): return (i - 1) // 2
    @staticmethod
    def _left(i):   return 2 * i + 1
    @staticmethod
    def _right(i):  return 2 * i + 2

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def insert(self, item):
        """item = (prioritas, urutan_masuk, pesanan). O(log n)"""
        self._data.append(item)              # taruh di akhir array dulu
        self._heapify_up(len(self._data) - 1)  # lalu "naikkan" ke posisi yang benar

    def _heapify_up(self, i):
        while i > 0 and self._data[i][:2] < self._data[self._parent(i)][:2]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def delete_root(self):
        """Hapus & kembalikan elemen prioritas tertinggi (akar/index 0). O(log n)"""
        if self.is_empty():
            return None
        root = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last          # elemen terakhir naik jadi akar sementara
            self._heapify_down(0)         # lalu "turunkan" ke posisi yang benar
        return root

    def _heapify_down(self, i):
        n = len(self._data)
        while True:
            l, r = self._left(i), self._right(i)
            smallest = i
            if l < n and self._data[l][:2] < self._data[smallest][:2]:
                smallest = l
            if r < n and self._data[r][:2] < self._data[smallest][:2]:
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def remove_by_id(self, pesanan_id):
        """Hapus pesanan tertentu (untuk pembatalan). O(n) - perlu cari dulu."""
        for i, (_, _, pesanan) in enumerate(self._data):
            if pesanan.id == pesanan_id:
                last = self._data.pop()
                if i < len(self._data):
                    self._data[i] = last
                    self._heapify_down(i)
                    self._heapify_up(i)
                return True
        return False

    def display(self):
        if self.is_empty():
            print("   (Antrean dapur kosong)")
            return
        for idx, (prioritas, _, pesanan) in enumerate(self._data):
            label = "Take Away Express" if prioritas == 1 else "Dine In"
            print(f"   [{idx}] ID#{pesanan.id} - {pesanan.nama_pelanggan} ({label}, prioritas={prioritas})")
