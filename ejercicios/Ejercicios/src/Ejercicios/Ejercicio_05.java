/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Ejercicios;

import javax.swing.JOptionPane;


public class Ejercicio_05 {

    
    public static void main(String[] args) {
        double sueldoBasico = 1250;
        double porcentajeComision = 0.07;
        double porcentajeDescuento = 0.12;

        String monto = JOptionPane.showInputDialog("Ingrese el monto total vendido por el vendedor: ");
        double montoVendido = Double.parseDouble(monto);

        double comision = montoVendido * porcentajeComision;
        double sueldoBruto = sueldoBasico + comision;
        double descuento = sueldoBruto * porcentajeDescuento;
        double sueldoNeto = sueldoBruto - descuento;

        JOptionPane.showMessageDialog(null,
                "Comisión: S/. " + String.format("%.2f", comision) + "\n"
                + "Sueldo bruto: S/. " + String.format("%.2f", sueldoBruto) + "\n"
                + "Descuento: S/. " + String.format("%.2f", descuento) + "\n"
                + "Sueldo neto: S/. " + String.format("%.2f", sueldoNeto)+
                " de vendedor de la empresa");
    }
    
}
