import unittest

import Renta1

class RentaTest(unittest.TestCase):
    def testbaseGravable(self):

        ingresos_brutos_anuales = 80_000_000
        aportes_salud_pension = 4_800_000
        numero_dependientes = 6_000_000

        result = Renta1.obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes)

        expected: 69_200_000

        self.assertAlmostEqual(expected, result, 2)


    def testBaseGravableUVT(self):
        
        base_gravable = 69_200_000

        result = Renta1.obtener_base_gravable_en_uvt(base_gravable)

        expected = 1_390

        self.assertAlmostEqual(expected, result, 2)
        pass

    def testImpuestos(self):
        
        result = Renta1.obtener_impuesto()

        expected = 2_834_627

        self.assertAlmostEqual(expected, result, 2)
        pass