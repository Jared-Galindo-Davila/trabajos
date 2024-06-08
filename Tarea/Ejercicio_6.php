<?php

$colores = ["rojo", "verde", "azul", "rojo", "amarillo"];
$colores_unicos = array_unique($colores);
print_r($colores_unicos); 

$frutas = ["manzana" => "roja", "pera" => "verde", "naranja" => "naranja"];
$igual = array_search("verde", $frutas);
echo $igual; 

?>