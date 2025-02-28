

VALOR_UVT: int = 49_799 #Unidad de valor tributario
ingresos_brutos_anuales = 1800000000
aportes_salud_pension = 0
numero_dependientes = 0
intereses_credito_hipotecario = 0
consumos_tarjeta_credito = 0
depositos_bancarios = 0
patrimonio_bruto = 0

def obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario):
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
