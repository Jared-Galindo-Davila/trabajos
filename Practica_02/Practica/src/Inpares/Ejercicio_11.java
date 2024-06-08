/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.Scanner;


public class Ejercicio_11 {

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double saldoAnterior = 500;
        double montoCompras = 1500;
        System.out.println("Banco ABC");
        System.out.print("Ingrese el pago depositado en el corte anterior: ");
        double pagoAnterior = sc.nextDouble();

        double saldoActual = saldoAnterior + montoCompras - pagoAnterior;

        double pagoMinimo = 0.15 * saldoActual;

        double intereses = 0.12 * saldoActual;
        double multa = 200;
        double pagoSinIntereses = 0.85 * saldoActual + intereses + multa;

        System.out.println("Saldo actual: S/. " + saldoActual);
        System.out.println("Pago minimo: S/. " + pagoMinimo);
        System.out.println("Pago para no generar intereses: S/. " + pagoSinIntereses);

    }
    
}
