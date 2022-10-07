from operator import contains
import dns.resolver

ips = []
domains = []

"""
Returns SPF record for a given domain.
Returns None if no SPF record is found.
"""
def get_spf_record(domain):
    txt_records = dns.resolver.resolve(domain, "TXT").response.answer[0]
    for i in txt_records:
        if "v=spf1" in str(i):
            return str(i)
    return None

def gather_all(ospf):
    ospf = ospf.split(" ")
    for i in ospf:
        if i.startswith("include:"):
            print(i[8:])

if __name__ == "__main__":
    domain = "yeti.com"
    #domain = input("Enter a domain: ")
    ospf = get_spf_record(domain)
    gather_all(ospf)
