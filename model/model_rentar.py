from alchemyClasses.rentar import Renta
from alchemyClasses import db

class AdministradorRentas:
    @staticmethod
    def mostrar_todas_las_rentas():
        """Muestra todas las rentas."""
        todas_las_rentas = Renta.query.all()
        for renta in todas_las_rentas:
            print(f"Renta: {renta}")

    @staticmethod
    def buscar_renta_por_id(id_renta):
        """Busca una renta por ID."""
        renta = Renta.query.get(id_renta)
        if renta:
            print(f"Encontrado: {renta}")
        else:
            print(f"Renta ID {id_renta} no encontrada.")

    @staticmethod
    def actualizar_fecha_renta(id_renta, nueva_fecha):
        """Actualiza la fecha de una renta."""
        renta = Renta.query.get(id_renta)
        if renta:
            renta.fecha_renta = nueva_fecha
            db.session.commit()
        else:
            print(f"Renta ID {id_renta} no encontrada para actualizar.")

    @staticmethod
    def eliminar_renta_por_id(id_renta):
        """Elimina una renta por su ID."""
        renta = Renta.query.get(id_renta)
        if renta:
            db.session.delete(renta)
            db.session.commit()
        else:
            print(f"Renta ID {id_renta} no encontrada para eliminar.")

