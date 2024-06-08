<?php

function calcularPromedio($numeros) {
    $suma = array_sum($numeros);
    $cantidad = count($numeros);
    $promedio = $suma / $cantidad;
    return $promedio;
}

$lista_numeros = [10, 20, 30, 40, 50];
$promedio = calcularPromedio($lista_numeros);
echo "El promedio de los números es: $promedio";


?>

