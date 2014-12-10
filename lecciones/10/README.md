[[
title: Lección 10: Extensión de Módulos Base
author: STRT Grupo I+D+I
]]

Lección 10: Extensión de Módulos Base
=====================================

[TOC]

Herencia de objetos
-------------------

Los objetos de negocio pueden heredar de un módulo base, esta herencia se puede utilizar para modificar, extender, utilizar métodos.

**Estructura de definición**

	_inherit = 'nombre_objeto_base_a_heredar'

**_inherit**: Se utiliza cuando heredamos Modelos o Clases en OpenERP.
**_inherits**: La lista de objetos base que el objeto hereda. Esta lista es un diccionario de la forma: {'name_of_the_parent_object': 'name_of_the_field', ...}.


Existen dos formas de extender un objeto. Ambas formas generan una nueva clase, que tiene campos y funciones heredadas, así como campos y métodos adicionales.

* **Forma 1**: Las instancias de estas clases son visibles por las vistas (views or trees) que operan con la clase padre. Este tipo de herencia se denomina herencia de clase (class inheritance), es de utilidad para sobreescribir métodos de la clase padre.

Ejemplo:

	class nombre_clase(osv.osv):
		_name = 'nombre_objeto_base'
		_inherit = 'nombre_objeto_base'
		_columns = {
			'campo_1: fields.tipo_campo('text_campo'),
		}
	nombre_clase()


* **Forma 2**: Las instancias de estas clases no son visibles por las vistas (views or trees) que operan con la clase padre. Las instancias de estas clases contienen todos las propiedades y métodos de la instancia padre junto con las propiedades y métodos definidos en la nueva entidad. Este tipo de herencia se denomina herencia por prototipos (inheritance by prototyping). La nueva subclase contiene una copia de las propiedades de la clase padre.

Ejemplo:

	class nombre_clase(osv.osv):
		_name = 'nombre_objeto_negocio'
		_inherit = 'nombre_objeto_base'
		_columns = {
			'campo_1: fields.tipo_campo('text_campo'),
		}
	nombre_clase()

**Ejemplo de aplicación**:

	class res_users(osv.osv):
		_inherit = "res.users"
		_columns = {
		   'prestamo_id'  : fields.one2many('biblioteca.libro_prestamo', 'user_id', 'Préstamos'),
		}

	res_users()

Se adiciona el campo 'user_id' al objeto biblioteca.libro_prestamo:

	'user_id': fields.many2one('res.users', 'Usuario solicitante',
                help= 'Usuario que solicita el préstamo'
        ),

Con este ejemplo relacionamos el objeto de negocio res.users con los préstamos de los libros. Se extieden el objeto res.users y se le adiciona el campo prestamo_id.

Herencia de vistas
------------------

También podemos heredar vistas, al igual que se puede heredar objetos. Parámetros:

* ***inherid_id***: ID de la vista ha heredar. La '<carpetapadre> es la primera carpeta que se encuentra en ADDONS, en la cuál se encuentra el fichero xml, en el que está definida la vista.

**Estructura de definición**

	<record model="ir.ui.view" id="nombre_form_inherit">
		<field name="name">nombre.form.inherit</field>
		<field name="model">nombre</field>
		<field name="type">form</field>
		<field name="inherit_id" ref="carpetapadre.idVistaPadre" />
		<field name="arch" type="xml">
			<field name="campoareemplazar" position="after">
			<field name="nuevocampo" />
		 </field>
		 <notebook position="inside">
			 <page string="texto para la nueva pestaña">
				 <group col="2" colspan="2">
					<separator string="texto del separador" colspan="2"/>
					<field name="nuevocampo2"/>
					<field name="nuevocampo3" nolabel="1"/>
				 </group>
			 </page>
		</notebook>
		</field>
	</record>


id es el nuevo identificador de la nueva vista. Por definición manejar el nombre del id terminado en 'form_view_inh' para identificar que es una vista heredada.

**Ejemplo de aplicación**:

	<record id="res_users_form_inherit" model="ir.ui.view">
		<field name="name">res.users.form.inherit</field>
		<field name="model">res.users</field>
		<field name="type">form</field>
		<field name="inherit_id" ref="base.view_users_form"/>
		<field name="arch" type="xml">
		<page string="Access Rights" position="after">
			<page string="Detalles Adicionales">
			   <group col="2">
				  <field name="prestamo_id"/>
				</group>
			 </page>
		</page>
		</field>
	</record>

En este ejemplo se extiende la vista base.view_users_form y se adiciona el nuevo campo prestamo_id.

Ejercicios propuestos
---------------------

1. Revisar la extensión del objeto y la vista realizada en la lección.
1. Consultar los préstamos realizados por los usuarios, igresando al menú usuarios ubicado en configuración, pestaña detalles adicionales.