from django.shortcuts import render
from funciones.B_Accion import Accion, empresas_argentinas, empresas_extranjeras, empresas_compradas
from funciones.B_Estrategias import nombre_estrategias
from datetime import datetime, timedelta
from funciones.B_Screener import Screener


def primera_vista(request):
    empresas = ['Locales', 'Extranjeras']
    data = {'nombre_estrategias': nombre_estrategias, 'empresas_extranjeras': empresas_extranjeras, 'empresas_argentinas': empresas_argentinas,
            'empresas_compradas': empresas_compradas, 'empresas': empresas}
    return render(request, 'pagina_screener_principal.html', data)


def segunda_vista(request):
    fecha_hoy = datetime.now().date()
    lista_seteos = []
    for num_seteo in range(8):
        name = "range"+str(num_seteo)
        try:
            seteo = request.GET[name]
            lista_seteos.append(int(seteo))
        except:
            pass
    nombre_estrategia = request.GET['dropdown_estrategias']
    empresas = request.GET['dropdown_acciones']
    margen = request.GET['margen']
    
    fecha_inicio = fecha_hoy-timedelta(max(lista_seteos))
    fecha_hoy = str(fecha_hoy)
    fecha_inicio = str(fecha_inicio)
    objeto_screener = Screener(
        nombre_estrategia, empresas, margen, fecha_inicio, fecha_hoy, lista_seteos)
    result = objeto_screener.corre_screener_simple()    

    if result=={}:
        encontro="NO"
    else:
        encontro="SI"   

    data = {'nombre_estrategias': nombre_estrategias, 'empresas_extranjeras': empresas_extranjeras, 'empresas_argentinas': empresas_argentinas,
            'empresas_compradas': empresas_compradas, 'result': result,'encontro':encontro}

    return render(request, 'pagina_screener_principal_corrida.html', data)
