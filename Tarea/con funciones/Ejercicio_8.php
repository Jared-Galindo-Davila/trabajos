<?php

function esPalindromo($palabra) {
    $palabra = strtolower(str_replace(' ', '', $palabra));
    return $palabra == strrev($palabra);
}

$palabra = "reconocer";
if (esPalindromo($palabra)) {
    echo "$palabra es un palíndromo.";
} else {
    echo "$palabra no es un palíndromo.";
}

?>