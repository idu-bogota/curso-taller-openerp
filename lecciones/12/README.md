[[
title: Lección 12: Campos y Atributos Avanzados
author: STRT Grupo I+D+I
]]

Lección 12: Campos y Atributos Avanzados
========================================

[TOC]

Related
-------

Los campos related se utiliza cuando el campo es una referencia de un id de otra tabla. Esto es para hacer referencia a la relación de una relación.


**Estructura de definición**

	'nombre_campo_related': fields.related (
		'id_busqueda',
		'campo_busqueda',
		type = "tipo_campo",
		relation = "objeto_negocio_a_relacionar",
		string = "Texto del campo",
		store = False
	)

* **id_busqueda**: nombre de campo id de referencia del objeto de negocio relacionado para realizar la búsqueda.
* **campo_busqueda**: nombre del campo de referencia, el cual devuelve el valor de ese campo según la busqueda realizada por el id_busqueda en el objeto de negocio a relacionar.
* **type**: Tipo del campo related. Tipo de relación para el campo related con el objeto de negocio.
* **relation**: Nombre del objeto de negocio al cual se aplica la relación con el camṕo tipo related.
* **string**: Texto para el campo tipo related.
* **store**: Este puede ser definida como True o False, segun lo requerido, con este valor estamos indicando si el valor devuelto por campo_busqueda es almacenado o no en la base de datos.

**Ejemplo de aplicación**:


Domain
------

El atributo domain es un atributo aplicado a los campos para definir una restricción de dominio en un campo relacional, su valor por defecto es vacio.

**Estructura de definición**

	domain = [('campo', 'operador_comparacion', valor)])

* **campo**: nombre del campo del objeto de negocio, este campo será utilizado para la restricción.
* **operador_comparacion**: operador para comparar el campo con el valor establecido.
* **valor**: valor asignado para evaluar la restricción de dominio.

**Ejemplo de aplicación**:

Function
--------

Un campo funcional es un campo cuyo valor se calcula mediante una función, en lugar de ser almacenado en la base de datos.

**Estructura de definición**

	'nombre_campo_function' : fields.function(
            _nombre_metodo,
            type='tipo_campo',
            obj= "objeto_de_negocio.function",
            method= True,
            string= "Texto del campo"
	)

**Ejemplo de aplicación**:

Ejercicios propuestos
---------------------

1. Revisar los cambios realizados en el módulo ejemplo biblioteca.
1. Adicionar un campo tipo function.
