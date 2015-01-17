Lección 03: Vistas Básicas
=============================

[TOC]

Para ingresar, actualizar, eliminar y desplegar registros para los Modelos definidos en Odoo se hace uso de la interfaz web, esta interfaz se define a través de vistas.

Al crear un módulo la interfaz de usuario se define a través de archivos XML, estos archivos son cargados en la base de datos en el momento de instalarse el módulo. La interfaz web es creada dinámicamente utilizando la configuración de vistas para cada Modelo disponible en la base de datos a partir de los archivos XML instalados.

Existen diferentes tipos de vistas disponibles en OpenERP, un Modelo puede tener asociadas varias vistas, las vistas básicas son:

- form: formulario
- tree: listado/árbol
- search: búsqueda

Cada tipo de vista permite una presentación diferente de los datos almacenados. Para el despliegue de las vistas se utiliza comunmente un enlace desde el menú de opciones de la interfaz web, estos menús son creados en conjunto con las vistas en el XML y cargadas posteriormente a la base de datos. En la lección anterior creamos un menú item directamente en la base de datos, pero para poder replicar este item en otras instalaciones de Odoo, es necesario que exista la definición del menú en el código de un módulo.

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
    - atributo **`col`**: Indica el número de columnas que el elemento va a contener para organizar los elementos incluidos en el grupo. Por defecto un grupo tiene dos columnas.
- **`sheet`**: Permite agrupar los elementos de un formulario dentro de un recuadro que emula una página impresa, dandole margen al formlario.
- **`header`**: Permite organizar una cabecera donde incluir botones de acción y desplegar el estado del objeto.
- **`HTML Tags`**: También se pueden adicionar tags HTML para personalizar la estructura de la vista.
- **`field`**: Despliega o permite la edición del dato del registro para un campo especifico del Modelo.
    - atributo **`name`**: Obligatorio. Indica el nombre del campo en el modelo.
    - atributo **`widget`**: Permite indicar que el campo tenga una visualización diferente a la predefinida. Algunos widgets son: `statusbar`, `progressbar`, `selection`
    - atributo **`class`**: Indica una clase CSS usada para darle estilo al campo. Algunas clases predefinidas son: `oe_inline`, `oe_left`, `oe_right`, `oe_read_only`, `oe_edit_only`, `oe_no_button`, `oe_avatar`.

