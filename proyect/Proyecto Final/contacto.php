<?php
if($_SERVER['REQUEST_METHOD']==='POST'){
    //Paso#2: Declaramos las variables
    $nombre=$_POST['nombre'];
    $email=$_POST['email'];
    $mensaje=$_POST['mensaje'];

    //paso#3: establecer destinatario
    $destinatario='gbarboza@senati.pe';
    //paso#4: establecer el asunto
    $asunto='CONTACTO DESDE MI SITIO WEB';
    //PASO#5: ESTABLECEMOS EL CUERPO DEL MENSAJE 
    $cuerpo="NOMBRE: ". $nombre . "\n";
    $cuerpo.="EMAIL: ". $email . "\n";
    $cuerpo.="MENSAJE: ". $mensaje . "\n";

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