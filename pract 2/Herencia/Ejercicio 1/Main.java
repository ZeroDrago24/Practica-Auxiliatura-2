public class Main {
    public static void main(String[] args) {
        Coche coche1 = new Coche("Toyota", "Corolla", 2020, 20000, 4, "Gasolina");
        Moto moto1 = new Moto("Yamaha", "YZF-R3", 2022, 6000, "321cc", "4 tiempos");

        System.out.println(coche1.mostrarInfo());
        System.out.println(moto1.mostrarInfo());
    }
}

class Vehiculo {
    protected String marca;
    protected String modelo;
    protected int año;
    protected double precioBase;

    public Vehiculo(String marca, String modelo, int año, double precioBase) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.precioBase = precioBase;
    }

    public String mostrarInfo() {
        return "El vehículo con la marca " + marca + ", modelo " + modelo + ", año " + año + ", precio base " + precioBase;
    }
}

class Coche extends Vehiculo {
    private int numPuertas;
    private String tipoCombustible;

    public Coche(String marca, String modelo, int año, double precioBase, int numPuertas, String tipoCombustible) {
        super(marca, modelo, año, precioBase);
        this.numPuertas = numPuertas;
        this.tipoCombustible = tipoCombustible;
    }

    @Override
    public String mostrarInfo() {
        return "El coche con la marca " + marca + ", modelo " + modelo + ", año " + año + ", precio base " + precioBase +
                ", número de puertas " + numPuertas + ", tipo de combustible " + tipoCombustible;
    }
}

class Moto extends Vehiculo {
    private String cilindrada;
    private String tipoMotor;

    public Moto(String marca, String modelo, int año, double precioBase, String cilindrada, String tipoMotor) {
        super(marca, modelo, año, precioBase);
        this.cilindrada = cilindrada;
        this.tipoMotor = tipoMotor;
    }

    @Override
    public String mostrarInfo() {
        return "La moto con la marca " + marca + ", modelo " + modelo + ", año " + año + ", precio base " + precioBase +
                ", cilindrada " + cilindrada + ", tipo de motor " + tipoMotor;
    }
}
