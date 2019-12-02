from datetime import datetime
from MetaTrader5 import *
from pytz import timezone
import matplotlib.pyplot as plt

utc_tz = timezone('UTC')

# conecte-se ao MetaTrader 5
MT5Initialize()
# esperamos que o terminal MetaTrader 5 estabeleça a conexão com servidor de negociação e sincronize o ambiente
MT5WaitForTerminal()

# consultamos o estado e os parâmetros de conexão
print(MT5TerminalInfo())
# obtemos informações sobre a versão do MetaTrader 5
print(MT5Version())

# solicitamos 1 000 ticks de EURAUD
euraud_ticks = MT5CopyTicksFrom("EURAUD", datetime(2019, 4, 1, 0), 1000, MT5_COPY_TICKS_ALL)
# solicitamos ticks de AUDUSD no intervalo 2019.04.01 13:00 - 2019.04.02 13:00
audusd_ticks = MT5CopyTicksRange("AUDUSD", datetime(2019, 4, 1, 13), datetime(2019, 4, 2, 13), MT5_COPY_TICKS_ALL)

# obtemos barras de vários instrumentos de diferentes maneiras
eurusd_rates = MT5CopyRatesFrom("EURUSD", MT5_TIMEFRAME_M1, datetime(2019, 4, 5, 15), 1000)
gbpusd_rates = MT5CopyRatesFromPos("GBPUSD", MT5_TIMEFRAME_M1, 0, 1000)
eurjpy_rates = MT5CopyRatesRange("EURJPY", MT5_TIMEFRAME_M1, datetime(2019, 4, 1, 13), datetime(2019, 4, 2, 13))
# concluímos a conexão ao MetaTrader 5
MT5Shutdown()

# DATA
print('euraud_ticks(', len(euraud_ticks), ')')
for val in euraud_ticks[:10]: print(val)
print('audusd_ticks(', len(audusd_ticks), ')')
for val in audusd_ticks[:10]: print(val)
print('eurusd_rates(', len(eurusd_rates), ')')
for val in eurusd_rates[:10]: print(val)
print('gbpusd_rates(', len(gbpusd_rates), ')')
for val in gbpusd_rates[:10]: print(val)
print('eurjpy_rates(', len(eurjpy_rates), ')')
for val in eurjpy_rates[:10]: print(val)

# PLOTTING
x_time = [x.time.astimezone(utc_tz) for x in euraud_ticks]
# preparamos os arrays Bid e Ask
bid = [y.bid for y in euraud_ticks]
ask = [y.ask for y in euraud_ticks]

# plotamos os ticks no gráfico
plt.plot(x_time, ask, 'r-', label='ask')
plt.plot(x_time, bid, 'g-', label='bid')
# exibimos rótulos
plt.legend(loc='upper left')
# adicionamos cabeçalho
plt.title('EURAUD ticks')
# mostramos o gráfico
plt.show()