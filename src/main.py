import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")   # evita problemas al ejecutar por consola


def cargar_datos():
    df = pd.read_csv("data/spotify_data_clean.csv")
    return df


def procesar_fechas(df):
    df["album_release_date"] = pd.to_datetime(df["album_release_date"], errors="coerce")
    df["release_year"] = df["album_release_date"].dt.year
    return df


def limpiar_datos(df):
    df = df.dropna(subset=["artist_name"]).copy()

    df["artist_genres"] = df["artist_genres"].fillna("SIN_GENERO")
    df["artist_genres"] = df["artist_genres"].str.strip().str.lower()
    df["artist_name"] = df["artist_name"].str.strip()
    df["artist_followers"] = df["artist_followers"].astype(int)

    return df


######################################################
# ANALISIS
######################################################

def top_artistas(df, n=10):
    top = df["artist_name"].value_counts().head(n)
    print("\n--- Top artistas con más canciones ---")
    print(top)
    return top


def top_generos(df, n=10):
    top = df["artist_genres"].value_counts().head(n)
    print("\n--- Top géneros más frecuentes ---")
    print(top)

    top.plot(kind="bar")
    plt.title("Top géneros más comunes")
    plt.xlabel("Género")
    plt.ylabel("Cantidad de canciones")
    plt.tight_layout()
    plt.savefig("output_top_generos.png")
    plt.close()

    return top


def popularidad_por_año(df):
    pop_year = df.groupby("release_year")["track_popularity"].mean()
    print("\n--- Popularidad por año ---")
    print(pop_year)
    return pop_year


def canciones_por_año(df):
    df.groupby("release_year")["track_id"].count().plot()
    plt.title("Canciones por año")
    plt.xlabel("Año")
    plt.ylabel("Cantidad")
    plt.savefig("output_canciones_por_año.png")
    plt.close()


######################################################
# GRAFICOS
######################################################

def graficar_popularidad(df):
    df["track_popularity"].hist(bins=40)
    plt.title("Distribución de popularidad")
    plt.xlabel("Popularidad")
    plt.ylabel("Cantidad de canciones")
    plt.savefig("output_popularidad.png")
    plt.close()


def grafico_followers_vs_pop(df):
    plt.scatter(df["artist_followers"], df["track_popularity"], alpha=0.5)
    plt.xlabel("Followers del artista")
    plt.ylabel("Popularidad de la canción")
    plt.title("Popularidad vs Followers")
    plt.savefig("output_followers_pop.png")
    plt.close()


######################################################
# MAIN
######################################################

def main():
    df = cargar_datos()
    df = procesar_fechas(df)
    df = limpiar_datos(df)

    print("Datos cargados correctamente")

    print("\nColumnas:", df.columns)
    print("\nPrimeras filas:", df.head())

    print("\n--- Estadísticas descriptivas ---")
    print(df.describe())

    # análisis
    top_artistas(df)
    top_generos(df)
    popularidad_por_año(df)
    canciones_por_año(df)

    # gráficos
    graficar_popularidad(df)
    grafico_followers_vs_pop(df)

    # export final
    df.to_csv("datos_procesados.csv", index=False)


if __name__ == "__main__":
    main()