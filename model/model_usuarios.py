from alchemyClasses.usuarios import Usuario
from alchemyClasses import db

class AdministradorUsuarios:
    @staticmethod
    def mostrar_todos_los_usuarios():
        """Lista todos los usuarios."""
        todos_los_usuarios = Usuario.query.all()
        for usuario in todos_los_usuarios:
            print(f"Usuario: {usuario}")

    @staticmethod
    def buscar_usuario_por_id(id_usuario):
        """Encuentra un usuario por ID."""
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            print(f"Encontrado: {usuario}")
        else:
            print(f"Usuario ID {id_usuario} no localizado.")

    @staticmethod
    def actualizar_nombre_por_id(id_usuario, nuevo_nombre):
        """Actualiza el nombre de un usuario por su ID."""
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            usuario.nombre = nuevo_nombre
            db.session.commit()
        else:
            print(f"Usuario ID {id_usuario} no disponible para actualizar.")

    @staticmethod
    def eliminar_usuario_por_id(id_usuario):
        """Elimina un usuario por su ID."""
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        else:
            print(f"Usuario ID {id_usuario} no encontrado para eliminar.")

