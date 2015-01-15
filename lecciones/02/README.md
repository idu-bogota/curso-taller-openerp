Lección 02: Modelos Odoo
========================

Esta lección explica la forma básica de construir Modelos Odoo y definir sus campos.

[TOC]

Mi primer Modelo Odoo
---------------------

Cada Modelo contiene campos y métodos. Para crear un modelo solo es necesario crear una clase python que herede de **models.Model**, models.Model es la clase base que se encarga de servir como [ORM - Object Relational Mapping](http://es.wikipedia.org/wiki/Mapeo_objeto-relacional) y gestiona el acceso y almacenamiento de datos en PostgreSQL.

Estructura básica de un objeto de negocio:

```python
class mi_modulo_mi_objeto_de_negocio(osv.osv):
    _name = 'mi_modulo.mi_objeto_de_negocio'
    _description = 'descripción del objeto de negocio'

    nombre_campo_1 = fields.tipo_dato(parametros),
    nombre_campo_2 = fields.tipo_dato(parametros),
```

Ejemplo:

```python
class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Contiene la información de libros'

    name = fields.Char('Titulo', size=255, help='Título del libro')
    active = fields.Boolean('Active', help='Activo/Inactivo')
```

En este ejemplo se crea el objeto de negocio Libro que corresponde al módulo Bibloteca, el objeto esta compuesto por dos campos *name* y *active*, esta definición va a crear una tabla **biblioteca_libro** en la base de datos PostgreSQL para almacenar todos los registros de este objeto de negocio.

- **_name** indica el nombre con el cual se va a hacer referencia a este objeto de negocio la plataforma OpenERP el objeto se llama **biblioteca.libro**.

- **_description** contiene la descripción del Modelo como forma de documentar el mismo. No usar Tíldes o carácteres especiales en esta sección.

Definición de campos
--------------------

Los campos que hace parte del Modelo se definen como atributos de la clase python y son instancias del módulo python **fields.Field**. Al crear un campo en el Modelo puede definir los siguientes atributos básicos:

* **string:** Etiqueta/label que se despliega en la interfaz de usuario
* **help:** Ayuda que se despliega en la interfaz como un tooltip
* **readonly:** Indica que el campo es de solo lectura, por defecto *False*
* **required:** Indica que el campo es obligatorio, por defecto *False*
* **index:** Crea un [indice en la base de datos](http://es.wikipedia.org/wiki/%C3%8Dndice_%28base_de_datos%29), por defecto *False*

Puede consultar [mayor información acerca de los campos que se pueden crear en Odoo](https://www.odoo.com/documentation/8.0/reference/orm.html#fields) en la documentación de referencia del sitio de Odoo.

### Tipos de datos

Odoo permite crear diferentes tipos de campos en un Modelo, los básicos son:

- fields.Char(string=None, otros_parametros)
- fields.Boolean(string=None, otros_parametros)
- fields.Integer(string=None, otros_parametros)
- fields.Float(string=None, digits=None, otros_parametros)
- fields.Text(string=None, otros_parametros)
- fields.Selection(selection=None, string=None, otros_parametros)
- fields.Html(string=None, otros_parametros)
- fields.Date(string=None, otros_parametros)
- fields.Datetime(string=None, otros_parametros)

Ejemplo:


```python
class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Contiene la información de libros'

    name = fields.Char('Titulo', size=255, help='Título del libro')
    active = fields.Boolean('Active', help='Activo/Inactivo')
    descripcion = fields.Text('Descripción')
    fecha_publicacion = fields.Date('Fecha', help='Fecha de publicación')
    precio = fields.Float('Precio', help='Precio de compra', digits=(10,2))
    state = fields.Selection(
        [
            ('solicitud', 'Solicitado'),
            ('en_compra', 'Proceso de compra'),
            ('adquirido', 'Adquirido'),
            ('catalogado', 'Catalogado'),
            ('baja', 'De baja')
        ],
        'Estado',
    )
```

### Tip

El campo llamado **active** tiene un significado especial en la plataforma, por defecto la interfaz que lista los registros del Modelo no muestra los registros que tengan el valor de active igual a *False*.

Desplegar Modelos en la interfaz
--------------------------------

1. Para visualizar un Modelo en la interfaz web, lo primero que se requiere es instalar el módulo donde esta el código del Modelo (o actualizar si el módulo ya estaba instalado y tiene cambios en el código), siguiendo las instrucciones de la lección anterior y usando el código de ejemplo de la lección.

1. Luego se requiere crear una entrada de menú (menu item) que permita acceder al Modelo, para esto debe

    1. Ingresar a *Técnico >> Estructura de la base de datos >> Modelos*, en esta página se despliega un listado de todos los Modelos instalados en Odoo.
    1. Buscar y seleccionar el Modelo **biblioteca.libro**, en la página del Modelo se despliega la metadata que almacena Odoo acerca del Modelo creado a través del código python
    1. Al final de la página aparece un botón llamado **Crear un menú**, hacer clic en él y llenar el formulario con los siguientes datos:
       - Nombre del menú: **Libro**
       - Menú padre: **Configuración/Configuración**

    El menú padre **Configuración/Configuración** es uno ya existente en la plataforma, se puede usar uno cualquiera de los que existe o crear uno nuevo.

    1. Recargar la página, luego de esto podrá observar que se despliega el submenú *Configuración* y el menú item *Libro*. Al hacer click en él se despliega el listado de libros y el botón para crear un nuevo registro. Estas vistas son autogeneradas, más adelante en el taller se indica como construir las vistas con código XML.


Ejercicio propuesto
-------------------

Tomando como base el código fuente disponible en la lección:

1. Revisar la metadata que almacena Odoo para los Modelos y Campos de los módulos instalados.
1. Explore la base de datos PostgreSQL utilizando el programa *pgadmin3*, busque y revise la tabla *biblioteca_libro*, hacer una captura de pantalla para tenerlo como referencia y poder comparar la tabla luego de realizar los cambios de los siguientes ejercicios de esta lección.
1. Adicionar nuevos estados al campo de tipo selección *state*: solicitado, proceso de compra, adquirido.
1. Adicionar un texto de ayuda para cada uno de los campos que no lo tenga y verifique en la interfaz que se despliega.
1. Adicionar los campos:

   - isbn tipo char tamaño 13
   - paginas tipo integer
   - fecha_compra tipo date
   - nombre_autor tipo char tamaño 255

1. Crear un nuevo Modelo llamado **biblioteca.libro_prestamo** y adicione los campos:

   -  fecha_prestamo tipo datetime
   -  duracion_prestamo tipo integer
   -  fecha_devolucion tipo datetime.

1. Crear un menú de acceso al objeto **biblioteca.libro_prestamo** que tenga como menú padre **Configuración/Configuración**.
1. Adicione, modifique y elimine registros para el Modelo **biblioteca.libro**, revise que pasa cuando el campo active esta en True o en False.
1. Explore la base de datos utilizando el programa *pgadmin3*, busque y revise como ha cambiado la tabla *biblioteca_libro* luego de los cambios realizados en el módulo.
