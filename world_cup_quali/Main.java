package world_cup_quali;

import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String point = sc.nextLine();
        sc.close();
        if(Integer.parseInt(point) >= 12){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
