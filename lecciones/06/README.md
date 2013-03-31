## Interfaz de usuario (II)

Vamos a ver como la interfaz puede cambiar dinámicamente utilizando los atributos **attrs** y **on_change**, también veremos como adicionar botones que realicen acciones especificas en el objeto de negocio.

### attrs

Este atributo permite que se cambie los valores definidos para *readonly*, *invisible* y *required* basado en los valores del formulario, de acuerdo a la regla del criterio pasado en el diccionadio.

    <field name="tabla_relacionada_id" attrs="{'invisible': [('state', '=', 'draft')], 'required': [('state', '=', 'active')], 'readonly': [('state','=','cancelled')]}"/>

El ejemplo anterior hace que el campo *tabla_relacionada_id* no aparezca en el formulario cuando el *state* es *draft*; el campo va a ser obligatorio si el estado es *active* y quedará en modo solo lectura cuando el estado es *cancelled*

### on_change

Este atributo permite ejecutar un método en el objeto de negocio cuando el valor del campo cambia. Solo debe referenciar el método a ser llamado y los parametros a ser pasados al método, como en el siguiente ejemplo:

    <field name="active" on_change="onchange_active(active)"/>

El método en el objeto de negocio recibe los valores pasados como parámetros y retornar un diccionario cambios en la interfaz, tal como lo muestra el siguiente ejemplo:

    def onchange_active(self, cr, uid, ids, active):
        if not active:
            return {'value': {'state': 'cancelled'} }
        return {
            'warning': {'message': 'Cambiando el estado a "activo"'},
            'value': {'state': 'active'},
            'domain': {'tabla_relacionada_id': "[('state','=','active')]" },
        }

* **value**: Este diccionario indica nuevos valores a ser asignados a otros campos del formulario
* **warning**: Hace que se despliegue un mensaje en la interfaz
* **domain**: El diccionario puede cambiar el valor del atributo *domain* de otro campo en el formulario

## Botones de acción

Se puede invocar acciones especificas del objeto de negocio a través de botones en la interfaz de usuario. Para esto utilizamos la etiqueta `button`, como en el ejemplo acontinuación:

    <button name="next_monday_date" string="Poner la fecha del próximo lunes" type="object" icon="gtk-ok" states="active"/>

* **name**: Indica el nombre del método a llamar
* **string**: Indica el label del botón
* **type**: Indica el tipo del botón, para este caso el tipo es object, existen otros tipos adicionales usados para gestión de workflows y acciones.
* **icon**: Indica el icono a utilizar en el botón
* **states**: Indica los estados en los cuales el botón será desplegado.

