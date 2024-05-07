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
- dna.chars() // convert string to char
- mapToObj(c -> (char) c) // when you use the chars() method on a String, it returns an IntStream representing the characters of the string as integer values. Each integer value corresponds to the Unicode code point of the character. However, to work with characters in a more convenient way, you often want to convert these integer values back to characters. That's why we use the mapToObj() method to convert each integer value to its corresponding character representation.
- map(DnaStrand :: dna_helper) // applying a function to each element
- map(Object::toString) // convert chat to string
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
