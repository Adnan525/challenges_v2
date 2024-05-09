package extended_weekend;

import java.time.LocalDate;
import java.util.List;

public class Main {
    public static String [] solve(int a, int b){
        Integer score = 0;
        String first = "";
        String last = "";
        for(int year = a; year <= b; year++){
            for(int month = 1; month <= 12; month++){
                LocalDate date = LocalDate.of(year, month, 1);
                Integer first_day = date.getDayOfWeek().getValue();
                // System.out.println(first_day);
                Integer number_of_days = date.lengthOfMonth();
                if(first_day == 5 && number_of_days ==31){ // monday is 1 here, in python it's 0
                    score+=1;
                    first = first.equals("") ? date.getMonth().name():first;
                    last =  date.getMonth().name();
                }
            }
        }
        return List.of(first, last, score.toString()).stream().toArray(String[]::new);
    }

    public static void main(String[] args) {
        System.out.println(solve(2016,2020)[0] + " "+solve(2016,2020)[1]+" "+solve(2016,2020)[2]);
    }
    
}
