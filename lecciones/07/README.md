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

* **Nombre del Modelo Relacionado**: Nombre del Modelo que contiene el campo Many2one que apunta a este Modelo. Ej. `biblioteca.prestamo`
* **Nombre del campo que contine la relación**: Nombre del campo Many2one que existe en el Modelo relacionado. Ej. `libro_id`

Por convención el nombre del campo se le adiciona el sufijo **_ids**

[Mayor información del campo One2many en la información oficial de referencia de Odoo](https://www.odoo.com/documentation/8.0/reference/orm.html#openerp.fields.One2many)

Ejemplo:

```python
from openerp import models, fields, api

class biblioteca_prestamo(models.Model):
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

many2many consiste en que un objeto de negocio A se relaciona con un objeto de negocio B y a su vez el objeto de negocio B se relaciona con el objeto de negocio A, de tal forma que al persistirse cualquier objeto también se persista la lista de objetos que posee. Su estructura es la siguiente:

	'nombre_campo_ids': fields.many2one('nombre_tabla_a_relacionar', 'nombre_tabla_nueva', 'campo_id_en_A', 'campo_id_en_B', 'Descripción del campo')

Los parámetros recibidos por este campo son:

* **nombre_tabla_a_relacionar**: Nombre del objeto de negocio relacionado.
* **ondelete**: Indica como se manejará la eliminación del objeto padre, aquí los valores disponibles en la documentación de PostgreSQL (set null, cascade)
* **domain**: Criterio que limita los objetos que serán relacionados, más adelante se dan mayores ejemplos del criterio de búsqueda.

los parámetros a utilizar son:

* **nombre_tabla_a_relacionar**: Nombre del objeto de negocio relacionado.
* **nombre_tabla_nueva**: Nombre de la tabla relación donde se almacena la relación muchos a muchos.
* **campo_id_en_A**: Nombre del campo en la tabla relación donde se almacena el ID del objeto actual.
* **campo_id_en_B**: Nombre del campo en la tabla relación donde se almacena el ID del objeto objetivo.

Por convención el nombre del campo se le adiciona el sufijo **_ids**

Ejemplo (campo genero_ids):

	class biblioteca_libro(osv.osv):
		_name = "biblioteca.libro"
		_order= 'fecha'
		_columns = {
			'active': fields.boolean('Active', help='Activo/Inactivo'),
			'isbn': fields.char('ISBN', size = 255, required=True,),
			.
			.
			.
			'genero_ids': fields.many2many('biblioteca.libro_genero','biblioteca_libro_clasificaciones',
					'genero_id',
					'libro_id',
					'Género del Libro',
			),
			'editorial': fields.char('Editorial', size = 255, help='Editorial del libro'),
		}

	biblioteca_libro()

Para adicionar el campo en la vista solo debe adicionarlo en la vista correspondiente como lo haría con cualquier otro campo usando la etiqueta `<field>`.


Ejercicios propuestos
---------------------

1. Verificar los cambios en los campos donde se aplicaron las relaciones. Ver código ejemlo.
1. Crear el objeto de negocio editorial, con los campos name, pais.
1. Crear vista y menú de acceso para el objeto de negocio editorial.
1. Cambiar el tipo del campo editorial ubicaco en el objeto de negocio libro, por el tipo de campo many2many. Moficiar el nombre de campo a editorial_ids y crear la relación.
1. Verifique en la vista los cambios realizados.
