import sys
import os
import ipaddress


def main():
    if len(sys.argv) != 3:
        print(f"(+) Usage: {sys.argv[0]} <ip subnet> <subnet mask>")
        print(f"(+) Example: {sys.argv[0]} 10.10.1.0 24")
        sys.exit(-1)

    for ip in ipaddress.IPv4Network(f"{sys.argv[1]}/{sys.argv[2]}"):
        print(ip)
        response = os.system("ping -c 1 -W 1 " + str(ip))
        if response == 0:
            print(f"{ip} is up!")
        else:
            print(f"{ip} is down!")

if __name__ == "__main__":
    main()
