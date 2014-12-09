Lección 08: Otros Widgets y Vistas
==================================

[TOC]

Widgets
-------

Widget es la clase base para todos los componentes visuales, un widget es un componente genérico dedicado a mostrar el contenido al usuario.

Existen diferentes widgets:

**widget="many2many_tags"**: Igual que many2many
**widget="monetary"**: Permite visualizar el simbolo moneda
**widget="mail_followers"**: Permite adicionar seguidores
**widget="mail_thread"**: Mail a grupos
**widget="statusbar"**: Muestra la barra de estado
**widget="progressbar"**: Muestra la barra de progreso
**widget="html"**: Muestra los campos HTML
**widget="url"**: Muestra la url como un enlace
**widget=”integer”**: Permite almacenar solo valores enteros
**widget="image"**: Muestra el valor del campo como una imagen
**widget="handle"**: Permite organizar un listado de registros y almacenar la posición en un campo con el nombre **sequence**.

Ejemplo de aplicación de widget:

	<field name="state" widget="statusbar"/>


Vista tipo kanban
-----------------

Las vistas tipo kanban permiten manejar información importante (campos principales) en imágenes o tarjetas, es util para poder identificar los registros de una forma más rápida y así agilizar la consulta sobre los datos.

Ejemplo para la creación de una vista tipo kanban:

	<record model="ir.ui.view" id="libro_kanban">
	<field name="name">libro.kanban</field>
	<field name="model">biblioteca.libro</field>
	<field name="type">kanban</field>
	<field name="arch" type="xml">
	<kanban version="7.0" class="oe_background_grey">
		<field name="titulo"/>
		<field name="autor"/>
		<field name="user_id"/>
		<templates>
			<t t-name="kanban-box">
				<div class="oe_resource_vignette">
					<div t-attf-class="oe_kanban_color_#{kanban_getcolor(record.state.value)} oe_kanban_card oe_kanban_global_click">
						<div class="oe_kanban_project_avatars">
							<img t-att-src="kanban_image('res.users', 'image', record.user_id.raw_value)"
								t-att-title="record.user_id.value"
								width="24" height="24"
								class="oe_kanban_avatar"
							/>
						</div>
					</div>
					<div class="oe_resource_details">
						<ul>
						   <li><field name="state"/></li>
						   <field name="titulo"/>
						   <field name="autor"/>
						 </ul>
					</div>
				</div>
			</t>
		</templates>
	</kanban>
	</field>
	</record>

Para que la vista se despliegue es necesario adicionar en el action_libro el tipo de vista kanban.

	<record model="ir.actions.act_window" id="action_libro">
	  <field name="name">Libro</field>
	  <field name="res_model">biblioteca.libro</field>
	  <field name="view_type">form</field>
	  <field name="view_mode">tree,form,graph,kanban</field>
	</record>


Vista tipo gantt
----------------

Las vistas tipo gantt permiten mostrar el tiempo planificado o transcurrido para el desarrollo de tareas o actividades, es una vista dinámica, se puede hacer click en cualquier parte del gráfico, arrastrar y soltar el objeto en otra ubicación.


Ejemplo para la creación de una vista tipo gantt:

	<record id="biblioteca_libro_prestamo_gantt" model="ir.ui.view">
		  <field name="name">biblioteca.libro_prestamo.gantt</field>
		  <field name="model">biblioteca.libro_prestamo</field>
		  <field eval="2" name="priority"/>
		  <field name="arch" type="xml">
			  <gantt date_start="fecha_prestamo" date_stop="fecha_regreso" string="Préstamos" default_group_by="libro_id">
			  </gantt>
		  </field>
	</record>

Para que la vista se despliegue es necesario adicionar en el action_libro_prestamo el tipo de vista gantt.

	<record model="ir.actions.act_window" id="action_libro_prestamo">
		  <field name="name">Prestamo</field>
		  <field name="res_model">biblioteca.libro_prestamo</field>
		  <field name="view_type">form</field>
		  <field name="view_mode">tree,form,gantt</field>
	</record>

Vista tipo calendar
-------------------

Las vistas tipo calendar permiten visualizar la planificación en tiempo para el desarrollo de tareas o actividades, es una vista dinámica, se puede hacer click en cualquier parte del gráfico, arrastrar y soltar el objeto en otra ubicación.

Ejemplo para la creación de una vista tipo calendar:

	<record id="biblioteca_libro_prestamo_calendar" model="ir.ui.view">
		  <field name="name">biblioteca.libro_prestamo.calendar</field>
		  <field name="model">biblioteca.libro_prestamo</field>
		  <field eval="2" name="priority"/>
		  <field name="arch" type="xml">
			  <calendar color="libro_id" date_start="fecha_prestamo" date_stop="fecha_regreso" string="Informe de Préstamos">
				  <field name="libro_id"/>
			  </calendar>
		  </field>
	</record>

Para que la vista se despliegue es necesario adicionar en el action_libro_prestamo el tipo de vista calendar.

	<record model="ir.actions.act_window" id="action_libro_prestamo">
		  <field name="name">Prestamo</field>
		  <field name="res_model">biblioteca.libro_prestamo</field>
		  <field name="view_type">form</field>
		  <field name="view_mode">tree,form,gantt,calendar</field>
	</record>

Ejercicios propuestos
---------------------

1. Verificar las diferentes vistas creadas.
