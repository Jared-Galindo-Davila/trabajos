<?php

function sumarDigitos($numero) {
    $sum = 0;
    $numero = abs($numero); 
    while ($numero != 0) {
        $sum += $numero % 10;
        $numero = (int)($numero / 10);
    }
    return $sum;
}

$num = 12345;
$suma_digitos = sumarDigitos($num);
echo "La suma de los dígitos de $num es: $suma_digitos";

?>