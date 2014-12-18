[[
title: Lección 13: Campos y Atributos Avanzados
author: STRT Grupo I+D+I
]]

Lección 13: Workflow
====================

[TOC]

¿Que es Workflow?
-----------------

Los Workflow nos permiten gestionar las actividades relacionadas a los objetos de negocio, se representan como grafos dirigidos donde los nodos son las actividades y los conectores son las transiciones. La actividades son las tareas a realizar y las transiciones indica como el workflow cambia de una actividad a otra con el fin de gestionar los ciclos de vida de los objetos.

Creación de Workflow
--------------------

En la definición de un Workflow, se pueden indicar condiciones, señales, y transiciones, por lo que el comportamiento del workflow depende de las acciones realizadas por usuario sobre el objeto de negocio.

Lo primero a tener en cuenta es que el Worklow es definido en objetos de negocio con campo 'state'.


* **id**: id como identificador del workflow. Se define como “wkf_”+objeto_de_negocio
* **model**: Se define como ”workflow”.
* **Name**: Nombre para el Workflow.
* **Osv**: Nombre del objeto de negocio al cual se le define el Workflow.
* **on_create**: Crea el Workflow al crear el objeto.

Ejemplo de una declaración del workflow:

	<?xml version="1.0" encoding="UTF8"?>
	<openerp>
		<data>
		   <record id="wkf_nombreobjetodelworkflow" model="workflow">
		   <field name="name">nombremodulo.basic</field>
		   <field name="osv">object.name</field>
		   <field name="on_create">True</field>
		   </record>
		</data>
	</openerp>

Restricciones para Workflow
---------------------------

Seguridad para Workflow
-----------------------

Ejercicios propuestos
---------------------

1. Revisar el workflow definido para el objeto de negocio bliblioteca.libro del módulo ejemplo biblioteca.
1. Definir el workflow para el objeto de negocio biblioteca.libro_prestamo.