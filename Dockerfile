FROM ghcr.io/astral-sh/uv:0.13.6-python3.15-trixie@sha256:f68dfb3eaf23a53afb5f74833bdacc0ce586d69f8063c48f9f3ebbe42e048e4a

WORKDIR /srv

RUN mkdir -p /data/pretrained/
RUN wget -O /data/pretrained/ram_plus_swin_large_14m.pth https://huggingface.co/xinyu1205/recognize-anything-plus-model/resolve/main/ram_plus_swin_large_14m.pth

COPY uv.lock .python-version ./
RUN --mount=type=cache,target=/root/.cache/uv \
	uv sync --frozen --no-install-project

COPY pyproject.toml .
COPY src/recognize_anything_api src/recognize_anything_api/
COPY recognize_anything recognize_anything
COPY Makefile .

ENTRYPOINT ["make", "run"]
