#Nama : Muhammad Rizal Muhaimin
#NIM  : 13519136
#Deskripsi: Penyelesaian Cryptarithmetic dengan Algoritma Brute Force

import timeit
import os

def Tampilan_Awal():
    print(
    """
=========================================================
Penyelesaian Cryptarithmetic dengan Algoritma Brute Force
        Tugas Kecil 1 IF2211 Strategi Algoritma
                Semester II tahun 2020/2021
========================================================\n"""
            )

def String_unik(S1,S2):
    #membuat kata unik dari inputan yang ada
    Str_Unix =""
    for huruf in S1:
        if huruf not in Str_Unix:
            Str_Unix += huruf
    for huruf in S2:
        if huruf not in Str_Unix:
            Str_Unix += huruf
    return Str_Unix

def Str_to_angka(Str_Input,Str_Unik, List_acuan):
    #mengembalikan kata angka kedalam integer
    angka = ''
    for huruf in Str_Input:
        idx = 0
        while huruf != Str_Unik[idx]:
            idx += 1
        angka += str(List_acuan[idx])

    return int(angka)


def Awal_Kata_Not_Nol(Str_input, Str_unik,List_acuan):
    #Mengembalikan true ketika awal kata tidak direpresentasikan dengan nol (0)
    idx = 0
    while Str_input[0] != Str_unik[idx]:
        idx +=1
    return (List_acuan[idx] != 0)

def Semua_Awal_Not_Nol_rekursif(L,n,s,Str_Unik,List_acuan):
    #memastikan tidak ada hufuf awal di repesentasikan dengan nol (0)
    if s == n:
        return Awal_Kata_Not_Nol(L[s-1],Str_Unik, List_acuan)
    else:
        return Awal_Kata_Not_Nol(L[s-1],Str_Unik, List_acuan) and Semua_Awal_Not_Nol_rekursif(L,n,s+1,Str_Unik, List_acuan)

def incramentList(L):
    #proses incrament permutasi
    j = L[len(L)-1]
    while j in L:
        j += 1
    L[len(L)-1] = j

    while int(10) in L[1:]:
        idx = 0
        while L[idx] != 10:
            idx += 1
        
        j = L[idx-1]
        while j in L[0:idx]:
            j += 1

        L[idx-1] = j

        j = 0

        while j in L[0:idx]:
            j += 1

        L[idx] = j

        if(idx +1 < len(L)):
            for i in range(idx+1,len(L)):
                
                if L[i] in L[0:i]:
                    j = 0
                    while j in L[0:i]:
                        j+=1 
                    L[i] = j
                
def List_file_test ():
    #membaca list file yang ada di file test
    print("Daftar file test:\n")
    path = "../test"
    Dir_test = os.listdir(path)
    for namefile in Dir_test:
        print(namefile)

def Read_file_test():
    #membaca file dan menampilkan data file dan mengembalikan list string
    nfile = input("\nMasukkan Nama File\n>:")
    try:
        path = "../test/"+str(nfile)
        File = open(path, 'r')
        print("\nCryptarithmetic:")
        List_kata =[]
        Line = File.readline()
        List_kata.append(Line.strip())
        while Line:
            print(Line, end="")
            Line = File.readline()
            List_kata.append(Line.strip())
        print("\n")
        List_kata.pop()
        List_kata[len(List_kata)-2] = List_kata[len(List_kata)-1]
        List_kata.pop()
        List_kata[len(List_kata)-2] = List_kata[len(List_kata)-2][:len(List_kata[len(List_kata)-2])-1]

        return List_kata

    except:
        print("Maaf Nama File salah")


def Cryptarithmetic_dengan_Algoritma_Brute_Force():
    #PROGRAM UTAMA
    List_input = Read_file_test() #def
    S_Unik = ""

    for i in range(len(List_input)-1):
        if i == 0 :
            S_Unik = String_unik(List_input[i], List_input[i+1]) #def
        else:
            S_Unik = String_unik(S_Unik,List_input[i+1]) #def

    listAngka = [i for i in range(len(S_Unik))] #representasi S_unik dalam anggka
    start = timeit.default_timer() # catat waktu mulai
    n_permutasi = 1

    while listAngka[0] !=10: #konodisi berhenti 
        found = False
        while (not found):
            List_nilai =[]
            for kata in List_input:
                List_nilai.append( Str_to_angka(kata,S_Unik, listAngka))
            
            if (sum(List_nilai[0:len(List_nilai)-1]) == List_nilai[len(List_nilai)-1] and Semua_Awal_Not_Nol_rekursif(List_input,len(List_input),1,S_Unik,listAngka)):
                found = True #kondisi ditemukan
            else:
                incramentList(listAngka)
                n_permutasi += 1
                if(listAngka[0] ==10): break
            
        if(listAngka[0] == 10): break
        stop = timeit.default_timer() # catat waktu selesai
        lama_eksekusi = stop - start # lama eksekusi dalam satuan detik

        print("Salah satu solusinya adalah:")

        Total = str(Str_to_angka(List_input[len(List_input)-1],S_Unik, listAngka))
        for i in range(len(List_input)):
            if i == len(List_input)-1:
                print("-"*len(Total)+"+")
                
            else:
                n = len(Total) - len(str(Str_to_angka(List_input[i],S_Unik, listAngka)))
                print(" "*n,end='')
            print(Str_to_angka(List_input[i],S_Unik, listAngka))

        print("\nDengan",end=" ")
        for i in range(len(S_Unik)):
            print(S_Unik[i],":",listAngka[i],end=", ")

        print("\nLama eksekusi: ",lama_eksekusi,"detik &",n_permutasi,"permutasi.\n")
        incramentList(listAngka)
        n_permutasi += 1

    print("""
=========================================================
                   Proses Selesai
=========================================================""")

# RUN PROGRAM
run = True
while run:
    Tampilan_Awal()
    List_file_test ()
    Cryptarithmetic_dengan_Algoritma_Brute_Force()
    N = input("Play Again? (y) :> ")
    if N != "y":
        run = False
