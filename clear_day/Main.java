package clear_day;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        sc.close();

        String[] temp = str.split(" ");
        
        int result = 7 - Arrays.stream(temp)
                        .mapToInt(Integer::parseInt)
                        .sum();
        System.out.println(result);
    }
}
