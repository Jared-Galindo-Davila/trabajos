<?php
$serverName = ""; // Nombre del servidor SQL Server
$connectionOptions = array(
    "Database" => "WEB_PET", // Nombre de tu base de datos
    "Uid" => "usuario", // Usuario de SQL Server
    "PWD" => "contraseña" // Contraseña de SQL Server
);

// Intenta establecer la conexión
$conn = sqlsrv_connect($serverName, $connectionOptions);

if ($conn) {
    echo "Conexión exitosa.";
} else {
    echo "Error al conectar a la base de datos: " . print_r(sqlsrv_errors(), true);
}
?>
