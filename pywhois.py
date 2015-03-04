import pythonwhois
import datetime
import time

def waiter(TIME):
    print "Waiting for: " + str(TIME) + ' seconds.'
    time.sleep(TIME)
    return 1

#Gets the list of domains to check
def getdomainlist(PATH):
    f = open(PATH, 'r')
    domainlist=[]
    for lines in f:
        domainlist.append(lines.replace('\n', ''))
    return domainlist

#Path to the domain list
PATH = 'c:\\Users\\chasej\\desktop\\domainlist.txt'
domainlist = getdomainlist(PATH)

#All of the TLDS to check
TLDS=['.org','.com','.net','.io']

finaldomainlist=[]
#Generate full domain + each of the tlds
for toplevel in TLDS:
    for domain in domainlist:
        finaldomainlist.append(domain + toplevel)

print finaldomainlist
availabledomains=[]
expiringsoon=[]

for domains in finaldomainlist:
    waiter(10)
    print "Checking: " + domains
    w = pythonwhois.get_whois(domains)
    now = datetime.datetime.now()
    print w
    try:
        expirationdate = w['expiration_date'][0]
        print "Expiration Date: " + str(expirationdate.day) + '-' + str(expirationdate.month) + '-' + str(expirationdate.year)
        if expirationdate.month == now.month and expirationdate.year == now.year:
            print "Domain Expiring this month and year"
            expiringsoon.append(domains)
        if expirationdate.month == now.month+1 and expirationdate.year == now.year:
            print "Domain Expiring next month"
            expiringsoon.append(domains)
    except KeyError:
        print "No Exiration Found, possibly available domain"
        availabledomains.append(domains)

print 'Pritning available domains: '
for domains in availabledomains:
    print domains
print 'Printing domains Expiring soon: '
for domains in expiringsoon:
    print domains