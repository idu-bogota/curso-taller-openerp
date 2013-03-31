## Objetos de negocio (III)

Las aplicaciones comunes requieren que los datos esten relacionados, veremos a continuación como manejar las relaciones entre Objetos de Negocios, a través de nuevos tipos de campos one2many, many2one y many2many.

### Relaciones uno a muchos

Para la relación uno a muchos se utilizan los siguientes tipos de campos:

* **many2one**: Este campo crea la llave foranea entre las tablas de dos objetos de negocios

      class mi_modulo_mi_tabla(osv.osv):
          _name = "mi_modulo.mi_tabla"
          _columns = {
              ...
              'tabla_relacionada_id': fields.many2one('mi_modulo.mi_tabla_relacionada', 'Tabla Relacionada', domain="[('state','=','active')]", ondelete='set null'),
              ...
          }

  Los parámetros recibidos por este campo son:

  * Nombre del objeto de negocio relacionado.
  * **ondelete**: Indica como se manejará la eliminación del objeto padre, aquí los valores disponibles en la documentación de PostgreSQL (set null, cascade)
  * **domain**: Criterio que limita los objetos que serán relacionados, más adelante se dan mayores ejemplos del criterio de búsqueda.

* **one2many**: Este campo es el inverso de many2one, permite que el objeto padre pueda acceder a todos los objetos relacionados

        class mi_modulo_mi_tabla_relacionada(osv.osv):
            _name = "mi_modulo.mi_tabla_relacionada"
            _columns = {
                ...
                'related': fields.one2many('mi_modulo.mi_tabla', 'tabla_relacionada_id', 'Objetos relacionados'),
            }

    Los parámetros recibidos por este campo son:

    * Nombre del objeto de negocio relacionado.
    * Nombre del campo que contiene la relación en la tabla relacionada

Por convención el nombre del campo se le adiciona el sufijo **_id**

Para adicionar el campo en la vista solo debe adicionarlo en la vista correspondiente como lo haría con cualquier otro campo usando la etiqueta `<field>`.

### Relación muchos a muchos

La relación de muchos a muchos se maneja con el campo **many2many** como en el ejemplo siguiente:

    class mi_modulo_mi_tabla(osv.osv):
        _name = "mi_modulo.mi_tabla"
        _columns = {
            ...
            'partner_ids': fields.many2many('res.partner', 'mi_modulo_partner_rel', 'mi_tabla_id', 'partner_id', 'Proveedores'),
            ...
        }

los parámetros a utilizar son:

* Nombre del objeto de negocio relacionado.
* Nombre de la tabla relación donde se almacena la relación muchos a muchos.
* Nombre del campo en la tabla relación donde se almacena el ID del objeto actual.
* Nombre del campo en la tabla relación donde se almacena el ID del objeto objetivo.

Por convención el nombre del campo se le adiciona el sufijo **_ids**

## Criterios de búsqueda

El críterio de búsqueda que es utilizado en OpenERP en diversos ámbitos es un arreglo de tuplas que tiene la siguiente estructura:

    [('campo','operador','valor'), ... ]

Los operadores que puede utilizar son: =, !=, >, >=, <, <=, like, ilike, in, not in, child_of, parent_left, parent_right

Por ejemplo para limitar los objetos que tienen *status* igual a *draft* el criterio sería:

    [('status','=','draft')]

Si desea que adicionalmente el objeto tenga el campo booleano *active* con valor *Verdadero* es:

    [('status','=','draft'), ('active','=',True)]

Por defecto el criterio une todas las tuplas con el operador lógico **AND**, si desea puede utilizar los siguientes operadores:

* **&** para AND
* **|** para OR
* **!** para NOT

Los operadores lógicos se aplican como prefijos, ejemplo:

    [('name','=','ABC'),'!',('language.code','=','en_US'),'|',('country_id.code','=','be'),('country_id.code','=','de'))

lo que equivale a:

    (name is 'ABC' AND (language is NOT english) AND (country is Belgium OR Germany))



