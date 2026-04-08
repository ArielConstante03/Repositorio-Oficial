"""
EJEMPLOS DE USO - CONVERSOR DE UNIDADES
Demostraciones prácticas del programa
"""

from conversor_unidades import ConversorUnidades

def ejemplos_basicos():
    """Muestra ejemplos básicos de conversión"""
    conversor = ConversorUnidades()
    
    print("\n" + "="*60)
    print("EJEMPLOS BÁSICOS DE CONVERSIÓN")
    print("="*60)
    
    # Ejemplo 1: Conversión de pesos
    print("\n1️⃣ CONVERSIÓN DE PESOS:")
    print("-" * 40)
    valor = 5
    resultado, _ = conversor.convertir_pesos(valor, 'kg', 'g')
    print(f"  {valor} kilogramos = {resultado} gramos")
    
    resultado, _ = conversor.convertir_pesos(valor, 'kg', 'lb')
    print(f"  {valor} kilogramos = {resultado:.2f} libras")
    
    resultado, _ = conversor.convertir_pesos(10, 'lb', 'g')
    print(f"  10 libras = {resultado:.2f} gramos")
    
    # Ejemplo 2: Conversión de líquidos
    print("\n2️⃣ CONVERSIÓN DE LÍQUIDOS:")
    print("-" * 40)
    valor = 1
    resultado, _ = conversor.convertir_liquidos(valor, 'l', 'ml')
    print(f"  {valor} litro = {resultado} mililitros")
    
    resultado, _ = conversor.convertir_liquidos(valor, 'l', 'gal')
    print(f"  {valor} litro = {resultado:.3f} galones")
    
    resultado, _ = conversor.convertir_liquidos(250, 'ml', 'taza')
    print(f"  250 mililitros = {resultado:.3f} tazas")
    
    # Ejemplo 3: Conversión de gases
    print("\n3️⃣ CONVERSIÓN DE GASES (VOLUMEN):")
    print("-" * 40)
    resultado, _ = conversor.convertir_gases(1, 'm³', 'l')
    print(f"  1 metro cúbico = {resultado} litros")
    
    resultado, _ = conversor.convertir_gases(5000, 'cm³', 'l')
    print(f"  5000 centímetros cúbicos = {resultado} litros")
    
    # Ejemplo 4: Conversiones cruzadas (líquido a peso)
    print("\n4️⃣ CONVERSIÓN LÍQUIDO → PESO:")
    print("-" * 40)
    resultado, _ = conversor.liquido_a_peso(1, 'l', 'agua', 'kg')
    print(f"  1 litro de agua = {resultado} kilogramos")
    
    resultado, _ = conversor.liquido_a_peso(1, 'l', 'aceite', 'g')
    print(f"  1 litro de aceite = {resultado:.1f} gramos")
    
    resultado, _ = conversor.liquido_a_peso(250, 'ml', 'leche', 'g')
    print(f"  250 mililitros de leche = {resultado:.1f} gramos")
    
    # Ejemplo 5: Conversiones cruzadas (peso a líquido)
    print("\n5️⃣ CONVERSIÓN PESO → LÍQUIDO:")
    print("-" * 40)
    resultado, _ = conversor.peso_a_liquido(1, 'kg', 'agua', 'l')
    print(f"  1 kilogramo de agua = {resultado} litros")
    
    resultado, _ = conversor.peso_a_liquido(100, 'g', 'aceite', 'ml')
    print(f"  100 gramos de aceite = {resultado:.1f} mililitros")
    
    resultado, _ = conversor.peso_a_liquido(500, 'g', 'alcohol', 'ml')
    print(f"  500 gramos de alcohol = {resultado:.1f} mililitros")
    
    print("\n" + "="*60)


