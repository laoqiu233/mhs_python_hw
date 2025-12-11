#!/bin/bash

rm -rf ./artifacts
mkdir ./artifacts

# Demonstrating nl with file
cat > ./artifacts/nl_source <<EOF
Hello
world!
This is
a test!
test!
test!
test!
test!
test!
test!
test!
test!
test!
EOF

poetry run python nl.py artifacts/nl_source > ./artifacts/nl_output_file

# Demonstrating nl with stdin

poetry run python nl.py > ./artifacts/nl_output_stdin <<EOF
Goodbye
world!
This is
the final test
for nl.py!
stdin!
stdin!
stdin!
stdin!
stdin!
stdin!
stdin!
stdin!
stdin!
EOF

# Demo tail from one file

poetry run python tail.py artifacts/nl_output_file > ./artifacts/tail_output_one_file

# Demo tail from multiple files

poetry run python tail.py artifacts/nl_output_file artifacts/nl_output_stdin > ./artifacts/tail_output_multiple_files

# Demo tail from stdin

poetry run python nl.py <<EOF | poetry run python tail.py > ./artifacts/tail_output_stdin 
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
hello!
EOF

# Demo wc single file

poetry run python wc.py nl.py > artifacts/wc_single_file

# Demo wc multiple files

poetry run python wc.py nl.py tail.py > artifacts/wc_multiple_file

# Demo wc stdin

poetry run python wc.py > artifacts/wc_stdin <<EOF
hello
world
test!
EOF