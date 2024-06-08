<?php

function contarPalabras($frase) {
    $palabras = str_word_count($frase);
    return $palabras;
}

$frase = "Hola ingeniero Wilman";
$cantidadpalabras = contarPalabras($frase);
echo "La frase tiene $cantidadpalabras palabras.";

?>