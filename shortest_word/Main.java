package shortest_word;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Stream;

public class Main {
    public static Integer findShort(String s){
        String[] target = s.split(" ");
        String shortest_word = Arrays.asList(target).stream()
                                .min(Comparator.comparing(word -> word.length()))
                                .orElse("");
    return shortest_word.length();
    }


    public static Integer findShort_optim(String s){
        return Stream.of(s.split(" "))
                .mapToInt(String::length)
                .min()
                .getAsInt();
    }

    public static void main(String[] args) {
        System.out.println(findShort("bitcoin take over the world maybe who knows perhaps"));
    }
    
}
