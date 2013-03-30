## Objetos de negocio (II)

Los objetos de negocio permite configuración adicional que permite agregar reglas para mantener la consistencia de los datos en nuestro módulo o cambiar el comportamiento de la plataforma.

### Cambiando el ordenamiento por defecto

Para que los datos se organizen de manera diferente puede utilizar el atributo **_order** e indicar el nombre del campo a utilizarse para el ordenamiento (por defecto sde organizan por *id*).

    class mi_modulo_mi_tabla(osv.osv):
        _name = "mi_modulo.mi_tabla"
        _order= 'name'
        ...
        ...

### Valores por defecto

Los objetos pueden ser cargados con valores por defecto usando el diccionario **_defaults**

    def _random_quantity(self, cr, uid, context = None):
        """
        Método de la clase para generar un valor entero aleatorio
        """
        return randint(5,100)

    _defaults = {
        'active': True,
        'state': 'draft',
        'price': lambda *a: random(), #Genera un valor flotante aleatorio
        'quantity': _random_quantity, #Llama al método de la clase previamente definido
    }

En este diccionario se adiciona como llave el nombre del campo y como valor lo que deseamos sea el valor por defecto o una función que hace el cálculo del mismo. Se pueden utilizar funciones lambda o métodos de la clase. Debe recordar que los métodos de la clase deben estar previamente definidos para poder utilizarlos.

Los parámetros recibidos por el método de la clase son:
* **cr**: Es el cursor de la BD
* **uid**: Es el ID del usuario actual
* **context**: es Un diccionario que puede contener valores de configuración, por defecto se encuentra el idioma del usuario

### Restricciones

Se pueden definir dos tipos de restricciones una por métodos de la clase y otra utilizando constrains SQL, como se muestra a continuación

        _sql_constraints = [
            ('unique_name','unique(name)','El nombre debe ser único'),
        ]

        def _check_date(self, cr, uid, ids, context = None):
            is_valid_data = True
            present = datetime.now()
            for obj in self.browse(cr,uid,ids,context=None):
                if not obj.date or not obj.datetime:
                    continue

                date = datetime.strptime(obj.date, '%Y-%m-%d')
                date_time = datetime.strptime(obj.datetime, '%Y-%m-%d %H:%M:%S')
                if(date < present or date_time < present):
                    is_valid_data = False

            return is_valid_data

        _constraints = [
            (_check_date,'Fecha debe ser en el futuro',['date','datetime']),
        ]

Las restricciones SQL se definen como un arreglo de tuplas que contienen:

* nombre de la restricción
* restricción SQL a aplicar
* El mensaje de error a ser desplegado en caso de que se viole la restricción

Las restricciones por métodos de la clase se definen como un arreglo de tuplas que contienen:

* método a ser invocado
* El mensaje de error a ser desplegado en caso de que se viole la restricción
* Campos que van a invocar la revisión de la restricción, el método se llama solo cuando estos campos son modificados

Los parámetros que recibe el método de la clase que hace la restricción son:

* **cr**: Es el cursor de la BD
* **uid**: Es el ID del usuario actual
* **ids**: Son los IDs de los objetos a los cuales se les va a aplicar la restricción
* **context**: es Un diccionario que puede contener valores de configuración, por defecto se encuentra el idioma del usuario
