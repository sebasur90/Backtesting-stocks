from django.shortcuts import render
from funciones.B_Accion import Accion, empresas_argentinas, empresas_extranjeras, empresas_compradas
from funciones.B_Estrategias import nombre_estrategias
from funciones.Programa_general_estrategias import estrategia_individual


def primera_vista(request):

    data = {'nombre_estrategias': nombre_estrategias, 'empresas_extranjeras': empresas_extranjeras, 'empresas_argentinas': empresas_argentinas,
            'empresas_compradas': empresas_compradas}

    return render(request, 'pagina_estrategia_principal.html', data)


def segunda_vista(request):

    fecha_inicio = request.GET['trip-start']
    fecha_fin = request.GET['trip-end']
    nombre_accion = request.GET['dropdown_acciones']
    nombre_estrategia = request.GET['dropdown_estrategias']
    stop = request.GET['stop_loss']
    lista_seteos = []

    for num_seteo in range(8):
        name = "range"+str(num_seteo)
        try:
            seteo = request.GET[name]
            lista_seteos.append(seteo)
        except:
            pass

    objeto_estrategia = estrategia_individual(
        nombre_accion, nombre_estrategia, fecha_inicio, fecha_fin, stop, lista_seteos)
    objeto_estrategia.__str__()
    res, accion_evaluada, momento_compra, momento_venta, nombre_completo_accion = objeto_estrategia.decide_estrategia()

    accion_evaluada = accion_evaluada.reset_index()
    momento_compra = momento_compra.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                            double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)
    momento_venta = momento_venta.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                          double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)

    accion_evaluada = accion_evaluada.to_json(path_or_buf=None, orient='records', date_format='epoch',
                                              double_precision=10, force_ascii=True, date_unit='ms', default_handler=None)

    data = {'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin, 'accion_evaluada': accion_evaluada, 'nombre_accion': nombre_accion, 'stop': stop,
            'nombre_estrategia': nombre_estrategia, 'momento_compra': momento_compra, 'momento_venta': momento_venta, 'resultados': res, 'lista_seteos': lista_seteos,
            'nombre_completo_accion': nombre_completo_accion}
    return render(request, 'pagina_estrategia_corrida.html', data)


def index(request):

    return render(request, 'index.html')
