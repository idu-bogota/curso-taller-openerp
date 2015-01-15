{
    "name" : "mi_modulo",
    "version" : "1.0",
    "author" : "xx",
    "category" : "xx",
    "summary" : "módulo de la lección 1",
    "depends" : ['base',],
    "data" : [
        'mi_modulo_view.xml',
        'mi_modulo_datos.xml',
    ],
    "demo": [
        'mi_modulo_demo.xml',
    ],
    "installable" : True,
    "description" : """
Módulo lección 01
=================

Este módulo muestra la estructura básica para crear un módulo en Odoo.

Si al crear la base de datos se crea con la opción de cargar datos de ejemplo, los datos demo
de este módulo van a ser cargados.
""",
}