FROM ghcr.io/astral-sh/uv:0.13.6-python3.15-trixie@sha256:f68dfb3eaf23a53afb5f74833bdacc0ce586d69f8063c48f9f3ebbe42e048e4a

WORKDIR /srv

RUN mkdir -p /data/pretrained/
RUN wget -O /data/pretrained/ram_plus_swin_large_14m.pth https://huggingface.co/xinyu1205/recognize-anything-plus-model/resolve/main/ram_plus_swin_large_14m.pth

COPY uv.lock .python-version ./
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
	uv sync --frozen --no-install-project

COPY pyproject.toml .
COPY src/ram_api src/ram_api/

RUN --mount=type=cache,target=/root/.cache/uv \
	uv sync --locked

RUN uv run src/ram_api/init.py

COPY Makefile .

ENTRYPOINT ["make", "run"]
