rm -rf artifacts/generated
mkdir -p artifacts/generated

# task 1
poetry run --project=.. python compare_fib.py >> artifacts/generated/1.out

# task 2
poetry run --project=.. python compare_integrate.py >> artifacts/generated/2.out

# task 3 
# как будто проще вручную сделать), см artifacts/ipc.out