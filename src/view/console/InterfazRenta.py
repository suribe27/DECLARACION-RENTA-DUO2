from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

import sys
import os

# Agregar la raíz del proyecto solo si no está en sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

print("Rutas en sys.path:")
for path in sys.path:
    print(path)

try:
    from src.model.LogicaRenta import obtener_base_gravable
    print("✅ Import exitoso de LogicaRenta")
except ModuleNotFoundError as e:
    print("🚨 Error importando LogicaRenta:", e)



# Importar funciones de tu lógica de renta
from model.LogicaRenta import obtener_base_gravable, obtener_base_gravable_en_uvt, obtener_impuesto, IngresosNegativosError, DependientesExcedidoError, AportesSaludExcedidoError, IngresosInferioresAlMinimoError, VALOR_UVT, VALOR_MINIMO_IMPUESTO

class RentaApp(App):
    
    def build(self):
        self.title = "Calculadora de Impuesto sobre la Renta (Colombia)"
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Crear los campos de entrada
        self.ingresos_input = TextInput(hint_text="Ingrese ingresos brutos anuales", multiline=False)
        self.aportes_input = TextInput(hint_text="Ingrese aportes a salud y pensión", multiline=False)
        self.dependientes_input = TextInput(hint_text="Ingrese número de dependientes", multiline=False)
        self.intereses_input = TextInput(hint_text="Ingrese intereses crédito hipotecario", multiline=False)
        
        # Crear botón de cálculo
        self.calculate_button = Button(text="Calcular Impuesto", on_press=self.calcular_impuesto)

        # Labels para mostrar los resultados
        self.result_label = Label(text="Resultados aparecerán aquí", size_hint_y=None, height=44)
        self.base_gravable_label = Label(text="Base gravable: ", size_hint_y=None, height=44)
        self.base_gravable_uvt_label = Label(text="Base gravable en UVT: ", size_hint_y=None, height=44)
        self.impuesto_label = Label(text="Impuesto de renta: ", size_hint_y=None, height=44)

        # Agregar los elementos al layout
        layout.add_widget(self.ingresos_input)
        layout.add_widget(self.aportes_input)
        layout.add_widget(self.dependientes_input)
        layout.add_widget(self.intereses_input)
        layout.add_widget(self.calculate_button)
        layout.add_widget(self.base_gravable_label)
        layout.add_widget(self.base_gravable_uvt_label)
        layout.add_widget(self.impuesto_label)
        
        return layout

    def calcular_impuesto(self, instance):
        try:
            # Obtener los valores de los campos de texto
            ingresos_brutos_anuales = float(self.ingresos_input.text)
            aportes_salud_pension = float(self.aportes_input.text)
            numero_dependientes = int(self.dependientes_input.text)
            intereses_credito_hipotecario = float(self.intereses_input.text)

            # Calcular la base gravable
            base_gravable = obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario)
            self.base_gravable_label.text = f"Base gravable: ${base_gravable:,.2f}"

            # Calcular la base gravable en UVT
            base_gravable_en_uvt = obtener_base_gravable_en_uvt(base_gravable)
            self.base_gravable_uvt_label.text = f"Base gravable en UVT: {base_gravable_en_uvt} UVT"

            # Calcular el impuesto
            impuesto = obtener_impuesto(base_gravable_en_uvt)
            self.impuesto_label.text = f"Impuesto de renta: ${impuesto:,.2f}"

        except ValueError:
            self.mostrar_popup("Error", "Por favor, ingrese valores numéricos válidos.")
        except IngresosNegativosError as e:
            self.mostrar_popup("Error", str(e))
        except DependientesExcedidoError as e:
            self.mostrar_popup("Error", str(e))
        except AportesSaludExcedidoError as e:
            self.mostrar_popup("Error", str(e))
        except IngresosInferioresAlMinimoError as e:
            self.mostrar_popup("Error", str(e))
        except Exception as e:
            self.mostrar_popup("Error inesperado", str(e))

    def mostrar_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=message))
        close_button = Button(text="Cerrar", on_press=lambda x: self.close_popup())
        content.add_widget(close_button)

        self.popup = Popup(title=title, content=content, size_hint=(None, None), size=(400, 200))
        self.popup.open()

    def close_popup(self):
        self.popup.dismiss()

if __name__ == "__main__":
    RentaApp().run()