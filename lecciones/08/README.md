## Creación de Reportes en PDF

La creación de reportes en formato PDF es una utilidad bastante útil para tener una vista de impresión de los objetos de negocio, los pasos para crear un reporte en PDF son:

1. Instalar el módulo  base_report_designer
1. Crear el template del reporte en OpenOffice
1. Convertir el documento OpenOffice en un archivo RML (Report Markup Language)
1. Crear la clase python que se va a encargar de generar el reporte
1. Crear archivo XML para registrar el reporte en la base de datos

### Instalar el módulo base_report_designer

Para instalar el módulo debe ingresar como administrador en la opción *Configuración -> módulos*, luego activa la opción *extra* y coloca el nombre *base_report_designer* y presiona enter, luego hace click en el botón *instalar*, la interfaz se recargará y se desplegará una ventana con información del módulo, incluido la opción de descargar un plugin para OpenOffice.

### Crear el template del reporte en OpenOffice

Puede crear un documento en OpenOffice Writer con el formato que ud desee. Para indicar en donde debe colocarse los datos que vienen de la base de datos ud debe adicionar unas etiquetas especiales como en el ejemplo siguiente:

    [[ repeatIn(objects,'o') ]]

    Datos básicos
    Nombre: [[ o.name ]]
    Activo: [[ o.active ]]
    Estado: [[ o.state ]]

    Tabla Relacionada
    Nombre: [[ o.tabla_relacionada_id.name ]]
    Activa: [[ o.tabla_relacionada_id.active ]]
    Estado: [[ o.tabla_relacionada_id.state ]]

* **[[ repeatIn(objects,'o') ]]**: Esta linea indica que va a iniciar el loop para generar la impresión de los objetos seleccionados, cada objeto seleccionado a ser impreso va a ser llamado 'o', ud puede cambiarlo por el nombre que le convenga.

* **[[ o.field_name ]]**: Aquí se indica que va a obtener el valor del campo *'field_name'* del objeto *'o'*

Al finalizar guarde el documento en formato .odt

Alternativamente puede instalar el plugin que descargo al instalar el módulo base_report_designer y este adicionará un menú que le asistirá en la creación del reporte.

### Convertir el documento OpenOffice en un archivo RML

Luego procedemos a convertir el documento ODT en formato RML que va a ser el que finalmente OpenERP va a procesar, para esto ejecutamos el siguiente comando:

    cd ~/workspace/leccion08/mi_modulo/report/ #ingrese al directorio donde ud tenga almacenado el código del módulo del curso
    python *<directorio_addons>*/base_report_designer/openerp_sxw2rml/openerp_sxw2rml.py mi_reporte.odt > mi_reporte.rml

* El **directorio_addons** en una instalación normal utilizando el archivo .deb es: `/usr/share/pyshared/openerp/addons/`
* **openerp_sxw2rml.py** es el script que convierte el documento .odt en .rml

### Crear la clase python que se va a encargar de generar el reporte

Dentro de la carpeta del módulo se crea un paquete llamado *report*, (esto es opcional, es solo una forma de mantener organizado el código fuente utilizando paquetes de python). Dentro de este paquete crea un módulo para el reporte y una clase como la siguiente:

    from report import report_sxw

    class mi_reporte(report_sxw.rml_parse):
        def __init__(self, cr, uid, name, context=None):
            super(mi_reporte, self).__init__(cr, uid, name, context=context)

    report_sxw.report_sxw('report.mi_modulo.mi_reporte', 'mi_modulo.mi_tabla', 'addons/mi_modulo/report/mi_reporte.rml', parser=mi_reporte, header=True)

* Nuestra clase del reporte hereda de **report_sxw.rml_parse** y luego definimos el constructor heredando de la clase padre, esta clase puede tener código adicional para poder darle mayor lógica a la generación del reporte en caso de ser necesaria

* Luego instanciamos el objeto del reporte y pasamos los siguientes parámetros
  * **report.mi_modulo.mi_reporte**: El nombre en el sistema del reporte
  * **mi_modulo.mi_tabla**: El nombre del objeto de negocio de donde vamos a consultar los datos
  * **addons/mi_modulo/report/mi_reporte.rml**: Ruta relativa del archivo RML
  * **parser**: Es el nombre de la clase python que va a realizar el parser del documento RML
  * **header**: Indica si se va o no a adicionar la cabecera que esta configurada para los reportes dentro de la base de datos

### Crear archivo XML para registrar el reporte en la base de datos

Se genera un archivo xml con el siguiente contenido:

    <?xml version="1.0" encoding="utf-8"?>
    <openerp>
        <data>
            <report auto="False" id="mi_modulo_report_mi_reporte" model="mi_modulo.mi_tabla" name="mi_modulo.mi_reporte" rml="mi_modulo/report/mi_reporte.rml" string="Generar Reporte en PDF" />
        </data>
    </openerp>

Los parametros son auto explicativos, el valor de string es el nombre del enlace que va a aparecer en el menu de la derecha en la vista formulario de un objeto y en la vista de listado para generar el reporte (aparece luego de seleccionar uno o más objetos).

El archivo debe ser referenciado en __openerp__.py para ser cargado en la actualización del módulo

    {
        "name" : "mi_modulo",
        "version" : "7.0",
        "author" : "xx",
        "category" : "xx",
        "description" : "xx",
        "init_xml" : [],
        "depends" : ['base','crm'],
        "update_xml" : [
            'mi_modulo_view.xml',
            'mi_modulo_reports.xml'
        ],
        "active" : False,
        "installable" : True,
    }

## Ejercicios propuestos

1. Ingrese a la vista de listado del objeto *mi_modulo.mi_tabla*, seleccione uno o varios de los registros que se despliegan haciendo click en el checkbox junto a cada registro, al hacer esto se va a desplegar un menú en la parte derecha de la interfaz, haga click en la opción 'Generar Reporte en PDF' y vea el reporte generado para los objetos seleccionados. Abra el archivo *mi_modulo/report/mi_reporte.rml* y modifiquelo para que se despliegue el campo *price*, ejecute nuevamente el reporte para ver el cambio realizado.

2. Ahora utilizando LibreOffice abra el archivo *mi_modulo/report/mi_reporte.odt* y modifiquelo para que se despliegue el campo *quantity*, utilice el comando *openerp_sxw2rml.py* para crear nuevamente el archivo .rml con el nuevo cambio, sobreescriba el archivo existente *mi_modulo/report/mi_reporte.rml* y ejecute nuevamente el reporte para ver el cambio realizado.

3. Ahora utilizando LibreOffice haga cambios de estilo en el reporte, adicione una imagen, utilice una tabla para presentar los datos, etc, actualice el .rml y ejecute nuevamente el reporte para ver los cambios.

