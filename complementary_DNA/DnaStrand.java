package complementary_DNA;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class DnaStrand {

    private static final Map<Character, Character> dnaMap = new HashMap<>();

    static {
        dnaMap.put('A', 'T');
        dnaMap.put('T', 'A');
        dnaMap.put('C', 'G');
        dnaMap.put('G', 'C');
    }
    public static char dna_helper(char c) {
        // can use getordefault
        return dnaMap.get(c);
    }
    
    public static String makeComplement(String dna) {
        return dna.chars()
        .mapToObj(c -> (char) c)
        .map(DnaStrand :: dna_helper)
        .map(Object::toString)
        .collect(Collectors.joining());
    }
    public static void main(String[] args) {
        System.out.println(makeComplement("TAACG"));
    }
  }