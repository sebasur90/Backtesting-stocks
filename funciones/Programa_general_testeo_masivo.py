from funciones.B_Accion import Accion
from funciones.B_Estrategias import estrategias
#from funciones.B_Screener import screener_estrategia
from funciones.B_resultados import resultados_estrategias
from funciones.B_testeo_masivo import testeo_masivo


class testeo_masivo_individual():
    def __init__(self, tiker, estrategia, start, end, stop, lista_seteos, escreener_completo=False):
        self.tiker = tiker
        self.estrategia = estrategia
        self.start = start
        self.end = end
        self.stop = stop
        self.lista_seteos = lista_seteos
        self.escreener_completo = escreener_completo

    def testeo_masivo_estrat_cruce_medias(self):

        objeto_testeo = testeo_masivo(
            self.tiker, self.start, self.end, self.escreener_completo)
        resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta = objeto_testeo.testeo_masivo_estrat_cruce_medias(self.lista_seteos[0],
                                                                                                                               self.lista_seteos[1], self.lista_seteos[
                                                                                                                                   2], self.lista_seteos[3],
                                                                                                                               self.stop)

        return resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta

    def testeo_masivo_estrat_cruce_precio_contra_medias(self):

        objeto_testeo = testeo_masivo(
            self.tiker, self.start, self.end, self.escreener_completo)
        resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta = objeto_testeo.testeo_masivo_estrat_media_contra_precio(self.lista_seteos[0],
                                                                                                                                      self.lista_seteos[1], self.lista_seteos[
            2], self.lista_seteos[3],
            self.stop)
        return resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta

    def testeo_masivo_estrat_maximos_minimos_historicos(self):

        objeto_testeo = testeo_masivo(
            self.tiker, self.start, self.end, self.escreener_completo)
        resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta = objeto_testeo.testeo_masivo_estrat_maximos_minimos_historicos(self.lista_seteos[0],
                                                                                                                                             self.lista_seteos[1], self.lista_seteos[
            2], self.lista_seteos[3],self.lista_seteos[4],
            self.stop)
        return resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta

    def decide_estrategia(self):
        if self.estrategia == 'CRUCE-MEDIAS':
            resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta = self.testeo_masivo_estrat_cruce_medias()
            return resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta
        if self.estrategia == 'CRUCE-PRECIOS-CONTRA-MEDIA':
            resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta = self.testeo_masivo_estrat_cruce_precio_contra_medias()
            return resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta

        if self.estrategia == 'MAXIMOS-Y-MINIMOS-HISTORICOS':
            resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta = self.testeo_masivo_estrat_maximos_minimos_historicos()
            return resultado_testeo, dataframes_testeo, momentos_compra, momentos_venta
