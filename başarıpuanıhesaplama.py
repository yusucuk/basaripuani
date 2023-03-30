öğrenciadı = input("Öğrencinin Adını Giriniz:")
vize = int(input("vize notunu giriniz:"))
final = int(input("final notunu giriniz:"))
BaşarıPuanı = vize*4/10 + final*6/10
print(öğrenciadı)
print("Başarı Puanı")
print(BaşarıPuanı)

if BaşarıPuanı >= 85 and BaşarıPuanı <= 100:
    print("Geçme notunuz: AA")

if BaşarıPuanı >= 70 and BaşarıPuanı <= 85:
        print("Geçme notunuz: BA")

if BaşarıPuanı >= 60 and BaşarıPuanı <= 70:
        print("Geçme notunuz: BB")

if BaşarıPuanı >= 50 and BaşarıPuanı <= 60:
        print("Geçme notunuz: CB")

if BaşarıPuanı >= 40 and BaşarıPuanı <= 50:
        print("Geçme notunuz: CC")

if BaşarıPuanı >= 0 and BaşarıPuanı <= 40:
        print("Geçme notunuz: FF")
