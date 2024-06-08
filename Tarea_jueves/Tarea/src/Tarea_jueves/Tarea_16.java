/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Tarea_jueves;

import java.util.Scanner;


public class Tarea_16 {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double longitud,ancho;
        System.out.println("Ingrese el valor de la longitud del rectangulo: ");
        longitud=sc.nextDouble();
        
        System.out.println("Ingrese el valor del ancho de un rectangulo: ");
        ancho = sc.nextDouble();

       
        double area= longitud * ancho;
        System.out.println("EL area del rectangulo es:" + area + "cm");
       
        double perimetro=2*(longitud+ancho);
        System.out.println("El perimetro del rectangulo es: " + perimetro + "cm");
    }
    
}
