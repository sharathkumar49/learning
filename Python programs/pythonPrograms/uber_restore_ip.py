# Uber: Find all possible valid IP addresses from a string
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
            part = s[start:start+l]
            if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start+l, path+[part])
    backtrack(0, [])
    return res

if __name__ == "__main__":
    s = input("Enter digits: ")
    print("Valid IPs:", restore_ip_addresses(s))
