Lección 04: Reglas Básicas y Restricciones
==========================================

[TOC]

Los objetos de negocio permite configuraciones adicionales que permite agregar reglas y restricciones para mantener la consistencia de los datos o cambiar el comportamiento de la plataforma.

Ordenamiento por defecto: _order
--------------------------------

Para que los datos se organizen de manera diferente puede utilizar el atributo **_order** e indicar el nombre del campo a utilizarse para el ordenamiento (por defecto se organizan por *id*).

    class biblioteca_libro(osv.osv):
        _name = "biblioteca.libro"
        _order= 'name'
        .
        .
        .
        }
	biblioteca_libro()

Campos requeridos: required
---------------------------

En la definición de campos el atributo requiered se define para indicar si el campo es requerido o no en la creación de un registro en el objeto de negocio. True inica que el campo es requerido y False que el campo es no requerido.

Si no se define el atributo required en el campo, por defecto toma el valor de required = False.

	_columns = {
        'active': fields.boolean('Active', help='Activo/Inactivo'),
        'isbn': fields.char('ISBN', size = 255, required=True),
			.
            .
            .
    }

Campos de solo lectura: readonly
--------------------------------

En la definición de campos el atributo readonly se define para indicar si el campo puede o no ser editable por el usuario. True campo no editable y False campo editable.

Si no se define el atributo readonly en el campo, por defecto toma el valor de readonly = False.

	_columns = {
        'active': fields.boolean('Active', help='Activo/Inactivo', readonly=True),
			.
            .
            .
    }


Valores por defecto: _defaults
------------------------------

Los objetos pueden ser cargados con valores por defecto usando el diccionario **_defaults**

La forma básica de definir un valor por defecto es:

	_defaults = {
        'active': True,
        'state': 'solicitud',
	}

Se puede definir valores por defecto que son resultado de la generación de un método:

	def _random_paginas(self, cr, uid, context = None):
        """
        Método de la clase para generar un valor entero aleatorio
        """
        return randint(5,100)

    _defaults = {
        'active': True,
        'state': 'solicitud',
        'precio': lambda *a: random(), #Genera un valor flotante aleatorio
        'paginas': _random_paginas, #Llama al método de la clase previamente definido
    }

En este diccionario se adiciona como llave el nombre del campo y como valor lo que deseamos sea el valor por defecto o una función que hace el cálculo del mismo. Se pueden utilizar funciones lambda o métodos de la clase. Debe recordar que los métodos de la clase deben estar previamente definidos para poder utilizarlos.

Los parámetros recibidos por el método de la clase son:
* **cr**: Es el cursor de la BD
* **uid**: Es el ID del usuario actual
* **context**: Diccionario que puede contener valores de configuración, por defecto se encuentra el idioma del usuario

[ver información de como definir un método en python](http://https://docs.python.org/2/tutorial/classes.html)

Restricciones para el objeto de negocio: _constraints
-----------------------------------------------------

Las restricciones tipo _constraints se utiliza para programar validaciones para el usuario, estas son definidas por métodos de la clase.

	def _check_date(self, cr, uid, ids, context = None):
        is_valid_data = True
        present = datetime.now()
        for obj in self.browse(cr,uid,ids,context=None):
            if not obj.date or not obj.datetime:
                continue

            date = datetime.strptime(obj.date, '%Y-%m-%d')
            date_time = datetime.strptime(obj.datetime, '%Y-%m-%d %H:%M:%S')
            if(date > present or date_time > present):
                is_valid_data = False

        return is_valid_data

    _constraints = [
        (_check_date,'Fecha debe ser anterior a la fecha actual',['date','datetime']),
        ]

Las restricciones por métodos de la clase se definen como un arreglo de tuplas que contienen:

* método a ser invocado
* El mensaje de error a ser desplegado en caso de que se viole la restricción
* Campos que van a invocar la revisión de la restricción, el método se llama solo cuando estos campos son modificados

Los parámetros que recibe el método de la clase que hace la restricción son:

* **cr**: Es el cursor de la BD
* **uid**: Es el ID del usuario actual
* **ids**: Son los IDs de los objetos a los cuales se les va a aplicar la restricción
* **context**: es Un diccionario que puede contener valores de configuración, por defecto se encuentra el idioma del usuario

Restricciones para el objeto de negocio: _sql_constraints
---------------------------------------------------------

Otro tipo de restricción que se puede utilizar para programar validaciones para el usuario es _sql_constraints.

    _sql_constraints = [
        ('unique_isbn','unique(isbn)','El ISBN debe ser único'),
    ]

*En este ejemplo se restringe al usuario la duplicación de registros validados por el campo isbn definido como campo único.*

Las restricciones SQL se definen como un arreglo de tuplas que contienen:

* nombre de la restricción
* restricción SQL a aplicar
* El mensaje de error a ser desplegado en caso de que se viole la restricción


Ejercicios propuestos
---------------------

* Definir en ordenamiendo del objeto de negocio por el campo **fecha**
* Crear un nuevo registro donde verique los valores definidos por defecto.
* Modificar el código para que el valor por defecto del campo **state** sea **Solicitud**
* Modificar el código para que el campo **descripcion** cree un método que retorne como valor por defecto el texto ***Ingresar la descripción del libro***
* Adicionar una restricción para que el campo **precio** no acepte valores menores a 1000 ni valores mayores a 500000
