-- USAR LA BD PRUEBA

CREATE TABLE demostracion_triggers(
    id serial primary key not null,
    mensaje text,
    created_at timestamp default now()
);

create function registrar_accion()
returns trigger as $$
begin
    --Insertar un mensaje en la tabla de demostracion
    insert into demostracion_triggers(mensaje) values('SE INSERTO UN NUEVO REGISTRO');
    -- NEW > sera la informacion que me viene en el trigger, la informacion que se agregara ni bien se ejecute el trigger
    return new;
end;
$$ language plpgsql;

create trigger trigger_registrar_registros
after insert on clientes
for each row -->cada vez que se haga un nuevo ingreso de un cliente, se ejecutara el trigger
execute function registrar_accion();

 INSERT INTO clientes (nombre, correo, status, activo) VALUES
  ('Jose Martines Perez', 'jmartines@gmail.com', 'BUEN_CLIENTE', true);

CREATE OR REPLACE FUNCTION crear_clientes_y_cuentas(
    nombre_cliente text,
    correo_cliente text,
    status_cliente status_enum,
    cliente_activo boolean,
    tipo_moneda tipo_moneda_enum)
returns VOID as $$
--> justo antes de empezar la funcion, tenemos que declarar las variables a utilizar en la funcion
DECLARE 
    nuevo_cliente_id int; --< este cliente_id lo usare ppara, al momento de crear la cuenta, relacionarlo con él
    -- inicia la ejecucion de la funcion
begin
    -- RETURNING se puede llamar cuando hacemos un ISERT | UPDATE | DELETE y sirve para retornar la informacion resultante de la operacion
    insert into clientes(nombre, correo, status, activo) values(nombre_cliente, correo_cliente, status_cliente, cliente_activo)
    returning id into nuevo_cliente_id;
    --> ahora procedemos a crear la cuenta del cliente
    insert into cuentas(numero_cuenta, tipo_moneda, cliente_id) values('', tipo_moneda, nuevo_cliente_id);
end;
$$ language plpgsql;

--> para ver las funciones que existen en la BD 
\df

-- https://www.postgresql.org/docs/current/tutorial-transactions.html
BEGIN;
INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                    ( 4, null, 100, NOW());


INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                    (4, 3, 20, NOW());


INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                    (null, 4, 40, NOW());

-- TODO ESTA BIEN Guardamos los cambios de manera permanente
COMMIT;

-- SI LLEGASE A FALLAR ALGO PODEMOS DEJAR SIN EFECTO ESTE GRUPO DE OPERACION
ROLLBACK;