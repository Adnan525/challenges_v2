package fraction_sum;

public class Main{
    public static Integer gcd(Integer a, Integer b){
        if(a%b == 0)
            return b;
        else
            return gcd(b%a, a);
    }
    public static Integer fraction_sum(Integer a, Integer b){
        Integer gcd = gcd(a, b);
        return a/gcd + b/gcd;
    }
    public static void main(String[] args) {
        // System.out.println(gcd(16, 60));
        System.out.println(fraction_sum(2, 4));
    }  
}