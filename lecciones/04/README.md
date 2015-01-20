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
    isbn = fields.Char('ISBN', size=255, help="International Standard Book Number", copy=False)

```


- Atributo **`required`** se usa para indicar si el **campo es obligatorio** o no en la creación/edición de un registro en el Modelo. True indica que el campo es requerido y False que el campo es no requerido.

    Si no se define el atributo required en el campo, por defecto toma el valor de required = False.

    En la interfaz web el campo va a tener un fondo de color azul claro que va a indicar que el campo es obligarotio


- Atributo **`readonly`** se usa para indicar si el campo **puede o no ser editable** por el usuario. use True si el campo es no editable y False que pueda ser editable.

    Si no se define el atributo readonly en el campo, por defecto toma el valor de readonly = False.


- Atributo **`default`** se usa para indicar el valor por defecto que va a tener el campo cuando se cree un registro nuevo. Se puede indicar el valor a tomarse o una función que retornaría el valor por defecto a utilizarse. En este diccionario se adiciona como llave el nombre del campo y como valor lo que deseamos sea el valor por defecto o una función que hace el cálculo del mismo. Se pueden utilizar funciones lambda o métodos de la clase. Debe recordar que los métodos de la clase deben estar previamente definidos para poder utilizarlos. [Más información acerca de valores por defecto](https://www.odoo.com/documentation/8.0/howtos/backend.html#default-values)

- Atributo **`copy`** se usa para indicar que cuando se duplique un registro el campo debe o no ser copiado. `copy=False` evita que se copie, por defecto el valor es `True`


Restricciones de Modelo: @api.constrains
----------------------------------------

Si se desea que los Modelos tengan restricciones que sean verificadas antes de almacenar los registros, estas se deben definir como métodos de la clase donde se utiliza el decorador @api.constrains.

```python
from openerp.exceptions import ValidationError
import datetime

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'

    @api.one
    @api.constrains('fecha_publicacion','fecha_compra')
    def _check_fechas(self):
        present = datetime.now()
        if self.fecha_compra and self.fecha_compra > present:
            raise ValidationError("Fecha de compra incorrecta")
        if self.fecha_publicacion and self.fecha_publicacion > present:
            raise ValidationError("Fecha de publicación incorrecta")


```

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


Si la base de datos ya tiene datos que violan la restricción, esta no va a crearse, ni aplicarse. Cuando esto pase, va a aparecer un error en el log del servidor como el siguiente:

    2015-01-20 13:34:29,959 10290 INFO nombre_basedatos openerp.modules.module: module biblioteca: creating or updating database tables
    2015-01-20 13:34:30,009 10290 WARNING nombre_basedatos openerp.models.schema: Table 'biblioteca_libro': unable to add 'unique(isbn)' constraint !
    If you want to have it, you should update the records and execute manually:
    ALTER TABLE "biblioteca_libro" ADD CONSTRAINT "biblioteca_libro_unique_isbn" unique(isbn)

Para aplicar la restricción SQL ud debe corregir los datos primero, para este caso eliminando los ISBN duplicados y actualizar nuevamente el módulo.

Ejercicios propuestos
---------------------

Utilizando el código de la lección:

- Crear un nuevo registro y verificar que los campos `active`, `fecha_publicacion` y `precio` se llenan con el valor por defecto indicado en el código.
- Modificar el código para que el campo `fecha_compra` tenga un valor por defecto.
- Modificar el código para que el valor por defecto del campo `state` sea *Solicitud*
- Modificar el código para que el campo `nombre_autor` tenga un valor por defecto generado aleatoriamente utilizando [generador de nombres en python] (https://pypi.python.org/pypi/names/)
- Cambie el atributo `copy` del campo `name` a *False*, verifique que sucede cuando se utiliza la opción de *Más >> Duplicar* en la vista formulario de un registro de libro. Revise nuevamente dejando `copy` con el valor de *True*
- Verifique que no puede crear/editar un libro y asignar un ISBN ya utilizado por otro libro. Ajuste los datos para poder activar la restricción si esta no fue aplicada.
- Adicionar una restricción utilizando el decorador `@api.constraints` para que el campo `paginas` no acepte valores menores a 0 ni valores mayores a 5000
- Utilizando `_sql_constraints` adicione un constraint para que el campo `precio` no acepte valores negativos. Ver [sentencia SQL soportada por posgreSQL para CHECK](http://www.postgresql.org/docs/9.4/static/ddl-constraints.html)
