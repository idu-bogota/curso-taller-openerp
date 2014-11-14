Lección 03: Vistas Básicas
=============================

[TOC]

La forma de visualización de los objetos de negocio en OpenERP, es por medio de las vistas. La interfaz de usuario es creada dinámicamente utilizando la configuración definida en la base de datos, al crear un módulo la interfaz de usuario se crea a través de archivos XML que tienen los datos a ser insertados en la base de datos y que son cargados en el momento de instalarse el módulo.

Existen diferentes tipos de vistas disponibles en OpenERP, las cuales puedes ser asociadas a un mismo objeto:

* Formulario
* Lista
* Calendario
* Diagramas de Gantt
* Gráficos de datos
* Búsqueda

Cada tipo de vista permite una presentación diferente de los datos almacenados. Para el despliegue de las vistas se utiliza comunmente un enlace desde el menú de opciones de la interfaz, estos menús son creados en conjunto con las vistas.

Definición de una vista
-----------------------

Estructura para la creación de una vista a través de un archivo XML es la siguiente:

    <record model="ir.ui.view" id="mi_objeto_de_negocio_vista">
        <field name="name">mi_objeto_de_negocio.vista</field>
        <field name="model">mi_modulo.mi_objeto_de_negocio</field>
        <field name="arch" type="xml">
            <tree string="mi_objeto_de_negocio">
                <field name="campo_1"/>
                <field name="campo_2"/>
                <field name="campo_3"/>
						.
                        .
                        .
                <field name="campo_n"/>
            </tree>
        </field>
    </record>

* **`<record>`**: Tag utilizado para insertar registros en la base de datos asociados a un objeto de negocio definido en el atributo model, este tag no es solo utilizado para definición de vistas, tema explicado en las siguiente lecciones.
* **`model`**: Indica de que tipo es el registro que se va a crear en la base de datos, para el caso de las vistas es: *ir.ui.view*.
* **`id`**: Es un identificador único para el registro, este identificador sirve para referenciar el registro en otros elementos y documentos XML.
* **`<field>`**: Este tag es utilizado para almacenar un valor especifico de acuerdo al record.model contenedor.
* atributo **`name`**: Indica el nombre del campo en la base de datos en el cual se va a almacenar el valor
* **`name`**: Es el nombre con el cual se identifica la vista
* **`model`**: Indica el modelo al cual esta vista estará enlazado
* **`arch`**: Indica la estructura de la vista, dentro de este tag se coloca en forma de documento XML la definición de la vista, esta puede cambiar de acuerdo al tipo de vista definido.

Vista tipo lista
----------------

El tipo de vista lista o tree, se utiliza para visualizar el listado de registros del objeto de negocio; en este tipo de vista se selecciona los campos más relevantes para ser desplegados. Cada lista puede ser definido utilizando los siguientes elementos básicos:

* **string**: El título de la vista
* **colors**: Se puede asignar un color de letra a los elementos que cumplan con una condición especifica
* editable: Se puede indicar que el registro sea editable desde la vista tipo lista sin necesidad de abrir el objeto en un formulario.

Ejemplo para la creación de una vista tipo lista:

	<record model="ir.ui.view" id="biblioteca_libro_tree">
        <field name="name">biblioteca.libro.tree</field>
        <field name="model">biblioteca.libro</field>
        <field name="arch" type="xml">
            <tree string="Biblioteca Libro" colors="blue:state=='draft'" editable="top">
                <field name="isbn"/>
                <field name="titulo"/>
                <field name="autor"/>
                <field name="paginas"/>
            </tree>
        </field>
    </record>


Vista tipo formulario
---------------------

Los formularios permiten creación y/o edición de registros, cada formulario puede ser definido utilizando los siguientes elementos básicos:

* atributo **`string`**: Indica el label a ser utilizado en el elemento
* atributo **`colspan`**: Indica el número de columnas en el cual va a expandirse el elemento
* atributo **`col`**: Indica el número de columnas que el elemento va a contener para ubicar los elementos incluidos
* **`separator`**: Crea una linea separadora con un label
* **`label`**: Crea un label de texto
* **`group`**: Permite agrupar elementos y opcionalmente asignar un label
* **`notebook`**: Crea un contenedor de tabs
* **`page`**: Crea un tab dentro del *notebook*
* **`newline`**: Crea un salto de linea

Ejemplo para la creación de una vista tipo formulario:

	<record model="ir.ui.view" id="biblioteca_libro_form">
        <field name="name">biblioteca.libro.form</field>
            <field name="model">biblioteca.libro</field>
            <field name="arch" type="xml">
                <form string="Biblioteca Libro">
                    <separator string="">
                    <label string="Este es un formulario de prueba"/>
                    <group string="Libros" colspan="2">
                        <field name="titulo"/>
                    </group>
                    <group string="Estado" colspan="2">
                        <field name="active"/>
                        <field name="state"/>
                    </group>
                    <notebook colspan="4">
                        <page string="Detalles">
                            <field name="isbn"/>
                            <field name="autor"/>
                            <field name="descripcion"/>
                            <newline />
                            <field name="paginas"/>
                        </page>
                        <page string="Fechas">
                            <field name="fecha"/>
                        </page>
                    </notebook>
                </form>
          </field>
    </record>

Vista tipo Gráfica
------------------

Esta vista permite desplegar los datos disponibles en una grafica. Cada vista gráfica puede ser definida utilizando los siguientes elementos básicos:

* atributo **`type`**: Indica el tipo de gráfica a utilizarse (pie, bar), por defecto pie
* atributo **`orientation`**: Indica la orientación de las barras (horizontal, vertical)
* **`field`**: Se debe ingresar como mínimo dos campos field (eje X, eje Y, eje Z), un tercero es opcional 3
* atributo **`group`**: Se coloca en 1 para el campo a ser utilizado en el GROUP BY
* atributo **`operator`**: Indica el tipo de operador de agregación a ser utilizado (+,*,**,min,max)

Ejemplo para la creación de una vista tipo gráfico:

    <record model="ir.ui.view" id="libro_graph">
        <field name="name">libro.graph</field>
        <field name="model">biblioteca.libro</field>
        <field name="arch" type="xml">
            <graph type="bar" orientation="horizontal" string="Gráfico">
                <field name="state"/>
                <field name="paginas" operator="min"/>
            </graph>
        </field>
    </record>

Ejercicios propuestos
---------------------

* Adicione a la vista tipo lista el campo fecha del objeto de negocio *biblioteca.libro*
* Asigne nuevos colores a la vista tipo lista para los estados activo y cancelado del objeto de negocio *biblioteca.libro*
* Modifique la vista tipo gráfica de tipo *bar* a *pie* y los parámetros de agrupación y operadores de agregación, compruebe los cambios en la interfaz de usuario
* Crear la vista tipo lista y tipo formulario para el objeto de negocio *biblioteca.libro_prestamo*.
* Crear el item del menú para el objeto de negocio *biblioteca.libro_prestamo*.
