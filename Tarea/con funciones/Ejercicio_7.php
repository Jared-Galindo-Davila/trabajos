<?php

function calcularRectangulo($base, $altura) {
    $area = $base * $altura;
    $perimetro = 2 * ($base + $altura);
    return ["area" => $area, "perimetro" => $perimetro];
}

$baserect = 5;
$alturarect = 10;
$resultado = calcularRectangulo($baserect, $alturarect);
echo "El área del rectángulo es: {$resultado['area']} y el perímetro es: {$resultado['perimetro']}.";

?>