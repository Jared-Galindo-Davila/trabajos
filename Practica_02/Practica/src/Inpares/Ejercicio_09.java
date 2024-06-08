/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.Scanner;

public class Ejercicio_09 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] calificaciones = new int[100];

        System.out.println("Ingrese las calificaciones de los estudiantes:");
        for (int i = 0; i < calificaciones.length; i++) {
            calificaciones[i] = sc.nextInt();
        }

        int suma = 0;
        for (int calificacion : calificaciones) {
            suma += calificacion;
        }

        double promedio = (double) suma / calificaciones.length;

        int estudiantesArribaPromedio = 0;

        for (int calificacion : calificaciones) {
            if (calificacion > promedio) {
                estudiantesArribaPromedio++;
            }
        }

        System.out.println("Promedio del grupo: " + promedio);
        System.out.println("Estudiantes con calificaciones arriba del promedio: " + estudiantesArribaPromedio);

      
    }

}
