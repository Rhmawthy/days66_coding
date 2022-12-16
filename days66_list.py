#inputan list


data = int(input("masukkan angka :"))

genap = [ i for i in range (2,data+1,2)]
ganjil = [i for i in range (1,data+1,2)]

if data %2 == 0 :
    print(genap)
elif data %2 !=0 :
    print(ganjil)

         




