Lección 07: Relaciones entre Modelos
====================================

[TOC]

Las aplicaciones comunes requieren que los datos esten relacionados, veremos a continuación como manejar las relaciones entre Modelos, a través de nuevos tipos de campos one2many, many2one y many2many.

Relaciones Many2one
-------------------

Utilizando un campo de tipo Many2one creamos una relación directa entre el Modelo actual (donde se define el campo) y algún otro Modelo, este campo crea la llave foranea entre las tablas de dos Modelos. Su estructura básica es la siguiente:

	nombre_campo_id = fields.Many2one('Nombre del Modelo', 'Etiqueta', [...])

Los parámetros recibidos por este tipo de campo son:

- **Nombre del Modelo**: Nombre del Modelo con el cual crear la [relación de llave foránea](http://www.postgresql.org/docs/9.4/static/tutorial-fk.html), ej. `biblioteca.libro`, `res.partner`, `res.users`
- **Etiqueta**: Etiqueta a desplegarse en la vista web para este campo
- **ondelete**: Indica a la base de datos como manejar la relación cuando el registro del modelo relacionado sea eliminado. Los valores disponibles son: `set null`, `restrict`, `cascade`; por defecto se usa `set null`
- **domain**: Criterio que limita el listado de registros a ser listados para ser relacionados con el Modelo actual. ej. Ver solo los libros catalogados y no los que estan en compra. :white_up_pointing_index: Ud puede agregar el dominio como un *string* `domain="[('state', '=', 'catalogado')]"` o como una *lista de tuplas* `domain=[('state', '=', 'catalogado')]`, cuando se adiciona como string el dominio se evalua en el lado del cliente y puede usar nombres de campos despues del operador, pero cuando es una lista de tuplas se evalua en el lado del servidor y no permite el manejo de campos, solo de valores.

[Mayor información del campo Many2one en la información oficial de referencia de Odoo](https://www.odoo.com/documentation/8.0/reference/orm.html#openerp.fields.Many2one)

Ejemplo:

```python
from openerp import models, fields, api

class biblioteca_prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Registro de prestamo'

    libro_id = fields.Many2one('biblioteca.libro', 'Libro prestado', domain=[('state', '=', 'catalogado')])
```

### Despliegue en la vista

Para que el campo se despliegue en la vista debe simplemente agregar en el documento XML el tag `field` con el nombre del campo, como se hace regularmente. Pero de manera adicional tiene la posibilidad de adicionar los siguientes atributos:

- Atributo **`widget`**: permite indicar que se utilice `selection`, para que la el widget de selección sea mucho más simple que el que viene por defecto y no despliegue la opción de crear o editar.

- Atributo **domain**: Permite a nivel de vista adicionar restriciones de campos a desplegar para la selección de registros a ser relacionados.

Relaciones One2many
-------------------

Un campo One2many permite que el Modelo actual (donde se define el campo) pueda acceder a todos los registros relacionados, este campo requiere que el Modelo relacionado tenga creado un campo tipo Many2one que haga referencia al Modelo actual. Su estructura es la siguiente:

	nombre_campo_ids = fields.One2many('Nombre del Modelo Relacionado', 'Nombre del campo que contine la relación', 'Etiqueta', [...])

Los parámetros recibidos por este campo son:

- **Nombre del Modelo Relacionado**: Nombre del Modelo que contiene el campo Many2one que apunta a este Modelo. Ej. `biblioteca.prestamo`
- **Nombre del campo que contine la relación**: Nombre del campo Many2one que existe en el Modelo relacionado. Ej. `libro_id`

Por convención el nombre del campo se le adiciona el sufijo **_ids**

[Mayor información del campo One2many en la información oficial de referencia de Odoo](https://www.odoo.com/documentation/8.0/reference/orm.html#openerp.fields.One2many)

Ejemplo:

```python
from openerp import models, fields, api

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro de la biblioteca'

    prestamo_ids = fields.One2many('biblioteca.prestamo', 'libro_id', 'Prestamos realizados')
```

### Despliegue en la vista

Para que el campo se despliegue en la vista debe simplemente agregar en el documento XML el tag `field` con el nombre del campo, como se hace regularmente. ej `<field name="prestamo_ids"/>`. Pero de manera adicional puede indicar como desplegar los registros relacionados:

- Atributo **`mode`**: Por defecto se despliegan los registros relacionados utilizando la vista tipo listado o `tree` del Modelo relacionado, pero se puede indicar si se desa utilizar una vista tipo [`graph`](https://www.odoo.com/documentation/8.0/reference/views.html#graphs) o [`kanban`](https://www.odoo.com/documentation/8.0/reference/views.html#kanban), estas vistas se explicarán en otra lección.

Se puede definir la estructura de la vista a ser utilizada dentro de la misma etiqueta `field` tal como se muestra a continuación:

    <field name="prestamo_ids">
        <tree>
            <field name="fecha"/>
            <field name="fecha_devolucion"/>
        </tree>
    </field>

Relaciones many2many
--------------------

La relación many2many consiste en que un Modelo A puede tener relación con uno o varios registros del Modelo B y a su vez el Modelo B se puede relacionar con varios registros del Modelo A, a diferencia de one2many donde la cardinalidad es de muchos a uno. Para esto se requiere de una tabla intermedia que almacena la relación entre los Modelos, esta tabla es generada automáticamente y no se puede acceder como un Modelo independiente. Su estructura es la siguiente:

	nombre_campo_ids = fields.Many2many('Nombre Modelo del Relacionado', string='Etiqueta')

Los parámetros recibidos por este campo son:

- **Nombre del Modelo Relacionado**: Nombre del Modelo que contiene el campo Many2one que apunta a este Modelo. Ej. `biblioteca.prestamo`
- **domain**: Criterio que limita el listado de registros a ser listados para ser relacionados con el Modelo actual.

Por defecto Odoo genera el nombre de la tabla intermedia y de los campos relacionados, pero estos pueden ser indicados explicitamente utilizando

- **relation**: Nombre de la tabla a utilizar para almacenar los registros de la relación
- **column1**: Nombre de la columna en la tabla de relación que va a contener los IDs del **Modelo actual** (donde se esta definiendo el campo)
- **column2**: Nombre de la columna en la tabla de relación que va a contener los IDs del **Modelo relacionado**

Por convención el nombre del campo se le adiciona el sufijo **_ids**

Ejemplo:

```python
from openerp import models, fields, api

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro de la biblioteca'

    genero_ids = fields.Many2many('biblioteca.genero', string="Generos")

class biblioteca_genero(models.Model):
    _name = 'biblioteca.genero'
    _description = 'Genero literario'

    libro_ids = fields.Many2many('biblioteca.libro', string="Libros")

```

:white_up_pointing_index: El ejemplo va a crear una tabla para la relación llamada `biblioteca_genero_biblioteca_libro_rel` y con los campos: `biblioteca_libro_id` y `biblioteca_genero_id`

### Despliegue en la vista

Para que el campo se despliegue en la vista debe simplemente agregar en el documento XML el tag `field` con el nombre del campo, como se hace regularmente. ej `<field name="genero_ids"/>`. Pero de manera adicional puede indicar como desplegar los registros relacionados:

- Atributo **`widget`**: Por defecto se despliegan los registros relacionados utilizando la vista tipo listado o `tree` del Modelo relacionado, pero se puede indicar si se desea utilizar un widget diferente como **`many2many_tags`**.


Ejercicios propuestos
---------------------

Utilizando el código de ejemplo de la lección:

1. Crear un prestamo y ver como el campo libro solo muestra los libros en estado *catalogado*.
1. Adicione generos a uno registro del Modelo libro.
1. En la vista tipo formulario del Modelo prestamo adicionar el atributo `widget="selection"` en el campo `libro_id`, nota la diferencia?
1. En la vista tipo formulario del Modelo libro adicionar el atributo `widget="many2many_tags"` en el campo `genero_ids`, nota la diferencia? Adicione nuevos generos a varios registros del Modelo libro.
1. En la vista tipo formulario del Modelo libro adicionar en el listado de prestamos el campo `duracion_dias`.
1. Crear un Modelo **biblioteca.editorial** con el campo `name`
1. Crear una relación many2one de *libro* a *editorial* y el inverso one2many de *libro* a *editorial*, desplegarlos en las vista formulario.
1. Crear un Modelo **biblioteca.autor** con el campo `name`
1. Crear una relación many2many de *libro* a *autor* y el inverso de *autor* a *libro*, desplegarlos en las vista formulario.
1. Verifique a través de pgadmin3 la estructura de las tablas y los *constraints* creados.
