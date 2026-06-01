import java.util.Scanner;

public class AreaRectangulo {

    // 1. Declaración del método
    public static double calcularArea(double base, double altura) {
        // 3. Realiza el cálculo
        double area = base * altura;
        
        // 4. Retorna el resultado
        return area;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedir datos al usuario
        System.out.print("Ingrese la base del rectángulo: ");
        double base = scanner.nextDouble();

        System.out.print("Ingrese la altura del rectángulo: ");
        double altura = scanner.nextDouble();

        // 5. Llamar al método
        double resultado = calcularArea(base, altura);

        // Mostrar resultado
        System.out.println("El área del rectángulo es: " + resultado);
        System.out.println("--------------------");
        System.out.println("Gracias por usar el programa.");
       
        scanner.close();
    }
}
