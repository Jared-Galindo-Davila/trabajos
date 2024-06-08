<?php

function listaPrimos($limite) {
    $primos = [];
    for ($i = 2; $i <= $limite; $i++) {
        if (esPrimo($i)) {
            $primos[] = $i;
        }
    }
    return $primos;
}

$limiteprimos = 30;
$listaprimos = listaPrimos($limiteprimos);
echo "Los números primos hasta $limiteprimos son: " . implode(", ", $listaprimos);

?>