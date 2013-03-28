from osv import fields, osv

class mi_modulo_mi_tabla(osv.osv):
    _name = "mi_modulo.mi_tabla"
    _columns = {
        'name' : fields.char('name',size=255),
        'description' : fields.char('description',size=255),
    }
mi_modulo_mi_tabla()