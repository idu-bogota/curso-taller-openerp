Lección 05: Busquedas, Filtros y Agrupamientos
==============================================

[TOC]

Búsquedas
---------

La búsquedas (search) permiten visualizar los registros resultantes de la aplicación de una búsqueda, la cual puede ser indicada por el valor específico de uno o varios campos. Las búsquedas utilizan la vista de tipo lista para desplegar los registros resultantes. Cada parámetro de búsqueda puede ser definido utilizando los siguientes elementos básicos:

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

Después de haber definido los criterios de búqueda, se pueden crear filtros, los cuales deben ir en la etiqueta <search> y por medio de un  <separator/>.

	<record model="ir.ui.view" id="biblioteca_libro_search">
		<field name="name">biblioteca.libro.search</field>
		<field name="model">biblioteca.libro</field>
		<field name="arch" type="xml">
			<search string="Biblioteca Libro">
				<field name="isbn" string="ISBN del libro"/>
				<field name="titulo" string="Título del libro"/>
				<field name="autor" string="Nombre del autor del libro"/>
				<separator/>
				<filter name="state" string="Estado en progreso " domain="[('state','=','open')]" help="Estado del regristro En progreso " icon="terp-check"/>
				 <filter name="state" string="Estado pendiente " domain="[('state','=','pending')]" help="Estado del regristro En progreso " icon="terp-check"/>
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

