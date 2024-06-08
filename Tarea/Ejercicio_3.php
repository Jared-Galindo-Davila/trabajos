<?php

$cadena = "Manzana,Naranja,Pera";
$frutas = explode(",", $cadena);
print_r($frutas); 

$frut = ["Manzana", "Naranja", "Pera"];
$cadena = implode(", ", $frut);
echo $cadena;

?>