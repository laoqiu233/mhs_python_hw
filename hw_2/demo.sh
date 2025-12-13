rm -rf artifacts
mkdir artifacts

# Prepare an image for further use
curl -L https://picsum.photos/200 --output artifacts/image.jpg

# Run the main file
# Use parent dir because dependency is installed there
poetry run --project=.. python -m demo > artifacts/input.tex

# Build the docker container
docker build -t hw2-latex-renderer .
docker run --rm -v "$(pwd)/artifacts:/artifacts" hw2-latex-renderer