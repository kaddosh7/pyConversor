import csv

historiaTemperaturas = {}


def temp_added(entradas, resultado, fecha):
    historiaTemperaturas[entradas] = {"Resultado": resultado, "Fecha": fecha}
    historial = f'Convertiste: {entradas} grados a {resultado} en fecha: {fecha}'
    return historial


def show_temp_conversions():
    i = 0
    for entradas, results in historiaTemperaturas.items():
        i += 1
        print(f'{i}.- Conversion {entradas}, Resultados: {results["Resultado"]}, Fecha:{results["Fecha"]}')


def export_csv_temp_conversions(file_name='historiales/his_docs/temp_conversions.csv'):
    with open(file_name, mode='w', newline='', encoding='utf-8') as temp_conversions:
        write_history = csv.writer(temp_conversions)
        write_history.writerow(['Temperatura', 'Resultado', 'Fecha'])

        for clave, valores in historiaTemperaturas.items():
            write_history.writerow([clave, valores['Resultado'], valores['Fecha']])
