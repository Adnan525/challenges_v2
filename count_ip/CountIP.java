import java.util.stream.IntStream;

public class CountIP{
    public static long ipsBetween(String start, String end) {
        long ip1 = IntStream.range(0, start.split("\\.").length)
                    .mapToLong(i -> (long) (Integer.parseInt(start.split("\\.")[i]) * Math.pow(256, 3 - i)))
                    .sum();

        long ip2 = IntStream.range(0, end.split("\\.").length)
                    .mapToLong(i -> (long) (Integer.parseInt(end.split("\\.")[i]) * Math.pow(256, 3 - i)))
                    .sum();


		return Math.abs(ip1 - ip2);
	}
    public static void main(String[] args) {
        System.out.println(ipsBetween("0.0.0.0", "255.255.255.255"));
    }
}