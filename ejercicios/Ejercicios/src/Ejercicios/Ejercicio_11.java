/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio_11 {

    public static void main(String[] args) {
        Object[] libros = {"El ser excelente.", "El secreto de las 7 semillas.", "El espejo del líder."};
        double[] precios = {10, 9, 15};

        int libro = JOptionPane.showOptionDialog(
            null,
            "Seleccione el libro:",
            "Book Selection",
            JOptionPane.DEFAULT_OPTION,
            JOptionPane.PLAIN_MESSAGE,
            null,
            libros,
            libros[0]
        );

        if (libro != JOptionPane.CLOSED_OPTION) {
            String quantityStr = JOptionPane.showInputDialog(
                    null,
                    "Ingrese la cantidad de libros:"
            );

            if (quantityStr != null) {
                int cant = Integer.parseInt(quantityStr);
                boolean isDomestic = JOptionPane.showConfirmDialog(
                        null,
                        "¿Es compra a domicilio?",
                        "Domestic Check",
                        JOptionPane.YES_NO_OPTION
                ) == JOptionPane.YES_OPTION;

                double bseprecio = precios[libro];
                double precio = bseprecio * cant;

                if (isDomestic) {
                    precio = precio * 1.03;
                }

                double unitPrice = precio / cant;

                JOptionPane.showMessageDialog(
                        null,
                        "El precio total a pagar por " + cant + " libros es $ " + String.format("%.2f", precio)
                        + "\nEl precio unitario por libro es $ " + String.format("%.2f", unitPrice));
            }
        }
    }
}
