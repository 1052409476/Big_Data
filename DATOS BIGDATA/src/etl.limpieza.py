# from calcular_valores 
from    calcular_valores import calcular_suma 
from etl_reporte_llamadas import get_data, save_data
import pandas as pd

# main()
#   datos = leer_datos(nombre del archivo : str) -> pd.dataframe
#   datos = remover_duplicados_y_nulos(datos: pd.dataframe) -> pd.dat
#   datos = convertir_str_a_num(datos, col='EDAD') -> pd.dataframe  
#   datos = corregir_fechas(datos, col='FECHA1') -> pd.dataframe
#   datos = corregir_fechas(datos, col='FECHA2') -> pd.dataframe
#   save_data()

def remremover_duplicados_y_nulos(datos: pd.dataframe):
    # llenar la funcion
    # Eliminar registros duplicados
    print('forma inical', data.shape)
    data = data.drop_duplicates()
    data.reset_index(inplace=true, drop=true)
    print('forma final', data )
    return data_clean

def main():
    datos = get_data(filename='llamas***.csv')
    datos = remremover_duplicados_y_nulos(df=datos)

    save_data(reporte=)