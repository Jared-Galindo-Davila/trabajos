<?php
if($_SERVER['REQUEST_METHOD']==='POST'){
    //Paso#2: Declaramos las variables
    $nombre=$_POST['nombre'];
    $apellido=$_POST['apellido'];
    $email=$_POST['email'];
    $telefono=$_POST['telefono'];
    $fecha=$_POST['fecha'];
    $hora=$_POST['hora'];


    
    //paso#3: establecer destinatario
    $destinatario='gbarboza@senati.pe';
    //paso#4: establecer el asunto
    $asunto='CONTACTO DESDE MI SITIO WEB';
    //PASO#5: ESTABLECEMOS EL CUERPO DEL MENSAJE 
    $cuerpo="NOMBRE: ". $nombre . "\n";
    $cuerpo.="Apellido: ". $apellido . "\n";
    $cuerpo.="EMAIL: ". $email . "\n";
    $cuerpo.="CELULAR: ". $telefono . "\n";
    $cuerpo.="Fecha: ". $fecha . "\n";
    $cuerpo.="Hora: ". $hora . "\n";

    //paso#6: establecemos el metodo que nos va a permitir 
    //juntar las variables y enviarlo finalmente 
    //al correo que le hemos indicado
    if(mail($destinatario, $asunto, $cuerpo)){
        echo "El mensaje se envio correctamente";
    }else{
        echo "¡HORROR! El mensaje no se envio.";
    }
}
?>