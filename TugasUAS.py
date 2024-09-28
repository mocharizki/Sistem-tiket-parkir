def main():
    type = input("masukan tipe data kendaraan anda\n>Sepeda\n>Motor\n>Mobil\nSilahkan Masukan Tipe Kendaraan :")
   
    for i in range(1):
        print("----------")
    if i == "Sepeda" or type == "sepeda" :
        plat = input("Masukan Nomor Kendaraan : ")
        jamsuk = float(input ("Jam Masuk : "))
        jamlar = float(input ("Jam Keluar : "))
        lampar = int(jamlar - jamsuk)
        if lampar<=2:
            hitung = 1000
        else :
            hitung = 500 * (lampar - 2) + 1000
        print("Lama Parkir\t\t:", int (lampar), "jam")
        print("Biaya Parkir Sepeda : Rp.", int(hitung))
    elif i == "Motor" or type == "motor" :
        plat = input("Masukan Nomor Kendaraan: ")
        jamsuk = float(input ("Jam Masuk : "))
        jamlar = float(input ("Jam Keluar : "))
        lampar = int(jamlar - jamsuk)
        
        if lampar<=2:
            hitung = 3000
        else :
            hitung = 2000 * (lampar - 2) + 3000
        print("Lama Parkir\t\t:", int (lampar), "jam")
        print("Biaya Parkir Motor : Rp.", int(hitung))
    elif i =="Mobil" or type == "mobil" :
        plat = input("Masukan Nomor Kendaraan: ")
        jamsuk = float(input ("Jam Masuk : "))
        jamlar = float(input ("Jam Keluar : "))
        lampar = int(jamlar - jamsuk)
        if lampar<=3:
            hitung = 5000
        else :
            hitung = 2000 * (lampar - 3) + 5000
        print("Lama Parkir\t\t:", int (lampar), "jam")
        print("Biaya Parkir Mobil : Rp.", int(hitung))
    else :
        main()
  
    kembali = int(input("Tunai : "))
    if kembali== hitung:
        kembalian = 0
    elif kembali>= hitung:
        kembalian = kembali - hitung
    else :
        print("not found")
    print("kembalian yang dibayarkan : Rp.",kembalian) 

    print("\n==================================")
    print("Selamat Datang Di Stasiun Cikarang")
    print("==================================")
    print("Tanggal : {now}")
    print("Jenis Kendaraan\t\t:", type)
    print ("Nomor Kendaraan \t: ",plat)
    print("Lama Parkir\t\t:", int (lampar), "jam")
    print("Total Pembayaran\t:", hitung)
    print("Tunai\t\t\t:", kembali)
    print("Kembalian\t\t:",kembalian)
    print("===================================")
    print("Terima Kasih Atas Kunjungan Anda")
    print("===================================")

main ()