#!/usr/bin/env python3
import dns.resolver

#check if the domain exists (no NXDOMAIN) and check if the domain has a MX records
def validate(domain):
	try:
		try:
			answers = dns.resolver.query(domain, 'MX')
			if len(answers) >0:
				print(domain, " -  MX found")
		except dns.resolver.NoAnswer:
			print(domain, " - NoAnswer")
		except dns.resolver.NoNameservers:
			print(domain, " -  no resolver NS servers found")
	except dns.resolver.NXDOMAIN:
		print(domain, " -  non existent domain")

list = 'disposable_email_blacklist.conf'
f = open(list, 'r')

for line in f:
	if '\n' == line[-1]:
		line = line[:-1]
		validate(line)
