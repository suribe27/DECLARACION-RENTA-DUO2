import unittest

import sys

from src.model.LogicaRenta import obtener_base_gravable, obtener_impuesto, obtener_base_gravable_en_uvt, \
    IngresosNegativosError, DependientesExcedidoError, AportesSaludExcedidoError, IngresosInferioresAlMinimoError

sys.path.append("src")


class RentaTestNorm(unittest.TestCase):
    """TEST NORMALES"""

    def test_base_gravable_1(self):
        ingresos_brutos_anuales = 80_000_000
        aportes_salud_pension = 3_200_000
        numero_dependientes = 0
        intereses_credito_hipotecario = 0

        result = obtener_base_gravable(
            ingresos_brutos_anuales,
            aportes_salud_pension,
            numero_dependientes,
            intereses_credito_hipotecario
        )

        expected = 76_800_000

        self.assertAlmostEqual(expected, result, 0)

    def test_base_gravable_uvt_1(self):
        base_gravable = 76_800_000

        result = obtener_base_gravable_en_uvt(base_gravable)

        expected = 1_542

        self.assertAlmostEqual(expected, result, 0)

    def test_impuestos_1(self):
        base_gravable_en_uvt = 1_542

        result = obtener_impuesto(base_gravable_en_uvt)

        expected = 4_276_738

        self.assertAlmostEqual(expected, result, 0)

    """TEST NORMAL 2"""

    def test_base_gravable_2(self):
        ingresos_brutos_anuales = 150_000_000
        aportes_salud_pension = 5_000_000
        numero_dependientes = 0
        intereses_credito_hipotecario = 15_000_000

        result = obtener_base_gravable(
            ingresos_brutos_anuales,
            aportes_salud_pension,
            numero_dependientes,
            intereses_credito_hipotecario
        )

        expected = 130_000_000

        self.assertAlmostEqual(expected, result, 0)

    def test_base_gravable_uvt_2(self):
        base_gravable = 130_000_000

        result = obtener_base_gravable_en_uvt(base_gravable)

        expected = 2_610

        self.assertAlmostEqual(expected, result, 0)

    def test_impuestos_2(self):
        base_gravable_en_uvt = 2_610

        result = obtener_impuesto(base_gravable_en_uvt)

        expected = 18_465_469

        self.assertAlmostEqual(expected, result, 0)

    """TEST NORMAL 3"""

    def test_base_gravable_3(self):
        ingresos_brutos_anuales = 120_000_000
        aportes_salud_pension = 0
        numero_dependientes = 0
        intereses_credito_hipotecario = 0

        result = obtener_base_gravable(
            ingresos_brutos_anuales,
            aportes_salud_pension,
            numero_dependientes,
            intereses_credito_hipotecario
        )

        expected = 120_000_000

        self.assertAlmostEqual(expected, result, 0)

    def test_base_gravable_uvt_3(self):
        base_gravable = 120_000_000

        result = obtener_base_gravable_en_uvt(base_gravable)

        expected = 2_410

        self.assertAlmostEqual(expected, result, 0)

    def test_impuestos_3(self):
        base_gravable_en_uvt = 2_410

        result = obtener_impuesto(base_gravable_en_uvt)

        expected = 15_676_725

        self.assertAlmostEqual(expected, result, 0)


