import java.util.ArrayList;

class Habitacion {
    private String nombre;
    private double tamaño;

    public Habitacion(String nombre, double tamaño) {
        this.nombre = nombre;
        this.tamaño = tamaño;
    }

    public String mostrar() {
        return nombre + " - " + tamaño + " m²";
    }
}

class Casa {
    private String direccion;
    private ArrayList<Habitacion> habitaciones;

    public Casa(String direccion) {
        this.direccion = direccion;
        this.habitaciones = new ArrayList<>();
    }

    public void agregarHab(String nombre, double tamaño) {
        Habitacion habitacion = new Habitacion(nombre, tamaño);
        habitaciones.add(habitacion);
    }

    public void muestra() {
        System.out.println("La casa con la dirección: " + direccion);
        System.out.println("Con las habitaciones:");
        for (Habitacion h : habitaciones) {
            System.out.println(h.mostrar());
        }
    }
}

public class CasaHabitacion {
    public static void main(String[] args) {
        Casa casa1 = new Casa("Av. Central 123");
        casa1.agregarHab("Planta Alta", 45.0);
        casa1.agregarHab("Sala", 23.5);
        casa1.agregarHab("Cocina", 15.0);

        casa1.muestra();
    }
}
