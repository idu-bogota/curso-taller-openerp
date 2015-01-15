Lección 01: Estructura de un módulo Odoo
========================================

Directorios y archivos básicos
------------------------------

El módulo de Odoo tiene la siguiente estructura básica:

    └── mi_modulo
        ├── __init__.py
        ├── mi_modulo.py
        ├── mi_modulo_view.xml
        └── __openerp__.py

- **`__init__.py`**: Define el paquete python. El archivo incluye los módulos que hacen parte del paquete.

        import mi_modulo

- **`__openerp__.py`**: Define los metadatos del modulo Odoo. En la documentación de referencia de Odoo puede encontrar [mayor información de como definir un módulo](https://www.odoo.com/documentation/8.0/reference/module.html)

        {
            "name" : "mi_modulo",
            "version" : "1.0",
            "author" : "xx",
            "category" : "xx",
            "description" : "xx",
            "depends" : ['base',],
            "data" : ['mi_modulo_view.xml','mi_modulo_datos.xml',],
            "demo" : ['mi_modulo_demo.xml',],
            "installable" : True,
        }

    - **name**: Nombre del módulo en Odoo
    - **data**: Archivos xml/csv a ser cargados en el momento de la instalación/actualización del módulo, de esta forma se puede cargar datos iniciales, configuración de vistas, flujos de trabajo, configuración de seguridad.
    - **demo**: Archivos xml/csv a ser cargados en el momento de la instalación del módulo pero cuando la base de datos se creó con la opción de cargar datos de ejemplo.
    - **depends**: Lista los módulos que deben estar instalados en el sistema como requisito para instalar este módulo.

- **`mi_modulo.py`**: Módulo python que contiene los objetos de negocio de nuestro módulo. Ejemplo:

        # -*- coding: utf-8 -*-
        from openerp import models, fields

        class mi_modulo_mi_tabla(models.Model):
            _name = "mi_modulo.mi_tabla"

            name = fields.Char('Nombre', size=25)
            description = fields.Char('Descripción', size=255)


- **`mi_modulo_view.xml`**: Archivo XML que contiene la definición de las vistas, acciones y menús a ser desplegados. Ejemplo:

        <?xml version="1.0"?>
        <openerp>
        <data>
            <record model="ir.ui.view" id="mi_tabla_form">
                <field name="model">mi_modulo.mi_tabla</field>
                <field name="arch" type="xml">
                    <form>
                        <group>
                         <field name="name"/>
                         <field name="description"/>
                        </group>
                    </form>
              </field>
            </record>
            <record model="ir.ui.view" id="mi_tabla_tree">
                <field name="model">mi_modulo.mi_tabla</field>
                <field name="arch" type="xml">
                    <tree>
                        <field name="name"/>
                        <field name="description"/>
                    </tree>
                </field>
            </record>
            <record model="ir.actions.act_window" id="mi_tabla_action">
                <field name="name">Tabla</field>
                <field name="res_model">mi_modulo.mi_tabla</field>
                <field name="view_mode">tree,form</field>
            </record>
            <menuitem id="menu_root" name="Mi Módulo"/>
            <menuitem id="menu_mi_modulo" name="Mi Módulo" parent="menu_root"/>
            <menuitem id="menu_mi_modulo_mi_tabla" parent="menu_mi_modulo" name="Mi Tabla" action="mi_tabla_action"/>
        </data>
        </openerp>

La estructura y nombre de archivos puede ajustarse de acuerdo a las preferencias del desarrollador, lo importante es ajustar las referencias a los archivos a cargarse en el momento de la instalación en el archivo __openerp__.py, por ejemplo:

    mi-carpeta-de-modulos
    ├── nombre_modulo
    │   ├── __init__.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   └── nombre_modulo.py
    │   ├── __openerp__.py
    │   └── views
    │       └── nombre_modulo.xml
    ├── otro_modulo
    │   ├── __init__.py
    │   ├── models.py
    │   ├── __openerp__.py
    │   └── views.xml
    └── mi_modulo
        ├── __init__.py
        ├── __openerp__.py
        ├── mi_modulo.py
        └── mi_modulo_view.xml


Carga de datos con archivos XML
--------------------------------

Como se ve en el sección anterior un archivo XML se puede usar para cargar datos al Odoo en el momento de instalar o actualizar un módulo, por cada registro que se desea cargar en la base de datos se debe utilizar las etiquetas **record** y **field**.

    <?xml version="1.0"?>
    <openerp>
    <data>
        <record model="res.users" id="mi_usuario">
            <field name="name">Usuario creado</field>
            <field name="login">username</field>
        </record>
        <record model="mi_modulo.mi_tabla" id="dato_1">
            <field name="name">dato 1</field>
            <field name="description">Esto es un dato que se carga al instalar el módulo</field>
            <field name="usuario_id" ref="mi_usuario"/>
        </record>
    </data>
    </openerp>

- **`<record>`**: Tag utilizado para insertar registros en la base de datos asociados a un Modelo que se indica en el atributo model, este tag no es solo utilizado para definición de vistas, sino para cualquier dato que se quiera almacenar en Odoo a través de XML.

    - Atributo **`model`**: Indica en que Modelo se va a crear el nuevo registro de datos, para el caso de las vistas todo se almacena en: *ir.ui.view*.
    - Atributo **`id`**: Es un identificador único para el registro, este identificador sirve para referenciar el registro en otros elementos y documentos XML en este y otros módulos.

- **`<field>`**: Este tag es utilizado para almacenar un valor en un campo especifico del Modelo.
    - atributo **`name`**: Indica el nombre del campo en la base de datos en el cual se va a almacenar el valor
    - atributo **`ref`**: Se indica el ID utilizado en otro registro en este archivo XML o en alguno creado en otro módulo. Para otro módulo o archivo XML debe indicarse el id incluyendo el nombre del módulo ej. `otro_modulo.id_del_objeto`

[Mayor información acerca de como cargar datos en Odoo](https://www.odoo.com/documentation/8.0/reference/data.html)

Instalación del módulo
----------------------

1. Para instalar el módulo este debe estar disponible en la carpeta addons del servidor Odoo, se pueden utilizar varias carpetas addons en una instalación de Odoo, las carpetas se definen en el archivo de configuración */etc/odoo/openerp-server.conf* en el parametro *addons_path*, ejemplo:

        [options]
        db_host = False
        db_port = False
        db_user = openerp
        db_password = False
        addons_path = /usr/lib/python2.7/dist-packages/openerp/addons,/opt/mi-carpeta-de-modulos

    Igualmente se puede pasar el parametro `--addons-path=/ruta/addons` al iniciar el servidor de Odoo

1. Luego se reinicia el servidor

1. Buscar el nuevo módulo creado en *Configuración > Módulos locales*, si no aparece en el listado luego de buscarlo por el nombre es porque debe registrar el nuevo módulo en la base de datos ya creada, para esto entra como administrador a la opción *Configuración -> Módulos -> Actualizar lista de módulos -> Actualizar* (Si no aparece la opción debe ingresar a *Configuración > Usuarios > Administrador* y en la pestaña de *Permisos de Acceso* activar la opción *Características técnicas* y luego recargar la página).

1. Para instalar el módulo solo debe hacer clic en instalar en el módulo.

Actualizar un módulo
--------------------

- Cuando se realizan **cambios en los archivos Python** es necesario reiniciar el servidor de Odoo para que los cambios sean tomados, para esto debe detener el proceso que se esta ejecutando o de lo contratio obtendrá un mensaje **error: [Errno 98] Address already in use** en la consola de eclipse como se ve a continuación:

        Exception in thread openerp.service.httpd:
        Traceback (most recent call last):
          File "/usr/lib/python2.7/threading.py", line 810, in __bootstrap_inner
            self.run()
          [ ... mas mensajes removidos para facilitar la lectura ... ]
          File "/usr/lib/python2.7/socket.py", line 224, in meth
            return getattr(self._sock,name)(*args)
        error: [Errno 98] Address already in use

    Si hay cambios en archivos XML estos no se van a aplicar con solo reiniciar el servidor.

- Cuando los **cambios son solo en archivos XML** se puede hacer la actualización a través de la interfaz web de administración del Odoo. Para esto debe:

  1. Ingresar a *Configuración > Módulos locales*
  1. Buscar el módulo a actualizar por el nombre
  1. Hacer click en el botón **Actualizar**

- Cuando se esta desarrollado se requiere constantemente actualizar los módulos sobre los que se trabaja, para esto se puede adicionar como parámetro de inicio del servidor Odoo el argumento `--update=nombre_modulo` o `-u nombre_modulo`. En eclipse adicionar este argumento en el Run Configuration que este utilizando. Esto ejecutará la atualización automática del módulo cada vez que reinicia el Odoo server, evitando hacer la actualización a través de la interfaz web como se mostró en el paso anterior.

Ejercicio propuesto
-------------------

1. Cree un nuevo proyecto PyDev en eclipse y use el código disponible en la carpeta *$RUTA_CURSO_TALLER/lecciones/01/src/*

1. Cree un nuevo perfil de ejecución de Odoo a través de  *Run > Run Configurations* que incluya el parámetro *--addons-path* y este apunte a la carpeta donde esta el código del proyecto creado en eclipse.

1. Instale el módulo en la base de datos de Odoo que creó en la lección anterior.

1. Examine como se adicionan y editan registros a través del menu *Mi Módulo > Mi Tabla*

1. Abra el archivo **mi_modulo_datos.xml** y adicione un nuevo registro. Debe actualizar el módulo luego de cambiar el archivo XML.

1. Modifique el archivo **mi_modulo_datos.xml** y adicioné un nuevo registro, actualice el módulo para ver el nuevo registro creado.