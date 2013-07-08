## Extendiendo módulos

Los módulos existentes se deben modificar a través del uso de la herencia no modificandolos directamente. Veremos como se puede hacer esta herencia a nivel de vistas y de objetos de negocios.

### Extensión de objetos de negocio

Para extender un objeto de negocio, se debe crear una clase en nuestro módulo y utilizar el mismo nombre del objeto que se desea extender **_name**, junto el atributo **_inherit** que debe tener el mismo nombre del objeto que se desea extender. En el siguiente ejemplo se extenderá el objeto *res.partner* para adicionar la relación muchos a muchos que creamos en lecciones pasadas.

    class res_partner(osv.osv):
        _name = "res.partner"
        _inherit = "res.partner"

        _columns = {
            'mi_tabla_ids': fields.many2many('mi_modulo.mi_tabla', 'mi_modulo_partner_rel', 'partner_id', 'mi_tabla_id', 'Mi Tabla'),
        }

Como se puede ver la herencia no se hace de la misma forma que la definida en Python, este tipo de herencia de clase es propia de OpenERP y su framework OpenObjects. Existen otro tipo de herencia *por prototipo* definida en el framework que puede ser revisada en [Libro de desarrollo de OpenERP](http://doc.openerp.com/v6.1/developer/03_modules_2.html#object-inheritance-inherit)

Luego de definir la clase y su relación de herencia, se pueden adicionar más campos o modificar los existentes, asi como cambiar cualquier otro atributo de la clase simplemente redefiniendolo.

### Extensión de vistas

Para extender una vista, se define la vista del objeto tal como se hace para objetos nuevos y se adiciona el atributo **inherit_id** indicando el ID de la vista a extender. Luego de esto se puede cambiar la vista adicionando etiquetas nuevas para la vista ubicandolas antes, despues o remplazando ya existentes.

    <!-- vista extendida de res.partner -->
    <record model="ir.ui.view" id="mi_modulo_res_partner_form">
        <field name="name">mi_modulo.res_partner.form</field>
            <field name="model">res.partner</field>
            <field name="type">form</field>
            <field name="inherit_id" ref="base.view_partner_form"/>
            <field name="arch" type="xml">
                <field name="name" position="before">
                    <separator string="Puesto antes del nombre" colspan="10"/>
                </field>
                <field name="name" position="after">
                        <separator string="Puesto despues del nombre" colspan="10"/>
                        <field name="comment" />
                        <newline />
                </field>
                <page string="Notes" position="replace">
                    <page string="mi tabla">
                        <field name="mi_tabla_ids" nolabel="1" />
                    </page>
                </page>
          </field>
    </record>

Más información relacionada con la herencia en las vistas puede ser encontrada en [el libro de desarrollo de OpenERP](http://doc.openerp.com/v6.1/developer/03_modules_3.html#inheritance-in-views)

    ------------
    | /!\ Nota |
    ------------

    El código de este módulo requiere que se encuentre instalado el módulo de CRM, para instalar este y otras dependencias, debe hacer la actualización del módulo manualmente. Si no lo hace aparecerá un error que indica que el Objeto *mi_modulo.mi_tabla_relacionada* no existe.

## Ejercicios propuestos

* A través del menú de OpenERP ingrese a *Ventas >> Address Book >> Clientes* seleccione uno de los registros que aparece listado y observe como se despliegan etiquetas como: *Puesto antes del nombre* y *Puesto despues del nombre*, así como la relación dget que muestra la relación de muchos a muchos *mi_tabla_ids*

* Instale un módulo nuevo en el OpenERP a su elección, escoja una de los objetos de negocio creados por el nuevo módulo y extiendalo adicionando un nuevo campo y haciendo que este nuevo campo se despliegue en la interfaz.

Para ver que objetos de negocio han sido creados puede **activar el modo de desarrollador**, solo necesita hacer click en el ícono (i) que aparece en la parte superior derecha de la interfaz (al lado izquierdo del enlace de *cerrar sesión*), se desplegará un cuadro de diálogo *acerca de*, en la parte superior derecha del cuadro de dialógo aparece el enlace *Activar modo de desarrollador* , haga click en el, la interfaz se recargará y ud podra ver que aparecen nuevos elementos en las vistas de los objetos de negocio. Cuando ud pasa el puntero del mouse sobre uno de los campos de los formularios de edición podrá observar un tooltip que indica valores como:

* Nombre del campo
* Objeto de negocio al que pertenece
* Tipo del campo
* Modificadores

Con los datos desplegados ud ya tiene la información necesaria para poder realizar la extensión del módulo, sin tener que modificar el código fuente original.
