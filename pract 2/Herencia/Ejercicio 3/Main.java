 import java.util.ArrayList;

class Persona {
    String ci, nombre, ape, cel;
    int fecha_nac;

    public Persona(String ci, String nombre, String ape, String cel, int fecha_nac) {
        this.ci = ci;
        this.nombre = nombre;
        this.ape = ape;
        this.cel = cel;
        this.fecha_nac = fecha_nac;
    }

    public int edad() {
        return 2025 - fecha_nac;
    }
}

class Estudiante extends Persona {
    static ArrayList<Estudiante> guardar = new ArrayList<>();
    String ru;
    int fecha_ingreso, semestre;

    public Estudiante(String ci, String nombre, String ape, String cel, int fecha_nac, String ru, int fecha_ingreso, int semestre) {
        super(ci, nombre, ape, cel, fecha_nac);
        this.ru = ru;
        this.fecha_ingreso = fecha_ingreso;
        this.semestre = semestre;
    }

    public void guardarEstudiante() {
        guardar.add(this);
    }

    public static void mostrar() {
        for (Estudiante est : guardar) {
            System.out.println("El estudiante " + est.nombre + " " + est.ape + ", celular " + est.cel +
                    ", nacido en " + est.fecha_nac + ", RU " + est.ru + ", ingresó en " + est.fecha_ingreso +
                    ", semestre " + est.semestre);
        }
    }

    public static void mostrarMayores() {
        System.out.println("\nEstudiantes mayores de 25 años:");
        for (Estudiante est : guardar) {
            if (est.edad() > 25) {
                System.out.println(est.nombre + " " + est.ape + ", edad: " + est.edad() + ", semestre: " + est.semestre);
            }
        }
    }
}

class Docente extends Persona {
    static ArrayList<Docente> guardarDoc = new ArrayList<>();
    String nit, profesion, especialidad;

    public Docente(String ci, String nombre, String ape, String cel, int fecha_nac, String nit, String profesion, String especialidad) {
        super(ci, nombre, ape, cel, fecha_nac);
        this.nit = nit;
        this.profesion = profesion;
        this.especialidad = especialidad;
    }

    public void guardarDocente() {
        guardarDoc.add(this);
    }

    public static void mostrarDoc() {
        for (Docente doc : guardarDoc) {
            System.out.println(doc.nombre + " " + doc.ape + ", " + doc.cel + ", " + doc.profesion + ", " + doc.especialidad);
        }
    }

    public static void mostrarDocentesIngenieria() {
        System.out.println("\nDocentes de Ingeniería:");
        for (Docente doc : guardarDoc) {
            if (doc.profesion.equals("Ingeniero") || doc.profesion.equals("Ingeniera")) {
                System.out.println(doc.nombre + " " + doc.ape + ", " + doc.cel + ", " + doc.profesion + ", " + doc.especialidad);
            }
        }
    }
}

public class Main {
    public static void mostrarMismoApellido() {
        System.out.println("\nEstudiantes y Docentes con el mismo apellido:");
        boolean hayCoincidencia = false;
        for (Estudiante est : Estudiante.guardar) {
            for (Docente doc : Docente.guardarDoc) {
                if (est.ape.equals(doc.ape)) {
                    System.out.println("- " + est.nombre + " " + est.ape + " (Estudiante) y " +
                            doc.nombre + " " + doc.ape + " (Docente)");
                    hayCoincidencia = true;
                }
            }
        }
        if (!hayCoincidencia) {
            System.out.println("No se encontraron coincidencias.");
        }
    }

    public static void main(String[] args) {
        Estudiante e1 = new Estudiante("123", "Luis", "López", "789456", 1990, "RU123", 2021, 7);
        Estudiante e2 = new Estudiante("456", "María", "Mamani", "123789", 1999, "RU456", 2022, 5);
        e1.guardarEstudiante();
        e2.guardarEstudiante();

        Estudiante.mostrar();
        Estudiante.mostrarMayores();

        Docente d1 = new Docente("789", "Carlos", "López", "987654", 1980, "NIT123", "Ingeniero", "Sistemas");
        Docente d2 = new Docente("321", "Ana", "Rojas", "654987", 1985, "NIT456", "Licenciada", "Matemáticas");
        Docente d3 = new Docente("654", "Jorge", "Mamani", "321654", 1975, "NIT789", "Doctor", "Física");
        Docente d4 = new Docente("987", "Lucía", "Quiroz", "963852", 1990, "NIT321", "Ingeniera", "Electrónica");
        d1.guardarDocente();
        d2.guardarDocente();
        d3.guardarDocente();
        d4.guardarDocente();

        Docente.mostrarDoc();
        Docente.mostrarDocentesIngenieria();

        mostrarMismoApellido();
    }
}
