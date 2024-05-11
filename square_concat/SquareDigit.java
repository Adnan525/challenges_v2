package square_concat;

import java.util.stream.Collectors;

public class SquareDigit {

    public static int squareDigits(Integer n) {
      StringBuilder s_b = new StringBuilder();
      Integer remainder = 0;
      Integer div = n;
      for (Character ch : n.toString().toCharArray()){
        remainder = div%10;
        div = div/10;
        s_b.insert(0, Integer.toString((int)Math.pow(remainder, 2)));
      }
      return Integer.parseInt(s_b.toString());
    }

    public static Integer squareDigits_flex(Integer n){
      return Integer.parseInt(String.valueOf(n)
      .chars()
      .map(i -> Integer.parseInt(String.valueOf((char)i)))
      .map(i -> (int)Math.pow(i, 2))
      .mapToObj(Integer::toString)
      .collect(Collectors.joining("")));
    }

    public static void main(String[] args) {
      // System.out.println(squareDigits(9119)); //811181
      System.out.println(squareDigits_flex(9119));;
    }
  
  }