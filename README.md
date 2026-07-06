# Sistem Antrean dan Pemesanan Restoran

**UAS Algoritma dan Struktur Data — Kelompok 8**
Program Studi S1 Pendidikan Teknik Informatika dan Komputer, FKIP — Universitas Sebelas Maret

Implementasi **Queue**, **Stack**, **Binary Search Tree (BST)**, dan **Binary Heap** dari nol (tanpa library struktur data bawaan Python), diintegrasikan dalam satu sistem antrean & pemesanan restoran berbasis Command Line Interface (CLI) yang berjalan di Google Colab.

## Studi Kasus

Restoran dengan dua jenis pesanan:
- **Dine In** (makan di tempat)
- **Take Away Express** (bawa pulang, mendapat bonus prioritas di dapur)

## Anggota Kelompok

| Nama | NIM | Fokus |
|---|---|---|
| Queennera Martha Kusuma Wardhani | K3525012 | Queue & Binary Search Tree |
| Adibah Ruhil | K3525044 | Stack & Binary Heap |
| Diah Anggraeni | K3525055 | Integrasi Sistem |

## Alur Proses Bisnis

```
Pelanggan Datang
        |
        v
   [ QUEUE ]  Antrean pelanggan menunggu giliran dilayani (FIFO)
        |
        v
   [ BST ]    Begitu pesanan dibuat, disimpan sbg data aktif (key = ID Pesanan)
        |     -> mendukung pencarian, insert, delete efisien
        v
   [ HEAP ]   Setiap pesanan diberi skor prioritas (priority_score)
        |     -> Take Away Express mendapat bonus prioritas, diproses dapur lebih dulu
        v
   [ STACK ]  Pesanan yang selesai diproses dicatat sbg riwayat transaksi (LIFO)
        |     -> mendukung pembatalan/undo lewat operasi pop
```

Traversal BST yang dipakai: **Inorder** — karena BST di-key berdasarkan ID pesanan, inorder traversal otomatis menghasilkan daftar pesanan aktif yang terurut rapi berdasarkan ID.

## Struktur Data & Kompleksitas

| Struktur Data | Implementasi | Digunakan Untuk | Kompleksitas Operasi Utama |
|---|---|---|---|
| `Queue` | Linked List (`NodeQueue`) | Antrean pelanggan (FIFO) | enqueue/dequeue/peek: O(1), display: O(n) |
| `Stack` | Linked List (`NodeStack`) | Riwayat transaksi (LIFO) | push/pop/peek: O(1), display: O(n) |
| `BST` | Node (`NodeBST`), key = ID Pesanan | Data pesanan aktif | insert/search/delete: O(h), inorder: O(n) |
| `BinaryHeap` | Array (list Python murni) | Prioritas proses dapur | insert/delete_root: O(log n), peek: O(1) |

*(h = tinggi tree, n = jumlah elemen)*

## Cara Menjalankan

1. Buka file [`UAS__ALGORITMA_Kel_8_Restoran_StrukturData.ipynb`](./UAS__ALGORITMA_Kel_8_Restoran_StrukturData.ipynb) — bisa dibuka langsung di GitHub, atau klik untuk buka di Google Colab.
2. Di Colab: **Runtime → Run all** untuk menjalankan seluruh cell dari atas ke bawah secara berurutan.
3. Pada cell terakhir, program (`main()`) otomatis berjalan dan menampilkan menu — ketik pilihan di kotak input yang muncul di bawah cell.

## Menu Program

```
1. Pelanggan baru datang (masuk antrean)        [QUEUE]
2. Layani pelanggan berikutnya (buat pesanan)   [QUEUE -> BST & HEAP]
3. Dapur proses pesanan prioritas tertinggi     [HEAP -> BST delete -> STACK]
4. Cari pesanan aktif berdasarkan ID            [BST - Search]
5. Batalkan transaksi terakhir (undo)           [STACK - pop]
6. Tampilkan antrean pelanggan                  [QUEUE - display]
7. Tampilkan pesanan aktif (BST - inorder)      [BST - inorder]
8. Tampilkan antrean prioritas dapur (Heap)     [HEAP - display]
9. Tampilkan riwayat transaksi (Stack)          [STACK - display]
0. Keluar
```

## Ketentuan Implementasi

- 100% Python standar, tanpa instalasi library tambahan.
- Tidak menggunakan `queue`, `collections.deque`, `heapq`, `PriorityQueue`, atau library struktur data/tree bawaan lainnya — `BinaryHeap` memakai `list` Python murni sebagai array, bukan modul `heapq`.
- Seluruh data disimpan di memori (tidak menggunakan database).
- Seluruh kode berada dalam satu file `.ipynb`.

## Dokumen Terkait

- 📄 Laporan lengkap (penjelasan implementasi, alasan pemilihan struktur data, analisis Big-O, pembagian tugas): lihat file laporan PDF pada submission terpisah.

---
*Project ini dibuat untuk memenuhi tugas UAS mata kuliah Algoritma dan Struktur Data.*