def ejemplo_receta():
    """Ejemplo práctico: Adaptando una receta de cocina"""
    conversor = ConversorUnidades()
    
    print("\n" + "="*60)
    print("EJEMPLO PRÁCTICO: ADAPTANDO UNA RECETA")
    print("="*60)
    
    print("\nReceta original (para 4 personas):")
    print("  • 500 ml de leche")
    print("  • 250 g de harina")
    print("  • 100 g de mantequilla")
    
    # Ajustar para 8 personas (doble)
    print("\nAjustada para 8 personas (doble):")
    resultado, _ = conversor.convertir_liquidos(500 * 2, 'ml', 'l')
    print(f"  • {resultado} litros de leche")
    
    resultado, _ = conversor.convertir_pesos(250 * 2, 'g', 'kg')
    print(f"  • {resultado} kilogramos de harina")
    
    resultado, _ = conversor.convertir_pesos(100 * 2, 'g', 'oz')
    print(f"  • {resultado:.1f} onzas de mantequilla")
    
    # Convertir a volumen la leche
    print("\nSi quieres medir la leche con tazas:")
    resultado, _ = conversor.convertir_liquidos(1000, 'ml', 'taza')
    print(f"  • 1 litro de leche ≈ {resultado:.1f} tazas")
    
    print()


def ejemplo_laboratorio():
    """Ejemplo práctico: Conversiones en un laboratorio"""
    conversor = ConversorUnidades()
    
    print("\n" + "="*60)
    print("EJEMPLO PRÁCTICO: LABORATORIO QUÍMICO")
    print("="*60)
    
    print("\nMezcla de soluciones:")
    print("-" * 40)
    
    # Mezcla de soluciones
    solucion1 = 250  # ml
    solucion2 = 500  # ml
    
    resultado, _ = conversor.convertir_liquidos(solucion1 + solucion2, 'ml', 'l')
    print(f"Volumen total: {solucion1} + {solucion2} ml = {resultado} litros")
    
    # Si la densidad es 1.05 g/ml
    peso_total = (solucion1 + solucion2) * 1.05
    resultado, _ = conversor.convertir_pesos(peso_total, 'g', 'kg')
    print(f"Peso total (densidad 1.05 g/ml): {resultado:.3f} kilogramos")
    
    # Concentración de disolución
    soluto = 50  # gramos
    disolvente = 950  # ml (agua)
    
    print(f"\nSolución: {soluto} g de soluto en {disolvente} ml de agua")
    resultado, _ = conversor.convertir_pesos(soluto, 'g', 'mg')
    print(f"  Soluto: {resultado} miligramos")
    
    resultado, _ = conversor.convertir_liquidos(disolvente, 'ml', 'l')
    print(f"  Disolvente: {resultado} litros")
    
    concentracion = (soluto / (soluto + disolvente)) * 100
    print(f"  Concentración: {concentracion:.2f}%")
    
    print()


def ejercicios_practicos():
    """Ejercicios para practicar conversiones"""
    print("\n" + "="*60)
    print("EJERCICIOS PRÁCTICOS")
    print("="*60)
    
    ejercicios = [
        ("Convierte 2.5 litros de agua a kilogramos", "2.5 l agua → kg"),
        ("¿Cuántos mililitros hay en 3 galones?", "3 gal → ml"),
        ("Convierte 150 libras a kilogramos", "150 lb → kg"),
        ("¿Cuántas cucharadas hay en 100 ml?", "100 ml → tbsp"),
        ("Convierte 1 metro cúbico a litros", "1 m³ → l"),
        ("¿Cuántos gramos pesa 1 litro de aceite?", "1 l aceite → g"),
        ("Convierte 500 gramos de leche a mililitros", "500 g leche → ml"),
        ("¿Cuántos centímetros cúbicos hay en 2 litros?", "2 l → cm³"),
    ]
    
    print("\n📚 Intenta resolver estos ejercicios:\n")
    for i, (pregunta, pista) in enumerate(ejercicios, 1):
        print(f"{i}. {pregunta}")
        print(f"   (Pista: {pista})")
    
    print("\n¡Ejecuta el programa con: python conversor_unidades.py\n")


if __name__ == "__main__":
    # Ejecutar todos los ejemplos
    ejemplos_basicos()
    ejemplo_receta()
    ejemplo_laboratorio()
    ejercicios_practicos()
