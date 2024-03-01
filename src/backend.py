import pandas as pd
from contrato import Vendas
from openpyxl import load_workbook


def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)
        erros = []
        # Verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"

        # Validar cada linha com o schema escolhido
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                erros.append(f"Erro na linha {index + 2}: {e}")

        return True, None

    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Erro inesperado: {str(e)}"


# # def excel_to_sql(df):
# #     df.to_sql('vendas', con=DATABASE_URL, if_exists='replace', index=False)
