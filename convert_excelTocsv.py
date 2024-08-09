import pandas as pd
import argparse

def convert_excel_to_csv(excel_file, csv_file):
  """Convierte un archivo Excel a CSV.

  Args:
    excel_file: Ruta al archivo Excel.
    csv_file: Ruta al archivo CSV de salida.
  """

  df = pd.read_excel(excel_file)
  df.to_csv(csv_file, index=False)
  print(f"Archivo nuevo creado en {csv_file}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Convierte un archivo Excel a CSV')
  parser.add_argument('excel_file', help='Ruta al archivo Excel')
  parser.add_argument('csv_file', help='Ruta al archivo CSV de salida')
  args = parser.parse_args()

  convert_excel_to_csv(args.excel_file, args.csv_file)
