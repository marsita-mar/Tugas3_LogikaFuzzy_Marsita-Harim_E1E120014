pilih=1
def menu():
    global pilih
    print("-"*3,"Menu","-"*3)
    print("1. Linier")
    print("2. Segitiga")
    print("3. Trapesium")
    print("4. Sigmoid")
    print("5. Gauss")
    print("6. Beta")
    print("7. Keluar")
    pilih=int(input("Masukan pilihan Anda: "))

def program_linier(x,a,b):
    print("Pilih Linier Naik atau Linier Turun")
    print("1.1 Linier Naik")
    print("1.2 Linier Turun")
    pilih=int(input("Linier Naik/Linier Turun: "))
    if pilih==1:
        if x<=a:
            print("Derajat Keanggotaan = 0 ")
        elif x>=a and x<=b:
            hitung=(x-a)/(b-a)
            print("Derajat Keanggotaan= ",hitung)
        elif x>=b:
            print("Derajat Keanggotaan = 1 ")
    elif pilih==2:
        if x>=a and x<=b:
            hitung=(b-x)/(b-a)
            print("Derajat Keanggotaan= ",hitung)
        elif x>=b:
            print("Derajat Keanggotaan = 0 ")

def program_segitiga(x,a,b,c):
    if x<=a or x>=c:
        print("Derajar Keanggotaan = 0 ")
    elif x>=a and x<=b:
        hitung=(x-a)/(b-a)
        print("Derajat Keanggotaan = ",hitung)
    elif x>=a and x<=b:
        hitung=(x-b)/(c-b)
        print("Derajat Keanggotaan = ",hitung)

def program_trapesium(x,a,b,c,d):
    if x<=a or x>=d:
        print("Derajar Keanggotaan = 0 ")
    elif x>=a and x<=b:
        hitung=(x-a)/(b-a)
        print("Derajat Keanggotaan = ",hitung)
    elif x>=b and x<=c:
        print("Derajat Keanggotaan = 1 ")
    elif x>c and x<d:
        hitung=(d-x)/(d-c)
        print("Derajat Keanggotaan = ",hitung)

def program_sigmoid(x,A,Y,B):
    """
    A=Alpha
    Y=Gamma
    B=Beta
    """
    print("Pilih Sigmoid Kurva S-Pertumbuhan ATAU Penyusutan")
    print("1.1 Pertumbuhan")
    print("1.2 Penyusutan")
    pilih=int(input("Pertumbuhan/Penyusutan: "))
    if pilih==1:
        if x <= A:
            print("Derajat Keanggotaan: 0 ")
        elif x >= A and x <= B:
            hitung = 2 * (((x - A) / (Y - A)) ** 2)
            print("Derajat Keanggotaan = ", hitung)
        elif x >= B and x <= Y:
            hitung = 1 - (2 * (((Y - x) / (Y - A)) ** 2))
            print("Derajat Keanggotaan = ", hitung)
        elif x >= Y:
            print("Derajat Keanggotaan = 1 ")
    elif pilih==2:
        if x <= A:
            print("Derajat Keanggotaan: 1 ")
        elif x >= A and x <= B:
            hitung = 1 - (2 * (((Y - x) / (Y - A)) ** 2))
            print("Derajat Keanggotaan = ", hitung)
        elif x >= B and x <= Y:
            hitung = 2 * (((x - A) / (Y - A)) ** 2)
            print("Derajat Keanggotaan = ", hitung)
        elif x >= Y:
            print("Derajat Keanggotaan = 0 ")

def program_gauss(x,k,Y):
    pangkat=-(k*((Y-x)**2))
    """
    rumus fungsi keanggotaan gauss
    G(x;k;Y)=e**((-k(Y-x)**2)**2)
    dimana e=2,7182
    """
    hitung=2.7182**pangkat
    print("Derajat Keanggotaan = ",hitung)

def program_beta(x,Y,B,A):
    """
    A=Alpha
    Y=Gamma
    B=Beta
    """
    b_bawah=((x-Y)/B)**2
    hitung=1/(1+b_bawah)
    print("Derajat Keanggotaan = ",hitung)

while pilih<7:
    menu()
    if pilih==1:
        x = int(input("Masukan nilai x: "))
        a = int(input("Masukan nilai a: "))
        b = int(input("Masukan nilai b: "))
        program_linier(x,a,b)
    elif pilih==2:
        x = int(input("Masukan nilai x: "))
        a = int(input("Masukan nilai a: "))
        b = int(input("Masukan nilai b: "))
        c = int(input("Masukan nilai c: "))
        program_segitiga(x, a, b, c)
    elif pilih==3:
        x = int(input("Masukan nilai x: "))
        a = int(input("Masukan nilai a: "))
        b = int(input("Masukan nilai b: "))
        c = int(input("Masukan nilai c: "))
        d = int(input("Masukan nilai d: "))
        program_trapesium(x,a,b,c,d)
    elif pilih==4:
        x= int(input("Masukan nilai x= "))
        A = int(input("Masukan nilai A= "))
        Y = int(input("Masukan nilai Y= "))
        B = int(input("Masukan nilai B= "))
        program_sigmoid(x, A, Y, B)
    elif pilih==5:
        x= int(input("Masukan nilai x= "))
        k = int(input("Masukan nilai k= "))
        Y = int(input("Masukan nilai Y= "))
        program_gauss(x,k,Y)
    elif pilih==6:
        x= int(input("Masukan nilai x= "))
        Y = int(input("Masukan nilai Y= "))
        B = int(input("Masukan nilai B= "))
        A = int(input("Masukan nilai A= "))
        program_beta(x,Y,B,A)
    else:
        print("Anda Keluar")

