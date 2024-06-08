/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.Scanner;


public class Ejercicio_19 {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int NUM_TRABAJADORES = 20;
        
        int[] horasTrabajadas = new int[NUM_TRABAJADORES];
        double[] pagoPorHora = new double[NUM_TRABAJADORES];

        for (int i = 0; i < NUM_TRABAJADORES; i++) {
            System.out.println("Ingrese las horas trabajadas del trabajador " + (i + 1) + ":");
            horasTrabajadas[i] = sc.nextInt();
            System.out.println("Ingrese el pago por hora del trabajador " + (i + 1) + ":");
            pagoPorHora[i] = sc.nextDouble();
        }

        for (int i = 0; i < NUM_TRABAJADORES; i++) {
            double sueldoSemanal = calcularSueldoSemanal(horasTrabajadas[i], pagoPorHora[i]);
            System.out.println("Sueldo semanal del trabajador " + (i + 1) + ": S/. " + sueldoSemanal);
        }

    }

    public static double calcularSueldoSemanal(int horasTrabajadas, double pagoPorHora) {
        double sueldo = 0;

        if (horasTrabajadas > 50) {
            System.out.println("Error: El trabajador ha excedido las 50 horas permitidas.");
        } else {
            if (horasTrabajadas > 40) {
                int horasExtras = horasTrabajadas - 40;
                sueldo = (40 * pagoPorHora) + (horasExtras * pagoPorHora * calcularFactorHorasExtras(horasExtras));
            } else {
                sueldo = horasTrabajadas * pagoPorHora;
            }
        }

        return sueldo;
    }

    public static double calcularFactorHorasExtras(int horasExtras) {
        if (horasExtras >= 41 && horasExtras <= 45) {
            return 2;
        } else if (horasExtras >= 46 && horasExtras <= 50) {
            return 3;
        } else {
            return 0;
        }
    }
    
}
