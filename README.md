Para correr el programa insertar el siguiente comando en la raiz del proyecto,
ejecutarlo y se creara el visual del cluster de datos a nivel de la raiz

docker run --rm -v "$(pwd):/app" umap-tarea:v1 python main.py