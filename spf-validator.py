from operator import contains
import dns.resolver


"""
Returns SPF record for a given domain.
Returns None if no SPF record is found.
"""
def get_spf_record(domain):
    txt_records = dns.resolver.resolve(domain, "TXT").response.answer[0]
    for i in txt_records:
        if "v=spf1" in str(i):
            return str(i)
        else:
            return None

if __name__ == "__main__":
    domain = "google.com"
    #domain = input("Enter a domain: ")
    get_spf_record(domain)
