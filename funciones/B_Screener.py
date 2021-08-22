
from funciones.B_resultados import resultados_estrategias
from funciones.B_Estrategias import estrategias


class Screener():
    def __init__(self, estrategia, empresas, margen, start, end, lista_seteos):
        if empresas == 'Extranjeras':
            self.empresas = ['AAPL', 'ABEV', 'ABT', 'ACH', 'ADBE', 'ADI', 'ADP', 'AEG', 'AEM', 'AGRO', 'AIG', 'AMAT', 'AMD', 'AMGN', 'AMX', 'AMZN', 'ANF', 'ARCO', 'ARNC', 'ASR',
                             'AUY', 'AVY', 'AXP', 'AZN', 'BA', 'BABA', 'BAC', 'BB', 'BBD', 'BBVA', 'BCS', 'BG', 'BHP', 'BIDU', 'BIIB', 'BK', 'BMY', 'BP', 'BRFS', 'BSBR',  'C', 'CAH', 'CAJ', 'CAR', 'CAT', 'CBD', 'CDE', 'CEO',  'CL', 'COST', 'CRM', 'CS', 'CSCO', 'CVX', 'CX', 'DD', 'DE', 'DEO', 'DESP', 'DIS',  'E', 'EBAY', 'EBR', 'ELP', 'ERIC', 'ERJ', 'FB', 'FCX', 'FDX', 'FMCC', 'FMX', 'FNMA', 'FSLR', 'GE', 'GFI', 'GGB', 'GILD', 'GLOB', 'GLW', 'GOLD', 'GOOGL', 'GRMN', 'GS', 'GSK', 'HD', 'HDB', 'HL', 'HMC', 'HMY', 'HNP', 'HOG', 'HON', 'HPQ', 'HSBC', 'HSY', 'IBM', 'IBN', 'IFF', 'INFY', 'ING', 'INTC', 'IP', 'ITUB', 'JCI', 'JD', 'JNJ', 'JPM', 'KB', 'KEP', 'KGC', 'KMB', 'KO', 'KOF', 'LFC', 'LLY', 'LMT', 'LVS', 'MBT', 'MCD', 'MDT', 'MELI', 'MFG', 'MMC', 'MMM', 'MO', 'MRK', 'MSFT', 'MSI', 'MUFG', 'NEM', 'NFLX', 'NG', 'NGG', 'NKE', 'NMR', 'NOK', 'NSANY', 'NTCO', 'NTES', 'NUE', 'NVDA', 'NVS', 'ORAN', 'ORCL', 'PAC', 'PBI', 'PBR', 'PCAR', 'PCRFY', 'PEP', 'PFE', 'PG', 'PHG', 'PKX', 'PSO', 'PTR', 'PYPL', 'QCOM', 'RIO', 'ROST', 'SAN', 'SAP', 'SBS', 'SBUX', 'SCCO', 'SID', 'SIEGY', 'SLB', 'SNA', 'SNAP', 'SNP', 'SUZ', 'SYY', 'T', 'TEF', 'TGT', 'TIIAY', 'TM', 'TMO', 'TOT', 'TRIP', 'TRV', 'TS', 'TSLA', 'TSM', 'TTM', 'TV', 'TWTR', 'TX', 'TXN', 'UGP', 'UN', 'URBN', 'USB', 'V', 'VALE', 'VEDL', 'VIST', 'VIV', 'VOD', 'VRSN', 'VZ', 'WB', 'WBK', 'WFC', 'WMT', 'X', 'XOM', 'XRX', 'YELP',
                             'YY', 'YZCAY']
        elif empresas == 'Locales':
            self.empresas = ['BBAR.BA', 'BMA.BA', 'CEPU.BA', 'CRES.BA', 'EDN.BA', 'GGAL.BA', 'IRCP.BA',
                             'IRSA.BA', 'LOMA.BA', 'PAMP.BA', 'SUPV.BA', 'TGSU2.BA', 'TXAR.BA', 'YPFD.BA']
        self.start = start
        self.end = end
        self.resultados_generales = {}
        self.dataframes_generados = {}
        self.listas_generadas = {}
        self.screener_realizado = {}
        self.titulos = {}
        self.mejores_estrategias = {}
        self.ruta = ""
        self.lista_seteos = lista_seteos
        self.estrategia = estrategia
        self.margen = int(margen)

    def corre_screener_simple(self):
        completados = 1
        for empresa in self.empresas:

            try:
                estrat = estrategias(empresa, self.start, self.end)
                if self.estrategia == "CRUCE-MEDIAS":
                    accion_corrida, momento_compra, momento_venta = estrat.estrat_cruce_medias(
                        self.lista_seteos[0], self.lista_seteos[1], stop="SI")
                if self.estrategia == "CRUCE-PRECIOS-CONTRA-MEDIA":
                    
                    accion_corrida,  momento_compra, momento_venta = estrat.estrat_media_contra_precio(
                        self.lista_seteos[0], self.lista_seteos[1], stop="SI")
                if self.estrategia == 'MAXIMOS-Y-MINIMOS-HISTORICOS':
                    accion_corrida, momento_compra, momento_venta = estrat.estrat_maximos_minimos_historicos(
                        self.lista_seteos[0], self.lista_seteos[1], self.lista_seteos[2], stop="SI")

                result = resultados_estrategias(accion_corrida)
                res, accion_evaluada = result.evalua_resultados()

                print("Listo " + empresa)

                print(f'Completados {completados} de {len(self.empresas)}')
                print("")
                completados = completados+1
                x = 0
                while x > -self.margen:
                    x = x-1
                    if accion_corrida.Trade.iloc[x] == 1:
                        self.screener_realizado[empresa] = {
                            'nombre': empresa,   'nombre_completo': estrat.nombre_completo,
                            'sector': estrat.sector, 'ultimo_precio': estrat.ultimo_precio,
                            'senal': "COMPRA", 'dia_senal':     accion_corrida.index[x]
                        }

                        break
            except:
                continue

        return self.screener_realizado
