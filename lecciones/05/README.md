Lección 05: Dominios, Busquedas, Filtros y Agrupamientos
========================================================

[TOC]

Dominios
--------

Los dominios en Odoo son utilizados para filtrar los registros a los que se tiene acceso en las vistas o en consultas dentro del código del Modelo.

Estos dominios se pueden asimilar a las condiciones que se agregan en un WHERE en una sentencia SQL. Si para nuestro ejemplo de la biblioteca normalmente en SQL ejecutamos

	SELECT * FROM biblioteca_libre WHERE paginas > 100 AND nombre_autor ILIKE '%cervantes%'

en Odoo el dominio se estructuraría

	[('paginas','>',100),('nombre_autor','ilike','%cervantes%')]`

Un dominio es un listado de criterios, en el ejemplo anterior hay dos criterios, estos criterios estan formados por:

- **`Nombre del campo`** del Modelo sobre el cual se aplica el filtro.
- **`Operador`** a utilizarse para la búsqueda a realizar [=, !=, >, >=, <, <=, =?, =like, like, not like, ilike, not ilike, =ilike, in, not in, child_of](https://www.odoo.com/documentation/8.0/reference/orm.html#domains)
- **`Valor`**: Valor sobre el cual se compara para la búsqueda

Los criterios se pueden combinar utilizando operadores lógicos en [notación prefijo o polaca](http://es.wikipedia.org/wiki/Notaci%C3%B3n_polaca) usando los operadores siguientes:

- '&' AND, operador por defecto
- '|' OR
- '!' NOT

Para una consulta SQL como esta:

    SELECT * FROM biblioteca_libro WHERE paginas > 100 AND nombre_autor ILIKE '%cervantes%' OR nombre_autor ILIKE '%marquez%'

El dominio sería:

    [('paginas','>',100),'|',('nombre_autor','ilike','%cervantes%'),('nombre_autor','ilike','%marquez%')]`

Búsquedas
---------

Las búsquedas (search) permiten visualizar los registros resultantes de la aplicación de una búsqueda, la cual puede ser indicada por el valor específico de uno o varios campos. Las búsquedas utilizan la vista de tipo lista para desplegar los registros resultantes. Cada parámetro de búsqueda puede ser definido utilizando los siguientes elementos básicos:

* **name**: Nombre del campo por el cual se realiza la búsqueda
* **string**: El título de la búsqueda

Ejemplo para la creación de una búsqueda:

	<record model="ir.ui.view" id="biblioteca_libro_search">
        <field name="name">biblioteca.libro.search</field>
        <field name="model">biblioteca.libro</field>
        <field name="arch" type="xml">
            <search string="Biblioteca Libro">
                <field name="isbn" string="ISBN del libro"/>
                <field name="titulo" string="Título del libro"/>
                <field name="autor" string="Nombre del autor del libro"/>
            </search>
        </field>
    </record>

Las búsquedas son aplicadas en campos que no es posible definir su valor.

Filtros
-------

Después de haber definido los criterios de búqueda, se pueden crear filtros, los cuales deben ir en la etiqueta <search> y por medio de un <separator/>.

	<record model="ir.ui.view" id="biblioteca_libro_search">
		<field name="name">biblioteca.libro.search</field>
		<field name="model">biblioteca.libro</field>
		<field name="arch" type="xml">
			<search string="Biblioteca Libro">
				<field name="isbn" string="ISBN del libro"/>
				<field name="titulo" string="Título del libro"/>
				<field name="autor" string="Nombre del autor del libro"/>
				<separator/>
				<filter name="state" string="En solicitud" domain="[('state','=','solicitud')]" help="Estado del regristro en solicitud" icon="terp-check"/>
				 <filter name="state" string="En proceso de compra" domain="[('state','=','compra')]" help="Estado del regristro en proceso de compra" icon="terp-check"/>
			</search>
		</field>
	</record>

Agrupamientos
-------------

En las búsquedas se puede crear agrupamientos:

       <record model="ir.ui.view" id="biblioteca_libro_search">
               <field name="name">biblioteca.libro.search</field>
               <field name="model">biblioteca.libro</field>
               <field name="arch" type="xml">
                       <search string="Biblioteca Libro">
                               <field name="isbn" string="ISBN del libro"/>
                               <field name="titulo" string="Título del libro"/>
                               <field name="autor" string="Nombre del autor del libro"/>
                               <separator/>
                               <group expand="0" string="Group By...">
                                       <filter string="Clasificación del Libro" icon="terp-folder-violet" domain="[]" context="{'group_by':'clasificacion'}"/>
                                       <filter string="Género del Libro" icon="terp-go-month" domain="[]" context="{'group_by':'genero'}"/>
                                       <filter string="Editorial" icon="terp-go-month" domain="[]" context="{'group_by':'editorial'}"/>
                               </group>
                       </search>
               </field>
       </record>


Ejercicios propuestos
---------------------

1. Realizar la carga de datos ubicado en el archivo biblioteca_libro.csv
1. Utilizar las busquedas, filtros y agrupamientos de la lección.
1. Adicionar un nuevo criterio de búsqueda y verifique su funcionamiento.
1. Adicionar un nuevo filtro y verifique su funcionamiento.
1. Adicionar un nuevo agrupamiento y verifique su funcionamiento.

