# DECLARACION DE RENTA

## ¿Quién hizo esto?
- Miguel Martinez Tamayo
- Juan Esteban Vallejo

## ¿Qué es y para qué es?
Programa que permite calcular si un usuario debe declarar renta, proporcionando valores como el impuesto a pagar y su vase gravable en Unidad de Valor Tributario (UVT) y en pesos colombianos (COP)

## ¿Cómo lo hago funcionar?
- **Prerrequisitos**: inicializar la consola de sus sistema operativo.
- **Ejecución**: En la consola, ubicados en la carpeta raíz del proyecto, utilice el siguiente comando:
   ´´´
  py ConsolaRenta.py
  ´´´ 


## ¿Cómo está hecho?
link de excel para la declaracion de impuestos de un asalariado (CASOS DE PRUEBA)
https://docs.google.com/spreadsheets/d/1IwasnT6Vj87bwmWxKCBOTA8iFx_RkNW8GP2FXW7QbEE/edit?usp=sharing

**Variables de entrada:**
Criterios a tener en cuenta para el proceso de declaración de impuestos, ya que si la persona supera uno o más, deberá cumplir con la declaración de sus ingresos para evitar sanciones:

    1. Ingresos brutos anuales.
    2. Aportes a salud y pensión.
    3. Número de dependientes.
    4. Intereses de crédito hipotecario.
    5. Consumos con tarjeta de crédito.
    6. Consignaciones/depósitos bancarios.
    7. Patrimonio bruto.
    8. Retenciones en la fuente.
    9. Tipo de cambio (si hay ingresos en USD).

**Variables de salida:**
Esto se obtiene al calcular la declaración de renta de la persona.

    1. Base gravable.
    2. Base gravable en uvt.
    3. Impuesto(menos retenciones, solo si aplica).

**Procesos y operaciones:**
Las formulas del impuesto se obtuvieron en base al artículo 241 del Estatuto Tributario Nacional:

![image](https://github.com/user-attachments/assets/1bb101d8-3c00-4e88-be18-5a97614735ff)

El valor de la Unidad de Valor Tributario (UVT) para el año 2025 es de $49.799 pesos colombianos.
Este valor se utiliza como referencia para diversas obligaciones tributarias y sanciones en Colombia. Para declarar la renta, los ingresos brutos mínimos para declarar renta son 1.400 UVT, lo que equivale a $69.718.600 pesos colombianos.

**Reglas generales para la declaración obligatoria de renta**

Los contribuyentes asalariados en Colombia están obligados a presentar una declaración de renta si cumplen con alguna de las siguientes condiciones:

    1.El valor de los activos poseídos al 31 de diciembre supera las 4,500 Unidades Tributarias (UVT), lo que equivale aproximadamente a COP 224.095.5000 
    
    2.Los cargos a tarjetas de crédito durante el año fiscal superan las 1,400 UVT (aproximadamente COP 69.718.600) 
    
    3.El valor total de las compras en efectivo supera las 1,400 UVT (COP 69.718.600) 
    
    4.El valor total de los depósitos bancarios y otras inversiones supera las 1,400 UVT (COP 69.718.600) 
    
    5.Los ingresos durante el año fiscal superan las 1,400 UVT (COP 69.718.600) 



