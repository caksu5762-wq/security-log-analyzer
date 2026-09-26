logs= [
    {
        "ip":"192.168.1.10",
        "status":"success"
    },
    {
        "ip":"192.168.1.20",
        "status":"failed"
    },
    {
        "ip":"192.168.1.30",
        "status":"failed"
    },
    {
        "ip":"192.168.1.20",
        "status":"failed"
    },
    {
        "ip":"192.168.1.20",
        "status":"failed"
    },
    {
        "ip":"192.168.1.40",
        "status":"success"
    }
]

failed_ips=[]
for log in logs:
    if log["status"] == "failed":
        failed_ips.append(log["ip"])

unique_ips = set(failed_ips)
for ip in unique_ips:
    count = failed_ips.count(ip)
    if count >=3:
        print("şüpheli ip",ip)
        print("başarısız deneme",count)

suspicions_ips=[]

failed_ips=[]
with open("security.log","r",encoding="utf-8") as file:
    okuyucu = file.readlines()
    for log in okuyucu:
        parçalar = log.strip().split()
        if len(parçalar) >= 2 and parçalar[1] == "failed":
            failed_ips.append(parçalar[0])

unique_ips = set(failed_ips)
for ip in unique_ips:
    count = failed_ips.count(ip)
    if count >=3:
        suspicions_ips.append(ip)


report_lines=[]
report_lines.append("=== SECURİTY ANALYSIS REPORT ===")
for ip in suspicions_ips:
    count = failed_ips.count(ip)
    if count >= 10:
        severity = "CRİTİCAL"
    elif count >=5:
        severity = "HİGH"
    else:
        severity = "MEDİUM"
    if count >= 3:
        report_lines.append(ip + " başarısız deneme-" + str(count) + " RİSK:" + severity)

report_lines.append("TOPLAM ŞÜPHELİ İP:" + str(len(suspicions_ips)))

with open("report.lines","w",encoding="utf-8",newline="") as file:
    file.write("\n".join(report_lines))
    






