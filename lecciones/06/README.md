Lección 06: Vista Dinámica
==========================

[TOC]

on_change
---------

El atributo on_change permite ejecutar un método en el objeto de negocio cuando se realiza cualquier tipo de cambio sobre el valor del campo al cual se le asocia el atributo on_change.

La estructura para el uso del atributo es la siguiente:

	<field name="nombre_campo" on_change="nombre_metodo_a_ejecutar(nombre_parametro)"/>

Para el uso del atributo se indica en nombre del campo al cual se le asocia el atributo on_change, se referencia el método a ser llamado y los parámetros a ser pasados al método. Ejemplo del código en la vista:

    <field name="active" on_change="onchange_active(active)"/>

El método recibe los valores de los campos indicados como parámetros y retorna un diccionario con nuevos valores asignados a los campos del objeto de negocio, reflejado como cambios en la interfaz. Ejemplo del código en el objeto de negocio:

    def onchange_active(self, cr, uid, ids, active):
        if not active:
            return {'value': {'state': 'baja'} }
        return {
            'warning': {'message': 'Cambiando el estado a "activo"'},
            'value': {'state': 'solicitud'},
        }

* **value**: Diccionario con los nuevos valores a ser asignados a otros campos del formulario
* **warning**: Despliegue de mensaje en la interfaz

attr
----------

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

Ejercicios propuestos
---------------------

1. Verificar los cambios en la vista al activar el atributo on_change del código ejemplo.
1. Verificar los cambios en la vista según los atributos invisible, required y readonly del código ejemplo.