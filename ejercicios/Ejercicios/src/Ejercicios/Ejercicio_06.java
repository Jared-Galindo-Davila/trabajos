/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio_06 {

    public static void main(String[] args) {
        String eda = JOptionPane.showInputDialog(null,
                "Ingrese su edad: ");

        int edad = Integer.parseInt(eda);

        if (edad >= 18) {
            JOptionPane.showMessageDialog(null,
                    "Es mayor de edad.");
        } else {
            JOptionPane.showMessageDialog(null,
                    "Es menor de edad.");
        }

    }

}
