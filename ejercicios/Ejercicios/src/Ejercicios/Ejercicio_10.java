/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Ejercicios;

import javax.swing.JOptionPane;


public class Ejercicio_10 {

   
    public static void main(String[] args) {
        String punt = JOptionPane.showInputDialog("Ingrese el puntaje del dado: (1, 2, 3, 4, 5, or 6)");
        int score = Integer.parseInt(punt);

        String classification = "";

        switch (score) {
            case 1:
            case 2:
                classification = "Sin suerte.";
                break;
            case 3:
            case 4:
                classification = "Con suerte.";
                break;
            case 5:
                classification = "Con estrella.";
                break;
            case 6:
                classification = "Fantástico.";
                break;
            default:
                classification = "Puntaje no válido.";
        }

        JOptionPane.showMessageDialog(null,"Clasificación: " + classification );
    }
    
}
