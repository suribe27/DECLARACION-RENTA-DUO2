from src.model.LogicaRenta import obtener_base_gravable, obtener_base_gravable_en_uvt, obtener_impuesto, IngresosNegativosError, DependientesExcedidoError, AportesSaludExcedidoError, IngresosInferioresAlMinimoError, VALOR_UVT, VALOR_MINIMO_IMPUESTO

def main():
    """
    """
    print("Calculadora de Impuesto sobre la Renta (Colombia)")
    print("-----------------------------------------------\n")

    try:
        ingresos_brutos_anuales = float(input("Ingrese sus ingresos brutos anuales en pesos colombianos: "))
        aportes_salud_pension = float(input("Ingrese el valor total de sus aportes a salud y pensión en pesos colombianos (o 0 si no aplica): "))
        numero_dependientes = int(input("Ingrese el número de dependientes (si aplica, sino ingrese 0): "))
        intereses_credito_hipotecario = float(input("Ingrese el valor de intereses de crédito hipotecario pagados (o 0 si no aplica): "))

        # Calcular la base gravable, manejando posibles excepciones
        try:
            base_gravable = obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario)
            print(f"\nBase gravable: ${base_gravable:,.2f}") # Formatear con separador de miles y 2 decimales

            base_gravable_en_uvt = obtener_base_gravable_en_uvt(base_gravable)
            print(f"Base gravable en UVT: {base_gravable_en_uvt} UVT")

            impuesto = obtener_impuesto(base_gravable_en_uvt)
            print(f"Impuesto de renta (aproximado, sin retenciones): ${impuesto:,.2f}") # Formatear con separador de miles y 2 decimales

        except IngresosNegativosError as e:
            print(f"\nError: {e}")
        except DependientesExcedidoError as e:
            print(f"\nError: {e}")
        except AportesSaludExcedidoError as e:
            print(f"\nError: {e}")
        except IngresosInferioresAlMinimoError as e:
            print(f"\nError: {e}")
        except Exception as e: # Capturar otras excepciones inesperadas
            print(f"\nOcurrió un error inesperado: {e}")


    except ValueError:
        print("\nError: Por favor, ingrese valores numéricos válidos para los datos solicitados.")
    except Exception as e: # Capturar otras excepciones generales (por si acaso)
        print(f"\nOcurrió un error general: {e}")

if __name__ == "__main__":
    main()
