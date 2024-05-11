package detect_program;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static boolean check(String sentence){
        Set<Character> test = new HashSet<>();
        char[] char_arr = sentence.toLowerCase().toCharArray();
        for(char c : char_arr){
            if((int)c >= 97 && (int)c <= 122)
                test.add(c); 
        }
        System.out.println(test.size());
        System.out.println(test);
        return test.size() == 26 ? true : false;
      }
      public static boolean check_flex(String sentence){
        return sentence.toLowerCase().chars().map(i -> (char) i).distinct().filter(Character::isLetter).count() == 26;
      }

    public static void main(String[] args) {
        String sentence = "hello world";
        char[] char_arr = sentence.toCharArray();

        // System.out.println("String Array");
        // Arrays.asList(sentence.split("")).stream()
        //                                        .forEach(System.out::println);

        // System.out.println("Char array : ");
        // Arrays.asList(char_arr).stream()
        //         .forEach(System.out::println);

        // sentence.chars().mapToObj(i -> (char)i).forEach(System.out::println);

        // sentence.chars().boxed().map(i -> (char)i.intValue()).forEach(System.out::println);

        sentence.chars().map(i -> (char)i).forEach(System.out::println);
        // sentence.codePoints().map(i -> (char)i).forEach(System.out::println);
        // sentence.chars().boxed().map(i -> (char)i.intValue()).forEach(System.out::println);
      }
    
}