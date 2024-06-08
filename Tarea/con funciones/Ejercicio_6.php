<?php

function tablaMultiplicar($numero, $limite) {
    
    echo "Tabla del $numero \n";
    for ($i = 1; $i <= $limite; $i++) {
        echo "$numero x $i = " . ($numero * $i."\n");
    }
    
}

$numero_tabla = 7;
$limite_tabla = 10;
tablaMultiplicar($numero_tabla, $limite_tabla);

?>