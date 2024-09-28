from lib import cuadrado, triangulo, rectangulo
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado=4
print(f"El area de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")

base = 4
altura = 2
print(cuadrado.get_identificador())
print(f"El area de un triángulo de base {base} y altura {altura} es: {triangulo.get_area(base, altura)} y el perímetro es {triangulo.get_perimetro(base, base, base)}")

base = 2
altura = 4
print(f"El area de un rectangulo de base {base} y altura {altura} es: {rectangulo.get_area(base, altura)} y el perímetro es {rectangulo.get_perimetro(base, altura)}")