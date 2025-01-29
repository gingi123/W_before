import random
import math

New_list:list[str] = ["üveg","bronz","porcelán","alumínium","műanyag"]

x = random.choice(New_list)


print(f"1.feladat: Henger térfogat számítás")
r:int = int(input("Adja meg a henger alapjának sugarát: "))
m:int = int(input("Adja meg a henger magasságát: "))

V = r**2 * math.pi * m

print(f"A henger anyaga: {x}")
print(f"A henger térfogata: {V:0.2f}")





