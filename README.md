## Java Flex Coding :sunglasses: :nerd_face:
- static {...} in class will execute the block while loading the class before construct call
```
    private static final Map<Character, Character> dnaMap = new HashMap<>();

    static {
        dnaMap.put('A', 'T');
        dnaMap.put('T', 'A');
        dnaMap.put('C', 'G');
        dnaMap.put('G', 'C');
    }
```
- Arrays.stream()
- Strem.of(__array__)
- mapToInt(mapper) // .mapToInt(Integer::parseInt)
```
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
```
- sum()
- sorted()
- toList()
- dna.chars() // convert string to int stream that can represent char
- mapToObj(c -> (char) c)
- map(DnaStrand :: dna_helper) // applying a function to each element, __has to return something, can not be void__
- collect(Collectors.joining()); //join the strings
```
    public static String makeComplement(String dna) {
        return dna.chars()
        .mapToObj(c -> (char) c)
        .map(DnaStrand :: dna_helper)
        .map(Object::toString)
        .collect(Collectors.joining());
    }
```
- distinct()
- count()
- filter()
- boxed() \\ take prim type and wrap as object
```
    \\ java char[] behaves differently than string[], see detect_program main
    \\ BECAUSE OF PRIMITIVE DATA TYPE
    public static boolean check_flex(String sentence){
        return sentence.toLowerCase().chars().map(i -> (char) i).distinct().filter(Character::isLetter).count() == 26;
      }

        sentence.chars().mapToObj(i -> (char)i).forEach(System.out::println);

        sentence.chars().boxed().map(i -> (char)i.intValue()).forEach(System.out::println);

        sentence.chars().map(i -> (char)i).forEach(System.out::println);
```
- lambda (absolutely unnecessary :rofl:)
```
public class Main {
    private static Collinear_check result;
    static{
      result = (a, b, c, d) -> a*d==b*c;
    }
    
    
    public static boolean collinearity(int x1, int y1, int x2, int y2) {
      return result.check(x1, y1, x2, y2);
    }
    
    @FunctionalInterface
    interface Collinear_check{
        boolean check(int a, int b, int c, int d);
    }
  }
```
- map() vs mapToObj(), map() will have the same input and output type, usually primitive
```
    public static Integer squareDigits_flex(Integer n){
      return Integer.parseInt(String.valueOf(n)
      .chars()
      .map(i -> Integer.parseInt(String.valueOf((char)i)))
      .map(i -> (int)Math.pow(i, 2))
      .mapToObj(Integer::toString) // won't work with map()
      .collect(Collectors.joining("")));
    }
```

## Python Flex
- Set
```
import string

def is_pangram(s:str):
    for i in range(65, 91): # A - Z : 65 - 90
        if chr(i) not in s.upper():
            return False
        
    return True

def is_pangram_flex(s):
    return set(string.ascii_lowercase).issubset(s.lower())
```
- java map(s -> s-1<0 ? s : s-1) equivalent
```
transformed_numbers = list(map(lambda s: s if s - 1 < 0 else s - 1, candles))
```
## Regex
- capturing group
```
    public static String pigIt_ultraFlex(String str)
    {
        /*
         * capturing groups are separated using ()
         * first (\\w) captures the 1st character and referred using $1
         * 2nd capturing group(\\w*) captures the rest of the word and referred using $2
         */
        return str.replaceAll("(\\w)(\\w*)", "$2$1ay");
    }
```