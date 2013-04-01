# -*- coding: utf-8 -*-
from report import report_sxw

class mi_reporte(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(mi_reporte, self).__init__(cr, uid, name, context=context)

report_sxw.report_sxw('report.mi_modulo.mi_reporte', 'mi_modulo.mi_tabla', 'addons/mi_modulo/report/mi_reporte.rml', parser=mi_reporte, header=True)
