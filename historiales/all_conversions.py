import csv
historiaConversiones = {}


def data_added(entradas, resultado, fecha):
    historiaConversiones[entradas] = {"Resultados": resultado, "Fechas": fecha}
    historial = f'Convertiste: {entradas} grados a {resultado} en fecha: {fecha}'
    return historial


def export_csv_all_conversions(file_name='all_conversions.csv'):
    with open(file_name, mode='w', newline='', encoding='utf-8') as all_conversions:
        write_history = csv.writer(all_conversions)
        write_history.writerow(['Datos', 'Resultados', 'Fechas'])

        for clave, datos in historiaConversiones.items():
            write_history.writerow([clave, datos['Resultados'], datos['Fechas']])
