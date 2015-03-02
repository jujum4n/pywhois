#pywhois

 * Given a list of domains it checks the availability of domains and produces an ouput domain list
 * Works with several TLDS


This project is a work in progress, lacks error ehcking, and was used only for a specific purpose.

Todo:
 * Error Checking
 * Reporting
 * Deal with muti-TLDS

Example Usage:
```python
import pywhois

domains=pywhois.getdomainlist('c:\\Pathtofile\list.txt')

unregisteredlist=checkdomains(domains)

print unregisteredlist
```
