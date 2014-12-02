Lección 07: Relaciones entre Objetos de Negocio
===============================================

[TOC]

Las aplicaciones comunes requieren que los datos esten relacionados, veremos a continuación como manejar las relaciones entre Objetos de Negocios, a través de nuevos tipos de campos one2many, many2one y many2many.

Relaciones one2many
-------------------

one2many hace referencia hacia un campo específico de un objeto de negocio, creando la relación iniciada por el campo many2one, permite que el objeto padre pueda acceder a todos los objetos relacionados. Su estructura es la siguiente:

	'nombre_campo_ids': fields.one2many('nombre_tabla_a_relacionar', 'nombre_campo_tabla_a_relacionar_id', 'Descripción del campo')

Los parámetros recibidos por este campo son:

* **nombre_tabla_a_relacionar**: Nombre del objeto de negocio relacionado.
* **nombre_campo_tabla_a_relacionar_id**: Nombre del campo que contiene la relación en la tabla relacionada.

Por convención el nombre del campo se le adiciona el sufijo **_ids**

Ejemplo (campo clasificacion_ids):

	class biblioteca_libro(osv.osv):
		_name = "biblioteca.libro"
		_order= 'fecha'
		_columns = {
			'active': fields.boolean('Active', help='Activo/Inactivo'),
			'isbn': fields.char('ISBN', size = 255, required=True,),
			.
			.
			.
			'clasificacion_ids': fields.one2many('biblioteca.libro_clasificacion', 'libro_id', 'Clasificación del libro'),
			'editorial': fields.char('Editorial', size = 255, help='Editorial del libro'),
		}

	biblioteca_libro()


Para adicionar el campo en la vista solo debe adicionarlo en la vista correspondiente como lo haría con cualquier otro campo usando la etiqueta `<field>`.

Para la relación uno a muchos se utiliza el tipo de campo *many2one* este campo crea la llave foranea entre las tablas de dos objetos de negocio.

Relaciones many2one
-------------------

many2one hace referencia hacia un objeto de negocio, este campo crea la llave foranea entre las tablas de dos objetos de negocios. Su estructura es la siguiente:

	'nombre_campo_id': fields.many2one('nombre_tabla_a_relacionar', 'Descripción del campo', select= True, ondelete= 'cascade', domain="[('state','=','active')]" )

Los parámetros recibidos por este campo son:

* **nombre_tabla_a_relacionar**: Nombre del objeto de negocio relacionado.
* **ondelete**: Indica como se manejará la eliminación del objeto padre, aquí los valores disponibles en la documentación de PostgreSQL (set null, cascade)
* **domain**: Criterio que limita los objetos que serán relacionados, más adelante se dan mayores ejemplos del criterio de búsqueda.

Ejemplo (campo libro_id):

	class biblioteca_libro_clasificacion(osv.osv):
		_name = "biblioteca.libro_clasificacion"
		_columns = {
			'name': fields.char('Clasificación'),
			'libro_id': fields.many2one('biblioteca.libro','id del Libro',
				select=True,
				ondelete='cascade'
			),
		}

	biblioteca_libro_clasificacion()


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
