Lección 04: Reglas Básicas y Restricciones en Modelos
=====================================================

[TOC]

Los Modelos en Odoo permiten configuraciones adicionales que agregan reglas que permiten manejar la consistencia de los datos basado en las necesidades de la aplicación.

Campos requeridos, de solo lectura y valores por defecto
--------------------------------------------------------

Cada campo puede ser definido como requerido, de solo lectura o asignarsele un valor por defecto, un campo del Modelo puede asignarsele uno o varios de estos atributos. A continuación un ejemplo:

    ```python
    import random

    class biblioteca_libro(models.Model):
        _name = 'biblioteca.libro'

        def _precio_aleatorio(self):
            return random.random()

                name = fields.Boolean('Active', help='Activo/Inactivo', required=True)
                active = fields.Boolean('Active', help='Activo/Inactivo', default=True)
                fecha_publicacion = fields.Date('Fecha de Publicación', help='Fecha de publicación', default=fields.Date.today)
                precio = fields.Float('Precio', help='Precio de Compra', digits=(10, 2), default=_precio_aleatorio, readonly=True)

    ```


- Atributo `required` se usa para indicar si el **campo es obligatorio** o no en la creación/edición de un registro en el Modelo. True indica que el campo es requerido y False que el campo es no requerido.

    Si no se define el atributo required en el campo, por defecto toma el valor de required = False.

    En la interfaz web el campo va a tener un fondo de color azul claro que va a indicar que el campo es obligarotio


- Atributo `readonly` se usa para indicar si el campo **puede o no ser editable** por el usuario. use True si el campo es no editable y False que pueda ser editable.

    Si no se define el atributo readonly en el campo, por defecto toma el valor de readonly = False.


- Atributo `default` se usa para indicar el valor por defecto que va a tener el campo cuando se cree un registro nuevo. Se puede indicar el valor a tomarse o una función que retornaría el valor por defecto a utilizarse. En este diccionario se adiciona como llave el nombre del campo y como valor lo que deseamos sea el valor por defecto o una función que hace el cálculo del mismo. Se pueden utilizar funciones lambda o métodos de la clase. Debe recordar que los métodos de la clase deben estar previamente definidos para poder utilizarlos. [Más información acerca de valores por defecto](https://www.odoo.com/documentation/8.0/howtos/backend.html#default-values)


Restricciones de Modelo: @api.constrains
----------------------------------------

Si se desea que los Modelos tengan restricciones que se validen antes de almacenar los registros, estas son definidas por métodos de la clase donde se utiliza el decorador @api.constrains.

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

Restricciones SQL: _sql_constraints
-----------------------------------

Otro tipo de restricción que se puede utilizar para programar validaciones es a través del diccionario _sql_constraints, donde se pueden adicionar restricciones programadas con sentencias SQL.

    _sql_constraints = [
        ('unique_isbn','unique(isbn)','El ISBN debe ser único'),
    ]

*En este ejemplo se restringe al usuario la duplicación de registros validados por el campo isbn definido como campo único.*

Las restricciones SQL se definen como un arreglo de tuplas que contienen:

* Nombre de la restricción
* Restricción SQL a aplicar
* El mensaje de error a ser desplegado en caso de que se viole la restricción


Ejercicios propuestos
---------------------

* Crear un nuevo registro donde verique los valores definidos por defecto.
* Modificar el código para que el valor por defecto del campo **state** sea **Solicitud**
* Modificar el código para que el campo **descripcion** cree un método que retorne como valor por defecto el texto ***Ingresar la descripción del libro***
* Adicionar una restricción para que el campo **precio** no acepte valores menores a 1000 ni valores mayores a 500000
