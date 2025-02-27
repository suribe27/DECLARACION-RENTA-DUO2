from typing import Any

VALOR_UVT: int = 49_799
ingresos_brutos_anuales : float = 80_000_000
aportes_salud_pension : float = 4_800_000
numero_dependientes : float = 6_000_000

def obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes):
    base_gravable = ingresos_brutos_anuales - (aportes_salud_pension + numero_dependientes)
    return base_gravable

base_gravable = obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes)
print(obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes))


def obtener_base_gravable_en_uvt(base_gravable):
    base_gravable_en_uvt = base_gravable / VALOR_UVT

    return round(base_gravable_en_uvt)

base_gravable_en_uvt = obtener_base_gravable_en_uvt(base_gravable)
print(obtener_base_gravable_en_uvt(base_gravable))

def obtener_impuesto():
    
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

obtener_impuesto()
print(obtener_impuesto())
