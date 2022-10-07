from asyncio import gather
from operator import contains
import dns.resolver

ips = []
domains = []

"""
Returns SPF record for a given domain.
Returns None if no SPF record is found.
"""
def get_spf_record(domain):
    try: 
        txt_records = dns.resolver.resolve(domain, "TXT").response.answer[0]
        for i in txt_records:
            if "v=spf1" in str(i):
                return str(i)
        return None
    except:
        pass

def gather_all(spf):
    if spf is None:
        return
    if "include:" not in spf and ("a:" in spf or "ip4:" in spf):
        spf = spf.split(" ")
        for i in spf:
            if i.startswith("a:"):
                print(i[2:])
                domains.append(i[2:])
            if i.startswith("ip4:"):
                ips.append(i[4:])
        return
    spf = spf.split(" ")
    for i in spf:
        if i.startswith("a:"):
            print(i[2:])
            domains.append(i[2:])
        if i.startswith("ip4:"):
            ips.append(i[4:])
        if i.startswith("include:"):
            domains.append(i[8:])
            #print(i[8:])
            gather_all(get_spf_record(i[8:]))

if __name__ == "__main__":
    #domain = "google.com"
    domain = input("Enter a domain: ")
    spf = get_spf_record(domain)
    gather_all(spf)
    print(domains)
    print(ips)
