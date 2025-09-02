def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Sıfıra bölünemez!"
    return x / y

while True:
    print("\nBasit Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")
    
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")
    
    if secim == '5':
        print("Hesap makinesi kapatılıyor...")
        break
    
    if secim in ('1', '2', '3', '4'):
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        if secim == '1':
            print(f"{sayi1} + {sayi2} = {add(sayi1, sayi2)}")
        elif secim == '2':
            print(f"{sayi1} - {sayi2} = {subtract(sayi1, sayi2)}")
        elif secim == '3':
            print(f"{sayi1} * {sayi2} = {multiply(sayi1, sayi2)}")
        elif secim == '4':
            print(f"{sayi1} / {sayi2} = {divide(sayi1, sayi2)}")
    else:
        print("Geçersiz giriş!")