package how_many_steps;

public class Main {
    public static Integer count_steps(int a, int b){
        double count = Math.log(b/a) / Math.log(2);
        if (count < 1)
            return b-a;
        else if((int)count - count == 0.0)
            return (int)count;
        if(b % 2 == 0 && b/2 <= a){
            return b/2 == a ? 1 : a-b/2;
        }
        else {
            if(b%2 == 1)
                return 1 + count_steps(a, b-1);
            else
                return 1 + count_steps(a, b/2);
        }
    }
    public static void main(String[] args) {
        System.out.println(count_steps(1, 10));
    }
    
}
