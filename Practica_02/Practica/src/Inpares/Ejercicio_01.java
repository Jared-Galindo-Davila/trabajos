/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.ArrayList;
import java.util.List;


public class Ejercicio_01 {

    
    public static void main(String[] args) {
        List<Chofer> choferes = new ArrayList<>();
        choferes.add(new Chofer("Juan", new int[]{8, 7, 6, 8, 9, 5}, 10));
        choferes.add(new Chofer("Maria", new int[]{7, 7, 7, 7, 7, 7}, 12));
        choferes.add(new Chofer("Pedro", new int[]{9, 9, 9, 9, 9, 9}, 11));
        choferes.add(new Chofer("Luis", new int[]{8, 8, 8, 8, 8, 8}, 9));
        choferes.add(new Chofer("Ana", new int[]{6, 6, 6, 6, 6, 6}, 13));

        // Calcular los datos requeridos y generar el reporte
        int totalHorasSemana = 0;
        double totalPagoEmpresa = 0;
        int mayorHorasLunes = 0;
        String nombreMayorLunes = "";

        System.out.println("Reporte de la semana:\n");

        for (Chofer chofer : choferes) {
            int horasTrabajadas = chofer.calcularHorasTrabajadas();
            double sueldoSemanal = chofer.calcularSueldoSemanal();

            totalHorasSemana += horasTrabajadas;
            totalPagoEmpresa += sueldoSemanal;

            if (chofer.horasPorDia[0] > mayorHorasLunes) {
                mayorHorasLunes = chofer.horasPorDia[0];
                nombreMayorLunes = chofer.nombre;
            }

            System.out.println("Nombre: " + chofer.nombre);
            System.out.println("Total horas semana: " + horasTrabajadas);
            System.out.println("Sueldo semanal: $" + sueldoSemanal + "\n");
        }

        System.out.println("Total horas trabajadas en la semana: " + totalHorasSemana);
        System.out.println("Total a pagar por la empresa: $" + totalPagoEmpresa);
        System.out.println("El trabajador que labora mas horas el dia lunes es: " + nombreMayorLunes);
    }
    
}
