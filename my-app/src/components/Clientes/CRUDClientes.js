import React, { useState } from 'react';
import './CRUDClientes.css';

function CRUDClientes() {
  const [clientes, definir] = useState([]);
  const [originalCliente, original] = useState(null);
  const [nuevo, actualizar] = useState({
    nombre: '',
    apPat: '',
    apMat: '',
    email: '',
    password: '',
    superUser: false
  });
  const [editar, establecer] = useState(null);

  const cambiar = (e) => {
    const { name, type, checked, value } = e.target;
    const finalValue = type === 'checkbox' ? checked : value;
  
    if (editar) {
      // Actualiza los campos del cliente que está siendo editado en tiempo real
      const actualizados = clientes.map(cliente =>
        cliente.id === editar ? {...cliente, [name]: finalValue} : cliente
      );
      definir(actualizados);
      // También actualiza nuevo para mantener el formulario sincronizado
      actualizar(prev => ({ ...prev, [name]: finalValue }));
    } else {
      actualizar(prev => ({ ...prev, [name]: finalValue }));
    }
  };

  const añadir = () => {
    // Verificación simple para el formato del correo electrónico
    if (!nuevo.email.includes('@') || nuevo.email.indexOf('@') === nuevo.email.length - 1) {
      alert('Por favor, ingresa un correo electrónico válido ejemplo: hola@g, es decir Inlcuye @ y escribe una parte despues del @');
      return;
    }
    definir([...clientes, { ...nuevo, id: Date.now() }]);
    actualizar({ nombre: '', apPat: '', apMat: '', email: '', password: '', superUser: false });
  };

  const empezar = (id) => {
    const cliente = clientes.find(cliente => cliente.id === id);
    establecer(id);
    actualizar(cliente);
    original({ ...cliente });  // Guarda una copia del estado original
  };

  const guardar = () => {
    if (!nuevo.email.includes('@') || nuevo.email.indexOf('@') === nuevo.email.length - 1) {
      alert('Por favor, ingresa un correo electrónico válido ejemplo: hola@g, es decir Inlcuye @ y escribe una parte despues del @');
      return;
    }
    definir(clientes.map(cliente =>
      cliente.id === editar ? {...nuevo} : cliente
    ));
    establecer(null);
  };

  const eliminar = (id) => {
    definir(clientes.filter(cliente => cliente.id !== id));
  };

  return (
    <div className="usuarioss">
      <h2>Usuarios</h2>
      <div className="formulario">
        <input type="text" name="nombre" placeholder="Nombre" value={nuevo.nombre} onChange={cambiar} />
        <input type="text" name="apPat" placeholder="apPat" value={nuevo.apPat} onChange={cambiar} />
        <input type="text" name="apMat" placeholder="ApMat" value={nuevo.apMat} onChange={cambiar} />
        <input type="email" name="email" placeholder="Email" value={nuevo.email} onChange={cambiar} />
        <input type="password" name="password" placeholder="Password" value={nuevo.password} onChange={cambiar} />
        <label>
          SuperUser:
          <input type="checkbox" name="superUser" checked={nuevo.superUser} onChange={cambiar} />
        </label>
        {editar ? (
          <>
            <button onClick={guardar}>Guardar Edicion</button>
          </>
        ) : (
          <button onClick={añadir}>Agregar</button>
        )}
      </div>
      <div className="lista">
        {clientes.map(cliente => (
          <div key={cliente.id} className="cliente">
            <ul>
              <li>Nombre: {cliente.nombre}</li>
              <li>apPat: {cliente.apPat}</li>
              <li>ApMat: {cliente.apMat}</li>
              <li>Email: {cliente.email}</li>
              <li>Password: {cliente.password}</li>
              <li>SuperUser: {cliente.superUser ? 'Yes' : 'No'}</li>
            </ul>
            <button onClick={() => empezar(cliente.id)}>Editar</button>
            <button onClick={() => eliminar(cliente.id)}>Eliminar</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CRUDClientes;
