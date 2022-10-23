# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 22/23)
  
  Autor/a: Álvaro Ortiz Rosado
  
  En mi caso me toco el dataset cohes.csv
  
  ### Estructura de las carpetas del proyecto
  
  **scr**: Contiene los diferentes módulos de Python que conforman el proyecto:
  -coches. En este fichero encontraremos las funciones para leer los datos.
  -coches_test. En este fichero encontraremos la funcion para interpretarlos.
  * **data**: Contiene los datos recogidos en el fichero "coches_50".
  
  ### Funciones implementadas
  
  **lee_coches**. Esta función es la encargada de leer los datos de "coches_50" y de almacenarlos en forma de una lista de tuplas.
  **funciones parsea**. Estas dos funciones se encargan de cambiar de tipo string a datetime en el caso de parsea_fecha y a verdadero o falso en el caso de parsea_boolean.
* **test_lee_coches**. Esta función se encarga de devolver el número de columnas de datos leídos(con la función len) y de decirte las tres primeras líneas de datos y las tres últimas.
