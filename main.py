from lib import cuadrado, rectangulo

print("Proyecto Figuras")
print(cuadrado.get_dentificador())
lado = 4
print(f"El area de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")

base = 2
altura = 4
print(f"El area de un rectangulo de base {base} y altura {altura} es: {rectangulo.get_area(base, altura)} y el perímetro es {rectangulo.get_perimetro(base, altura)}")