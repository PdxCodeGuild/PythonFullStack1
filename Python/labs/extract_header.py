"""
>>> extract_domain("spf=pass (google.com: domain of jwackman@hvc.rr.com designates 2\
a00:1450:400c:c09::22d as permitted sender")
hvc.rr.com
"""


def extract_domain(email_header):
    start = email_header.find('@')
    end = email_header.find(" ", start)
    domain = header[start:end]

    return domain
