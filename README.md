# MythX API test

## Running

1. Install requirements:
```bash
$ pip install -r requirements.txt
```

2. Run test:
```bash
$ python mythx_test.py
```

## Docker

1. Build image:
```bash
$ docker build -t mythx-test .
```

2. Run test in docker:
```bash
$ docker run --rm -t mythx-test
```

## Settings
### Environment variables

| env     | Default             | Description     |
|---------|---------------------|-----------------|
| ETH_ADDRESS | 0x0000000000000000000000000000000000000000 | MythX account address |
| PASSWORD | trial | MythX account password |

### CLI params

| flag     | Value | Default             | Description     |
| ---------|---------------------|-----------------|
| --api-url | https://api.mythx.io| https://api.mythx.io | URL to MythX API |
| --no-cache | (without value) | Cache enabled | Specify if you wanna run without cache |