class RentaTestExt(unittest.TestCase):

    # Caso Extraordinario 4
    def test_base_gravable_4(self):
        ingresos_brutos_anuales = 120_000_000
        aportes_salud_pension = 4_800_000
        numero_dependientes = 0  # N/A se asume 0 para calculo
        intereses_credito_hipotecario = 0  # N/A se asume 0 para calculo

        result = obtener_base_gravable(
            ingresos_brutos_anuales,
            aportes_salud_pension,
            numero_dependientes,
            intereses_credito_hipotecario
        )
        expected = 115_200_000
        self.assertAlmostEqual(expected, result, 0)

    def test_base_gravable_uvt_4(self):
        base_gravable = 115_200_000
        result = obtener_base_gravable_en_uvt(base_gravable)
        expected = 2313
        self.assertAlmostEqual(expected, result, 0)

    def test_impuestos_4(self):
        base_gravable_en_uvt = 2313
        result = obtener_impuesto(base_gravable_en_uvt)
        expected = 14_324_184  # Valor tomado de la tabla como referencia
        self.assertAlmostEqual(expected, result, 0)

    # Caso Extraordinario 5
    def test_base_gravable_5(self):
        ingresos_brutos_anuales = 70_000_000
        aportes_salud_pension = 0  # N/A se asume 0 para calculo
        numero_dependientes = 0  # N/A se asume 0 para calculo
        intereses_credito_hipotecario = 0  # N/A se asume 0 para calculo

        result = obtener_base_gravable(
            ingresos_brutos_anuales,
            aportes_salud_pension,
            numero_dependientes,
            intereses_credito_hipotecario
        )
        expected = 70_000_000
        self.assertAlmostEqual(expected, result, 0)

    def test_base_gravable_uvt_5(self):
        base_gravable = 70_000_000
        result = obtener_base_gravable_en_uvt(base_gravable)
        expected = 1406
        self.assertAlmostEqual(expected, result, 0)

    def test_impuestos_5(self):
        base_gravable_en_uvt = 1406
        result = obtener_impuesto(base_gravable_en_uvt)
        expected = 2_989_932  # Valor tomado de la tabla como referencia
        self.assertAlmostEqual(expected, result, 0)

    # Caso Extraordinario 6
    def test_base_gravable_6(self):
        ingresos_brutos_anuales = 1_800_000_000
        aportes_salud_pension = 0
        numero_dependientes = 0
        intereses_credito_hipotecario = 0

        result = obtener_base_gravable(
            ingresos_brutos_anuales,
            aportes_salud_pension,
            numero_dependientes,
            intereses_credito_hipotecario
        )

        expected = 1_800_000_000

        self.assertAlmostEqual(expected, result, 0)

    def test_base_gravable_uvt_6(self):
        base_gravable = 1_800_000_000

        result = obtener_base_gravable_en_uvt(base_gravable)

        expected = 36_145

        self.assertAlmostEqual(expected, result, 0)

    def test_impuestos_6(self):
        base_gravable_en_uvt = 36_145

        result = obtener_impuesto(base_gravable_en_uvt)

        expected = 615_443_431

        self.assertAlmostEqual(expected, result, 0)


class RentaTestErr(unittest.TestCase):

    def test_base_gravable_7_error_ingresos_negativos(self):
        ingresos_brutos_anuales = -10_000_000  # Ingresos negativos, caso de error 7
        aportes_salud_pension = 0  # N/A, se asume 0
        numero_dependientes = 0  # N/A, se asume 0
        intereses_credito_hipotecario = 0  # N/A, se asume 0

        with self.assertRaises(IngresosNegativosError):  # Usar la clase de excepción personalizada
            obtener_base_gravable(
                ingresos_brutos_anuales,
                aportes_salud_pension,
                numero_dependientes,
                intereses_credito_hipotecario
            )

    def test_base_gravable_8_error_dependientes_excedido(self):
        ingresos_brutos_anuales = 90_000_000
        aportes_salud_pension = 0  # N/A, se asume 0
        numero_dependientes = 5  # Dependientes excedido límite, caso de error 8
        intereses_credito_hipotecario = 0  # N/A, se asume 0

        with self.assertRaises(DependientesExcedidoError):  # Usar la clase de excepción personalizada
            obtener_base_gravable(
                ingresos_brutos_anuales,
                aportes_salud_pension,
                numero_dependientes,
                intereses_credito_hipotecario
            )

    def test_base_gravable_9_error_aportes_salud_excedido_porcentaje(self):
        ingresos_brutos_anuales = 80_000_000
        aportes_salud_pension = 10_000_000  # Aportes a salud exceden %, caso de error 9
        numero_dependientes = 0  # N/A, se asume 0
        intereses_credito_hipotecario = 0  # N/A, se asume 0

        with self.assertRaises(AportesSaludExcedidoError):  # Usar la clase de excepción personalizada
            obtener_base_gravable(
                ingresos_brutos_anuales,
                aportes_salud_pension,
                numero_dependientes,
                intereses_credito_hipotecario
            )

    def test_base_gravable_10_error_ingresos_inferiores_al_minimo(self):
        ingresos_brutos_anuales = 60_000_000  # Ingresos inferiores al mínimo, caso de error 10 (Ejemplo: 60.000.000 < 69.718.600)
        aportes_salud_pension = 0  # N/A, se asume 0
        numero_dependientes = 0  # N/A, se asume 0
        intereses_credito_hipotecario = 0  # N/A, se asume 0

        with self.assertRaises(
                IngresosInferioresAlMinimoError):  # Usar la clase de excepción personalizada para Caso 10
            obtener_base_gravable(
                ingresos_brutos_anuales,
                aportes_salud_pension,
                numero_dependientes,
                intereses_credito_hipotecario
            )