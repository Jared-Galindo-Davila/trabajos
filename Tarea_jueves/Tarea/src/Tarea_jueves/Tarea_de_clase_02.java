/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Tarea_jueves;

import java.util.Scanner;


public class Tarea_de_clase_02 {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese el primer numero: ");
        int num1 = sc.nextInt();

        System.out.println("Ingrese el segundo numero: ");
        int num2 = sc.nextInt();

        System.out.println("Ingrese el tercer numero: ");
        int num3 = sc.nextInt();

        System.out.println("Ingrese el cuarto numero: ");
        int num4 = sc.nextInt();

        int suma = num1 + num2;
        int producto = num3 * num4;

        System.out.println("La suma de los dos primeros numeros es: " + suma);
        System.out.println("El producto de los dos ultimos numeros es: " + producto);
    }
    
}
