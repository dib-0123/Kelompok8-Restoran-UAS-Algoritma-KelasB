# Sistem Manajemen Restoran Terintegrasi

**UAS Algoritma dan Struktur Data**
Program Studi S1 Pendidikan Teknik Informatika dan Komputer, FKIP — Universitas Sebelas Maret

Implementasi **Queue**, **Stack**, **Binary Search Tree (BST)**, dan **Binary Heap** dari nol (tanpa library struktur data bawaan Python), diintegrasikan dalam satu sistem manajemen restoran berbasis Command Line Interface (CLI) yang berjalan di Google Colab.

## Studi Kasus

Restoran **"Warung Algoritma"** dengan dua jenis pesanan:
- **Dine In** (makan di tempat)
- **Take Away Express** (bawa pulang, prioritas dapur lebih tinggi)

## Anggota Kelompok

| Nama                            | NIM      | Fokus                     |
|---------------------------------|--------- |-------                    |
| Queennera Martha Kusuma Wardhani| K3525012 | Queue & Binary Search Tree|
| Adibah Ruhil                    | K3525044 | Stack & Binary Heap       |
| Diah Anggraeni                  | K3525055 | Integrasi Sistem          |

## Alur Proses Bisnis

```
Pelanggan Datang & Memesan
        |
        v
   [ QUEUE ]  Antrean pesanan masuk (FIFO)
        |
        v
   [ BST ]    Pesanan aktif, disimpan & dicari per ID
        |
        v
   [ HEAP ]   Antrean prioritas dapur
        |     (Take Away Express didahulukan dari Dine In)
        v
   [ STACK ]  Riwayat transaksi (Selesai / Dibatalkan) -> mendukung undo
```

## Struktur Data & Kompleksitas

| Struktur Data | Digunakan Untuk | Operasi Utama | Kompleksitas |
|---|---|---|---|
| Queue (Linked List) | Antrean pesanan masuk (FIFO) | enqueue, dequeue, peek, display | O(1) / O(1) / O(1) / O(n) |
| Stack (Linked List) | Riwayat transaksi & undo (LIFO) | push, pop, peek, display | O(1) / O(1) / O(1) / O(n) |
| Binary Search Tree | Pesanan aktif, dicari per ID | insert, search, delete, inorder | O(h) / O(h) / O(h) / O(n) |
| Binary Heap (array) | Prioritas proses dapur | insert, delete_root, peek | O(log n) / O(log n) / O(1) |

*(h = tinggi tree, n = jumlah elemen)*


## Menu Program

```
1. Tambah Pesanan Baru (Pelanggan Datang)      [QUEUE]
2. Proses Antrean Masuk (Staff Terima Pesanan) [QUEUE -> BST/HEAP]
3. Lihat Semua Pesanan Aktif                   [BST - Inorder]
4. Cari Pesanan Berdasarkan ID                 [BST - Search]
5. Dapur Proses Pesanan Prioritas Tertinggi    [HEAP]
6. Batalkan Pesanan Berdasarkan ID             [BST/HEAP]
7. Undo Pembatalan Terakhir                    [STACK]
8. Lihat Riwayat Transaksi                     [STACK]
9. Lihat Statistik Sistem (BST & Heap)
0. Keluar
```

## Ketentuan Implementasi

- 100% Python standar, tanpa instalasi library tambahan.
- Tidak menggunakan `queue`, `collections.deque`, `heapq`, `PriorityQueue`, atau library struktur data/tree bawaan lainnya.
- Seluruh data disimpan di memori (tidak menggunakan database).
- Seluruh kode berada dalam satu file `.ipynb`.
