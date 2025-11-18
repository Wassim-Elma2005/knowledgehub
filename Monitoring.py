import datetime

host_name = input("What is the hostname of the machine that should be monitored: ")
ip_address = input("What is the system ip address: ")
metrics = input("What metrics should be monitored? (divide them with ','): ")
print(host_name, ip_address)
metrics_list = metrics.split(",")
for metric in metrics_list:
    print(metric.strip())