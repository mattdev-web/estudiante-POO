public class ControlAcceso {

    public static void main(String[] args) {

        // Declaración de variables booleanas
        boolean sistemaActivo = true;
        boolean tienePermiso = false;

        // Evaluación de condiciones
        if (sistemaActivo == true) {

            if (tienePermiso == true) {
                System.out.println("Acción ejecutada");
            } else {
                System.out.println("Permiso denegado");
            }

        } else {
            System.out.println("Sistema inactivo");
        }
    }
}
