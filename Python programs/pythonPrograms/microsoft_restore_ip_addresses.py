# Microsoft: Restore IP Addresses
# Given a string containing only digits, return all possible valid IP address combinations.

def restore_ip_addresses(s):
    res = []
    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))
            return
        for l in range(1, 4):
            if start + l > len(s):
                break
            seg = s[start:start+l]
            if (seg.startswith('0') and len(seg) > 1) or int(seg) > 255:
                continue
            backtrack(start+l, path+[seg])
    backtrack(0, [])
    return res

if __name__ == "__main__":
    s1 = "25525511135"
    print(restore_ip_addresses(s1))  # Output: ["255.255.11.135", "255.255.111.35"]
    s2 = "0000"
    print(restore_ip_addresses(s2))  # Output: ["0.0.0.0"]
    s3 = "101023"
    print(restore_ip_addresses(s3))  # Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
