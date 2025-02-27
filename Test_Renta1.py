import unittest

import LogicaRenta

class RentaTest(unittest.TestCase):
    def testbaseGravable(self):

        ingresos_brutos_anuales = 80_000_000
        aportes_salud_pension = 4_800_000
        numero_dependientes = 6_000_000

        result = LogicaRenta.obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes)

        expected = 69_200_000

        self.assertAlmostEqual(expected, result, 0)


    def testBaseGravableUVT(self):
        
        base_gravable = 69_200_000

        result = LogicaRenta.obtener_base_gravable_en_uvt(base_gravable)

        expected = 1_390

        self.assertAlmostEqual(expected, result, 0)
        pass

    def testImpuestos(self):
        
        result = LogicaRenta.obtener_impuesto()

        expected = 2_838_543

        self.assertAlmostEqual(expected, result, 0)
        pass