from django.shortcuts import render
from funciones.B_Accion import Accion, empresas_argentinas, empresas_extranjeras, empresas_compradas
from funciones.B_Estrategias import nombre_estrategias
from funciones.Programa_general_testeo_masivo import testeo_masivo_individual
from funciones.Programa_general_estrategias import estrategia_individual
import numpy as np
import json


class Dataframe_seleccionado():
    def __init__(self):
        self.fecha_inicio = ""
        self.fecha_fin = ""
        self.nombre_accion = ""
        self.nombre_estrategia = ""
        self.stop = ""
        self.lista_seteos = ""
        self.conjunto_dataframes = ""


dataframe_seleccionado = Dataframe_seleccionado()


def primera_vista(request):

    data = {'nombre_estrategias': nombre_estrategias, 'empresas_extranjeras': empresas_extranjeras, 'empresas_argentinas': empresas_argentinas,
            'empresas_compradas': empresas_compradas}
    return render(request, 'pagina_testeo_masivo_principal.html', data)


def segunda_vista(request, dataframe_verificar=dataframe_seleccionado):
    fecha_inicio = request.GET['trip-start']
    fecha_fin = request.GET['trip-end']
    nombre_accion = request.GET['dropdown_acciones']
    nombre_estrategia = request.GET['dropdown_estrategias']
    stop = request.GET['stop_loss']
    lista_seteos = []
    for num_seteo in range(20):
        name = "range"+str(num_seteo)
        try:
            seteo = request.GET[name]
            lista_seteos.append(int(seteo))
        except:
            pass

    dataframe_seleccionado.fecha_inicio = fecha_inicio
    dataframe_seleccionado.fecha_fin = fecha_fin
    dataframe_seleccionado.nombre_accion = nombre_accion
    dataframe_seleccionado.nombre_estrategia = nombre_estrategia
    dataframe_seleccionado.stop = stop

    objeto_seteo = testeo_masivo_individual(
        nombre_accion, nombre_estrategia, fecha_inicio, fecha_fin, stop, lista_seteos)

    dataframes_generados, mejores_resultados_dataframe, momento_compra, momento_venta = objeto_seteo.decide_estrategia()
    dataframe_verificar.conjunto_dataframes = dataframes_generados
    momento_compra = 0
    momento_venta = 0
    lista_dataframes = []

    for x, y in dataframes_generados.items():
        lista_dataframes.append(dataframes_generados[x].to_json(path_or_buf=None, orient='records', date_format='epoch',
                                                                double_precision=10, force_ascii=True, date_unit='ms', default_handler=None))

    lista_10_mejores_dataframes = (
        list(mejores_resultados_dataframe.Estrategia))
    for x, z in zip(lista_10_mejores_dataframes, range(len(lista_10_mejores_dataframes))):
        if x == lista_10_mejores_dataframes[0]:
            estrategias_comparadas = dataframes_generados[x].reset_index(
            )[['Date', 'Buy_and_Hold', 'capital_estrategia']]
            estrategias_comparadas.columns = [
                'Date', 'Buy_and_Hold', 'capital_estrategia_'+str(x)]

        if z < 10:
            estrategias_comparadas['capital_estrategia_' +
                                   str(x)] = np.array(dataframes_generados[x]['capital_estrategia'])

    lista_10_mejores_dataframes = json.dumps(lista_10_mejores_dataframes)
    estrategias_comparadas = estrategias_comparadas.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                                            double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)

    mejores_resultados_dataframe = mejores_resultados_dataframe.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                                                        double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)

    data = {'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin, 'nombre_accion': nombre_accion, 'stop': stop,
            'nombre_estrategia': nombre_estrategia, 'momento_compra': momento_compra, 'momento_venta': momento_venta, 'lista_seteos': lista_seteos,
            'mejores_resultados_dataframe': mejores_resultados_dataframe, 'lista_dataframes': lista_dataframes, 'estrategias_comparadas': estrategias_comparadas,
            'lista_10_mejores_dataframes': lista_10_mejores_dataframes}

    return render(request, 'pagina_testeo_masivo_corrido.html', data)


def tercera_vista(request, dataframe_verificar=dataframe_seleccionado):

    estrat_seleccionada = request.GET['nombre']
    estrat_seleccionada = estrat_seleccionada.split("_")
    dataframe_verificar.lista_seteos = estrat_seleccionada

    objeto_estrategia = estrategia_individual(
        dataframe_verificar.nombre_accion, dataframe_verificar.nombre_estrategia, dataframe_verificar.fecha_inicio, dataframe_verificar.fecha_fin,
        dataframe_verificar.stop, dataframe_verificar.lista_seteos)

    objeto_estrategia.__str__()
    res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion = objeto_estrategia.decide_estrategia()

    accion_evaluada = accion_evaluada.reset_index()
    momento_compra = momento_compra.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                            double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)
    momento_venta = momento_venta.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                          double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)

    accion_evaluada = accion_evaluada.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                              double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)

    

    data = {'fecha_inicio': dataframe_verificar.fecha_inicio, 'fecha_fin': dataframe_verificar.fecha_fin, 'accion_evaluada': accion_evaluada, 'nombre_accion': dataframe_verificar.nombre_accion,
            'stop': dataframe_verificar.stop,            'nombre_estrategia': dataframe_verificar.nombre_estrategia, 'momento_compra': momento_compra, 'momento_venta': momento_venta,
            'resultados': res, 'lista_seteos': dataframe_verificar.lista_seteos,            'nombre_completo_accion': nombre_completo_accion}

    return render(request, 'pagina_testeo_masivo_corrido_revisada.html', data)
