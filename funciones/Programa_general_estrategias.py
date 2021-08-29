from funciones.B_Estrategias import estrategias
from funciones.B_resultados import resultados_estrategias


class estrategia_individual():
    def __init__(self, tiker, estrategia, start, end, stop, lista_seteos):
        self.tiker = tiker
        self.estrategia = estrategia
        self.start = start
        self.end = end
        self.stop = stop
        self.lista_seteos = lista_seteos

    def estrat_cruce_medias(self):
        estrat = estrategias(self.tiker, self.start, self.end)
        accion_corr, momento_compra, momento_venta = estrat.estrat_cruce_medias(
            int(self.lista_seteos[0]), int(self.lista_seteos[1]), self.stop)
        result = resultados_estrategias(accion_corr)
        res, accion_evaluada = result.evalua_resultados()
        nombre_completo_accion = estrat.nombre_completo
        return res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion

    def estrat_maximos_minimos_historicos(self):
        estrat = estrategias(self.tiker, self.start, self.end)
        accion_corr,  momento_compra, momento_venta = estrat.estrat_maximos_minimos_historicos(
            int(self.lista_seteos[0]), int(self.lista_seteos[1]), int(self.lista_seteos[2]), self.stop)
        result = resultados_estrategias(accion_corr)
        res, accion_evaluada = result.evalua_resultados()
        nombre_completo_accion = estrat.nombre_completo
        return res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion

    def estrat_media_contra_precio(self):
        estrat = estrategias(self.tiker, self.start, self.end)
        accion_corr,  momento_compra, momento_venta = estrat.estrat_media_contra_precio(
            int(self.lista_seteos[0]), int(self.lista_seteos[1]), self.stop)
        result = resultados_estrategias(accion_corr)
        res, accion_evaluada = result.evalua_resultados()
        nombre_completo_accion = estrat.nombre_completo
        return res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion

    def decide_estrategia(self):
        if self.estrategia == 'CRUCE-MEDIAS':
            res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion = self.estrat_cruce_medias()
            return res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion

        if self.estrategia == 'MAXIMOS-Y-MINIMOS-HISTORICOS':
            res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion = self.estrat_maximos_minimos_historicos()
            return res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion

        if self.estrategia == 'CRUCE-PRECIOS-CONTRA-MEDIA':
            res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion = self.estrat_media_contra_precio()
            return res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion

    def __str__(self):
        print('tiker ' + str(self.tiker))
        print('estrategia ' + str(self.estrategia))
        print('start ' + str(self.start))
        print('end ' + str(self.end))
        print('stop ' + str(self.stop))
        for set in range(len(self.lista_seteos)):
            print('seteo '+str(set)+str(" ") + str(self.lista_seteos[set]))
