/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Inpares;


public class Chofer {
    String nombre;
    int[] horasPorDia;
    double sueldoPorHora;

    public Chofer(String nombre, int[] horasPorDia, double sueldoPorHora) {
        this.nombre = nombre;
        this.horasPorDia = horasPorDia;
        this.sueldoPorHora = sueldoPorHora;
    }

    public int calcularHorasTrabajadas() {
        int totalHoras = 0;
        for (int horas : horasPorDia) {
            totalHoras += horas;
        }
        return totalHoras;
    }

    public double calcularSueldoSemanal() {
        int horasTrabajadas = calcularHorasTrabajadas();
        return horasTrabajadas * sueldoPorHora;
    }
}
