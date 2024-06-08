/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.Scanner;

public class Ejercicio_13 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el numero de cita del paciente: ");
        int numeroCita = sc.nextInt();

        double montoCita = 0;
        if (numeroCita <= 3) {
            montoCita = 200;
        } else if (numeroCita <= 5) {
            montoCita = 150;
        } else if (numeroCita <= 8) {
            montoCita = 100;
        } else {
            montoCita = 50;
        }
        double montoTotalTratamiento = montoCita * numeroCita;

        //double montoTotalTratamiento = 200 * 3 + 150 * 2 + 100 * 3 + 50 * (numeroCita - 8);
        System.out.println("Monto a pagar por la cita: S/. " + montoCita);
        System.out.println("Monto total pagado por el tratamiento: S/. " + montoTotalTratamiento);
    }

}
