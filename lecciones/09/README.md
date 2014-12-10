[[
title: Lección 09: Navegar Registros
author: STRT Grupo I+D+I
]]

Lección 09: Navegar Registros
=============================

[TOC]


Añadir un botón a la vista formulario
--------------------------------------

Se puede adicionar botones de acción a la vista formulario,  los botones de acción permiten al usuario realizar diversas acciones en el registro actual. Maneja los siguientes atributos:
  Identificador del botón, que se utiliza para indicar qué método debe ser llamado, que envió la señal o que la acción ejecutada.

* ***name***: Nombre de la función que se activiara por medio del boton. Identificador del botón, se utiliza para indicar qué método debe ser llamado, que señal o que acción se ejecutará.
* ***string***: Etiqueta que se mostrará en el botón.
* ***type***: Define el tipo de acción realizada cuando se activa el botón.
	* *workflow* (default): El botón enviará una señal de workflow al modelo actual con el Name del botón como señal del workflow y retornará como parámetro el ID del registro (en una lista). La señal del  workflow puede retornar una acción la cual será ejecutada, de lo contrario devolverá False.
	* *object*: El botón ejecutará el método de nombre Name en el modelo actual, retornará como parámetro el ID del registro (en una lista). Retorna una acción la cual será ejecutada.
	* action: El botón activará la ejecución de una acción (ir.actions.actions). El ID de esta acción es el Name del botón.
* ***special***: Sólo tiene un valor *cancelar*, lo que indica que el popup debe cerrarse sin realizar ninguna llamada RPC o acción. Se usa en ventanas popup-type, por ejemplo wizard.El atributo special y type son incompatibles.
* ***confirm***: Ventana de confirmación antes de ejecutar la tarea del botón.
* ***icon***: Mostrar un icono en el botón.
* ***states, attrs, invisible***: Significado estándar para esos atributos de vista.
* ***default_focus***: Si se establece en un valor Truthy, automáticamente  se selecciona el botón, tambien usado si se presiona RETURN en la vista formulario.

**Estructura para adicionar un botón en la vista**

	<button name="nombre_funcion" type="object"></button>

Ejemplo de adicion de un botón:

	<button name="confirmar_compra" states="solicitud" string="Confirmar proceso de Compra" icon="gtk-execute"/>
	<button special="cancel" string="Cancelar Solicitud"/>

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
    * *value*: Valor con que realizar la comparación.

El dominio de búsqueda puede ser una combinación que use 3 operadores lógicos que pueden añadirse entre tuplas:

* '&': Y lógico. Por defecto,se omite el operador.
* '|': O lógico.
* '!': No lógico o negación.

**Estructura de definición del método**

	search(cr, uid, args, offset=0, limit=None, order=None, context=None, count=False)

Ejemplo:

	libros_pool = self.pool.get('biblioteca.libro')
	libros_ids = libros_pool.search(cr, uid,[('state','=','compra')], context=context)

En este ejemplo el método search realiza una búsqueda por todos los registros del objeto *biblioteca.libro* y cuando un registro coincida con el criterio de búsqueda 'state','=','compra', el id del registro se almacenará en libros_ids.

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

Ejemplo de aplicación del método read:

**Adición de función en el objeto de negocio biblioteca.libro_prestamo**

	def obtener_promedio_prestamo_metodo_read(self,cr,uid,ids,context=None):
        prestamo_ids = self.read(cr, uid, ids, ['prestamo_ids'], context=context)
        prestamo_pool = self.pool.get('biblioteca.libro_prestamo')
        prestamo_records = prestamo_pool.read(cr, uid, prestamo_ids[0]['prestamo_ids'], ['fecha_prestamo', 'fecha_regreso'], context=context)
        tiempo_total = 0
        for record in prestamo_records:
            tiempo_dias = (datetime.strptime(record['fecha_regreso'],'%Y-%m-%d') - datetime.strptime(record['fecha_prestamo'],'%Y-%m-%d')).days
            tiempo_total = tiempo_total + tiempo_dias
        raise osv.except_osv('Promedio de tiempo de préstamo','{0} días'.format(tiempo_total))
        return True

**Adición de boton en la vista formulario del objeto de negocio biblioteca.libro_prestamo**

	<button name="obtener_promedio_prestamo_metodo_read" string="Promedio de Préstamo (read)" type="object"/>

En este ejemplo de aplicación se realiza una búsqueda en los registros de préstamos que correspondan al estado entregado de los libros con id libro_id, se realiza un cálculo del promedio de tiempo de préstamo del libro. record_ids solo almacena una lista con los campos 'fecha_prestamo' y 'fecha_regreso' por cada registro encontrado.

Método Browse
-------------

El método browse obtiene registros como objetos permitiendo utilizar la notación de puntos para explorar los campos y las relaciones, permite consultar con facilidad campos relacionados de forma encadenada a partir de un objeto.

**Estructura de definición del método**

	browse (cr, uid, ids, context=None)

Ejemplo:

	libros_pool = self.pool.get('biblioteca.libro')
	libros_ids = libros_pool.search(cr, uid,[('state','=','compra')], context=context)
	libros_records = libros_pool.browse(cr, uid, libros_ids, context=context)

En este ejemplo el método browse obtiene los registros que correspondan a los ids almacenados en libros_ids, estos registros se almacenan en libros_records.

Ejemplo de aplicación del método browse:

**Adición de función en el objeto de negocio biblioteca.libro_prestamo**

	def obtener_promedio_prestamo_metodo_browse(self,cr,uid,ids,context=None):
        prestamo_ids = self.read(cr, uid, ids, ['prestamo_ids'], context=context)
        prestamo_pool = self.pool.get('biblioteca.libro_prestamo')
        prestamo_records = prestamo_pool.browse(cr, uid, prestamo_ids[0]['prestamo_ids'], context=context)
        tiempo_total = 0
        for record in prestamo_records:
            tiempo_dias = (datetime.strptime(record['fecha_regreso'],'%Y-%m-%d') - datetime.strptime(record['fecha_prestamo'],'%Y-%m-%d')).days
            tiempo_total = tiempo_total + tiempo_dias
        raise osv.except_osv('Promedio de tiempo de préstamo','{0} días'.format(tiempo_total))
        return True

**Adición de boton en la vista formulario del objeto de negocio biblioteca.libro_prestamo**

	<button name="obtener_promedio_prestamo_metodo_browse" string="Promedio de Préstamo (browse)" type="object"/>

Este ejemplo realiza la misma tarea que la función obtener_promedio_prestamo_metodo_read, con la diferencia que record_ids almacena el registro completo de los prestamo_ids encontrados.

Ejercicios propuestos
---------------------

1. Adicionar una restricción al préstamo por libros. Solo debe existir un préstamo activo por cada libro.
