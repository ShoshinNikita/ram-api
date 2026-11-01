# ram-api

Dockerized FastAPI wrapper around the [Recognize Anything Plus Model](https://github.com/xinyu1205/recognize-anything).

The model weights are baked into the docker image rather than fetched at runtime.
This means it's possible to run this image without granting it internet access
(`--network=none`).

```shell
make run-docker

curl -v -F file=@/opt/app/recognize_anything/images/demo/demo1.jpg localhost:8000/
```

## Build & Run

1. Clone the repository with submodules `git clone --recurse-submodules`
2. Run `make run-docker` to build a Docker image and run it

## License

See [./LICENSE](./LICENSE) and [./recognize_anything/NOTICE.txt](./recognize_anything/NOTICE.txt)
