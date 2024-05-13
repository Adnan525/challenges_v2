package pig_latin;
import java.util.Arrays;
import java.util.regex.*;
import java.util.stream.Collectors;

public class PigLatin {
    public static String pigIt_helper(String word){
        return word.matches("^\\W+$") ? word : word.substring(1)+word.charAt(0)+"ay"; 
    }
    public static String pigIt(String str) {
        String[] str_arr = str.split(" ");
        return Arrays.stream(str_arr)
                     .map(PigLatin::pigIt_helper)
                     .collect(Collectors.joining(" "));
    }
    public static void main(String[] args) {
        System.out.println(pigIt("Pig latin is cool")
                            .equals("igPay atinlay siay oolcay"));
    }
}
