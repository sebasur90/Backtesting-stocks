import yfinance as yf
from datetime import datetime


class Accion():

    def __init__(self, nombre_accion, start_date, end_date ,testeo_masivo=False):
        self.ticker = nombre_accion
        self.inicio = datetime.strptime(start_date, '%Y-%m-%d')
        self.final = datetime.strptime(end_date, '%Y-%m-%d')        
        self.datos_accion = yf.Ticker(self.ticker)
        self.accion = self.datos_accion.history(
            start=self.inicio, end=self.final).iloc[:, :5]
        self.testeo_masivo=testeo_masivo
        if  self.testeo_masivo ==False:   
            self.info = self.datos_accion.info
            self.sector = self.info['sector']
            self.nombre_completo = self.info['shortName']
            self.ultimo_precio = self.info['currentPrice']
        else:
            pass    


empresas_extranjeras = ['AAPL', 'ABEV', 'ABT', 'ACH', 'ADBE', 'ADI', 'ADP', 'AEG', 'AEM', 'AGRO', 'AIG', 'AMAT', 'AMD', 'AMGN', 'AMX', 'AMZN', 'ANF', 'ARCO', 'ARNC', 'ASR',
                        'AUY', 'AVY', 'AXP', 'AZN', 'BA', 'BABA', 'BAC', 'BB', 'BBD', 'BBVA', 'BCS', 'BG', 'BHP', 'BIDU', 'BIIB', 'BK', 'BMY', 'BP', 'BRFS', 'BSBR',  'C', 'CAH', 'CAJ', 'CAR', 'CAT', 'CBD', 'CDE', 'CEO',  'CL', 'COST', 'CRM', 'CS', 'CSCO', 'CVX', 'CX', 'DD', 'DE', 'DEO', 'DESP', 'DIS',  'E', 'EBAY', 'EBR', 'ELP', 'ERIC', 'ERJ', 'FB', 'FCX', 'FDX', 'FMCC', 'FMX', 'FNMA', 'FSLR', 'GE', 'GFI', 'GGB', 'GILD', 'GLOB', 'GLW', 'GOLD', 'GOOGL', 'GRMN', 'GS', 'GSK', 'HD', 'HDB', 'HL', 'HMC', 'HMY', 'HNP', 'HOG', 'HON', 'HPQ', 'HSBC', 'HSY', 'IBM', 'IBN', 'IFF', 'INFY', 'ING', 'INTC', 'IP', 'ITUB', 'JCI', 'JD', 'JNJ', 'JPM', 'KB', 'KEP', 'KGC', 'KMB', 'KO', 'KOF', 'LFC', 'LLY', 'LMT', 'LVS', 'MBT', 'MCD', 'MDT', 'MELI', 'MFG', 'MMC', 'MMM', 'MO', 'MRK', 'MSFT', 'MSI', 'MUFG', 'NEM', 'NFLX', 'NG', 'NGG', 'NKE', 'NMR', 'NOK', 'NSANY', 'NTCO', 'NTES', 'NUE', 'NVDA', 'NVS', 'ORAN', 'ORCL', 'PAC', 'PBI', 'PBR', 'PCAR', 'PCRFY', 'PEP', 'PFE', 'PG', 'PHG', 'PKX', 'PSO', 'PTR', 'PYPL', 'QCOM', 'RIO', 'ROST', 'SAN', 'SAP', 'SBS', 'SBUX', 'SCCO', 'SID', 'SIEGY', 'SLB', 'SNA', 'SNAP', 'SNP', 'SUZ', 'SYY', 'T', 'TEF', 'TGT', 'TIIAY', 'TM', 'TMO', 'TOT', 'TRIP', 'TRV', 'TS', 'TSLA', 'TSM', 'TTM', 'TV', 'TWTR', 'TX', 'TXN', 'UGP', 'UN', 'URBN', 'USB', 'V', 'VALE', 'VEDL', 'VIST', 'VIV', 'VOD', 'VRSN', 'VZ', 'WB', 'WBK', 'WFC', 'WMT', 'X', 'XOM', 'XRX', 'YELP',
                        'YY', 'YZCAY']

empresas_argentinas = ['BBAR', 'BMA', 'CEPU', 'CRESY', 'EDN', 'GGAL', 'IRCP',
                       'IRS', 'LOMA', 'PAMP.BA', 'SUPV', 'TEO', 'TGS', 'TS', 'TX', 'YPF']

empresas_compradas = ['AMGN', 'DIS', 'HSBC', 'GE', 'CDE', 'PG', 'FDX', 'NFLX', 'IBM',
                      'GOLD', 'KO']
