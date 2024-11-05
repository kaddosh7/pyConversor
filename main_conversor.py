# °C = (°F - 32) / 1.8  |  °F = (°C * 1.8) + 32  |  °K = °C + 273.15
from ConverDef.conversor_temperatura.celsius import conversor_c_f, conversor_c_k
from ConverDef.conversor_temperatura.fahrenheit import conversor_f_c, conversor_f_k
from ConverDef.conversor_temperatura.kelvin import conversor_k_c, conversor_k_f

from ConverDef.conversor_longitud.metros import conversor_m_k, conversor_m_p, conversor_m_mi
from ConverDef.conversor_longitud.kilometros import conversor_km_m, conversor_km_mi, conversor_km_p
from ConverDef.conversor_longitud.pies import conversor_p_m, conversor_p_km, conversor_p_mi
from ConverDef.conversor_longitud.millas import conversor_mi_m, conversor_mi_km, conversor_mi_p


print("\n=========================")
print("Sistema de Conversiones")
print("=========================")
while True:
    print(
        "\nOPCIONES: \n"
        "1. Conversor de Temperaturas\n"
        "2. Conversor de Longitudes\n"
        "0. Cerrar Sistema\n"
    )
    entrada = int(input("Seleccione una Opción: "))
    if entrada == 1:
        import temp_menu
        while True:
            op = float(input("Convertir a: "))
            if op == 1:
                inputNum = input(f"Cantidad de Grado: ")
                c_f = conversor_c_f(float(inputNum))
                cf_result = f"{c_f:.3f}°F"
                print(inputNum, "°C =", cf_result.format(c_f))
            elif op == 2:
                inputNum = input(f"Cantidad de Grado: ")
                c_k = conversor_c_k(float(inputNum))
                ck_result = f"{c_k:.3f}°K"
                print(inputNum, "°C =", ck_result.format(c_k))
            elif op == 3:
                inputNum = input(f"Cantidad de Grado: ")
                f_c = conversor_f_c(float(inputNum))
                fc_result = f"{f_c:.3f}°C"
                print(inputNum, "°F =", fc_result.format(f_c))
            elif op == 4:
                inputNum = input(f"Cantidad de Grado: ")
                f_k = conversor_f_k(float(inputNum))
                fk_result = f"{f_k:.3f}°K"
                print(inputNum, "°F =", fk_result.format(f_k))
            elif op == 5:
                inputNum = input(f"Cantidad de Grado: ")
                k_c = conversor_k_c(float(inputNum))
                kc_result = f"{k_c:.3f}°K"
                print(inputNum, "°F =", kc_result.format(k_c))
            elif op == 6:
                inputNum = input(f"Cantidad de Grado: ")
                k_f = conversor_k_f(float(inputNum))
                kf_result = f"{k_f:.3f}°K"
                print(inputNum, "°F =", kf_result.format(k_f))
            elif op == 0:
                print("Hasta Luego!")
                break
            else:
                print("Selccione una opción valida")
    elif entrada == 2:
        import long_menu
        # mts a km
        while True:
            op = float(input(f"Tipo de Medida: "))
            if op == 1:
                inputDist = input(f"Distancia: ")
                m_km = conversor_m_k(float(inputDist))
                mkm_result = f"{m_km:.6f} Kms"
                print(inputDist, "m = ", mkm_result.format(m_km))
            elif op == 2:
                inputDist = input(f"Distancia: ")
                m_p = conversor_m_p(float(inputDist))
                mp_result = f"{m_p:.6f} Pies"
                print(inputDist, "m = ", mp_result.format(m_p))
            elif op == 3:
                inputDist = input(f"Distancia: ")
                m_mi = conversor_m_mi(float(inputDist))
                mmi_result = f"{m_mi:.6f} Millas"
                print(inputDist, "m = ", mmi_result.format(m_mi))

            elif op == 4:
                inputDist = input(f"Distancia: ")
                km_m = conversor_km_m(float(inputDist))
                kmm_result = f"{km_m:.6f} metros"
                print(inputDist, "Km = ", kmm_result.format(km_m))
            elif op == 5:
                inputDist = input(f"Distancia: ")
                km_p = conversor_km_p(float(inputDist))
                kmp_result = f"{km_p:.6f} pies"
                print(inputDist, "Km = ", kmp_result.format(km_p))
            elif op == 6:
                inputDist = input(f"Distancia: ")
                km_mi = conversor_km_mi(float(inputDist))
                kmmi_result = f"{km_mi:.6f} Millas"
                print(inputDist, "Km = ", kmmi_result.format(km_mi))

            elif op == 7:
                inputDist = input(f"Distancia: ")
                p_m = conversor_p_m(float(inputDist))
                pm_result = f"{p_m:.6f} metros."
                print(inputDist, "pies = ", pm_result.format(p_m))
            elif op == 8:
                inputDist = input(f"Distancia: ")
                p_km = conversor_p_km(float(inputDist))
                pkm_result = f"{p_km:.6f} Kms"
                print(inputDist, "pies = ", pkm_result.format(p_km))
            elif op == 9:
                inputDist = input(f"Distancia: ")
                p_m = conversor_p_mi(float(inputDist))
                pkm_result = f"{p_m:.6f} metros."
                print(inputDist, "pies = ", pkm_result.format(p_m))

            elif op == 10:
                inputDist = input(f"Distancia: ")
                mi_m = conversor_mi_m(float(inputDist))
                mim_result = f"{mi_m:.6f} metros."
                print(inputDist, "millas = ", mim_result.format(mi_m))
            elif op == 11:
                inputDist = input(f"Distancia: ")
                mi_km = conversor_mi_km(float(inputDist))
                mikm_result = f"{mi_km:.6f} Kms"
                print(inputDist, "millas = ", mikm_result.format(mi_km))
            elif op == 12:
                inputDist = input(f"Distancia: ")
                mip = conversor_mi_p(float(inputDist))
                mip_result = f"{mip:.6f} pies."
                print(inputDist, "millas = ", mip_result.format(mip))
            elif op == 0:
                print("Hasta Luego!")
                break
            else:
                print("Seleccione una opción valida")
    elif entrada == 0:
        print("Adios!")
        exit()
    else:
        print("Seleccione una opción válida")
