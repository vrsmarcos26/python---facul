from Codigo_princi import FormaGeometrica, Quadrado, Circulo
from abc import ABC, abstractmethod #importa o módulo ABC (Abstract base ckasses)


if __name__ == '__main__':
    obj_quad = Quadrado(3)
    print(f"""\n ===== Quadrado =====
          
    - Lado: {obj_quad.get_lado()}
    - Área: {obj_quad.area()}
    - Perimetro: {obj_quad.area()}

""")
    print("Mudando valor do lado ...\n")
    obj_quad.set_lado(5)
    print(f"""\n ===== Quadrado =====
          
    - Lado: {obj_quad.get_lado()}
    - Área: {obj_quad.area()}
    - Perimetro: {obj_quad.area()}

""")
    obj_circulo = Circulo(5)
    print(f"""\n ===== Circulo =====
          
    - Raio: {obj_circulo.get_raio()}
    - Área: {obj_circulo.area_qd()}

""")
    print("Mudando valor do raio ...\n")
    obj_circulo.set_raio(2)
    print(f"""\n ===== Circulo =====
          
    - Raio: {obj_circulo.get_raio()}
    - Área: {obj_circulo.area_qd()}

""")
