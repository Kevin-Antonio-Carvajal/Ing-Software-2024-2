from alchemyClasses.peliculas import Pelicula
from alchemyClasses import db

class AdministradorPeliculas:
    @staticmethod
    def mostrar_todas_las_peliculas():
        """Muestra todas las películas."""
        lista_peliculas = Pelicula.query.all()
        for pelicula in lista_peliculas:
            print(f"Película: {pelicula}")

    @staticmethod
    def buscar_pelicula_por_id(id_pelicula):
        """Busca y muestra una película por su ID."""
        pelicula = Pelicula.query.get(id_pelicula)
        if pelicula:
            print(f"Encontrada: {pelicula}")
        else:
            print(f"Película ID {id_pelicula} no encontrada.")

    @staticmethod
    def renombrar_pelicula_por_id(id_pelicula, nuevo_nombre):
        """Renombra una película dado su ID."""
        pelicula = Pelicula.query.get(id_pelicula)
        if pelicula:
            pelicula.nombre = nuevo_nombre
            db.session.commit()
        else:
            print(f"Película ID {id_pelicula} no encontrada para renombrar.")

    @staticmethod
    def eliminar_pelicula_por_id(id_pelicula):
        """Elimina una película por su ID."""
        pelicula = Pelicula.query.get(id_pelicula)
        if pelicula:
            db.session.delete(pelicula)
            db.session.commit()
        else:
            print(f"Película ID {id_pelicula} no encontrada para eliminar.")

