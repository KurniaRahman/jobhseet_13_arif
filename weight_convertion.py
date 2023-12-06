def weight_convertion():
    berat = int(input("Masukkan berat badan anda > "))
    satuan = input("Masukkan satuan apa yang akan digunakan ? (K untuk KG, L untuk LBS >)")
   
    if satuan.lower() == 'k':
        print(f"Berat badan anda dikonversi menjadi kilogram adalah {round(berat * 0.453592)} kg")
    elif satuan.lower() == 'l':
        print(f"Berat badan anda dikonversi menjadi pound adalah {round(berat * 2.20462 )} lbs")

weight_convertion()
       