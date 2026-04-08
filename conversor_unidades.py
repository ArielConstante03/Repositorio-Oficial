"""
CONVERSOR DE UNIDADES - PESOS, LÍQUIDOS Y GASES
Programa para convertir entre diferentes tipos de unidades
"""

class ConversorUnidades:
    """Clase principal para convertir entre diferentes unidades"""
    
    # Factores de conversión a unidad base (gramos, mililitros, etc.)
    PESOS = {
        'gramo': 1,
        'g': 1,
        'kilogramo': 1000,
        'kg': 1000,
        'miligramo': 0.001,
        'mg': 0.001,
        'libra': 453.592,
        'lb': 453.592,
        'onza': 28.3495,
        'oz': 28.3495,
        'tonelada': 1000000,
        't': 1000000
    }
    
    LIQUIDOS = {
        'mililitro': 1,
        'ml': 1,
        'litro': 1000,
        'l': 1000,
        'galón (US)': 3785.41,
        'gal': 3785.41,
        'onza líquida (US)': 29.5735,
        'fl oz': 29.5735,
        'taza': 236.588,
        'pinta': 473.176,
        'cucharada': 14.8868,
        'cucharadita': 4.92892
    }
    
    GASES = {
        'metro cúbico': 1000000,
        'm³': 1000000,
        'litro': 1000,
        'l': 1000,
        'centímetro cúbico': 1,
        'cm³': 1,
        'cc': 1,
        'mililitro': 1,
        'ml': 1
    }
    
    # Densidades comunes a 20°C (g/ml) para conversiones cruzadas
    DENSIDADES = {
        'agua': 1.0,
        'aceite': 0.92,
        'leche': 1.03,
        'alcohol': 0.789,
        'mercurio': 13.6,
        'gasolina': 0.72,
        'aire': 0.0012
    }
    
    def __init__(self):
        self.historial = []
    
    def convertir_pesos(self, valor, unidad_origen, unidad_destino):
        """Convierte entre unidades de peso"""
        unidad_origen = unidad_origen.lower()
        unidad_destino = unidad_destino.lower()
        
        if unidad_origen not in self.PESOS or unidad_destino not in self.PESOS:
            return None, "Unidad de peso no válida"
        
        # Convertir a gramos (unidad base)
        gramos = valor * self.PESOS[unidad_origen]
        
        # Convertir de gramos a unidad destino
        resultado = gramos / self.PESOS[unidad_destino]
        
        return resultado, None
    
    def convertir_liquidos(self, valor, unidad_origen, unidad_destino):
        """Convierte entre unidades de líquidos"""
        unidad_origen = unidad_origen.lower()
        unidad_destino = unidad_destino.lower()
        
        if unidad_origen not in self.LIQUIDOS or unidad_destino not in self.LIQUIDOS:
            return None, "Unidad de líquido no válida"
        
        # Convertir a mililitros (unidad base)
        mililitros = valor * self.LIQUIDOS[unidad_origen]
        
        # Convertir de mililitros a unidad destino
        resultado = mililitros / self.LIQUIDOS[unidad_destino]
        
        return resultado, None
    
    def convertir_gases(self, valor, unidad_origen, unidad_destino):
        """Convierte entre unidades de gases (volumen)"""
        unidad_origen = unidad_origen.lower()
        unidad_destino = unidad_destino.lower()
        
        if unidad_origen not in self.GASES or unidad_destino not in self.GASES:
            return None, "Unidad de gas no válida"
        
        # Convertir a cm³ (unidad base)
        cm3 = valor * self.GASES[unidad_origen]
        
        # Convertir de cm³ a unidad destino
        resultado = cm3 / self.GASES[unidad_destino]
        
        return resultado, None
    
    def liquido_a_peso(self, valor, unidad_liquido, sustancia='agua', unidad_peso='gramo'):
        """Convierte un volumen de líquido a peso usando densidad"""
        sustancia = sustancia.lower()
        unidad_liquido = unidad_liquido.lower()
        unidad_peso = unidad_peso.lower()
        
        if sustancia not in self.DENSIDADES:
            return None, f"Sustancia no disponible. Disponibles: {list(self.DENSIDADES.keys())}"
        
        if unidad_liquido not in self.LIQUIDOS or unidad_peso not in self.PESOS:
            return None, "Unidad no válida"
        
        # Convertir volumen a mililitros
        ml = valor * self.LIQUIDOS[unidad_liquido]
        
        # Calcular peso en gramos (densidad * volumen)
        densidad = self.DENSIDADES[sustancia]
        gramos = ml * densidad
        
        # Convertir gramos a unidad destino
        resultado = gramos / self.PESOS[unidad_peso]
        
        return resultado, None
    
    def peso_a_liquido(self, valor, unidad_peso, sustancia='agua', unidad_liquido='mililitro'):
        """Convierte un peso de líquido a volumen usando densidad"""
        sustancia = sustancia.lower()
        unidad_peso = unidad_peso.lower()
        unidad_liquido = unidad_liquido.lower()
        
        if sustancia not in self.DENSIDADES:
            return None, f"Sustancia no disponible. Disponibles: {list(self.DENSIDADES.keys())}"
        
        if unidad_peso not in self.PESOS or unidad_liquido not in self.LIQUIDOS:
            return None, "Unidad no válida"
        
        # Convertir peso a gramos
        gramos = valor * self.PESOS[unidad_peso]
        
        # Calcular volumen en mililitros (peso / densidad)
        densidad = self.DENSIDADES[sustancia]
        ml = gramos / densidad
        
        # Convertir mililitros a unidad destino
        resultado = ml / self.LIQUIDOS[unidad_liquido]
        
        return resultado, None
    
    def listar_unidades(self):
        """Muestra todas las unidades disponibles"""
        print("\n" + "="*60)
        print("UNIDADES DISPONIBLES")
        print("="*60)
        
        print("\n📦 PESOS:")
        print(", ".join(self.PESOS.keys()))
        
        print("\n💧 LÍQUIDOS:")
        print(", ".join(self.LIQUIDOS.keys()))
        
        print("\n💨 GASES (Volumen):")
        print(", ".join(self.GASES.keys()))
        
        print("\n🧪 SUSTANCIAS (para conversiones líquido↔peso):")
        print(", ".join(self.DENSIDADES.keys()))
        print()
    
    def guardar_historial(self, descripcion):
        """Guarda una conversión en el historial"""
        self.historial.append(descripcion)
    
    def mostrar_historial(self):
        """Muestra el historial de conversiones"""
        if not self.historial:
            print("\nNo hay conversiones en el historial aún.\n")
            return
        
        print("\n" + "="*60)
        print("HISTORIAL DE CONVERSIONES")
        print("="*60)
        for i, item in enumerate(self.historial, 1):
            print(f"{i}. {item}")
        print()


