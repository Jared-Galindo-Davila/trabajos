<?php

function esPrimo($numero) {
    if ($numero <= 1) {
        return false;
    }
    for ($i = 2; $i <= sqrt($numero); $i++) {
        if ($numero % $i == 0) {
            return false;
        }
    }
    return true;
}

$numero = 17;
if (esPrimo($numero)) {
    echo "$numero es primo.";
} else {
    echo "$numero no es primo.";
}


?>