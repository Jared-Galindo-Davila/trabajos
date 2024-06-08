/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Tarea_jueves;

import java.util.Scanner;


public class Tarea_15 {

   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double lado;
        System.out.println("Ingrese el valor de un lado: ");
        lado=sc.nextDouble();
        
        //double lado=20:
        //double area=Math.pow(lado,2);
        //double perimetro=4*lado

       
        double area=Math.pow(lado, 2);
        System.out.println("EL area del cuadrado es:" + area + "cm");
       
        double perimetro=4*lado;
        System.out.println("El perimetro del cuadrado es: " + perimetro + "cm");
    }
    
}
