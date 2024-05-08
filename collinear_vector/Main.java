package collinear_vector;

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
