import pandas as pd
import matplotlib.pyplot as plt
from scraper import get_data
from analysis import analizar

def main():
    print("Obteniendo datos...")
    data = get_data()

    df = pd.DataFrame(data)
    df.to_csv("precios.csv", index=False)
    print("Datos guardados en precios.csv")

    print("Analizando...")
    resultado = analizar(df.head(10).to_string())

    print("\nRESULTADO:\n")
    print(resultado)

    # Preparar datos para gráfico
    # Convertimos precios a números (quitando símbolo £ y posibles caracteres extraños)
    df['price_num'] = (
        df['price']
        .str.replace('£', '', regex=False)    # quitar el símbolo £
        .str.replace('Â', '', regex=False)    # quitar el carácter extraño
        .str.replace(',', '', regex=False)    # quitar comas si hay miles
        .str.strip()                           # quitar espacios al inicio y fin
        .astype(float)                         # convertir a float
    )

    # Crear histograma de precios
    plt.figure(figsize=(10,6))
    plt.hist(df['price_num'], bins=15, color='skyblue', edgecolor='black')
    plt.title("Distribución de Precios")
    plt.xlabel("Precio (£)")
    plt.ylabel("Cantidad de productos")
    plt.grid(axis='y')
    plt.savefig("histograma_precios.png")  # Guarda la imagen
    plt.show()

if __name__ == "__main__":
    main()