def menu_principal():
    """Menú principal del conversor"""
    conversor = ConversorUnidades()
    
    while True:
        print("\n" + "="*60)
        print("     CONVERSOR DE UNIDADES")
        print("="*60)
        print("\n1. Convertir PESOS")
        print("2. Convertir LÍQUIDOS")
        print("3. Convertir GASES")
        print("4. Convertir LÍQUIDO → PESO (con sustancia)")
        print("5. Convertir PESO → LÍQUIDO (con sustancia)")
        print("6. Ver unidades disponibles")
        print("7. Ver historial")
        print("8. Salir")
        print("\n" + "-"*60)
        
        opcion = input("Selecciona una opción (1-8): ").strip()
        
        if opcion == '1':
            print("\n--- CONVERSIÓN DE PESOS ---")
            try:
                valor = float(input("Ingresa el valor: "))
                unidad_origen = input("Unidad origen (ej: kg, lb, g): ").strip()
                unidad_destino = input("Unidad destino (ej: g, oz, lb): ").strip()
                
                resultado, error = conversor.convertir_pesos(valor, unidad_origen, unidad_destino)
                
                if error:
                    print(f"❌ Error: {error}")
                else:
                    print(f"✓ {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
                    conversor.guardar_historial(f"{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
            except ValueError:
                print("❌ Error: Ingresa un valor numérico válido")
        
        elif opcion == '2':
            print("\n--- CONVERSIÓN DE LÍQUIDOS ---")
            try:
                valor = float(input("Ingresa el valor: "))
                unidad_origen = input("Unidad origen (ej: l, ml, gal): ").strip()
                unidad_destino = input("Unidad destino (ej: ml, l, gal): ").strip()
                
                resultado, error = conversor.convertir_liquidos(valor, unidad_origen, unidad_destino)
                
                if error:
                    print(f"❌ Error: {error}")
                else:
                    print(f"✓ {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
                    conversor.guardar_historial(f"{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
            except ValueError:
                print("❌ Error: Ingresa un valor numérico válido")
        
        elif opcion == '3':
            print("\n--- CONVERSIÓN DE GASES (VOLUMEN) ---")
            try:
                valor = float(input("Ingresa el valor: "))
                unidad_origen = input("Unidad origen (ej: l, m³, cm³): ").strip()
                unidad_destino = input("Unidad destino (ej: ml, l, m³): ").strip()
                
                resultado, error = conversor.convertir_gases(valor, unidad_origen, unidad_destino)
                
                if error:
                    print(f"❌ Error: {error}")
                else:
                    print(f"✓ {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
                    conversor.guardar_historial(f"{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}")
            except ValueError:
                print("❌ Error: Ingresa un valor numérico válido")
        
        elif opcion == '4':
            print("\n--- CONVERSIÓN LÍQUIDO → PESO ---")
            try:
                valor = float(input("Ingresa el volumen: "))
                unidad_liquido = input("Unidad de volumen (ej: ml, l): ").strip()
                sustancia = input("Sustancia (ej: agua, aceite, leche): ").strip()
                unidad_peso = input("Unidad de peso destino (ej: g, kg): ").strip()
                
                resultado, error = conversor.liquido_a_peso(valor, unidad_liquido, sustancia, unidad_peso)
                
                if error:
                    print(f"❌ Error: {error}")
                else:
                    print(f"✓ {valor} {unidad_liquido} de {sustancia} = {resultado:.4f} {unidad_peso}")
                    conversor.guardar_historial(f"{valor} {unidad_liquido} de {sustancia} = {resultado:.4f} {unidad_peso}")
            except ValueError:
                print("❌ Error: Ingresa valores válidos")
        
        elif opcion == '5':
            print("\n--- CONVERSIÓN PESO → LÍQUIDO ---")
            try:
                valor = float(input("Ingresa el peso: "))
                unidad_peso = input("Unidad de peso (ej: g, kg): ").strip()
                sustancia = input("Sustancia (ej: agua, aceite, leche): ").strip()
                unidad_liquido = input("Unidad de volumen destino (ej: ml, l): ").strip()
                
                resultado, error = conversor.peso_a_liquido(valor, unidad_peso, sustancia, unidad_liquido)
                
                if error:
                    print(f"❌ Error: {error}")
                else:
                    print(f"✓ {valor} {unidad_peso} de {sustancia} = {resultado:.4f} {unidad_liquido}")
                    conversor.guardar_historial(f"{valor} {unidad_peso} de {sustancia} = {resultado:.4f} {unidad_liquido}")
            except ValueError:
                print("❌ Error: Ingresa valores válidos")
        
        elif opcion == '6':
            conversor.listar_unidades()
        
        elif opcion == '7':
            conversor.mostrar_historial()
        
        elif opcion == '8':
            print("\n¡Gracias por usar el Conversor de Unidades! 👋\n")
            break
        
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
