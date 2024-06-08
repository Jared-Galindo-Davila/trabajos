/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Entregable;


public class Empleado {
    public int codigo;
    public String nombre;
    public int horasTrabajadas;
    public double tarifaHora;

    public Empleado(int codigo, String nombre, int horasTrabajadas, double tarifaHora) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.horasTrabajadas = horasTrabajadas;
        this.tarifaHora = tarifaHora;
    }

    public double calcularSueldoBruto() {
        return horasTrabajadas * tarifaHora;
    }

    public double calcularDescuento() {
        double sueldoBruto = calcularSueldoBruto();
        return 0.15 * sueldoBruto;
    }

    public double calcularSueldoNeto() {
        double sueldoBruto = calcularSueldoBruto();
        double descuento = calcularDescuento();
        return sueldoBruto - descuento;
    }

}
