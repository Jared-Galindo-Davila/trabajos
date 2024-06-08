/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Ejercicios;

import javax.swing.JOptionPane;


public class Ejercicio_09 {

    
    public static void main(String[] args) {
        String tribu = JOptionPane.showInputDialog("Ingrese el código de la tribuna: (Norte , Sur, Oriente Lateral, Oriente Medio, Occidente)");
        String tribuna = tribu.toUpperCase();

       String cant = JOptionPane.showInputDialog("Ingrese la cantidad de entradas: ");
        int cantidad = Integer.parseInt(cant);

        double unitPrice = 0;

        switch (tribuna) {
            case "NORTE":
                unitPrice = 40;
                break;
            case "SUR":
                unitPrice = 40;
                break;
            case "ORIENTE LATERAL":
                unitPrice = 80;
                break;
            case "ORIENTE MEDIO":
                unitPrice = 120;
                break;
            case "OCCIDENTE":
                unitPrice = 300;
                break;
            default:
                JOptionPane.showMessageDialog(null,"Código de tribuna no válido.");
        }

        double totalPrice = cantidad * unitPrice;

        JOptionPane.showMessageDialog(null,
                "Total a pagar: S/. " + String.format("%.2f", totalPrice)+
                " Precios de entradas FPF");

    }
    
}
