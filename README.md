# Censor-Api
## Pip Installs:
- pip install **flask**
- pip install **flask_restful**

## How to use:
### Example 1:
```
Example Api Call (USING CURL):
COMMAND:  curl 127.0.0.1:PORT/QCheck/"MESSAGE"
RESPONSE: MESSAGE
```
### Example 2:
```
Example Api Call (USING CURL):
COMMAND:  curl 127.0.0.1:PORT/QCheck/"BLACKLISTEDWORD you"
RESPONSE: "***** you"
```
### Example 3:
```python
import requests
PORT = 5555
MESSAGE = "place_holder_message"
TYPEOFCHECK = "TCheck"
r = requests.get(f"127.0.0.1:{PORT}/{TYPEOFCHECK}/{MESSAGE}")
print(r.text)
```

## Need To Know:
### Formatting Arguments:
- To use this API you must format your message argument to use a diameter that is not " ", the standard diameter is "_".


### API End Points:
- **/QCheck/MESSAGE** : QCheck AKA Quick check is the fastest API endpoint as it does no modulation to the string to check for potential censorship evasion.
- **/TCheck/MESSAGE** : TCheck AKA thorough check is the slower of the API endpoints as it modulates the string to detect potential censorship evasion.
- **/SCheck/MESSAGE** : SCheck AKA super check is the slowest of the API endpoints, this is because it stops and detects multiple types of censorship evasion.
<hr>

<div align="center">
  Written, developed and designed by Henry Dewsnap.
</div>
