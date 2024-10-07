# Antrian pelanggan di kasir minimarket 
queue = []

# Operasi enqueue (menambahkan pelanggan ke antrian)
queue.append("pelanggan 1")
queue.append("pelanggan 2")
queue.append("pelanggan 3")
queue.append("pelanggan 4")

print("Queue setelah operasi enqueue:", queue)
print(f"Jumlah pelanggan dalam antrian: {len(queue)}\n")

# Operasi dequeue (mengeluarkan pelangan dari antrian)
print("pelangan yang keluar dari antrian (dequeue):", queue.pop(0))
print("Sisa pelanggan dalam antrian:", queue)
print("pelenggan terdepan saat ini:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah pelanggan dalam antrian: {len(queue)}\n")

print("pelanggan yang keluar dari antrian (dequeue):", queue.pop(0))
print("Sisa pelanggan dalam antrian:", queue)
print("pelanggan terdepan saat ini:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah pelanggan dalam antrian: {len(queue)}\n")

print("pelanggan yang keluar dari antrian (dequeue):", queue.pop(0))
print("Sisa pelanggan dalam antrian:", queue)
print("pelanggan terdepan saat ini:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah pelanggan dalam antrian: {len(queue)}\n")

# Memeriksa apakah antrian kosong
print("Apakah antrian  kosong?:", len(queue) == 0)