def guess_number():
    angka_rahasia = 4
    guess = 0
    batas_guess = 3
    
    while guess < batas_guess:
        user = int(input("Masukkan tebakan > "))
        if user  == angka_rahasia:
            print("Selamat!, tebakan anda benar")
            break
        else:
            print("Tebakan salah!")
            guess += 1
    else:
        print(f"Anda tidak menemukan angkanya, angka rahasianya adalah {angka_rahasia}")

guess_number()