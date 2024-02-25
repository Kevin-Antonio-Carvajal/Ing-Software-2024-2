import pymysql
import random
from datetime import datetime, timedelta

def conexion():
    """Establece conexión con la base de datos."""
    return pymysql.connect(host='localhost', user='lab', password='Developer123!', database='lab_ing_software', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def ejecutar_consulta(sql, parametros=()):
    """Ejecuta consulta SQL y retorna resultados o ID."""
    with conexion().cursor() as cursor:
        cursor.execute(sql, parametros)
        conexion().commit()
        return cursor.lastrowid if cursor.lastrowid else cursor.fetchall()

def generar_usuario():
    """Genera datos aleatorios para usuario."""
    numero = random.randint(0, 100)
    return ('Usuario'+str(numero), 'ApellidoP'+str(numero), 'ApellidoM'+str(numero), 'contraseña'+str(numero), 'Usuario'+str(numero)+'@ejemplo.com', random.randint(0, 1))

def generar_pelicula():
    """Genera datos aleatorios para película."""
    generos = ['Aventura', 'Terror', 'Fantasía', 'Documental', 'Musical']
    return ('Película'+str(random.randint(1, 1000)), random.choice(generos), random.randint(80, 150), 1)

def agregar_usuario():
    """Inserta un nuevo usuario en la base de datos."""
    usuario = generar_usuario()
    ejecutar_consulta("INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, %s, %s, %s)", usuario)
    print(f"Usuario creado: {usuario[0]}")

def agregar_pelicula():
    """Inserta una nueva película en la base de datos."""
    pelicula = generar_pelicula()
    ejecutar_consulta("INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)", pelicula)
    print(f"Película añadida: {pelicula[0]}")

def agregar_renta():
    """Registra un alquiler de película."""
    usuario_id = ejecutar_consulta("SELECT idUsuario FROM usuarios ORDER BY RAND() LIMIT 1")[0]['idUsuario']
    pelicula_id = ejecutar_consulta("SELECT idPelicula FROM peliculas ORDER BY RAND() LIMIT 1")[0]['idPelicula']
    fecha_alquiler = datetime.now() - timedelta(days=random.randint(1, 7))
    duracion_alquiler = random.randint(2, 10)
    estado = random.randint(0, 1)
    ejecutar_consulta("INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)", (usuario_id, pelicula_id, fecha_alquiler, duracion_alquiler, estado))
    print("Alquiler registrado.")

def insertar_registros_en_todas_las_tablas():
    """Inserta registros en todas las tablas."""
    agregar_usuario()
    agregar_pelicula()
    agregar_renta()
    print("Registros insertados en todas las tablas.")

def filtrar_usuarios_por_apellido(terminacion):
    """Filtra usuarios por terminación de apellido."""
    usuarios = ejecutar_consulta("SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s", ('%'+terminacion, '%'+terminacion))
    for usuario in usuarios:
        print(usuario)

def cambiar_genero_pelicula(nombre, nuevo_genero):
    """Cambia el género de una película existente."""
    resultado = ejecutar_consulta("UPDATE peliculas SET genero = %s WHERE nombre = %s", (nuevo_genero, nombre))
    print("Género actualizado." if resultado else "Película no encontrada.")

def eliminar_rentas_antiguas():
    """Elimina rentas antiguas (más de 3 días)."""
    fecha_limite = datetime.now() - timedelta(days=3)
    eliminadas = ejecutar_consulta("DELETE FROM rentar WHERE fecha_renta < %s", (fecha_limite,))
    print(f"Rentas eliminadas: {eliminadas}")

