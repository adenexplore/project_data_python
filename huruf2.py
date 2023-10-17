huruf = input("masukkan sebuah huruf:")

if (huruf >= 'A'):
    if (huruf <= 'Z'):
        print("ini adalah huruf besar")
    elif (huruf >= 'a'):
        if (huruf <= 'z'):
            print("ini adalah huruf kecil")
        else:
            print("Huruf > z")
    else:
        print("Huruf > z tapi <a")
else:
    print("huruf<A")
