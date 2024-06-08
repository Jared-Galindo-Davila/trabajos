/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Inpares;

import java.util.Scanner;

public class Ejercicio_15 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese un numero entero positivo: ");
        int numero = sc.nextInt();

        boolean esCapicua = verificarCapicua(numero);

        if (esCapicua) {
            System.out.println("El numero " + numero + " es capicua.");
        } else {
            System.out.println("El numero " + numero + " no es capicua.");
        }

        sc.close();
    }

    public static boolean verificarCapicua(int numero) {
        int numeroReverso = 0;
        int numeroOriginal = numero;

        while (numero > 0) {
            int digito = numero % 10;
            numeroReverso = numeroReverso * 10 + digito;
            numero /= 10;
        }

        return numeroOriginal == numeroReverso;
    }

}
