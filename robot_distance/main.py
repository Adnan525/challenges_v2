import statistics as stat
from numpy import mean,std

def sensor_analysis(sensor_data:[(str, int, str, int)]):
    result  = [tu[1] for tu in sensor_data]
    mean = sum(result)/len(sensor_data)
    std_dev = stat.stdev(result)
    return (float("{0:.4f}".format(mean)), float("{0:.4f}".format(std_dev)))

def sensor_analysis_optim(sensor_data):
    data = [data[1] for data in sensor_data]
    return ( round(mean(data),4), round(std(data, ddof=1),4) )

sensor_data1 = [('Distance:', 116.28, 'Meters', 'Sensor 5 malfunction =>lorimar'), 
                ('Distance:', 117.1, 'Meters', 'Sensor 5 malfunction =>lorimar'), 
                ('Distance:', 123.96, 'Meters', 'Sensor 5 malfunction =>lorimar'), 
                ('Distance:', 117.17, 'Meters', 'Sensor 5 malfunction =>lorimar')]
print(sensor_analysis(sensor_data1))