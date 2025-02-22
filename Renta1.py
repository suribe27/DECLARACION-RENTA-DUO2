ingresos_brutos_anuales = 80_000_000
aportes_salud_pension = 4_800_000
numero_dependientes = 6_000_000

def obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes):
    base_gravable = ingresos_brutos_anuales - (aportes_salud_pension + numero_dependientes)
    return base_gravable

base_gravable = obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes)


def obtener_base_gravable_en_uvt(base_gravable):
    base_gravable_en_uvt = base_gravable / 42_412 #Valor de conversión para pasar a UVT

    return base_gravable_en_uvt

base_gravable_en_uvt = obtener_base_gravable_en_uvt(base_gravable)


def obtener_impuesto():
    impuesto = 0 + 443_205 + 2_493_826 + 11_197_454

obtener_impuesto()
