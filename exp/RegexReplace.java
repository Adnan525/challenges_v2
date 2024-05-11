package exp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexReplace {

  public static void main(String[] args) {
    String inputString = "BOAT,";

    String regex = "BOAT(\\s*)?,?(\\s*)?";
    String replacement = "regex_test, ";

    Pattern pattern = Pattern.compile(regex);

    Matcher matcher = pattern.matcher(inputString);

    String resultString = matcher.replaceAll(replacement);

    System.out.println("Original String: " + inputString);
    System.out.println("Replaced String: " + resultString);
  }
    
}
