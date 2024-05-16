package hash_to_array;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata {
    public static List<Object[]> hashToArray(HashMap<String, Object> h){
        SortedMap<String, Object> sortedMap = new TreeMap<>(h);
        Object[] keys = sortedMap.keySet().toArray();
        Object[] values = sortedMap.values().toArray();

        return IntStream.range(0, values.length)
                 .mapToObj(i -> new Object[]{keys[i], values[i]})
                 .collect(Collectors.toList());
    }

    public static String obj_arr_to_string(List<Object[]> l){
        return "[" + l.stream()
                      .map(obj -> "["+obj[0]+" Type ->"+obj[0].getClass()+", "+obj[1]+" Type ->"+obj[1].getClass()+"]")
                      .collect(Collectors.joining(", ")) + "]";
    }


    public static void main(String[] args) {
        // HashMap<String, Object> h = new HashMap<>();
        // h.put("apple", 10);
        // h.put("banana", 20);
        // h.put("cherry", 5);
    
        // List<Object[]> test = new ArrayList();
        // test.add(new Object[]{"apple", 10});
        // test.add(new Object[]{"banana", 20});
        // test.add(new Object[]{"cherry", 5});

        // String s1 = obj_arr_to_string(test);

        // String s2 = obj_arr_to_string(hashToArray(h));

        // System.out.println(s1.equals(s2));
        HashMap<String, Object> map = new HashMap<>();  // empty HashMap
        List<Object[]> expected = new ArrayList<>();
        System.out.println(obj_arr_to_string(expected).equals(obj_arr_to_string(hashToArray(map))));

    }
    
}
