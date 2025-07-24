this question is a bash-only question.

```shell

if [ $(wc -l < file.txt) -lt 10 ]; then
    echo "Error: File has less than 10 lines"
else
    sed -n '10p' file.txt
fi

```
