from dateutil.relativedelta import relativedelta
from datetime import datetime

hoje = datetime.now().date()
print(f"Hoje: {hoje}")
print(f"Daqui 1 mês {hoje + relativedelta(months=1)}")
print(f"Daqui 3 meses: {hoje + relativedelta(months=3)}")
print(f"Daqui 1 ano: {hoje + relativedelta(years=1)}")