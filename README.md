# DECLARACION DE RENTA

## ¿Quién hizo esto?
- Miguel Martinez Tamayo
- Juan Esteban Vallejo

## ¿Qué es y para qué es?
Programa que permite calcular si un usuario debe declarar renta, proporcionando valores como el impuesto a pagar y su vase gravable en Unidad de Valor Tributario (UVT) y en pesos colombianos (COP)

## ¿Cómo lo hago funcionar?
- Inicializar la consola de sus sistema operativo, y, a demás, buscar allí la ruta del archivo del programa (DECLARACION-RENTA).
- En la consola, ubicados en la carpeta raíz del proyecto, utilice el siguiente comando:

  ```
  py src/view/console/ConsolaRenta.py
  ```
## Descripciòn de la arquitectura

**Este proyecto presenta una arquitectura con una clara separación de responsabilidades, organizada en los siguientes directorios y archivos clave:**

  src/model: Este directorio contiene la capa del Modelo. Dentro de él, se encuentra el archivo LogicaRenta.py, que encapsula la lógica de negocio fundamental para el cálculo del impuesto sobre la renta. Esto incluye las funciones para determinar la base gravable, convertirla a UVT y calcular el impuesto final, así como las definiciones de las excepciones personalizadas para el manejo de errores. El archivo __init__.py (aunque esté vacío en la imagen) se utiliza para marcar el directorio model como un paquete de Python.
    
  src/view/console: Este directorio alberga la capa de la Vista (interfaz de usuario) específica para la consola. El archivo ConsolaRenta.py contiene el código para la interfaz de línea de comandos, permitiendo a los usuarios interactuar con la aplicación a través de la terminal para ingresar los datos necesarios y visualizar los resultados del cálculo del impuesto.
    
  tests: Este directorio está dedicado a las Pruebas. Aunque la imagen no muestra el contenido específico, se espera que contenga archivos de prueba (como el Test_Renta1.py mencionado en tu código anterior) que utilizan el módulo unittest para verificar la correcta funcionalidad de la lógica implementada en el modelo.

**Además de estas capas principales, se observan otros archivos en la raíz del proyecto:**

  README.md: Este es el archivo de documentación principal del proyecto, donde se deben incluir las instrucciones de uso, la descripción de la arquitectura y otra información relevante.
    
  DECLARACION DE RENTA.mp3: Este archivo es el audio en el que el experto que nos acompaña da una visión general de lo que sería el contexto de la declaración de renta de un asalariado.
    
  _pycache_: Este directorio es creado por Python para almacenar archivos bytecode compilados de los módulos, lo que ayuda a acelerar la carga de los programas.
    
  Archivos .cpython-*.pyc: Estos también son archivos bytecode compilados por Python para diferentes versiones del lenguaje.
    
  .vscode/settings.json: Este archivo contiene configuraciones específicas para el editor Visual Studio Code.
    
   En resumen, la arquitectura del proyecto sigue un patrón que separa la lógica de negocio (en el modelo) de la interfaz de usuario (en la vista/consola), facilitando la mantenibilidad y la realización de pruebas unitarias. La capa de pruebas (tests) asegura la calidad del código.

## Ejecución de Pruebas Unitarias

  A continuación, se explica cómo ejecutar las pruebas unitarias utilizando Visual Studio Code y PyCharm.

**Opción 1: Visual Studio Code (VS Code)**

  Abre tu proyecto en VS Code: Asegúrate de tener la carpeta raíz de tu proyecto abierta en Visual Studio Code.
  
  Instala la extensión de Python: Si aún no la tienes, instala la extensión oficial de Python de Microsoft desde el Marketplace de VS Code.
  
  Configura las pruebas (si es necesario):
  
  Ve a la vista de "Testing" (icono del matraz de laboratorio en la barra de actividad lateral). Si no lo ves, puedes habilitarlo desde el menú View > Explorer y buscando "Testing", o usando el comando View: Show Test Explorer.
  Si VS Code no detecta automáticamente tus pruebas, verás un mensaje para configurar las pruebas. Haz clic en "Configure Python Tests".
  Selecciona el framework de pruebas: Elige unittest.
  Selecciona el directorio raíz de las pruebas: Indica la carpeta donde guardaste tus archivos de prueba (por ejemplo, tests).
  Especifica el patrón de nombres de los archivos de prueba: El patrón predeterminado suele ser test*.py, que debería funcionar si nombraste tu archivo como test_renta.py.
  Haz clic en "Discover Tests".
  Ejecuta las pruebas:
  
  Una vez configuradas, la vista de "Testing" mostrará las pruebas que ha encontrado.
  Puedes ejecutar todas las pruebas haciendo clic en el botón "Run All Tests" (icono de play en la parte superior).
  También puedes ejecutar pruebas individuales o grupos de pruebas haciendo clic derecho sobre ellas y seleccionando "Run".
  Analiza los resultados: Los resultados de las pruebas se mostrarán en la vista de "Testing". Verás qué pruebas pasaron (icono de check verde) y cuáles fallaron (icono de aspa roja). Al seleccionar una prueba fallida, podrás ver los detalles del error en el panel de salida.

