def get_ip_from_line(line):
    if "brute22" in line:
        ip = line.split()[9].partition('=')[2]
        return(ip)


with open('syslog.log','r') as f:
    f2 = open('known_ip.txt','r+')
    syslines = f.readlines()
    known_ip = f2.read().splitlines()
    for line in syslines:
        ip = get_ip_from_line(line)
        if not ip in known_ip and ip is not None:
            known_ip.append(ip)
            print("ip sconosciuto")
            f2.write(ip + '\n')
    f2.close()


