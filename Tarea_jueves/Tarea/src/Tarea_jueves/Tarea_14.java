/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Tarea_jueves;

import java.util.Scanner;


public class Tarea_14 {

  
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Ingrese la radio del circulo: ");
        double r=sc.nextDouble();
        
        double pi=3.14;
        
        double area=pi * Math.pow(r, 2);
        
        
        System.out.println("El area del circulo con radio de " + r + " es: " + area);
        
        

    }
    
}
