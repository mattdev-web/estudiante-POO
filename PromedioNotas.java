import java.util.Scanner;

public class PromedioNotas {

    // Función con parámetros y retorno
    public static double calcularPromedio(double n1, double n2, double n3) {
        double promedio = (n1 + n2 + n3) / 3;
        return promedio;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Pedir datos
        System.out.println("Ingrese la primera nota:");
        double nota1 = sc.nextDouble();

        System.out.println("Ingrese la segunda nota:");
        double nota2 = sc.nextDouble();

        System.out.println("Ingrese la tercera nota:");
        double nota3 = sc.nextDouble();

        // Llamada a la función
        double resultado = calcularPromedio(nota1, nota2, nota3);

        // Mostrar resultado
        System.out.println("El promedio es: " + resultado);
    }
}