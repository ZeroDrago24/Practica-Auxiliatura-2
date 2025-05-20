import java.util.ArrayList;

class Parte {
    private String nombre;
    private String peso;

    public Parte(String nombre, String peso) {
        this.nombre = nombre;
        this.peso = peso;
    }

    public String mostrarInfo() {
        return nombre + " " + peso;
    }
}

class Avion {
    private String modelo;
    private String fabricante;
    private ArrayList<Parte> partes;

    public Avion(String modelo, String fabricante) {
        this.modelo = modelo;
        this.fabricante = fabricante;
        this.partes = new ArrayList<>();
    }

    public void agregarParte(String nombre, String peso) {
        Parte parte = new Parte(nombre, peso);
        partes.add(parte);
    }

    public void mostrar() {
        System.out.println("El avión " + modelo + " de " + fabricante);
        System.out.println("Con las partes:");
        for (Parte p : partes) {
            System.out.println(p.mostrarInfo());
        }
    }
}

public class AvionPartes {
    public static void main(String[] args) {
        Avion av = new Avion("BEBE", "Ovama");
        av.agregarParte("Motor", "1000 T");
        av.agregarParte("Alas", "500 T");
        av.agregarParte("Timón", "200 T");

        av.mostrar();
    }
}
