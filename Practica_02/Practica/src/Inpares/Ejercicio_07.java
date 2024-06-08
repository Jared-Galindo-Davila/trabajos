/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.Scanner;

public class Ejercicio_07 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de estudiantes: ");
        int N = scanner.nextInt();

        int menorA50 = 0;
        int entre50y80 = 0;
        int entre70y80 = 0;
        int mayorIgual80 = 0;

        for (int i = 1; i <= N; i++) {
            System.out.println("Ingrese la calificacion del estudiante " + i + ":");
            int calificacion = scanner.nextInt();

            if (calificacion < 50) {
                menorA50++;
            } else if (calificacion >= 50 && calificacion < 80) {
                entre50y80++;
                if (calificacion >= 70) {
                    entre70y80++;
                }
            } else {
                mayorIgual80++;
            }
        }

        System.out.println("Cantidad de estudiantes con calificacion menor a 50: " + menorA50);
        System.out.println("Cantidad de estudiantes con calificacion entre 50 y 79: " + entre50y80);
        System.out.println("Cantidad de estudiantes con calificacion entre 70 y 79: " + entre70y80);
        System.out.println("Cantidad de estudiantes con calificacion de 80 o más: " + mayorIgual80);

        scanner.close();
    }

}
