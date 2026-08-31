logs= [
    {
        "ip":"192.168.50.7",
        "status":"failed"
    },
    {
        "ip":"10.20.30.40",
        "status":"failed"
    },
    {
        "ip":"192.168.50.7",
        "status":"failed"
    },
    {
        "ip":"172.16.8.9",
        "status":"success"
    },
    {
        "ip":"10.20.30.40",
        "status":"failed"
    },
    {
        "ip":"192.168.50.7",
        "status":"failed"
    },
    {
        "ip":"10.20.30.40",
        "status":"failed"
    }
]

failed_ips=[]
for log in logs:
    print(log["status"]) == "failed"
    failed_ips.append(log["ip"])
    failed_ips.count("10.20.30.40")

unique_ips= set(failed_ips)
for ip in unique_ips:
   count= failed_ips.count(ip)
   if count >=3:
       print("Suspicious IP:",ip)
       print("Failed attempt:",count)

suspicious_ips = []
with open("auth.log","r") as file:
    logs = file.readlines()
failed_ips=[]
for log in logs:
    parçalar = log.strip().split()
    if parçalar[1] == "failed":
      failed_ips.append(parçalar[0])

unique_ips = set(failed_ips)
for ip in unique_ips:
    count = failed_ips.count(ip)
    if count >= 3:
        print("Suspicious IP:",ip)
        print("failed attempt:",count)
    suspicious_ips.append(ip)
print(suspicious_ips)











