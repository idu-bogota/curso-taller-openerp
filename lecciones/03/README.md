Lección 03: Vistas Básicas
=============================

[TOC]

Para ingresar, actualizar, eliminar y desplegar registros para los Modelos definidos en Odoo se hace uso de la interfaz web, esta interfaz
se define a través de vistas.

Al crear un módulo la interfaz de usuario se define a través de archivos XML, estos archivos son cargados en la base de datos en el
momento de instalarse el módulo. La interfaz web es creada dinámicamente utilizando la configuración de vistas para cada Modelo disponible en la base de datos
a partir de los archivos XML instalados.

Existen diferentes tipos de vistas disponibles en OpenERP, un Modelo puede tener asociadas varias vistas, las vistas básicas son:

- form: formulario
- tree: listado/árbol
- search: búsqueda

Cada tipo de vista permite una presentación diferente de los datos almacenados.
Para el despliegue de las vistas se utiliza comunmente un enlace desde el menú de opciones de la interfaz web,
estos menús son creados en conjunto con las vistas en el XML y cargadas posteriormente a la base de datos. En la lección anterior creamos
un menú item directamente en la base de datos, pero para poder replicar este item en otras instalaciones de Odoo, es necesario que exista
la definición del menú en el código de un módulo.

Definición de una vista
-----------------------

La estructura para la creación de una vista a través de un archivo XML es la siguiente:

    <record model="ir.ui.view" id="nombre_modelo_tipo_vista">
        <field name="name">Nombre de la vista</field>
        <field name="model">nombre_modulo.nombre_modelo</field>
        <field name="priority" eval="16"/>
        <field name="arch" type="xml">
            <tree>
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

- **`name`**: Es el nombre con el cual se identifica la vista
- **`model`**: Indica el modelo al cual esta vista estará enlazado
- **`priority`**: Indica el orden de prioridad de la vista para el Modelo, la vista con menor prioridad será la vista por defecto a utilizarse. Por defecto el valor es 16. También se usa para indicar el orden en que se aplican los cambios cuando se hereda la vista.
- **`arch`**: Indica la estructura de la vista, dentro de este tag se coloca en forma de documento XML la definición de la vista, esta puede cambiar de acuerdo al tipo de vista definido.

[Más información acerca de la definición de vistas](https://www.odoo.com/documentation/8.0/reference/views.html#common-structure)

Vista tipo listado
------------------

El tipo de vista listado o tree, se utiliza para visualizar el listado de registros que existe en la base de datos para el Modelo que se visualiza
en la vista; en este tipo de vista se deben adicionar los campos más relevantes para ser desplegados.
Cada lista puede ser definido utilizando los siguientes elementos básicos:

- **`default_order`**: Permite indicar el criterio de organización de los registros del listado.
- **`colors`**: Se puede asignar un color a la fuente de letra a los registros que cumplan con una condición especifica. [Consulte los colores válidos](http://www.w3.org/TR/css3-color/#colorunits)
- **`fonts`**: Se puede asignar un estilo de fuente de letra a los registros que cumplan con una condición especifica. Los estilos permitidos son `bold`, `italic`, `underline`.
- **`editable`**: Se puede indicar que el registro sea editable desde la vista tipo lista sin necesidad de abrir el objeto en un formulario. Los valores permitidos son `top` o `bottom`.

[Más información acerca de la definición de vistas tipo listado](https://www.odoo.com/documentation/8.0/reference/views.html#lists)

Ejemplo para la creación de una vista tipo lista:

    <record model="ir.ui.view" id="biblioteca_libro_tree">
        <field name="name">biblioteca.libro.tree</field>
        <field name="model">biblioteca.libro</field>
        <field name="arch" type="xml">
            <tree colors="blue:state=='solicitud';green:state=='catalogado'" editable="top" fonts="bold:state=='en_compra'">
                <field name="isbn"/>
                <field name="titulo"/>
                <field name="autor"/>
                <field name="paginas"/>
                <field name="state"/>
            </tree>
        </field>
    </record>


Vista tipo formulario
---------------------

Los formularios permiten creación y/o edición de registros, cada formulario puede ser definido utilizando los siguientes elementos básicos:

- **`notebook`**: Crea un contenedor de pestañas (tabs).
- **`page`**: Crea una pestaña dentro del *notebook*, requiere un atributo `string` con el nombre de la pestaña.
- **`newline`**: Crea un salto de línea, obligando a que los elementos siguientes se ubiquen en la siguiente línea.
- **`separator`**: Crea una linea separadora con una etiqueta definida en el atributo `string`
- **`label`**: Crea una etiqueta de texto
- **`group`**: Permite agrupar elementos y opcionalmente asignar una etiqueta
    - atributo **`colspan`**: Indica el número de columnas que va a tomar el grupo
    - atributo **`col`**: Indica el número de columnas que el elemento va a contener para organizar los elementos incluidos en el grupo
- **`sheet`**: Permite agrupar los elementos de un formulario dentro de una margen y bordes.
- **`header`**: Permite organizar una cabecera donde incluir botones de acción y desplegar el estado del objeto

Ejemplo para la creación de una vista tipo formulario:

	<record model="ir.ui.view" id="biblioteca_libro_form">
        <field name="name">biblioteca.libro.form</field>
        <field name="model">biblioteca.libro</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                </sheet>
                <label string="Este es un formulario de prueba"/>
                <group string="Libros" colspan="2">
                    <field name="name"/>
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
* Asigne nuevos colores a la vista tipo lista para los estados en **Proceso de compra** y **Catalogado** del objeto de negocio *biblioteca.libro*
* Modifique la vista tipo gráfica de tipo *bar* a *pie* y los parámetros de agrupación y operadores de agregación, compruebe los cambios en la interfaz de usuario
* Crear la vista tipo lista y tipo formulario para el objeto de negocio *biblioteca.libro_prestamo*.
* Crear el item del menú para el objeto de negocio *biblioteca.libro_prestamo*.
