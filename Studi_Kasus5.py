def biaya_parkir(jenis_kendaraan, waktu_parkir):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    else :
        tarif = 3000
    
    total_biaya = tarif * waktu_parkir
    return total_biaya

while True : 
    jenis_kendaraan = input("masukkan jenis kendaraan (mobil/motor): ")
    if jenis_kendaraan not in ("mobil", "motor"):
        print("kendaraan tidak valid, coba lagi.") 
        continue  

    jam_masuk = int(input("jam masuk : "))
    jam_keluar = int(input("jam keluar : "))
    lama_parkir = jam_keluar - jam_masuk 
    biaya_parkir = biaya_parkir(jenis_kendaraan, lama_parkir)

    print ("========PARKIR========")
    print (f"jenis kendaraan : {jenis_kendaraan}")
    print (f"jam masuk : {jam_masuk}")
    print (f"jam keluar : {jam_keluar}")
    print (f"lama parkir : {lama_parkir} jam")
    print (f"biaya parkir : Rp{biaya_parkir:,}")
    break