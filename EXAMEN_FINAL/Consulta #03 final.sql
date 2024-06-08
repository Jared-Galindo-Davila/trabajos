CREATE DATABASE Finali
USE Finali

CREATE TABLE empleados(
id_empleado VARCHAR(40) PRIMARY KEY,
nombre VARCHAR(40) NOT NULL,
telefono CHAR(9) NOT NULL,
domicilio VARCHAR(40) NOT NULL,
dni CHAR(8) NOT NULL,
contraseña VARCHAR(20) NOT NULL,
designacion VARCHAR(40) NOT NULL
)

CREATE TABLE factura(
id_factura VARCHAR(40) PRIMARY KEY,
nombre_cliente VARCHAR(40) NOT NULL,
telefono_factura CHAR(9) NOT NULL,
categoria VARCHAR(40) NOT NULL,
sub_categoria VARCHAR(40) NOT NULL,
articulo VARCHAR(40) NOT NULL,
cantidad INT NOT NULL,
precio FLOAT NULL
)

SELECT * FROM empleados
SELECT * FROM factura