[[
title: Lección 09: Navegar Registros
author: STRT Grupo I+D+I
]]

Lección 09: Navegar Registros
=============================

[TOC]

Método Search
-------------

Este método realiza la búsqueda de regristros, basándose en el dominio de búsqueda indicado. Maneja los siguientes parámetros:

* ***offset***: Número de registros a omitir. Parámetro  opcional, por defecto 0.
* ***limit***: Número máximo de registros a devolver. Parámetro opcional, por defecto None.
* ***order***: Columnas para establecer el criterio de ordenación. Opcional. Por defecto self._order=id.
* ***count***: Devuelve sólo el número de registros que coinciden con el criterio de búsqueda.
* ***args***: Lista de tuplas que especifican el dominio de búsqueda. Cada tupla de la lista del dominio de búsqueda necesita 3 elementos en la forma ('field_name', 'operator', value), donde:
	* *field_name*: Nombre del campo del objeto de negocio
    * *operator*: Operador de comparación (=, !=, >, >=, <,<=, like, ilike, in, not in, child_of, parent_left, parent_right).
        •value: Valor con que realizar la comparación.

El dominio de búsqueda puede ser una combinación que use 3 operadores lógicos que pueden añadirse entre tuplas:

* '&': Y lógico. Por defecto.
* '|': O lógico.
* '!': No lógico o negación.

**Estructura de definición del método**

	search(cr, uid, args, offset=0, limit=None, order=None, context=None, count=False)

Ejemplo de aplicación del método search:

	libros_pool = self.pool.get('biblioteca.libro')
	libros_ids = libros_pool.search(cr, uid,[('state','=','compra')], context=context)

En este ejemplo el método search realiza una búsqueda por todos los registros del objeto *biblioteca.libro* y cuando un registro coincida con el criterio de búsqueda 'state','=','compra', el id del registro se almacenará en libros_ids.

Método Browse
-------------

El método browse obtiene registros como objetos permitiendo utilizar la notación de puntos para explorar los campos y las relaciones, permite consultar con facilidad campos relacionados de forma encadenada a partir de un objeto.

**Estructura de definición del método**

	browse (cr, uid, ids, context=None)

Ejemplo de aplicación browse:

	libros_pool = self.pool.get('biblioteca.libro')
	libros_ids = libros_pool.search(cr, uid,[('state','=','compra')], context=context)
	libros_records = libros_pool.browse(cr, uid, libros_ids, context=context)

En este ejemplo el método browse obtiene los registros que correspondan a los ids almacenados en libros_ids, estos registros se almacenan en libros_records.

Método Read
-----------

Obtiene una lista de los valores de los campos fields de los registros ids, devuelve un diccionario con el nombre y valor de los campos solicitados. Tiene los siguientes parámetros:

* ***fields***: Lista de campos.

**Estructura de definición del método**

	read (cr, uid, ids, fields=None, context=None)

Ejemplo de aplicación read:

	libros_pool = self.pool.get('biblioteca.libro')
	libros_ids = libros_pool.search(cr, uid,[('state','=','compra')], context=context)
	libros_records = libros_pool.read(cr, uid, libros_ids, ['titulo','autor'])

En este ejemplo del método read obtiene una lista de los valores de los campos *'titulo', 'autor'* de los registros que coincidan con los ids almacenados en libros_ids, esta lista se almacena en libros_records como un diccionario con nombre y valor de los campos indicados.