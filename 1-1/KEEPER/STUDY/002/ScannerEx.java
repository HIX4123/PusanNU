import java.util.*;

class ScannerEx {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Scanning > ");
            String input = scanner.nextLine();
            int num = Integer.parseInt(input);

            System.out.println(" : " + input);
            System.out.printf("num = %d%n", num);
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }
    }
}