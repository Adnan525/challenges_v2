package least_larger;

import java.util.Arrays;
import java.util.List;

public class Main {
    public static int least_larger(List<Integer> a, Integer index){
        Integer targetVal = a.get(index);
        List<Integer> temp = a.stream()
                                .sorted()
                                .toList();
        Integer targetVal_index = temp.indexOf(targetVal);
        if(targetVal_index + 1 >= temp.size())
            return -1;
        else{
            Integer result_val = temp.get(targetVal_index + 1);
            return a.indexOf(result_val);
        }

    }
    public static void main(String[] args) {
        List<Integer> test = Arrays.asList(4, 1, 3, 5, 6);
        System.out.println(least_larger(test, 0)); // Output should be 3
        System.out.println(least_larger(test, 4)); // Output should be -1

        List<Integer> test2 = Arrays.asList(1, 3, 5, 2, 4);
        System.out.println(least_larger(test2, 0)); // Output should be 3

    }
    
}
