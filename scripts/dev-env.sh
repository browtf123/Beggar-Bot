docker run --name beggerbot -it --rm \
    -v "$(pwd)/poetry.lock:/home/worker/poetry.lock" \
    -v "$(pwd)/pyproject.toml:/home/worker/pyproject.toml" \
    -v "$(pwd)/src:/home/worker/src" \
    beggerbot