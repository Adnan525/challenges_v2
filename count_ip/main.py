def count_ip(ip_str_1: str, ip_str_2:str) -> int:
    """
    takes 2 str ip addresses and returns the number of available ip addresses
    :params- 2 ip strings 
    :return- int number
    :logic- treat each octet individually and consider their position in the IP address.
    Each octet contributes a specific weight to the final integer value based on its position.
    The first octet (leftmost) has the highest weight, followed by the second, third, and so on.
    We can use powers of 256 (since an IP address deals with bytes) to represent these weights.
    """
    
    ip1 = sum([int(oct)*pow(256, len(ip_str_1.split("."))-(i+1)) for i, oct in enumerate(ip_str_1.split("."))])
    ip2 = sum([int(oct)*pow(256, len(ip_str_1.split("."))-(i+1)) for i, oct in enumerate(ip_str_2.split("."))])
    return abs(ip1-ip2)

print(count_ip("10.0.0.0", "10.0.0.50"))

# from ipaddress import ip_address

# def ips_between(start, end):
#     return int(ip_address(end)) - int(ip_address(start))