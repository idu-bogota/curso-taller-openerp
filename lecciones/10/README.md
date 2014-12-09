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

**Estructura de definición **

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


Herencia de vistas
------------------