docker run --name beggerbot -it --rm \
    -v "$(pwd)/poetry.lock:/home/worker/poetry.lock" \
    -v "$(pwd)/pyproject.toml:/home/worker/pyproject.toml" \
    -v "$(pwd)/src:/home/worker/src" \
    -v "$(pwd)/.env:/home/worker/.env" \
    --entrypoint poetry \
    beggerbot run python3 ./src/main.py