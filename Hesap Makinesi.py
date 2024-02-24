import tkinter as tk

arayuz = tk.Tk()  
arayuz.title("Hesap Makinesi")  
arayuz.geometry("400x400")  

sonuc = tk.Label(arayuz, text="Sonuç", font="Courier 16 bold", width=30, justify="center")
sonuc.place(x=15, y=20)


sayi1 = tk.Entry(arayuz, width=30, justify="right")
sayi1.place(x=120, y=80)


sayi2 = tk.Entry(arayuz, width=30, justify="right")
sayi2.place(x=120, y=120)

def toplama_komut():
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    sonuc.configure(text="Sonuç: " + str(s1 + s2))

def cikarma_komut():
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    sonuc.configure(text="Sonuç: " + str(s1 - s2))

def bolme_komut():
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    if s2 != 0:
        sonuc.configure(text="Sonuç: " + str(s1 / s2))
    else:
        sonuc.configure(text="Bölen sifir olamaz!")

def carpma_komut():
    s1 = float(sayi1.get())
    s2 = float(sayi2.get())
    sonuc.configure(text="Sonuç: " + str(s1 * s2))

def temizle_komut():
    sayi1.delete(0, 'end')
    sayi2.delete(0, 'end')
    sonuc.configure(text="Sonuç")

toplama = tk.Button(arayuz, text="Toplama", width=30, command=toplama_komut)
toplama.place(x=100, y=160)

cikarma = tk.Button(arayuz, text="Çikarma", width=30, command=cikarma_komut)
cikarma.place(x=100, y=190)

bolme = tk.Button(arayuz, text="Bölme", width=30, command=bolme_komut)
bolme.place(x=100, y=220)

carpma = tk.Button(arayuz, text="Çarpma", width=30, command=carpma_komut)
carpma.place(x=100, y=250)

temizle = tk.Button(arayuz, text="Temizle", width=30, command=temizle_komut)
temizle.place(x=100, y=280)

sayi1.focus()

arayuz.mainloop()
