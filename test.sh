find . -name "*.wav"\
     -exec echo sh -c 'python -m encodec "$1" > "$1.txt" --force' {} \;
