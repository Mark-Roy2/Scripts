import hashlib
import argparse

patterns = [
    "{username}:{timestamp}",
    "{timestamp}:{username}",
    "{username}",
    "{timestamp}",
    "{username}-{timestamp}",
    "{timestamp}-{username}",
    "{username}_{timestamp}",
    "{timestamp}_{username}",
    "{username}.{timestamp}",
    "{timestamp}.{username}",
    "{username}/{timestamp}",
    "{timestamp}/{username}",
    "{username}|{timestamp}",
    "{timestamp}|{username}",
    "{username};{timestamp}",
    "{timestamp};{username}",
    "[{username}:{timestamp}]",
    "[{timestamp}:{username}]",
    "({username}:{timestamp})",
    "({timestamp}:{username})",
    "{{username}}:{{timestamp}}",
    "{{timestamp}}:{{username}}",
    "prefix_{username}:{timestamp}",
    "prefix_{timestamp}:{username}",
    "{username}:{timestamp}_suffix",
    "{timestamp}:{username}_suffix",
    "{username}@{timestamp}",
    "{timestamp}@{username}"
]

def check_seconds(timestamp, username, hash):
    timestamp = int(timestamp)
    for i in range(-5, 6):
        for pattern in patterns:
            string_value = pattern.format(username=username, timestamp=timestamp + i)
            hash_value = hashlib.md5(string_value.encode('utf-8')).hexdigest()
            if hash_value == hash:
                print(f"[+] A MATCH HAS BEEN FOUND: {string_value}")
                return
    # If no match found in seconds, check milliseconds
    check_milliseconds(timestamp, username, hash)

def check_milliseconds(timestamp, username, hash):
    milliseconds = timestamp * 1000
    for i in range(-5, 6):
        for n in range(0, 10000):
            for pattern in patterns:
                adjusted_timestamp = milliseconds + i * 1000 + n
                string_value = pattern.format(username=username, timestamp=adjusted_timestamp)
                hash_value = hashlib.md5(string_value.encode('utf-8')).hexdigest()
                if hash_value == hash:
                    print(f"[+] A MATCH HAS BEEN FOUND: {string_value}")
                    return
    print("[-] No match found in the given range.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--timestamp', help='unix timestamp', required=True)
    parser.add_argument('-u', '--username', help='username value', required=True)
    parser.add_argument('-H', '--hash', help='reset token hash value', required=True)
    args = parser.parse_args()

    check_seconds(args.timestamp, args.username, args.hash)

if __name__ == '__main__':
    main()
