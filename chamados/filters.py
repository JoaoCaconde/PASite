from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from chamados.models import ChamadoRPAEntradaManual


class ChamadoRPAEntradaManualFilter(AutoRQLFilterClass):
    MODEL = ChamadoRPAEntradaManual