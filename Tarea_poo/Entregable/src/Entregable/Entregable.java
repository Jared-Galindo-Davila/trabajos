/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Entregable;

public class Entregable {

    public static void main(String[] args) {
        Empleado empleado1 = new Empleado(1, GeneradorNombres.generarNombreAleatorio(), 40, 10.5);
        Empleado empleado2 = new Empleado(2, GeneradorNombres.generarNombreAleatorio(), 35, 12.0);
        Empleado empleado3 = new Empleado(3, GeneradorNombres.generarNombreAleatorio(), 45, 9.75);

        System.out.println("Empleado 1:");
        System.out.println("Nombre: " + empleado1.nombre);
        System.out.println("Sueldo Bruto: $" + empleado1.calcularSueldoBruto());
        System.out.println("Descuento: $" + empleado1.calcularDescuento());
        System.out.println("Sueldo Neto: $" + empleado1.calcularSueldoNeto());
        System.out.println();

        System.out.println("Empleado 2:");
        System.out.println("Nombre: " + empleado2.nombre);
        System.out.println("Sueldo Bruto: $" + empleado2.calcularSueldoBruto());
        System.out.println("Descuento: $" + empleado2.calcularDescuento());
        System.out.println("Sueldo Neto: $" + empleado2.calcularSueldoNeto());
        System.out.println();

        System.out.println("Empleado 3:");
        System.out.println("Nombre: " + empleado3.nombre);
        System.out.println("Sueldo Bruto: $" + empleado3.calcularSueldoBruto());
        System.out.println("Descuento: $" + empleado3.calcularDescuento());
        System.out.println("Sueldo Neto: $" + empleado3.calcularSueldoNeto());
    }

}
