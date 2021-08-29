import pandas as pd
from funciones.B_Estrategias import estrategias
from funciones.B_resultados import resultados_estrategias


class testeo_masivo(estrategias):

    def __init__(self, acc_elegida, start, end, testeo_masivo=True):
        estrategias.__init__(self, acc_elegida, start, end, testeo_masivo)
        self.resultados_generales = {}
        self.dataframes_generados = {}
        self.listas_generadas = {}
        self.screener_completo_resultados = {}
        self.acc = acc_elegida
        self.ruta = ""
        self.start = start
        self.end = end
        self.momentos_compra = {}
        self.momentos_venta = {}
        self.testeo_masivo = testeo_masivo

    def mejores_resultados(self, resultados):
        self.mejores_resultados_dataframe = pd.DataFrame(
            resultados).transpose()
        self.mejores_resultados_dataframe = self.mejores_resultados_dataframe.sort_values(
            by='Beneficio_Bruto', ascending=False)
        self.mejor_estrategia = self.mejores_resultados_dataframe.index[0]
        return self.mejores_resultados_dataframe, self.mejor_estrategia

    def testeo_masivo_estrat_maximos_minimos_historicos(self, cantidad_ruedas, rango_cant_minimos_inicio, rango_cant_minimos_fin,
                                                        rango_cant_maximos_inicio, rango_cant_maximos_fin, stop):
        import itertools

        rango_cant_minimos = range(int(rango_cant_minimos_inicio), int(
            rango_cant_minimos_fin), int(5))
        rango_cant_maximos = range(int(rango_cant_maximos_inicio), int(
            rango_cant_maximos_fin), int(5))
        contador = 0
        parametros = itertools.product(
            *[rango_cant_minimos, rango_cant_maximos])

        
        for par in parametros:
            cant_min, cant_max = par
            
            
            estrat = estrategias(self.acc, self.start,
                                 self.end, self.testeo_masivo)
            accion_corr, momentos_compra, momentos_venta = estrat.estrat_maximos_minimos_historicos(
                cantidad_ruedas, cant_min, cant_max, stop)
            nombre_estrategia = f"{cantidad_ruedas}_{cant_min}_{cant_max}"
            result = resultados_estrategias(accion_corr, nombre_estrategia)
            res, accion_evaluada = result.evalua_resultados()
            self.resultados_generales[nombre_estrategia] = res
            self.dataframes_generados[nombre_estrategia] = accion_evaluada
            self.momentos_compra[nombre_estrategia] = momentos_compra
            self.momentos_venta[nombre_estrategia] = momentos_venta

        self.mejores_resultados_dataframe, self.mejor_estrategia = self.mejores_resultados(
            self.resultados_generales)
        titulo_a_procesar = self.mejores_resultados_dataframe.index[0].split(
            "_")
        compra_venta = ['Ruedas minimos', 'Ruedas maximos',
                        'Cant Minimos', 'Cant maximos']

        titulo_a_procesar_lista = [x+"-"+y for x,
                                   y in zip(titulo_a_procesar, compra_venta)]
        titulo = " / ".join(titulo_a_procesar_lista) + \
            " / Stop loss: " + str(stop)

        return self.dataframes_generados, self.mejores_resultados_dataframe, self.momentos_compra, self.momentos_venta

    def testeo_masivo_estrat_cruce_medias(self, rango_rapido_inicio, rango_rapido_final, rango_lento_inicio, rango_lento_final, stop):
        import itertools
        MM_rapida = range(int(rango_rapido_inicio), int(
            rango_rapido_final), int(5))
        MM_lenta = range(int(rango_lento_inicio), int(
            rango_lento_final), int(10))
        contador = 0
        parametros = itertools.product(*[MM_rapida, MM_lenta])
        for par in parametros:
            MM_rap, MM_len = par
            if MM_len <= MM_rap:
                continue
            contador += 1
            estrat = estrategias(self.acc, self.start,
                                 self.end, self.testeo_masivo)
            accion_corr, momentos_compra, momentos_venta = estrat.estrat_cruce_medias(
                MM_rap, MM_len, stop)
            nombre_estrategia = f"{MM_rap}_{MM_len}"
            result = resultados_estrategias(accion_corr, nombre_estrategia)
            res, accion_evaluada = result.evalua_resultados()
            self.resultados_generales[contador] = res
            self.dataframes_generados[nombre_estrategia] = accion_evaluada
            
            self.momentos_compra[nombre_estrategia] = momentos_compra
            self.momentos_venta[nombre_estrategia] = momentos_venta

        self.mejores_resultados_dataframe, self.mejor_estrategia = self.mejores_resultados(
            self.resultados_generales)

        return self.dataframes_generados, self.mejores_resultados_dataframe, self.momentos_compra, self.momentos_venta

    def testeo_masivo_estrat_media_contra_precio(self, rango_rapido_inicio, rango_rapido_final, rango_lento_inicio, rango_lento_final, stop):
        import itertools
        MM_rapida = range(int(rango_rapido_inicio), int(
            rango_rapido_final), int(5))
        MM_lenta = range(int(rango_lento_inicio), int(
            rango_lento_final), int(10))
        contador = 0
        parametros = itertools.product(*[MM_rapida, MM_lenta])
        for par in parametros:
            MM_rap, MM_len = par
            if MM_len <= MM_rap:
                continue
            contador += 1
            estrat = estrategias(self.acc, self.start,
                                 self.end, self.testeo_masivo)
            accion_corr, momentos_compra, momentos_venta = estrat.estrat_media_contra_precio(
                MM_rap, MM_len, stop)
            nombre_estrategia = f"{MM_rap}_{MM_len}"
            result = resultados_estrategias(accion_corr, nombre_estrategia)
            res, accion_evaluada = result.evalua_resultados()
            self.resultados_generales[contador] = res
            self.dataframes_generados[nombre_estrategia] = accion_evaluada
            self.momentos_compra[nombre_estrategia] = momentos_compra
            self.momentos_venta[nombre_estrategia] = momentos_venta

        self.mejores_resultados_dataframe, self.mejor_estrategia = self.mejores_resultados(
            self.resultados_generales)

        return self.dataframes_generados, self.mejores_resultados_dataframe, self.momentos_compra, self.momentos_venta
