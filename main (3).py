'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
ulang = 1
nilaiX = 0 
nilaiY = 0
XkaliY = 0 
xPangkat = 0
yPangkat = 0
while ulang == 1:
    print("----------------------------")
    print("PROGRAM HITUNG X DAN Y")
    print("----------------------------")
    n = int(input("Masukkan jumlah x dan y yang akan diinput? "))
    x = []
    y = []
    for i in range(n):
        # TODO: write code...
        temp = int(input("nilai x[" + str((i)) + "] = "))
        x.append(temp)
        temp = int(input("nilai y[" + str((i)) + "] = "))
        y.append(temp)
    print("Hasil Perhitungan")
    print("----------------")
    print("-------------------------------------------------------------------------------------------")
    print("|idx\t|\tx\t|\ty\t|\tx.y\t|\tx^2\t|\ty^2\t|")
    print("-------------------------------------------------------------------------------------------")
    for i in range(n):
        print("| " + str(i) + "\t|\t"+ str(float(x[i])) +"\t|\t"+ str(float(y[i])) +"\t|\t" + str(float(x[i] * y[i])) +"\t|\t" + str(float(x[i] * x[i])) + "\t|\t"+ str(float(y[i] * y[i])) +"\t|")
        nilaiX += float(x[i])
        nilaiY += float(x[i])
        XkaliY += float(x[i] * y[i])
        xPangkat += float(x[i] * x[i])
        yPangkat += float(y[i] * y[i])
    print("-------------------------------------------------------------------------------------------")
    print("|sum\t|\t" + str(nilaiX) +"\t|\t" + str(nilaiY)  + "\t|\t" + str(XkaliY) + "\t|\t" + str(xPangkat) + "\t|\t" + str(yPangkat) + "\t|")
    print("-------------------------------------------------------------------------------------------")
    print("\n\n1. Hitung/Lagi")
    print("2. Selesai")
    ulang = int(input("Pilih 1/2 ? "))
else :
    ulang = 2