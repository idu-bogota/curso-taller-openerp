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

Ejemplo:

	class biblioteca_libro(osv.osv):
        _name = "biblioteca.libro"
        _columns = {
            'active': fields.boolean('Active', help='Activo/Inactivo'),
            'isbn': fields.char('ISBN', size = 255),
            'titulo' : fields.char('Titulo', size = 255, help='Título del libro'),
            'autor' : fields.char('Autor', size = 255, help='Autor del libro'),
            'descripcion': fields.text('descripcion'),
            'paginas': fields.integer('Paginas'),
            'fecha': fields.date('Fecha', help='Fecha de publicación'),
            'precio': fields.float('Precio', help='Precio de compra'),
            'state': fields.selection([('draft', 'Draft'),('open', 'In Progress'),('cancel', 'Cancelled'),('done', 'Done'),('pending', 'Pending')],'State'),
        }
	biblioteca_libro()

### Tips

Los campos de tipo de dato Boolean, se define como etiqueta_del_campo **active**, el cual tiene un significado especial en la plataforma, por defecto la interfaz de listado oculta los registros que tengan el campo active en *False*.

Desplegar objetos de negocio desde interfaz
------------------------

Para visualizar nuestro objeto de negocio desde la interfaz, lo primero es verificar que el módulo se encuentre instalado, para el ejemplo el módulo Biblioteca.

Para crear un menú de acceso al objeto de negocio, debe ingresar por el menú:

*Técnico --> Estructura de la base de datos --> Modelos*

En Modelos, buscar modelo para Biblioteca, seleccionar el modelo biblioteca.libro, en este último click sobre el botón Crear un menú:

* Nombre del menú: **Libro**
* Menú padre: **Configuración/Configuración**

El menú padre **Configuración/Configuración** es uno ya existente en la plataforma.

Después de crear el menú, usted debe actualizar la platoforma y se activa el Menú padre Configuración y el submenú Libro.

En el menú Libro, se crea por defecto dos tipos de vista, vista lista y vista formulario.


Ejercicio propuesto
-------------------

Tomando el código fuente disponible en la lección:

1. Adicionar nuevos estados al campo de tipo selección
1. Adicionar un texto de ayuda para cada uno de los campos que no lo tenga y verifique en la interfaz que se despliega
1. Adicionar los campos clasificacion, genero y editorial, tipo de campo char.
1. Crear un nuevo objeto de negocio llamado *biblioteca.libro_prestamo* y adicione los campos fecha_prestamo tipo date, duración_prestamo tipo integer, fecha_regreso tipo date.
1. Crear un menú acceso al objeto *biblioteca.libro_prestamo* que tenga como menú padre **Configuración/Configuración**. Recargue la página y el nuevo item del menú debe aparecer disponible desplegando un enlace a la vista de su objeto de negocio donde podrá listar, crear, modificar y consultar registros.