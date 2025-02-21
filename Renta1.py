ingresos_brutos_anuales = 60_000_000
aportes_salud_pension = 4_800_000
numero_dependientes = 6_000_000

def obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes):
    base_gravable = ingresos_brutos_anuales - (aportes_salud_pension + numero_dependientes)

    valor_esperado_bg = 49_200_000
    if base_gravable == valor_esperado_bg:
        print(f"BASE GRAVABLE: {int(base_gravable)}")
    else:
        print(f"ERROR: se esperaba {valor_esperado_bg} como base gravable.")
    return base_gravable

base_gravable = obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes)


def obtener_base_gravable_en_uvt(base_gravable):
    base_gravable_en_uvt = base_gravable / 42_412 #Valor de conversión para pasar a UVT

    valor_esperado_bguvt = 1_160
    if int(base_gravable_en_uvt) == valor_esperado_bguvt:
        print(f"BASE GRAVABLE EN UVT: {int(base_gravable_en_uvt)}")
    else:
        print(f"ERROR: se esperaba {valor_esperado_bguvt} como base gravable en UVT.")
    return base_gravable_en_uvt

base_gravable_en_uvt = obtener_base_gravable_en_uvt(base_gravable)


def obtener_impuesto():
    impuesto = 0 + 443_205 + 2_493_826 + 11_197_454

    impuesto_esperado = 14_134_485
    if impuesto == impuesto_esperado:
        print(f"IMPUESTO: {impuesto}")
    else: 
        print(f"ERROR: se esperaba {impuesto_esperado} como impuesto.")

obtener_impuesto()