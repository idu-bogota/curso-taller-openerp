## Interfaz de usuario

La interfaz de usuario es creada dinámicamente utilizando la configuración definida en la base de datos, al crear un módulo la interfaz de usuario se crea a través de archivos XML que tienen los datos a ser insertados en la base de datos y que son cargados en el momento de instalarse el módulo.

Existen diferentes tipos de vistas disponibles en OpenERP:
* Formulario
* Listado
* Calendario
* Diagramas de Gantt
* Gráficos de datos
* Búsqueda

Cada tipo de vista permite una presentación diferente de los datos almacenados. Para el despliegue de las vistas se utiliza comunmente un enlace desde el menú de opciones de la interfaz, estos menús son creados en conjunto con las vistas.

## Definición de una vista

La estructura para la creación de una vista a través de un archivo XML es la siguiente:

    <record model="ir.ui.view" id="mi_modulo_mi_tabla_tree">
        <field name="name">mi_modulo.mi_tabla.tree</field>
        <field name="model">mi_modulo.mi_tabla</field>
        <field name="type">tree</field>
        <field name="arch" type="xml">
            <tree string="mi_modulo mi_tabla">
                <field name="active"/>
                <field name="name"/>
                <field name="quantity"/>
                <field name="price"/>
            </tree>
        </field>
    </record>

* **<record>**: Este tag es utilizado para insertar registros en la base de datos asociados a un objeto de negocio definido en el atributo model, este tag no es solo utilizado para definición de vistas como se verá en las lecciones siguientes.
* **model**: Indica de que tipo es el registro que se va a crear en la base de datos, para el caso de las vistas es: *ir.ui.view*.
* **id**: Es un identificador único para el registro, este identificador sirve para referenciar el registro en otros elementos y documentos XML.
* **<field>**: Este tag es utilizado para almacenar un valor especifico de acuerdo al record.model contenedor.
* atributo **name**: Indica el nombre del campo en la base de datos en el cual se va a almacenar el valor
* **name**: Es el nombre con el cual se identifica la vista
* **model**: Indica el modelo al cual esta vista estará enlazado
* **type**: indica el tipo de vista
* **arch**: Indica la estructura de la vista, dentro de este tag se coloca en forma de documento XML la definición de la vista, esta puede cambiar de acuerdo al tipo de vista definido. Acontinuación se muestran algunos valores que pueden ser utilizados para este campo de acuerdo al tipo de vista

### Listado

La estructura para la creación de una vista tipo listado es como la siguiente:

    <tree string="my module data" colors="blue:state=='draft'" editable="top">
        <field name="name"/>
        <field name="description"/>
    </tree>

* **string**: El título de la vista
* **colors**: Se puede asignar un color de letra a los elementos que cumplan con una condición especifica
* **editable**: Se puede indicar que el registro sea editable en el mismo listado


### Formulario

Los formularios permiten creación y/o edición de registros, cada formulario puede ser definido utilizando los siguientes elementos básicos:

    <form string="mi_modulo mi_tabla">
        <separator string="Formulario" colspan="14"/>
        <field name="name"/>
        <label>Este es un formulario de prueba</label>
        <group string="Estado" colspan="2">
            <field name="active"/>
            <field name="state"/>
        </group>
        <notebook colspan="4">
            <page string="Detalles">
                <field name="description" colspan="4"/>
                <newline />
                <field name="quantity"/>
                <field name="price"/>
            </page>
            <page string="Fechas">
                <field name="date"/>
                <field name="datetime"/>
            </page>
        </notebook>
    </form>

* atributo **string**: Indica el label a ser utilizado en el elemento
* atributo **colspan**: Indica el número de columnas en el cual va a expandirse el elemento
* atributo **col**: Indica el número de columnas que el elemento va a contener para ubicar los elementos incluidos
* **separator**: Crea una linea separadora con un label
* **label**: Crea un label de texto
* **group**: Permite agrupar elementos y opcionalmente asignar un label
* **notebook**: Crea un contenedor de tabs
* **page**: Crea un tab dentro del *notebook*
* **newline**: Crea un salto de linea

### Grafica

Esta vista permite desplegar los datos disponibles en una grafica.

    <graph type="bar" orientation="horizontal">
        <field name="state" group="1"/>
        <field name="quantity" operator="+"/>
        <field name="price" operator="min"/>
    </graph>

* atributo **type**: Indica el tipo de gráfica a utilizarse (pie, bar), por defecto pie
* atributo **orientation**: Indica la orientación de las barras (horizontal, vertical)
* **field**: Se debe ingresar como mínimo dos campos field (eje X, eje Y, eje Z), un tercero es opcional 3
* atributo **group**: Se coloca en 1 para el campo a ser utilizado en el GROUP BY
* atributo **operator**: Indica el tipo de operador de agregación a ser utilizado (+,*,**,min,max)

