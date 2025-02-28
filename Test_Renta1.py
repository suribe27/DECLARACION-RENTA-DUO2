import unittest

import LogicaRenta

class RentaTestNorm(unittest.TestCase):
    
    """TEST NORMALES"""
    def testbaseGravable_1(self):

        ingresos_brutos_anuales = 80_000_000
        aportes_salud_pension = 4_800_000
        numero_dependientes = 6_000_000
        intereses_credito_hipotecario = 0

        result = LogicaRenta.obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario)

        expected = 69_200_000

        self.assertAlmostEqual(expected, result, 0)


    def testBaseGravableUVT_1(self):
        
        base_gravable = 69_200_000

        result = LogicaRenta.obtener_base_gravable_en_uvt(base_gravable)

        expected = 1_390

        self.assertAlmostEqual(expected, result, 0)
        

    def testImpuestos_1(self):
        
        base_gravable_en_uvt = 1_390
        
        result = LogicaRenta.obtener_impuesto(base_gravable_en_uvt)

        expected = 2_838_543

        self.assertAlmostEqual(expected, result, 0)
        
    """TEST NORMAL 2"""

    def testbaseGravable_2(self):

        ingresos_brutos_anuales = 150000000
        aportes_salud_pension = 12000000
        numero_dependientes = 0
        intereses_credito_hipotecario = 15000000

        result = LogicaRenta.obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario)

        expected = 123_000_000

        self.assertAlmostEqual(expected, result, 0)

    
    def testBaseGravableUVT_2(self):
        
        base_gravable = 123_000_000

        result = LogicaRenta.obtener_base_gravable_en_uvt(base_gravable)

        expected = 2_470

        self.assertAlmostEqual(expected, result, 0)
    

    def testImpuestos_2(self):
        
        base_gravable_en_uvt = 2_470
        
        result = LogicaRenta.obtener_impuesto(base_gravable_en_uvt)

        expected = 16_513_348

        self.assertAlmostEqual(expected, result, 0)

    """TEST NORMAL 3"""

    def testbaseGravable_3(self):

        ingresos_brutos_anuales = 120_000_000
        aportes_salud_pension = 0
        numero_dependientes = 0
        intereses_credito_hipotecario = 0

        result = LogicaRenta.obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario)

        expected = 120_000_000

        self.assertAlmostEqual(expected, result, 0)

    
    def testBaseGravableUVT_3(self):
        
        base_gravable = 120_000_000      

        result = LogicaRenta.obtener_base_gravable_en_uvt(base_gravable)

        expected = 2_410

        self.assertAlmostEqual(expected, result, 0)


    def testImpuestos_3(self):
        
        base_gravable_en_uvt = 2_410
        
        result = LogicaRenta.obtener_impuesto(base_gravable_en_uvt)

        expected = 15_676_725

        self.assertAlmostEqual(expected, result, 0)    


class RentaTestExt(unittest.TestCase):
    
    """
    CASOS EXTRAORDINARIOS 1 Y 2 PENDIENTES
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    """


    def testbaseGravable_6(self):

        ingresos_brutos_anuales = 1_800_000_000
        aportes_salud_pension = 0
        numero_dependientes = 0
        intereses_credito_hipotecario = 0

        result = LogicaRenta.obtener_base_gravable(ingresos_brutos_anuales, aportes_salud_pension, numero_dependientes, intereses_credito_hipotecario)

        expected = 1_800_000_000

        self.assertAlmostEqual(expected, result, 0)


    def testBaseGravableUVT_6(self):
        
        base_gravable = 1_800_000_000     

        result = LogicaRenta.obtener_base_gravable_en_uvt(base_gravable)

        expected = 36_145

        self.assertAlmostEqual(expected, result, 0)

    
    def testImpuestos_6(self):
        
        base_gravable_en_uvt = 36_145
        
        result = LogicaRenta.obtener_impuesto(base_gravable_en_uvt)

        expected = 615_443_431

        self.assertAlmostEqual(expected, result, 0)


class RentaTestErr(unittest.TestCase):

    

if __name__ == '__main__':
    unittest.main()