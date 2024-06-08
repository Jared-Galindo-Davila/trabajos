/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio_01 {

    public static void main(String[] args) {
        String base, altura;

        base = JOptionPane.showInputDialog("Ingresa la base de un rectangulo: ");
        double b = Double.parseDouble(base);

        altura = JOptionPane.showInputDialog("Ingresa la altura de un rectangulo: ");
        double h = Double.parseDouble(altura);
        double area = b * h;
        double perimeter = 2 * (b + h);

        JOptionPane.showMessageDialog(null, "El area de un rectangulo es: " + area + "\nEl perimetro de un rectangulo es: " + perimeter);

    }
}
