import whois
import datetime
import time

def timeout():
    return 1

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
TLDS=['.com', '.org', '.net', '.io']

finaldomainlist=[]
#Generate full domain + each of the tlds
for toplevel in TLDS:
    for domain in domainlist:
        finaldomainlist.append(domain + toplevel)

print finaldomainlist
for domains in finaldomainlist:
    waiter(3)
    print "Checking: " + domains
    w = whois.whois(domains)
    now = datetime.datetime.now()
    print w
    if w.expiration_date[0]:
        if now > w.expiration_date[0]:
            print domains + " is expired."