Instalación del ambiente para el curso
--------------------------------------

*   Descargar ubuntu 14.04 LTS http://www.ubuntu.com/download

*   Luego de instalado y reiniciado el sistema actualizar a los últimos paquetes disponibles

        sudo apt-get update
        sudo apt-get upgrade

*   Instalar el software que necesitaremos para el taller

        sudo apt-get install eclipse pgadmin3

Instalar Odoo 8.0
--------------------

*   Descargue la última versión para Linux, desde la línea de comandos ejecutar:

        sudo su
        wget -O - https://nightly.odoo.com/odoo.key | apt-key add -
        echo "deb http://nightly.odoo.com/8.0/nightly/deb/ ./" >> /etc/apt/sources.list
        apt-get update
        apt-get install odoo
        apt-get install -f

*   Para no generar conflictos entre la versión que se corre a través de eclipse y la existente en el sistema, debe desactivar el inicio del servicio Odoo con el comando

        sudo update-rc.d odoo disable
        sudo /etc/init.d/odoo stop

*   Configurar el usuario de base de datos `odoo` con clave `odoo`

        sudo su postgres
        createuser -d -S -R odoo
        psql -c "ALTER USER odoo WITH PASSWORD 'odoo';"

## Configuración de Eclipse como ambiente de desarrollo

*   Instalar el módulo PyDEV para desarrollo en Python
    * Ingresar a la opción del menú **Help > Install New Software**
    * En el cuadro de dialogo diligenciar **Work with:** con el valor http://pydev.org/updates y presionar la tecla **enter**
    * Desactivar el campo **Show only the latest versions of available software** para que muestre todas las versiones disponibles
    * Seleccionar para instalar la **versión 3.5.xxxxxx**, con versiones más actualizadas no se puede hacer debug de Odoo.
    * Continue con el proceso de instalación del plugin

*   Instalar el módulo Web Tools para incluir editor para archivos XML
    * Ingresar a la opción del menú **Help > Install New Software**
    * En el cuadro de dialogo diligenciar **Work with:** con el valor http://download.eclipse.org/webtools/repository/indigo y presionar la tecla **enter**
    * Seleccionar en la lista que aparece seleccione para instalar **Eclipse XML Editors and Tools**, se ha probado con la versión 3.3.2, pero cualquier versión reciente debe funcionar.
    * Continue con el proceso de instalación del plugin

## Crear un proyecto y configurar el entorno para ejecutar Odoo

-   En eclipse crear un nuevo proyecto PyDEV, si no se encuentra configurado el entorno de python eclipse le preguntará si desea auto configurarlo, ud debe hacer click en el botón **auto config** y aceptar los valores por defecto.
-   Ingrese a través del menú a la opción **Run > Run configurations**
-   Haga click en el icono (parte superior izquierda) **New Launch Configuration**
    -   En **Name** digite **servidor Odoo**
    -   En **Project** seleccione el nombre del nuevo proyecto
    -   En **Main Module** digite **/usr/bin/openerp-server**, este es el comando para iniciar el openerp
    -   En la pestaña **Arguments** en el campo **program arguments** ingrese:

            -r odoo -w odoo --db_host=localhost

        Estos son los parámetros que se pasarán al servidor de Odoo

        - -r es el nombre del usuario para conectarse a PostgreSQL
        - -w la clave asignada para conectarse a PostgreSQL

    -   Luego haga click en el boton **Apply** y **Run**
    -   Otro parámetro importante para el resto del curso es **`--addons-path`** el cual indica al servidor donde buscar el código de módulos adicionales de Odoo, podemos indicar que use la carpeta del proyecto eclipse con la variable **`${project_loc:NombreDeMiProyecto}`**, quedando el parámetro:

            -r openerp -w openerp --db_host=localhost --addons-path=${project_loc:NombreDeMiProyecto}

        **Nota**: :white_up_pointing_index: Recuerde cambiar **NombreDeMiProyecto** por el nombre del proyecto que usted acaba de crear
        
        Si uds adiciona este campo en este momento, al arrancar el servidor fallará indicando que la carpeta no es válida como addons-path, esto es porque aún no existen modulos Odoo en el proyecto.
        
            openerp-server: error: option --addons-path: The addons-path '/home/usuario/workspace/lecciones_odoo' does not seem to a be a valid Addons Directory!

        También puede ejecutar el servidor llamando un código disponible fuera de eclipse, por ejemplo:
        
            -r openerp -w openerp --db_host=localhost --addons-path=/directorio/otros/modulos
            
        Si ud indica un directorio que no existe el error que desplegará será:
        
            openerp-server: error: option --addons-path: The addons-path '/home/carpeta_vacia' does not seem to a be a valid Addons Directory!

        :happy_person_raising_one_hand: Uds puede utilizar el --addons-path para indicar donde se encuentra el código de la lección que este estudiando, ejemplo.
        
            -r openerp -w openerp --db_host=localhost --addons-path=/home/usuario/curso-taller-openerp/lecciones/01/src
        
        [Mayor información acerca de los parámetros de arranque del servidor Odoo](https://www.odoo.com/documentation/8.0/reference/cmdline.html#running-the-server)

*   Abrir en el navegador: http://localhost:8069 y accederá a la interfaz de Odoo
*   Ahora puede crear una base de datos haciendo click en **Manage Databases**
     * Master Password: es el password de super administrador de Odoo por defecto *admin*
     * New Database Name: Indique el nombre de la nueva base de datos a crear
     * Load Demonstration data: Indica si quiere que los módulos se instalen con datos de prueba
     * Default language: Indica el lenguaje a instalar por defecto
     * Admin password: Indica el password de administración de la nueva base de datos
*   El proceso de creación tomará algunos segundos, luego se presentará la pantalla con el listado de módulos disponibles en el sistema, puede elegir uno cualquiera ejemplo CRM

## Continuar con las lecciones del curso

Ya con esto esta listo Odoo y eclipse para continuar con el resto de las lecciones, El objetivo es ir creando nuestro módulo del taller en eclipse a medida que vamos avanzando de lección, cada lección tiene un archivo **README** que contiene la teoria de la lección y una carpeta **src** donde puede esta el código de ejemplo para lección, este código lo puede copiar y pegar en su proyecto de eclipse a medida que avanza en las lecciones. 

Al final de cada lección existe un ejercicio propuesto el cual le ayudará a afianzar lo visto en la lección.

## Ejercicio Propuesto

Explore la instalación de Odoo que realizó en las secciones anteriores y familiarícese con la interfaz y los diferentes elementos de la misma (menús, formularios, busquedas, listados, etc)
