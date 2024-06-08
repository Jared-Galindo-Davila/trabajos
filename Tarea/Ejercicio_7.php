<?php

$frutas = ["manzana" => "roja", "pera" => "verde", "naranja" => "naranja"];
if (array_key_exists("manzana", $frutas)) {
    echo "La clave 'manzana' existe en el array.";
} else {
    echo "La clave 'manzana' no existe en el array.";
}

$colores = ["rojo", "verde", "azul", "amarillo"];
$cantidad = count($colores);
echo $cantidad; 


?>