[Más información acerca de la definición de vistas tipo formulario](https://www.odoo.com/documentation/8.0/reference/views.html#forms)

Ejemplo para la creación de una vista tipo formulario:

    <record model="ir.ui.view" id="libro_form">
        <field name="name">biblioteca.libro.form</field>
        <field name="model">biblioteca.libro</field>
        <field name="arch" type="xml">
            <form>
                <header>
                    <field name="state" widget="statusbar" clickable="1"/>
                </header>
                <sheet>
                    <div class="oe_title">
                        <label for="name" class="oe_edit_only" string="Título" />
                        <h1><field name="name"/></h1>
                    </div>
                    <separator string="Detalles"/>
                    <group>
                        <field name="isbn"/>
                        <field name="nombre_autor"/>
                        <field name="paginas"/>
                        <field name="active"/>
                    </group>
                    <notebook>
                        <page string="Descripción">
                            <field name="descripcion" placeholder="Descripción del libro"/>
                        </page>
                        <page string="Fechas">
                            <group>
                                <label string="Fechas importantes en la gestión del libro" colspan="2" class="oe_read_only"/>
                                <field name="fecha_compra"/>
                            </group>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>

Window Actions y Menu Items
---------------------------

Los Actions indican a Odoo como debe responder frente a una acción del usuario, existen varios tipos de actions, el más utilizado es el Window Action, el cual define que modelo se va a desplegar, que vistas van a estar disponibles y la configuración general de las mismas. Para generar un action utilizamos el `record` para el model `ir.actions.act_window` a continuación se listan los atributos más relevantes para configurar el action:

- **`name`**: Un nombre para el action, se utiliza para desplegarse en la interfaz web.
- **`res_model`**: Se indica el nombre del Modelo del cual se va a presentar la información.
- **`view_type`**: Cuando se abre el tipo de vista listado, este parámetro indica si este se abre como un listado normal `form` o como un árbol desplegable `tree`.
- **`view_mode`**: Indica los tipos de vista que van a estar disponibles.
- **`limit`**: Se indica cuantos registros se van a desplegar en los listados. Por defecto se despliegan 80.
- **`view_id`**: Se puede indicar el ID de una vista especifica para ser desplegada.

[Más información acerca de la definición de window actions](https://www.odoo.com/documentation/8.0/reference/actions.html#window-actions-ir-actions-act-window)

Ejemplo para la creación de un action a ser utilizado en el menú:

    <record model="ir.actions.act_window" id="libro_action">
        <field name="name">Catálogo de Libros</field>
        <field name="res_model">biblioteca.libro</field>
        <field name="view_type">form</field>
        <field name="view_mode">tree,form</field>
        <field name="limit">10</field>
    </record>

La estructura de menús se define al igual que las vistas usando un documento XML. Para este caso vamos a usar el tag `menuitem`.

- atributo **`id`**: Identificador del menuitem para ser referenciado en otros menuitems
- atributo **`name`**: Indica el nombre a desplegarse en el menú.
- atributo **`parent`**: Indica el ID de otro menuitem que va a ser el item padre de este menu, esto permite generar el árbol de navegación. Si no tiene padre, el menuitem va a aparecer en la barra superior de navegación.
- atributo **`action`**: Indica el ID de una acción que va a ser ejecutada. Esta acción indica que Modelo va a ser desplegado y que vistas se van a incluir.

Acontinuación un ejemplo de como crear menú para ul módulo:

    <menuitem id="biblioteca_nav_menu" name="Biblioteca"/>
    <menuitem id="biblioteca_menu" name="Cátalogo" parent="biblioteca_nav_menu"/>
    <menuitem id="biblioteca_libro_menu" parent="biblioteca_menu" name="Libros" action="libro_action"/>

Ejercicios propuestos
---------------------

Tomando como base el código fuente disponible en la lección:

- Adiciones varios registros en el menú *Libros*. :white_up_pointing_index: Cuando esta en la vista formulario de un registro puede hacer click en la opción que aparece en la parte superior *más >> duplicar*, para crear una copia del registro actual.
- Cambie el estado de algunos registros a *solicitud* o *catalogado* y vea como cambia de colores el listado de libros.
- Adicione a la vista tipo listado del Modelo *biblioteca.libro* el campo fecha.
- Asigne nuevos colores a la vista tipo listado para los estados en **Proceso de compra** y **De baja** del Modelo *biblioteca.libro*
- Ingrese al menú *Biblioteca >> Catálogo >> Editar precios* y edite los precios de los libros.
	- Haga clic en el botón crear y adicione un nuevo registro
	- Modifique la vista con el id `precio_libro_tree` y coloque `editable="bottom"`
	- Actualice y cree un nuevo registro. Nota la diferencia?
- Ingrese al menú *Configuración >> Técnico >> Interfaz de usuario >> Elementos menú*, búsque los menus creados para el módulo y revise los datos que se almacenan en la base de datos a partir del XML.
- Ingrese al menú *Configuración >> Técnico >> Interfaz de usuario >> Vistas*, búsque las vistas creadas para el Modelo *biblioteca.libro* y revise los datos que se almacenan en la base de datos a partir del XML.
- Ingrese al menú *Configuración >> Técnico >> Acciones >> Acciones de ventana*, búsque las acciones creadas para el Modelo *biblioteca.libro* y revise los datos que se almacenan en la base de datos a partir del XML.
- Active el **modo desarrollador**, ingresando a la opción *Acerca de Odoo* que se despliega en el menú de la parte superior derecha en la barra negra de navegación donde dice *Administrador*.
	- Abra la vista listado del Modelo *biblioteca.libro*, en la parte superior del formulario, abajo del menú de navegación verá que aparece un campo de selección que dice *Depurar vista#xx*, haga clic y seleccione la opción *Editar TreeVista*.
	- En el cuadro de dialogo que se despliega puede observar que aparece la vista definida, modifique el campo en la pestaña *estructura* y adicione el campo `<field name="fecha_publicacion"/>`
	- Guarde y cierre el cuadro de diálogo y recargue la página. Verá que la interfaz se actualiza basado en el dato actualizado de la base de datos.
	- Ahora reinicie el servidor Odoo en el eclipse y note como los cambios que hizo en la base de datos se reversan luego de actualizado el módulo.
- Crear el item del menú para el Modelo *biblioteca.libro_prestamo*
- Cree las vistas tree y form para el Modelo *biblioteca.libro_prestamo*
