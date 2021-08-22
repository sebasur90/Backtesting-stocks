import numpy as np



class resultados_estrategias():
    def __init__(self, accion_sin_evaluar,estrategia="NO"):
        self.accion = accion_sin_evaluar
        self.resultado = {}
        self.estrategia=estrategia

    def evalua_resultados(self):
        self.accion['Retornos'] = np.where(((self.accion.Trade != 0)), self.accion.Dif_Close - 0.0085,
                                           np.where(self.accion.Posicion == 1, self.accion.Dif_Close, 0))
        self.accion['capital_estrategia'] = (
            self.accion.Retornos + 1).cumprod() * 100
        self.accion['Buy_and_Hold'] = (
            self.accion.Dif_Close + 1).cumprod() * 100        
        self.accion_evaluada = self.accion.copy(
        )
        self.resultado['Beneficio_Bruto'] = round(
            self.accion_evaluada.iloc[-1]['capital_estrategia']-100, 2)
        
        dataframe_estrategia = self.accion_evaluada[self.accion.Trade != 0]        
        self.resultado['trades'] = self.accion_evaluada['Trade'].count()
        self.accion_evaluada = self.accion_evaluada[[
            'Posicion', 'capital_estrategia']]
        
        self.accion_evaluada['resultado_trade'] = np.where((self.accion_evaluada.Posicion == -1) & (self.accion_evaluada.Posicion.shift(
        ) == 1), self.accion_evaluada['capital_estrategia']-dataframe_estrategia['capital_estrategia'].shift(), 0)
        self.resultado['trades_ganadores'] = self.accion_evaluada.resultado_trade[self.accion_evaluada.resultado_trade >= 0].count()
        self.resultado['suma_trades_ganadores'] = round(
            self.accion_evaluada.resultado_trade[self.accion_evaluada.resultado_trade >= 0].sum(), 2)
        self.resultado['trades_perdedores'] = self.accion_evaluada.resultado_trade[self.accion_evaluada.resultado_trade < 0].count()
        self.resultado['suma_trades_perdedores'] = abs(round(
            self.accion_evaluada.resultado_trade[self.accion_evaluada.resultado_trade < 0].sum(), 2))

        if self.resultado['trades_ganadores'] == 0:
            self.resultado['Ratio Acierto'] = 0
            self.resultado['Profit Factor'] = 0

        elif self.resultado['trades_perdedores'] == 0:
            self.resultado['Ratio Acierto'] = 100
            self.resultado['Profit Factor'] = 100

        else:
            self.resultado['Ratio Acierto'] = round(
                100 * self.resultado['trades_ganadores'] / self.resultado['trades'], 2)
            self.resultado['Profit Factor'] = round(
                self.resultado['suma_trades_ganadores'] / self.resultado['suma_trades_perdedores'], 2)
        
        self.resultado['capital_estrategia'] = round(
            self.accion['capital_estrategia'].iloc[-1], 2)
        self.resultado['Buy_Hold'] = round(
            self.accion['Buy_and_Hold'].iloc[-1], 2)
        if self.estrategia != "NO":
            self.resultado["Estrategia"]=self.estrategia
        else:
            pass
             
        return self.resultado, self.accion