**Opción 2: PyCharm**

  Abre tu proyecto en PyCharm: Asegúrate de tener la carpeta raíz de tu proyecto abierta en PyCharm.
  
  PyCharm detectará las pruebas automáticamente (generalmente): PyCharm tiene soporte integrado para unittest y, por lo general, detecta automáticamente los archivos y las clases de prueba dentro de tu proyecto.
  
  Ejecuta las pruebas:
  
  Desde el Explorador de Proyectos: Navega hasta la carpeta que contiene tus archivos de prueba (por ejemplo, la carpeta tests). Haz clic derecho sobre la carpeta o sobre un archivo de prueba específico (test_renta.py) y selecciona "Run 'Unittests in tests'" o "Run 'Unittest test_renta.py'", respectivamente.
  Desde el Editor de Código: Abre el archivo de prueba (test_renta.py). Haz clic derecho en cualquier lugar dentro de la clase de prueba (RentaTestNorm o RentaTestExt o RentaTestErr) o dentro de un método de prueba específico (por ejemplo, test_base_gravable_1) y selecciona "Run 'Unittests in <nombre_de_la_clase>' " o "Run '<nombre_del_método>' ".
  Analiza los resultados: PyCharm abrirá una ventana de "Run" en la parte inferior de la interfaz, mostrando los resultados de las pruebas. Verás una lista de las pruebas ejecutadas, indicando si pasaron (icono verde) o fallaron (icono rojo). Al seleccionar una prueba fallida, podrás ver la traza de la excepción y el punto exacto de la falla.
  
  Nota Importante: Asegúrate de que tu entorno de Python esté correctamente configurado en ambos IDEs para que puedan encontrar e importar las dependencias de tu proyecto, incluyendo el código fuente en la carpeta src.
  
## Ejecución de la Interfaz de Consola

  A continuación, se explica cómo ejecutar la interfaz de consola de la calculadora de impuesto sobre la renta utilizando Visual Studio Code y PyCharm.

**Opción 1: Visual Studio Code (VS Code)**

  Abre tu proyecto en VS Code: Asegúrate de tener la carpeta raíz de tu proyecto abierta en Visual Studio Code.
  
  Abre el archivo de la interfaz de consola: Navega hasta la carpeta src/view/console y abre el archivo ConsolaRenta.py.
  
  Abre la terminal integrada: En VS Code, abre la terminal integrada yendo al menú Terminal > New Terminal.
  
  Navega al directorio src/view/console: Utiliza el comando cd para cambiar el directorio actual de la terminal a la ubicación del script ConsolaRenta.py. Asumiendo que estás en la raíz del proyecto, el comando sería:

    cd src/view/console
    
  Ejecuta el script: Una vez que estés en el directorio correcto, ejecuta el script de Python utilizando el siguiente comando:


    python ConsolaRenta.py
    
  Interactúa con la calculadora: La calculadora se iniciará en la terminal y te pedirá que ingreses los datos solicitados (ingresos brutos anuales, aportes a salud y pensión, número de dependientes e intereses de crédito hipotecario). Ingresa los valores cuando se te solicite y presiona Enter.
  
  Visualiza los resultados: La calculadora mostrará la base gravable, la base gravable en UVT y el impuesto de renta calculado en la terminal.

**Opción 2: PyCharm**

  Abre tu proyecto en PyCharm: Asegúrate de tener la carpeta raíz de tu proyecto abierta en PyCharm.
  
  Abre el archivo de la interfaz de consola: Navega hasta la carpeta src/view/console en la ventana del proyecto y abre el archivo ConsolaRenta.py.
  
  Ejecuta el script:
  
  Haz clic derecho: Haz clic derecho en cualquier lugar dentro del archivo ConsolaRenta.py en el editor de código o en el nombre del archivo en la ventana del proyecto.
  Selecciona "Run 'ConsolaRenta'": En el menú contextual que aparece, selecciona la opción "Run 'ConsolaRenta'". Si es la primera vez que ejecutas este script, puede que veas una opción como "Run..." y debas seleccionar el archivo ConsolaRenta.py.
  Interactúa con la calculadora: PyCharm abrirá una ventana de "Run" en la parte inferior de la interfaz. La calculadora se iniciará en esta ventana y te pedirá que ingreses los datos solicitados. Ingresa los valores cuando se te solicite y presiona Enter.
  
  Visualiza los resultados: La calculadora mostrará la base gravable, la base gravable en UVT y el impuesto de renta calculado en la ventana de "Run".
  
  Nota Importante: Asegúrate de que tu entorno de Python esté correctamente configurado en ambos IDEs para que puedan encontrar e importar las dependencias de tu proyecto, incluyendo el código fuente en la carpeta src/model. La línea sys.path.append("src") en el script ayuda a que Python encuentre los módulos dentro de la carpeta src.

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

**Estructura de carpetas**



