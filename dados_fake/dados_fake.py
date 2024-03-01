import pandas as pd
from faker import Faker
from datetime import datetime

fake = Faker()

# Criar DataFrame sem contrato específico
df = pd.DataFrame({
    'Email': [fake.email() for _ in range(10)],
    'Data': [fake.date_time_between(start_date='-30d', end_date='now') for _ in range(10)],
    'Valor': [fake.pyfloat(left_digits=5, right_digits=2, positive=True) for _ in range(10)],
    'Produto': [fake.word() for _ in range(10)],
    'Quantidade': [fake.random_int(min=1, max=100) for _ in range(10)],
    'Categoria': [fake.random_element(elements=('A', 'B', 'C')) for _ in range(10)]
})

# Formatar a coluna 'Data' no formato dd/mm/yyyy
df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')

# Salvar DataFrame em um arquivo Excel incluindo apenas as colunas desejadas
df[['Email', 'Data', 'Valor', 'Produto', 'Quantidade', 'Categoria']
   ].to_excel('dados_fake.xlsx', index=False)
