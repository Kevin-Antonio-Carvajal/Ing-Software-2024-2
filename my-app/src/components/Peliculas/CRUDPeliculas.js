import React, { useState } from 'react';
import './CRUDPeliculas.css';

function CRUDPeliculas() {
  const [peliculas, definir] = useState([]);
  const [peliculaActual, actualizar] = useState({ nombre: '', genero: '', duracion: '', inventario: '' });
  const [editar, establecer] = useState(null);

  const cambiar = (e) => {
    const { name, value } = e.target;
    const actualizados = name === "duracion" || name === "inventario" ? parseInt(value, 10) : value;
  
    if (editar) {
      definir(peliculas.map(pelicula =>
        pelicula.id === editar ? { ...pelicula, [name]: actualizados } : pelicula
      ));
      actualizar(prevState => ({ ...prevState, [name]: actualizados }));
    } else {
      actualizar(prevState => ({ ...prevState, [name]: actualizados }));
    }
  };

  const añadir = () => {
    definir([...peliculas, { ...peliculaActual, id: Date.now() }]);
    actualizar({ nombre: '', genero: '', duracion: '', inventario: '' });
  };

  const empezar = (id) => {
    const pelicula = peliculas.find(pelicula => pelicula.id === id);
    establecer(id);
    actualizar(pelicula);
  };

  const guardar = () => {
    establecer(null);
  };

  const eliminar = (id) => {
    definir(peliculas.filter(pelicula => pelicula.id !== id));
  };

  return (
    <div className="Peliculas">
      <h2>Películas</h2>
      <div className="formulario-pelicula">
        <input type="text" name="nombre" placeholder="Nombre" value={peliculaActual.nombre} onChange={cambiar} />
        <input type="text" name="genero" placeholder="Género" value={peliculaActual.genero} onChange={cambiar} />
        <input type="number" name="duracion" placeholder="Duración" value={peliculaActual.duracion} onChange={cambiar} />
        <input type="number" name="inventario" placeholder="Inventario" value={peliculaActual.inventario} onChange={cambiar} />
        {editar ? (
          <>
            <button onClick={guardar}>Guardar Edicion</button>
          </>
        ) : (
          <button onClick={añadir}>Agregar</button>
        )}
      </div>
      <div className="lista">
        {peliculas.map(pelicula => (
          <div key={pelicula.id} className="pelicula">
            <ul>
              <li>Nombre: {pelicula.nombre}</li>
              <li>Género: {pelicula.genero}</li>
              <li>Duración: {pelicula.duracion} min</li>
              <li>Inventario: {pelicula.inventario} unidades</li>
            </ul>
            <button onClick={() => empezar(pelicula.id)}>Editar</button>
            <button onClick={() => eliminar(pelicula.id)}>Eliminar</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CRUDPeliculas;
