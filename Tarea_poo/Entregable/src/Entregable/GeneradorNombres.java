/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Entregable;

import java.util.ArrayList;
import java.util.Random;

public class GeneradorNombres {

    private static final String[] nombresOriginales = {"Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Diego", "Sofia", "Carlos", "Elena"};
    private static ArrayList<String> nombresDisponibles = new ArrayList<>();

    static {
        for (String nombre : nombresOriginales) {
            nombresDisponibles.add(nombre);
        }
    }

    public static String generarNombreAleatorio() {
        if (nombresDisponibles.isEmpty()) {
            return "No hay nombres disponibles";
        }

        Random random = new Random();
        int indice = random.nextInt(nombresDisponibles.size());
        String nombreAleatorio = nombresDisponibles.get(indice);
        nombresDisponibles.remove(indice);
        return nombreAleatorio;
    }
}
