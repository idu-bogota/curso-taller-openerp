## Objetos de Negocio

En esta lección veremos la forma básica de crear objetos de negocio, en lecciones posteriores se verán otras opciones disponibles.

Cada objeto de negocio contiene campos y métodos. Para crear un objeto de negocio solo es necesario crear una clase que herede de osv.osv que es la clase ORM que se encarga de gestionar el acceso y almacenamiento en la base de datos.

    class mi_modulo_mi_tabla(osv.osv):
        _name = "mi_modulo.mi_tabla"
        _columns = {
            'name' : fields.char('name',size=255),
            'description' : fields.char('description',size=255),
        }
    mi_modulo_mi_tabla()

En el ejemplo anterior se crea el objeto de negocio con dos campos *name* y *description* ambos son de tipo carácter y de tamaño 255, estos campos serán almacenados automáticamente en la base de datos PostgreSQL como varchar(255) en la tabla mi_modulo_mi_tabla.

El campo *_name* indica que dentro de la plataforma OpenERP el objeto se llama *mi_modulo.mi_tabla*, este nombre será usado en varias partes a lo largo del desarrollo de módulos.

## Definición de campos

Para adicionar un campo en un objeto de negocio solo necesita adicionarlo en el diccionario llamado **_columns** en la definición de la clase de la siguiente manera:

    _columns = {
        'nombre_campo' : fields.tipo_campo('label del campo en la interfaz', otros_atributos ...),
        ...,
        ...,
    }

La definición de un campo puede tener estos atributos adicionales:

* **required**: Indica si el campo es obligatorio o no
* **readonly**: Indica si el campo es editable
* **help**: Indica el texto que se despliega como ayuda
* **select**: Crea un index en la base de datos para el campo y agrega el campo en el formulario de busqueda

## Tipos de datos

Los tipos básicos de atributos disponibles para ser utilizados son:

* Boolean: *fields.boolean('activo')*
* Integer: *fields.integer('cantidad')*
* Date: *fields.date('fecha')*
* Datetime: *fields.datetime('fecha y hora')*
* char: *fields.char('nombre', size = 255)*, **size** indica el tamaño del campo de texto
* text: *fields.text('descripcion')*,
* float: *fields.float('precio', digits = (10,4))*, **digits** indica la precisión del numero, sin precisión se maneja como un float
* selection: *fields.selection([('o1','opcion uno'),('o2','opcion dos')], 'opciones')*
* binary: *fields.binary('foto', filters = '*.png')*

## Despliegue de los campos

Para desplegar los campos de los objetos de negocio se deben adicionar en las vistas definidas para los objetos, solo es necesario indicar el nombre del campo a desplegar y el sistema se encarga de desplegar el elemento gráfico acorde al tipo de dato.

## Tip

El campo *active* tiene un significado especial en la plataforma por defecto la interfaz de listado oculta los registros que tengan el campo active en *False*
