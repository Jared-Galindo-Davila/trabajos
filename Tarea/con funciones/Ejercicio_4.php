<?php

function fibonacci($n) {
    $fib = [0, 1];
    for ($i = 2; $i <= $n; $i++) {
        $fib[$i] = $fib[$i - 1] + $fib[$i - 2];
    }
    return $fib;
}

$limite = 10;
$serie_fibonacci = fibonacci($limite);
echo "Los primeros $limite números de la serie Fibonacci son: " . implode(", ", $serie_fibonacci);


?>
