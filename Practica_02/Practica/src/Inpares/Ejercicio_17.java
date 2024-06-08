/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.Scanner;

public class Ejercicio_17 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese la edad de la dama: ");
        int edad = scanner.nextInt();
        System.out.print("Ingrese la talla de la dama en metros: ");
        double talla = scanner.nextDouble();
        if (edad >= 17 && talla >= 165) {
            System.out.println("Postulante a la Escuela de Oficiales");
        } else {
            System.out.println("No cumple con los requisitos para postular a la Escuela de Oficiales");

        }

    }
}