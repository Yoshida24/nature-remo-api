# nature-remo-api

## Usage
Python 3.10.6

## Setup

```
cp .env.sample .env
```

then, write your properties on `.env`.

## Commands

run locally

```
-a & source .env & set +a & python3 app/src/main.py <command>
# e.g. -a & source .env & set +a & python3 app/src/main.py turn_off_aircon
```

build docker image

```
make docker_build
```

run docker conatiner

```bash
docker run -it nature_remo_api <command> --rm
# e.g. docker run -it nature_remo_api turn_off_aircon --rm
```
