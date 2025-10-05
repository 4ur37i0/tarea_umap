import pandas as pd # type: ignore
import umap # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

print("Iniciando el análisis de Fashion-MNIST con UMAP...")

# 1. Cargar los datos
try:
    # Asume que el archivo CSV tiene encabezados. Si no, ajusta `header=None`.
    df = pd.read_csv('fashion-mnist_test.csv') 
    print("Datos cargados exitosamente.")
except FileNotFoundError:
    print("Error: No se encontró el archivo 'fashion-mnist_test.csv'. Asegúrate de que esté en el mismo directorio.")
    exit()

# Mapeo de etiquetas numéricas a nombres de prendas para la leyenda del gráfico
label_map = {
    0: 'T-shirt/top', 1: 'Trouser', 2: 'Pullover', 3: 'Dress', 4: 'Coat',
    5: 'Sandal', 6: 'Shirt', 7: 'Sneaker', 8: 'Bag', 9: 'Ankle boot'
}

# 2. Separar características (píxeles) y etiquetas
# Asumimos que la primera columna 'label' es la etiqueta
if 'label' not in df.columns:
    print("Error: La columna 'label' no se encuentra en el CSV.")
    exit()
    
labels = df['label']
features = df.drop('label', axis=1)

# Normalizar los datos de píxeles (escala de 0 a 1)
features = features / 255.0

print(f"Datos preparados: {features.shape[0]} imágenes con {features.shape[1]} características cada una.")

# 3. Aplicar UMAP (Aquí es donde UMAP reemplaza a tmap)
# n_neighbors, min_dist, n_components son los parámetros principales para jugar
reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2, random_state=42)
print("Ejecutando UMAP... esto puede tardar unos momentos.")
embedding = reducer.fit_transform(features)
print("UMAP completado.")

# 4. Visualizar los resultados
plt.figure(figsize=(12, 10))
# Usamos Seaborn para un gráfico más claro con leyenda automática
scatter = sns.scatterplot(
    x=embedding[:, 0],
    y=embedding[:, 1],
    hue=labels.map(label_map), # Usar los nombres de las prendas para la leyenda
    palette=sns.color_palette("hsv", 10), # Paleta de 10 colores distintos
    s=10, # Tamaño de los puntos
    alpha=0.7
)
plt.title('Visualización de Fashion-MNIST con UMAP', fontsize=16)
plt.xlabel('Componente UMAP 1')
plt.ylabel('Componente UMAP 2')
plt.legend(title='Prenda', bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Guardar el gráfico en un archivo
output_filename = 'fashion_mnist_umap.png'
plt.savefig(output_filename, bbox_inches='tight')
print(f"Gráfico guardado como '{output_filename}'")