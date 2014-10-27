Lección 02: Objetos de Negocio
=============================

Esta lección explica la forma básica de construir objetos de negocio y definición de campos.

[TOC]

Mi primer Objeto de Negocio
---------------------------

Cada objeto de negocio contiene campos y métodos. Para crear un objeto de negocio solo es necesario crear una clase que herede de osv.osv que es la clase ORM que se encarga de gestionar el acceso y almacenamiento en la base de datos.

Estructura básica de un objeto de negocio:

    class mi_modulo_mi_objeto_de_negocio(osv.osv):
        _name = "mi_modulo.mi_objeto_de_negocio"
        _columns = {
            'nombre_campo_1' : fields.tipo_dato('etiqueta_del_campo', help='descripcion del campo'),
            'nombre_campo_2' : fields.tipo_dato('etiqueta_del_campo', help='descripcion del campo'),
        }
    mi_modulo_mi_objeto_de_negocio()

Ejemplo:

	class biblioteca_libro(osv.osv):
        _name = "biblioteca.libro"
        _columns = {
            'titulo' : fields.char('Titulo', help='Título del libro'),
            'autor' : fields.char('Autor', help='Autor del libro'),
        }
    biblioteca_libro()

En este ejemplo se crea el objeto de negocio Libro que corresponde al módulo Bibloteca, el objeto esta compuesto por dos campos *titulo* y *autor* ambos son de tipo carácter, estos campos serán almacenados automáticamente en la base de datos PostgreSQL como *character varying* en la tabla **biblioteca_libro**.

***_name*** indica que dentro de la plataforma OpenERP el objeto se llama **biblioteca.libro**.

***_columns*** es el diccionario de campos que conforman el objeto de negocio.

Definición de campos
--------------------

Los campos que conformen el objeto de negocio se deben adicionar en el diccionario llamado **_columns**:

	_columns = {
            'nombre_campo_1' : fields.tipo_dato('etiqueta_del_campo', help='descripcion del campo'),
            'nombre_campo_2' : fields.tipo_dato('etiqueta_del_campo', help='descripcion del campo'),
            'nombre_campo_3': ......
					.
                    .
                    .
             'nombre_campo_n': ......
        }

Se puede definir atributos adicionales en el campo del objeto de negocio:

* **help**: Indica el texto que se despliega como ayuda para el campo
* **select**: Crea un index en la base de datos para el campo y agrega el campo en el formulario de busqueda

###Tipos de datos

Los tipos de datos básicos como se puede definir un campo son:

* **Boolean:** *fields.boolean('etiqueta_del_campo')*
* **Integer:** *fields.integer('etiqueta_del_campo')*
* **Date:** *fields.date('etiqueta_del_campo')*
* **Datetime:** *fields.datetime('etiqueta_del_campo')*
* **char:** *fields.char('etiqueta_del_campo', size = 255)*, **size** indica el tamaño del campo de texto
* **text:** *fields.text('etiqueta_del_campo')*,
* **float:** *fields.float('etiqueta_del_campo', digits = (10,4))*, **digits** indica la precisión del numero, sin precisión se maneja como un float
* **selection:** *fields.selection([('nombre_item_1','etiqueta_item_1'),('nombre_item_2','etiqueta_item_2'),('nombre_item_3','etiqueta_item_3')], 'etiqueta_del_campo')*
* binary: *fields.binary('etiqueta_del_campo', filters = '*.png')*

### Tips

Los campos de tipo de dato Boolean, se define como etiqueta_del_campo **active**, el cual tiene un significado especial en la plataforma, por defecto la interfaz de listado oculta los registros que tengan el campo active en *False*.

Desplegar objetos de negocio desde interfaz
------------------------

Para desplegar los campos de los objetos de negocio se deben adicionar en las vistas definidas para los objetos, solo es necesario indicar el nombre del campo a desplegar y el sistema se encarga de desplegar el elemento gráfico acorde al tipo de dato.

Ejercicio propuesto
-------------------

Tomando el código fuente disponible en la lección:

1. Cambie el label de los diferentes campos y vea como se actualiza la interfaz
1. Adicione nuevos estados al campo de tipo selección
1. Convierta a requeridos los campos *date* y *description* y verifique en la interfaz el cambio
1. Adicione un texto de ayuda para cada uno de los campos y verifique en la interfaz que se despliega
1. Cree un nuevo objeto de negocio llamado *mi_modulo.mi_propia_tabla* y adicione como mínimo 3 campos en la clase. Ahora a través de la interfaz web de administración del OpenERP (cambiar la vista a extendida en las preferencias del usuario) ingrese a *Configuración >> Personalización >> Elementos del Menú >> Crear*, diligencie el formulario con los siguientes campos mínimos y guarde:

        * Menú: Agregue el nombre del enlace en el menu a desplegar
        * Menú padre: puede escoger un menu existente para adicionar un elemento de menú nuevo o dejarlo en blanco para que se cree un menú en la barra principal de navegación
        * Acción: ir.acciones.acc_ventana. En el combobox de selección que aparece a continuación haga click en crear y diligencie los siguientes campos y guarde:

            * Nombre de acción: Un nombre cualquiera para la acción, ej. listado de mi_modulo.mi_propia_tabla
            * Objeto: coloque el nombre del nuevo objeto de negocio: mi_modulo.mi_propia_tabla

    Recargue la página y el nuevo item del menú debe aparecer disponible desplegando un enlace a la vista de su objeto de negocio donde podrá listar, crear, modificar y consultar registros.

    Aquí se ve como OpenERP permite la personalización a través de desarrollo del módulo o a través de la interfaz de administración.
