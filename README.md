#pywhois

 * Given a list of domains it checks the availability of domains and produces an ouput domain list
 * Works with several TLDS


I'm no good at writing sample / filler text, so go write something yourself.

Look, a list!

 * foo
 * bar
 * baz

And here's some code!

```python
import pywhois

domains=pywhois.getdomainlist('c:\\Pathtofile\list.txt')

unregisteredlist=checkdomains(domains)

print unregisteredlist
```
