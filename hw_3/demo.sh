rm -rf artifacts
mkdir artifacts
mkdir -p artifacts/1 artifacts/2 artifacts/3
# task 3.1
poetry run --project=.. python matrix.py >> artifacts/1/out
# task 3.2
poetry run --project=.. python np_matrix.py >> artifacts/2/out
# task 3.3
poetry run --project=.. python cache.py >> artifacts/3/out