#!/bin/bash

charspool=('a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p'
'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z' '0' '1' '2' '3' '4' '5' '6' '7'
'8' '9' '0' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O'
'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z' '!' '£' '$' '%' '&' '=' '.' ',' ';' ':' '-' '_');

len=${#charspool[*]}

if [ $# -lt 1 ]; then
        num=12;

else
        num=$1;
fi
randomnumbers=$(head -c $num /dev/urandom | od -t u1 | awk '{for (i = 2; i <= NF; i++) print $i}')
echo -n "password: "
for c in $randomnumbers; do
        echo -n ${charspool[$((c % len))]}
done
echo
