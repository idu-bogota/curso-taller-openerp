## Estructura básica de un módulo

El módulo de Odoo tiene la siguiente estructura básica:

    └── mi_modulo
        ├── __init__.py
        ├── mi_modulo.py
        ├── mi_modulo_view.xml
        └── __openerp__.py

* **`__init__.py`**: Define el paquete python. El archivo incluye los módulos que hacen parte del paquete.

        import mi_modulo

* **`__openerp__.py`**: Define los metadatos del modulo Odoo. En la documentación de referencia de Odoo puede encontrar [mayor información de como definir un módulo](https://www.odoo.com/documentation/8.0/reference/module.html)

        {
            "name" : "mi_modulo",
            "version" : "1.0",
            "author" : "xx",
            "category" : "xx",
            "description" : "xx",
            "data" : ['mi_modulo_view.xml',],
            "installable" : True,
        }

    * **name**: Nombre del módulo en Odoo
    * **data**: Archivos xml/csv a ser cargados en el momento de la instalación/actualización del módulo, veremos más adelante archivos que pueden ser cargados (ej. datos, vistas, flujos de trabajo)
    * **depends**: Lista los módulos que deben estar instalados en el sistema previamente

* **`mi_modulo.py`**: Módulo python que contiene los objetos de negocio de nuestro módulo. Ejemplo:

        # -*- coding: utf-8 -*-
        from openerp import models, fields

        class mi_modulo_mi_tabla(models.Model):
            _name = "mi_modulo.mi_tabla"

            name = fields.Char('Nombre', size=25)
            description = fields.Char('Descripción', size=255)


* **`mi_modulo_view.xml`**: Archivo XML que contiene la definición de las vistas, acciones y menús a ser desplegados. Ejemplo:

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

## Instalación del módulo

1. Para instalar el módulo este debe estar disponible en la carpeta addons del servidor Odoo, se pueden utilizar varias carpetas addons en una instalación de Odoo, las carpetas se definen en el archivo de configuración */etc/odoo/openerp-server.conf* en el parametro *addons_path*, ejemplo:

        [options]
        db_host = False
        db_port = False
        db_user = openerp
        db_password = False
        addons_path = /usr/lib/python2.7/dist-packages/openerp/addons,/opt/mi-carpeta-de-modulos

    Igualmente se puede pasar el parametro *--addons-path=/ruta/addons* al iniciar el servidor de Odoo

1. Luego se reinicia el servidor

1. Busca el nuevo módulo creado en *Configuración > Módulos locales*, si no aparece en el listado luego de buscarlo por el nombre es porque debe registrar el nuevo módulo en la base de datos ya creada, para esto entra como administrador a la opción *Configuración -> Módulos -> Actualizar lista de módulos -> Actualizar* (Si no aparece la opción debe ingresar a *Configuración > Usuarios > Administrador* y en la pestaña de *Permisos de Acceso* activar la opción *Características técnicas* y luego recargar la página).

1. Para instalar el módulo solo debe hacer clic en instalar en el módulo.

## Ejercicio propuesto

1. Cree un nuevo proyecto PyDev en eclipse y use el código disponible en la carpeta *$RUTA_CURSO_TALLER/lecciones/01/src/*

1. Cree un nuevo perfil de ejecución de Odoo a través de  *Run > Run Configurations* que incluya el parámetro *--addons-path* y este apunte a la carpeta donde esta el código del proyecto creado en eclipse.

1. Instale el módulo en la base de datos de Odoo que creó en la lección anterior.