package robot_distance;

import java.util.Arrays;

public class Kata
{
    public static double[] sensorAnalysis(Object[][] sensor_data)
    {
        double average = Arrays.stream(sensor_data)
                              .mapToDouble(d -> (double)d[1])
                              .average()
                              .getAsDouble();

        double stnd_dev = Math.sqrt(Arrays.stream(sensor_data)
                                .mapToDouble(d -> (double)d[1])
                                .map(d_val -> d_val - average)
                                .map(deviation -> Math.pow(deviation, 2))
                                .sum()/(sensor_data.length-1)); // sample standard deviation

        return new double[] {Double.parseDouble(String.format("%.4f", average)),
                             Double.parseDouble(String.format("%.4f", stnd_dev))};
    }
    public static void main(String[] args) {
      Object[][] sensor_data = {
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 202.93, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 344.71, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 304.87, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 320.21, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 332.49, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 324.61, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 248.33, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 214.75, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 179.38, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 213.16, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 186.58, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 302.8, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 318.62, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 281.06, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 266.91, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 292.64, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 320.45, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 162.29, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 225.26, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"},
        {"Distance:", 158.42, "Meters", "Sensor 5 malfunction =>lorimar"}
    };
    Arrays.stream(sensorAnalysis(sensor_data)).forEach(System.out::println);
    
    }
}