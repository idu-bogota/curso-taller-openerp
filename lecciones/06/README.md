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

attrs
-----

La interfaz también puede cambiar dinámicamente utilizando el atributo **attrs** así como el ya visto **on_change**. el atributo attrs permite que se cambie los valores definidos para *invisible*, *required* y *readonly*, basado en los valores del formulario, de acuerdo a la regla del criterio pasado en el diccionario.

### Invisible

El atributo invisible permite dejar o no visible un campo en la vista. Ejemplo:

	<field name= "descripcion" attrs= "{'invisible': [('state', '=', 'baja')]}"/>

En el ejemplo se indica que el campo descripción es visible en la vista si el estado del libro es **De baja**.

### Required

El atributo required permite indicar si el campo es o no obligatorio en la vista. Ejemplo:

	<field name="paginas" attrs="{'required': [('state', '=', 'compra')]}"/>

En el ejemplo se indica que el campo paginas es obligatorio en la vista, si el estado del libro es **Proceso de Compra**.

### Readonly

El atributo readonly permite indicar si el campo es o no se solo lectura en la vista. Ejemplo:

	<field name="titulo" attrs="{'readonly': [('state','=','catalogado')]}"/>

En el ejemplo se indica que el campo titulo es unicamente de lectura en la vista, si el estado del libro es Catalogado.

Igualmente puede incluir todos los atributos en **attrs**. Ejemplo:

    <field name="titulo" attrs="{'invisible': [('state', '=', 'baja')], 'required': [('state', '=', 'compra')], 'readonly': [('state','=','catalogado')]}"/>

El ejemplo anterior hace que el campo titulo no aparezca en el formulario cuando el *state* es *baja*; el campo va a ser obligatorio si el estado es *compra* y quedará en modo solo lectura cuando el estado es *catalogado*

Botones
-------
- confirm
- states

Ejercicios propuestos
---------------------

1. Verificar los cambios en la vista al activar el atributo on_change del código ejemplo.
1. Verificar los cambios en la vista según los atributos invisible, required y readonly del código ejemplo.