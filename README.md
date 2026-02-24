# whisky_hunter.py
Web-API for [whiskyhunter.net](https://whiskyhunter.net) website for collectors, Investors &amp; whisky lovers that monitors data from whisky auctions

## Example
```python
from whisky_hunter import WhiskyHunter

whisky_hunter = WhiskyHunter()
auctions_info = whisky_hunter.get_auctions_info()
print(auctions_info)
```
