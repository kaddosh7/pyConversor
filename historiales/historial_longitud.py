import csv

historiaLongitud = {}


def long_added(entradas, resultado, fecha):
    historiaLongitud[entradas] = {"Resultado": resultado, "Fecha": fecha}
    historial = f'Convertiste: {entradas} grados a {resultado} en fecha: {fecha}'
    return historial


def show_long_conversions():
    i = 0
    for entradas, results in historiaLongitud.items():
        i += 1
        print(f'{i}.- Conversion {entradas}, Resultados: {results["Resultado"]}, Fecha:{results["Fecha"]}')


def export_csv_long_conversions(file_name='historiales/his_docs/long_conversions.csv'):
    with open(file_name, mode='w', newline='', encoding='utf-8') as long_conversions:
        write_history = csv.writer(long_conversions)
        write_history.writerow(['Longitud', 'Resultado', 'Fecha'])

        for clave, valores in historiaLongitud.items():
            write_history.writerow([clave, valores['Resultado'], valores['Fecha']])
