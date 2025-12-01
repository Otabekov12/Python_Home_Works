ism = input("Ismingizni yozing: ")

tugilgan_yil = int(input("Tug'ilgan yilingiz: "))

hozirgi_yil = 2025

yosh = hozirgi_yil - tugilgan_yil

# 5. Natijani ko'rsatish
print(ism + ", siz " + str(yosh) + " yoshdasiz")

txt = 'LMaasleitbtui'



mashinalar = ['Lamborghini', 'Maserati', 'Aston Martin', 'Audi', 'BMW', 
              'Mercedes', 'Toyota', 'Honda', 'Ford', 'Chevrolet']

print("Matn:", txt)




txt = "I'am John. I am from London"

parts = txt.split("from")

if len(parts) > 1:
    residence = parts[1].strip().rstrip('.')
    print("Residence:", residence)


matn = input("Matn kiriting: ")

print("Teskari:", matn[::-1])



matn = input("Matn kiriting: ")

unlilar = "aeiouAEIOU"
sanoq = 0

for harf in matn:
    if harf in unlilar:
        sanoq += 1

print(f"Matnda {sanoq} ta unli harf bor")

sonlar = input("Sonlarni vergul bilan ajrating: ")

sonlar_listi = sonlar.split(',')
sonlar_listi = [float(son.strip()) for son in sonlar_listi]

maksimum = max(sonlar_listi)

print(f"Ro'yxatdagi eng katta son: {maksimum}")




soz = input("So'z kiriting: ")

teskari = soz[::-1]

if soz == teskari:
    print(f"✅ '{soz}' - palindrome!")
else:
    print(f"❌ '{soz}' - palindrome emas!")




email = input("Email manzilingizni kiriting: ")

if "@" in email:
    domen = email.split("@")[1]
    print(f"Email domeni: {domen}")
else:
    print("❌ Noto'g'ri email formati!")


import random
import string

uzunlik = int(input("Parol uzunligini kiriting: "))


belgilar = string.ascii_letters + string.digits + string.punctuation


parol = ''.join(random.choice(belgilar) for _ in range(uzunlik))

print(f"Tasodifiy parol: {parol}")

