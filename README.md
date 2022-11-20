# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 22/23)
  
  Autor/a: Álvaro Ortiz Rosado
  
  En mi caso me toco el dataset cohes.csv
  
  ### Estructura de las carpetas del proyecto
  
  * **scr**: Contiene los diferentes módulos de Python que conforman el proyecto:
    * **\<coches\>**. En este fichero definiremos las funciones.
    * **\<coches_test\>**. En este fichero probaremos las funciones de "coches".
  * **data**: Contiene los datos recogidos en el fichero "coches_50".
  
  ### Funciones implementadas
  
  * **Funciones**:
   * **\<lee_coches\>**.Esta función es la encargada de leer los datos de "coches_50" y de almacenarlos en forma de una lista de tuplas.
  * **\<funciones parsea\>**. Estas dos funciones se encargan de cambiar de tipo string a datetime en el caso de parsea_fecha y a verdadero o falso en el caso de parsea_boolean.
  * **\<número_marcas_distintas\>**.Esta función se encarga de contar el número de marcas que hay en el fichero.
   * **\<media_kilómetros\>**.Esta función se encarga de calcular la media de los kilómetros recorridos por los coches de nuestro fichero.
   * **\<max_kilómetros\>**.Esta función se encarga de encontrar el máximo número de kilómetros reocrridos por un coche matriculado.
   * **\<marcas_con_menos_averías\>**.Esta función se encarga de hacer un ranking de las marcas con los coches con menos averías.
   * **\<agrupar_por_color\>**.Esta función se encarga de recopilar los datos en diccionarios, donde la clave del diccionario es el color del coche y su valor es toda la información sobre ciches de ese color.
  
  * **Test de dichas funciones**:
 * **\<test_lee_coches\>**. Esta función se encarga de devolver el número de columnas de datos leídos(con la función len) y de decirte las tres primeras líneas de datos y las tres últimas.
 * **\<test_número_marcas_distintas\>**. Esta función se encarga de mostrar el número de marcas distintas usando la función número_marcas_distintas.
 * **\<test_media_kilómetros\>**. Esta función se encarga de mostrar el número de kilómetros reocrridos de media usando la función media_kilómetros.
 * **\<test_max_kilómetros\>**. Esta función se encarga de mostrar el máximo de kilómetros recorridos usando la función max_kilómetros.
 * **\<test_marcas_con_menos_averías\>**. Esta función se encarga de mostrar las marcas con menos coches averiados usando la función marcas_con_menos_averías.
 * **\<test_agrupar_por_color\>**. Esta función se encarga de mostrar todos los datos de los coches del mismo color usando la función agrupar_por_color.  
