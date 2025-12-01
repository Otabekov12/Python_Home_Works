a = float(input("Kvadratning tomonini kiriting: "))
perimetr = 4 * a
yuza = a * a  # yoki a ** 2
print(f"Kvadratning perimetri: {perimetr}")
print(f"Kvadratning yuzasi: {yuza}")



import math

d = float(input("Aylananing diametrini kiriting: "))

uzunlik = math.pi * d

print(f"Aylananing uzunligi: {uzunlik:.2f}")

print("Ikki sonning o'rtacha qiymatini hisoblash dasturi")
print("-" * 40)

try:
    a = float(input("Birinchi sonni kiriting (a): "))
    b = float(input("Ikkinchi sonni kiriting (b): "))
    
    
    ortalama = (a + b) / 2
    
    # Natijalarni chiqarish
    print("\nNatijalar:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a + b = {a + b}")
    print(f"(a + b) / 2 = {ortalama}")
    print(f"\nJavob: {a} va {b} sonlarining o'rtacha qiymati: {ortalama}")
    
except ValueError:
    print("Xato: Iltimos, faqat son kiriting!")



print("Ikki sonning yig'indisi, ko'paytmasi va kvadratlarini hisoblash")
print("=" * 55)

a = float(input("Birinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))


yigindi = a + b

kopaytma = a * b

a_kvadrat = a ** 2  # yoki a * a

b_kvadrat = b ** 2  # yoki b * b

print("\n" + "=" * 55)
print("NATIJALAR:")
print("=" * 55)
print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {yigindi}")
print(f"a × b = {kopaytma}")
print(f"a² = {a_kvadrat}")
print(f"b² = {b_kvadrat}")
