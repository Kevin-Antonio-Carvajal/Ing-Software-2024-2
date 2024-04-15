import React, { useState } from 'react';
import './CRURentas.css';

function CRURentas() {
  const [rentas, definir] = useState([]);
  const [rentaActual, actualizar] = useState({
    idUsuario: '',
    idPelicula: '',
    fecha_renta: '',
    dias_de_renta: '',
    estatus: '1'
  });
  const [editar, establecer] = useState(null);

  const cambiar = (e) => {
    const { name, value } = e.target;
    const valorActualizado = value;  // No necesitas verificar el tipo si todos los inputs manejan valores directamente compatibles
  
    const rentaModificada = {...rentaActual, [name]: valorActualizado}; // Crea una nueva versión de rentaActual con el cambio aplicado
    actualizar(rentaModificada); // Actualiza rentaActual
  
    if (editar) {
      // Actualiza la lista de rentas en tiempo real
      const rentasActualizadas = rentas.map(renta =>
        renta.id === editar ? rentaModificada : renta
      );
      definir(rentasActualizadas); // Actualiza la lista de rentas con la renta modificada
    }
  };

  const añadir = () => {
    definir([...rentas, { ...rentaActual, id: Date.now() }]);
    actualizar({
      idUsuario: '',
      idPelicula: '',
      fecha_renta: '',
      dias_de_renta: '',
      estatus: '1'
    });
  };

  const empezar = (id) => {
    const renta = rentas.find(renta => renta.id === id);
    establecer(id);
    actualizar(renta);
  };

  const guardar = () => {
    definir(rentas.map(renta => 
      renta.id === editar ? {...rentaActual} : renta
    ));
    establecer(null);
  };

  const eliminar = (id) => {
    definir(rentas.filter(renta => renta.id !== id));
  };

  return (
    <div className="Renta">
      <h2>Rentas</h2>
      <div className="formulario-renta">
        <input type="text" name="idUsuario" placeholder="idUsuario" value={rentaActual.idUsuario} onChange={cambiar} />
        <input type="text" name="idPelicula" placeholder="idPelicula" value={rentaActual.idPelicula} onChange={cambiar} />
        <input type="date" name="fecha_renta" placeholder="Fecha de Renta" value={rentaActual.fecha_renta} onChange={cambiar} />
        <input type="number" name="dias_de_renta" placeholder="dias_de_renta" value={rentaActual.dias_de_renta} onChange={cambiar} />
        <select name="estatus" value={rentaActual.estatus} onChange={cambiar}>
          <option value="1">1</option>  
          <option value="0">0</option>  
        </select>
        {editar ? (
          <>
            <button onClick={guardar}>Guardar Edicion</button>
          </>
        ) : (
          <button onClick={añadir}>Agregar Renta</button>
        )}
      </div>
      <div className="lista">
        {rentas.map(renta => (
          <div key={renta.id} className="renta">
            <ul>
              <li>idUsuario: {renta.idUsuario}</li>
              <li>idPelicula: {renta.idPelicula}</li>
              <li>Fecha de Renta: {renta.fecha_renta}</li>
              <li>dias_de_renta: {renta.dias_de_renta}</li>
              <li>Estatus: {renta.estatus}</li>
            </ul>
            <button onClick={() => empezar(renta.id)}>Editar</button>
            <button onClick={() => eliminar(renta.id)}>Eliminar</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CRURentas;
