<?php

$frutas = ["Manzana", "Naranja"];
array_push($frutas, "Pera", "Banana");
print_r($frutas); 

$fruta = ["Manzana", "Naranja", "Pera"];
$ultima_fruta = array_pop($fruta);
echo $ultima_fruta; 

?>