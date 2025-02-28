

VALOR_UVT: int = 49_799 #Unidad de valor tributario
ingresos_brutos_anuales = 120_000_000
aportes_salud_pension = 1_000_000
numero_dependientes = 0
intereses_credito_hipotecario = 0
consumos_tarjeta_credito = 0
depositos_bancarios = 0
patrimonio_bruto = 0

class IngresosNegativosError(Exception):
    """Excepción para cuando los ingresos brutos anuales son negativos (Caso 7)."""
    pass

class DependientesExcedidoError(Exception):
    """Excepción para cuando el número de dependientes excede el límite (Caso 8)."""
    pass

class AportesSaludExcedidoError(Exception):
    """Excepción para cuando los aportes a salud y pensión superan el límite (Caso 9)."""
    pass
def obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario):
    if ingresos_brutos_anuales < 0:
        raise IngresosNegativosError("Los ingresos brutos anuales no pueden ser negativos (Caso 7).")

    if numero_dependientes > 4:
        raise DependientesExcedidoError("El número de dependientes excede el límite permitido de 4 (Caso 8).")

    if aportes_salud_pension > ingresos_brutos_anuales * 0.04:  # 4% de los ingresos brutos
        raise AportesSaludExcedidoError(
            "Los aportes a salud y pensión superan el 4% de los ingresos brutos anuales (Caso 9).")

    base_gravable = ingresos_brutos_anuales - (aportes_salud_pension + numero_dependientes + intereses_credito_hipotecario)
    return base_gravable

base_gravable = obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario)
print(obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario))


def obtener_base_gravable_en_uvt(base_gravable):
    base_gravable_en_uvt = base_gravable / VALOR_UVT

    return round(base_gravable_en_uvt)

base_gravable_en_uvt = obtener_base_gravable_en_uvt(base_gravable)
print(obtener_base_gravable_en_uvt(base_gravable))

def obtener_impuesto(base_gravable_en_uvt):
    
    if base_gravable_en_uvt > 1090 and base_gravable_en_uvt < 1700:
        impuesto: float = ((base_gravable_en_uvt - 1_090) * 0.19) * VALOR_UVT

    elif base_gravable_en_uvt > 1700 and base_gravable_en_uvt < 4100:
        impuesto: float = ((base_gravable_en_uvt - 1_700) * 0.28 + 116) * VALOR_UVT

    elif base_gravable_en_uvt > 4100 and base_gravable_en_uvt < 8670:
        impuesto: float = ((base_gravable_en_uvt - 4100) * 0.33 + 788) * VALOR_UVT
    
    elif base_gravable_en_uvt > 8670 and base_gravable_en_uvt < 18970:
        impuesto: float = ((base_gravable_en_uvt - 8670) * 0.35 + 2296) * VALOR_UVT

    elif base_gravable_en_uvt > 18970 and base_gravable_en_uvt < 31000:
        impuesto: float = ((base_gravable_en_uvt - 18970) * 0.37 + 5901) * VALOR_UVT

    elif base_gravable_en_uvt > 31000:
        impuesto: float = ((base_gravable_en_uvt - 31000) * 0.39 + 10352) * VALOR_UVT
    
    return round(impuesto)

obtener_impuesto(base_gravable_en_uvt)
print(obtener_impuesto(base_gravable_en_uvt))
