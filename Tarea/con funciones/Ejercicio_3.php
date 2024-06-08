<?php

function celsiusaFahren($celsius) {
    $fahren = ($celsius * 9/5) + 32;
    return $fahren;
}

$gradoscelsius = 25;
$fahrenheit = celsiusaFahren($grados_celsius);
echo "$gradoscelsius grados Celsius son equivalentes a $fahren grados Fahrenheit.";



?>
