import java.util.Arrays;
import java.util.stream.Collectors;

class Kata
{
  public static String helper_blowCandles(String[] candles_string_arr){
    return Arrays.asList(candles_string_arr).stream()
    .mapToInt(Integer::parseInt)
    .map(val -> val-1 < 0 ? 0 : val-1)
    .mapToObj(Integer::toString)
    .collect(Collectors.joining(""));
  }
  
  public static int blowCandles(String str)
  {
    if(Arrays.asList(str.split("")).stream().allMatch(s -> s.equals("0")) || str.equals(""))
      return 0;

    if(str.charAt(0) == '0' && str.length() > 3)
      return 0 + blowCandles(str.substring(1));

    else{
        String[] candles_string_arr = str.length() > 3 ?
                                      str.substring(0, 3).split("") : 
                                      str.split("");
        String result = helper_blowCandles(candles_string_arr);
        String mod_str = str.length() > 3 ? result + str.substring(3) : result;
        return 1 + blowCandles(mod_str);
    }
  }
  public static void main(String[] args) {
    // System.out.println(blowCandles("13"));
    // System.out.println(helper_blowCandles("0".split("")));
  }
}