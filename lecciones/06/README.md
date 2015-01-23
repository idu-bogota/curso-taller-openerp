Lección 06: Vistas Dinámicas
============================

[TOC]

Actualizar formulario al cambiar valores: @api.onchange
--------------------------------------------------------

Muchas veces es necesario que algunos campos del formulario se actualicen basados en las selecciones o datos que se ingresan en otros campos del formulario, para esto se utiliza el decorador `@api.onchange` en cualquier método python que se implemente en el Modelo. Ejemplo:

```python
from openerp import models, fields, api

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'

    @api.onchange('precio')
    def onchange_precio(self):
        if self.precio and self.precio > 1000:
            self.descripcion = 'Ta muy caro el libro'

```


De igual forma se puede utilizar un método onchange para enviarle al usuario mensajes de validación a medida que va llenando el formulario, esto no es un remplazo para las restricciones que se adicionen con _sql_constraints o @api.constraints, ya que onchange solo aplica a nivel de vista y no se llama en el momento de guardar los datos.


```python
from openerp import models, fields, api

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'

    @api.onchange('isbn')
    def onchange_warning_isbn(self):
        if self.isbn and len(self.isbn) < 10:
            self.descripcion = 'Verifique el ISBN cumpla con la norma'
            return {
                'warning': {
                    'title': "ISBN",
                    'message': "El largo del ISBN debe ser mayor o igual a 10 caracteres",
                }
            }

```

Si desea que un metodo @api.constraints sea también llamado cuando el usuario cambia el valor en el formulario web puede hacerlo adicionando el @api.onchange decorator. Pero debe tener en cuenta que el error se llama utilizando `raise ValidationError` y no retornando un diccionario como en el ejemplo anterior.

```python
from openerp import models, fields, api

class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'


    @api.one
    @api.constrains('paginas')
    @api.onchange('paginas')
    def _check_paginas(self):
        if self.paginas < 0 or self.paginas > 5000:
            raise ValidationError("Un libro debe tener entre 0 y 5000 páginas")

```

Si no se desea que se llame el onchange en una vista en particular puede adicionar en la vista:

	<field name="NOMBRE_DEL_CAMPO" on_change="0"/>

Mayor información del uso de onchange en:

- https://www.odoo.com/documentation/8.0/reference/orm.html#onchange-updating-ui-on-the-fly
- https://www.odoo.com/documentation/8.0/howtos/backend.html#onchange

Cambios basado en otros campos: attrs
-------------------------------------

La interfaz también puede cambiar dinámicamente utilizando el atributo **attrs** en las etiquetas `button`,`field`,`notebook`. El atributo *attrs* permite que se cambie los valores definidos para los campos en las opciones `invisible`, `required` y `readonly` de acuerdo a una regla de dominio que se cumpla.

- **Invisible**: El atributo invisible permite mostrar u ocultar un campo en la vista, el valor `True` oculta el campo. Ejemplo:

        <field name= "descripcion" attrs= "{'invisible': [('state', '=', 'baja')]}"/>

   En el ejemplo se indica que el campo descripción se oculta cuando el estado es del libro es **De baja**.

- **Required**: El atributo required permite indicar si el campo es o no obligatorio a nivel de la vista, esto no cambia el valor de required para el campo a nivel de modelo. Ejemplo:

        <field name="paginas" attrs="{'required': [('state', '=', 'en_compra')]}"/>

    En el ejemplo se indica que el campo *paginas* es obligatorio a nivel de vista si el estado del libro es **Proceso de Compra**.

- **Readonly**: El atributo readonly permite indicar si el campo es o no de solo lectura a nivel de la vista. Ejemplo:

        <field name="name" attrs="{'readonly': [('state','=','catalogado')]}"/>

    En el ejemplo se indica que el campo titulo es unicamente de lectura en la vista cuando el estado del libro es **Catalogado**.

Igualmente puede incluir todos los atributos en **attrs**. Ejemplo:

    <field name="name" attrs="{'invisible': [('state', '=', 'baja')], 'required': [('state', '=', 'compra')], 'readonly': [('precio','>',100)]}"/>

El ejemplo anterior hace que el campo titulo no aparezca en el formulario cuando el *state* es *baja*; el campo va a ser obligatorio si el estado es *compra* y quedará en modo solo lectura cuando el estado es *catalogado*

Igualmente si ud quiere en la vista utilizar los atributos `invisible`, `required` y `readonly` sin depender de una condición lo puede hacer como se muestra acontinuación:

    <field name="nombre_campo" invisible="1" required="1" readonly="1"/>


Ejercicios propuestos
---------------------

Utilizando el código de la lección:

1. Verifique que el precio no puede ser editable a través de la vista formulario del libro, pero si a través del menú editar precios. Verifique en la definición de la vista como se hizo.
1. Cambie un libro de estado y vea como se comporta la pestaña de *fechas* cuando esta en modo edición.
1. Coloque el libro en estado *Proceso de compra* y haga click en el botón *Comprado hoy*, vea como cambian los campos *fecha de compra* y el *estado* del libro.
1. Adicioné un botón llamado *Devolver compra* que aparezca cuando el estado sea *Adquirido* y que cambie la fecha de compra a vacio y el estado a *Proceso de Compra*
1. Ajuste los campos de *Editorial*, *Clasificación* y *Género* para que sean obligatorios cuando el estado del libro sea *Adquirido*
1. Ajuste los campos del formulario para que sean de solo lectura cuando el estado es *Catalogado* y *De baja*
