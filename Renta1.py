from typing import Any

ingresos_brutos_anuales : float = 80_000_000
aportes_salud_pension : float = 4_800_000
numero_dependientes : float = 6_000_000

def obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes):
    base_gravable = ingresos_brutos_anuales - (aportes_salud_pension + numero_dependientes)
    return base_gravable

base_gravable = obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes)
print(obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes))


def obtener_base_gravable_en_uvt(base_gravable):
    base_gravable_en_uvt = base_gravable / 49_799 #Valor de conversión para pasar a UVT

    return base_gravable_en_uvt

base_gravable_en_uvt = obtener_base_gravable_en_uvt(base_gravable)
print(obtener_base_gravable_en_uvt(base_gravable))

def obtener_impuesto():
    impuesto: float = ((base_gravable_en_uvt - 1_090) * 0.19) * 49_799
    return impuesto

obtener_impuesto()
print(obtener_impuesto())
