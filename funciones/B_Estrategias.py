import numpy as np
import pandas as pd
from funciones.B_Accion import Accion


nombre_estrategias = ['CRUCE-MEDIAS',
                      'MAXIMOS-Y-MINIMOS-HISTORICOS',
                      'CRUCE-PRECIOS-CONTRA-MEDIA']


class estrategias(Accion):
    def __init__(self, acc_elegida, start_date, end_date, testeo_masivo=False):
        Accion.__init__(self, acc_elegida, start_date, end_date, testeo_masivo)

    def corre_estrategia(self, stop):
        self.accion.Senal.ffill(inplace=True)
        if stop == "SI":
            self.accion['Posicion_estrategia'] = self.accion.Senal
            self.accion['Trade_estrategia'] = np.where(self.accion.Posicion_estrategia == 1 & (self.accion.Posicion_estrategia != self.accion.Posicion_estrategia.shift(
            )), 1, np.where((self.accion.Posicion_estrategia != self.accion.Posicion_estrategia.shift()) & self.accion.Posicion_estrategia.shift() == 1, -1, 0))
            self.accion = self.stop_loss()
        else:
            self.accion['Posicion'] = self.accion.Senal
            self.accion['Trade'] = np.where(self.accion.Posicion == 1 & (self.accion.Posicion != self.accion.Posicion.shift(
            )), 1, np.where((self.accion.Posicion != self.accion.Posicion.shift()) & self.accion.Posicion.shift() == 1, -1, 0))

        return self.accion

    def stop_loss_ciclo_for(self, ciclo, comprado):
        if (self.accion.Trade.iloc[ciclo] == 1):
            self.accion.loc[self.accion.Close.index[ciclo],
                            'SL'] = self.accion.Low.iloc[ciclo]*0.93
        if (pd.isna(self.accion.SL.iloc[ciclo]) == True) & (self.accion.Senal.iloc[ciclo] == 1):
            self.accion.loc[self.accion.Close.index[ciclo],
                            'SL'] = self.accion.SL.iloc[ciclo-1]
        if (comprado == 1) and (self.accion.loc[self.accion.SL.index[ciclo], 'SL'] >= self.accion.loc[self.accion.SL.index[ciclo], 'Low']):
            self.accion.loc[self.accion.Close.index[ciclo], 'Trade'] = -1
            self.accion.loc[self.accion.Close.index[ciclo],
                            'importante'] = 'STOP'
            comprado = 0
        return self.accion, ciclo, comprado

    def stop_loss(self):

        self.accion['accion'] = "NO"
        self.accion['Posicion'] = np.NaN
        self.accion['stop_loss'] = np.where((self.accion['Trade_estrategia'] == 1) & (
            self.accion['Posicion_estrategia'].shift() == -1), self.accion['Open']*0.93, np.NaN)
        self.accion['stop_loss'] = self.accion['stop_loss'].ffill()
        self.accion['senal_stop_loss'] = np.where(
            (self.accion['stop_loss'] >= self.accion['Open']), False, True)
        self.accion['stops'] = np.where(
            (self.accion['senal_stop_loss'] == False), False, True)
        self.accion['Posicion'] = np.where((self.accion['Posicion_estrategia'] == 1) & (self.accion['Trade_estrategia'] == 1), 1,
                                           np.where((self.accion['Posicion_estrategia'] == 1) & (self.accion['stops'] == False), -1,
                                                    np.where((self.accion['Posicion_estrategia'] == -1), -1,
                                                             np.NaN
                                                             )))
        self.accion['Posicion'] = self.accion['Posicion'].ffill()
        self.accion['Trade'] = np.where((self.accion['Posicion'] == 1) & (self.accion['Posicion'].shift() == -1) & (self.accion['Posicion_estrategia'].shift() == -1), 1,
                                        np.where((self.accion['Posicion'] == -1) & (self.accion['Posicion'].shift() == 1), -1, 0
                                                 ))

        return self.accion

    def estrat_cruce_medias(self, MM_rapida, MM_lenta, stop):
        self.accion['Dif_Close'] = self.accion.Close.pct_change()
        self.accion['MM_rapida'] = self.accion.Close.ewm(MM_rapida).mean()
        self.accion['MM_lenta'] = self.accion.Close.ewm(MM_lenta).mean()
        self.accion['diff_medias'] = self.accion.MM_rapida - \
            self.accion.MM_lenta
        self.accion['Senal'] = np.where(self.accion.diff_medias > 0, 1, -1)
        self.accion_corrida = self.corre_estrategia(stop)
        self.lista_grafico = ['MM_rapida', 'MM_lenta']
        self.titulo = f"MM_rapida_: {MM_rapida} /MM_lenta: {MM_lenta} / STOP LOSS: {stop}"
        momento_compra = self.accion_corrida.Close[self.accion_corrida.Trade == 1].reset_index(
        )
        momento_compra.columns = ['Date', 'Close']
        momento_venta = self.accion_corrida.Close[self.accion_corrida.Trade == -1].reset_index()
        momento_venta.columns = ['Date', 'Close']

        return self.accion_corrida,  momento_compra, momento_venta

    def estrat_media_contra_precio(self, MM_compra, MM_venta, stop):
        self.accion['Dif_Close'] = self.accion.Close.pct_change()
        self.accion['MM_compra'] = self.accion.Low.ewm(MM_compra).mean()
        self.accion['MM_venta'] = self.accion.Low.ewm(MM_venta).mean()
        self.accion['Senal'] = np.where((self.accion.Low.shift() < self.accion.MM_compra.shift()) & (self.accion.Low >= self.accion.MM_compra), 1,
                                        np.where((self.accion.High.shift() > self.accion.MM_venta.shift()) & (self.accion.High <= self.accion.MM_venta), -1, np.NaN))
        self.accion_corrida = self.corre_estrategia(stop)
        self.lista_grafico = ['MM_compra', 'MM_venta']
        self.titulo = f"MM_compra: {MM_compra} /MM_venta: {MM_venta}  / STOP LOSS: {stop}"
        momento_compra = self.accion_corrida.Close[self.accion_corrida.Trade == 1].reset_index(
        )
        momento_compra.columns = ['Date', 'Close']
        momento_venta = self.accion_corrida.Close[self.accion_corrida.Trade == -1].reset_index()
        momento_venta.columns = ['Date', 'Close']

        return self.accion_corrida,  momento_compra, momento_venta

    def estrat_maximos_minimos_historicos(self, cantidad_ruedas, cant_minimos, cant_maximos, stop):
        comprado = 0
        self.accion['Dif_Close'] = self.accion.Close.pct_change()
        self.accion['mi_ma'] = "NO"
        self.accion['importante'] = "NO"
        self.accion['Senal'] = 0
        self.accion['Trade'] = 0
        self.accion['SL'] = np.NaN
        for ciclo in range(len(self.accion)-1):

            minimos = list(
                self.accion.Low.iloc[ciclo-int(cantidad_ruedas):ciclo+1].sort_values(ascending=False).iloc[-int(cant_minimos):])
            maximos = list(
                self.accion.High.iloc[ciclo-int(cantidad_ruedas):ciclo+1].sort_values(ascending=True).iloc[-int(cant_maximos):])

            if self.accion.Low.iloc[ciclo] in minimos:

                self.accion.loc[self.accion.Close.index[ciclo],
                                'minimos_historicos'] = self.accion.Low.iloc[ciclo]
                self.accion.loc[self.accion.Close.index[ciclo],
                                'mi_ma'] = 'MIN'

            if self.accion.High.iloc[ciclo] in maximos:
                self.accion.loc[self.accion.Close.index[ciclo],
                                'maximos_historicos'] = self.accion.High.iloc[ciclo]
                self.accion.loc[self.accion.Close.index[ciclo],
                                'mi_ma'] = 'MAX'

            if (self.accion.mi_ma.iloc[ciclo-1] == 'MIN') & (self.accion.mi_ma.iloc[ciclo-1] == 'MIN') & (self.accion.mi_ma.iloc[ciclo] != 'MIN') & (self.accion.importante.iloc[ciclo-1] != 'STOP'):
                self.accion.loc[self.accion.mi_ma.index[ciclo], 'Senal'] = 1

            if (self.accion.mi_ma.iloc[ciclo-1] == 'MAX') & (self.accion.mi_ma.iloc[ciclo-2] == 'MAX') & (self.accion.mi_ma.iloc[ciclo] != 'MAX'):
                self.accion.loc[self.accion.mi_ma.index[ciclo], 'Senal'] = -1

            if (comprado == 0) and (self.accion.loc[self.accion.mi_ma.index[ciclo], 'Senal'] == 1):
                self.accion.loc[self.accion.mi_ma.index[ciclo], 'Trade'] = 1
                comprado = 1

            if (comprado == 1) and (self.accion.loc[self.accion.mi_ma.index[ciclo], 'Senal'] == -1):
                self.accion.loc[self.accion.mi_ma.index[ciclo], 'Trade'] = -1
                comprado = 0

            if self.accion.Senal.iloc[ciclo] == 0:
                self.accion.loc[self.accion.Senal.index[ciclo],
                                'Senal'] = self.accion.Senal.iloc[ciclo-1]

            if stop == "SI":
                self.accion, ciclo, comprado = self.stop_loss_ciclo_for(
                    ciclo, comprado)
            else:
                pass

        self.accion['Posicion'] = self.accion.Senal
        dataframe = self.accion.loc[self.accion[self.accion.Trade == 1].index[0]:]
        self.lista_grafico = ['minimos_historicos', 'maximos_historicos']

        self.titulo = f"minimos_historicos: {cantidad_ruedas}-{cant_minimos} /maximos_historicos: {cantidad_ruedas}-{cant_maximos} / STOP LOSS: {stop}"

        momento_compra = self.accion.Close[self.accion.Trade == 1].reset_index(
        )
        momento_compra.columns = ['Date', 'Close']
        momento_venta = self.accion.Close[self.accion.Trade == -1].reset_index()
        momento_venta.columns = ['Date', 'Close']

        return self.accion,  momento_compra, momento_venta
