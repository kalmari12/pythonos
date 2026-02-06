def összeg(lista) -> int:
    össz = 0
    for x in lista:
        össz += x
    return össz

def egyenlet(a: int, b: int, c: int, d = int(100)) -> float:
    return a/b*c*d+(d*c)-(a-d)

raktár = [5, 12, 65, 3, 7]
raktár2 = [56, 345, 233, 111, 345, 785]

print(f"a lista elemeinek az összege: {összeg(raktár)}")
print(f"A lista elemeinek az összege {összeg(raktár)}")

print(f"az egyenlet eredmenye {egyenlet(45, 12, 6)}")









