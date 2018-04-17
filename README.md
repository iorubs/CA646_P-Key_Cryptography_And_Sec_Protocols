# CA646_PKey_Crypto_and_Sec_Protocols
Pratical work for the module CA646 P-Key Cryptography & Sec Protocols

### Run:
#### RSA Run:
```bash
# $TYPE = one of [rsa, el_gamal, digital_signatures]
# $POSTFIX = rsa, eg or ds
docker run -it --rm -v "$PWD":/app -w /app python:3-alpine python $TYPE/practicals.py run_$POSTFIX
```

#### Individual functions:
```bash
docker run -it --rm -v "$PWD":/app -w /app python:3-alpine

>>> from $TYPE.practicals import $FUNC_NAME

# Then call the function.
```
