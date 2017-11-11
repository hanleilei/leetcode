# Transpose File

Given a text file file.txt, transpose its content.

You may assume that each row has the same number of columns and each field is separated by the ' ' character.

For example, if file.txt has the following content:

name age
alice 21
ryan 30
Output the following:

name alice ryan
age 21 30

非常扯淡的一个题目。。动辄TLE，答案是抄来的，如果有问，就用Perl搞定得了。


```bash
awk '
{
    for (i = 1; i <= NF; i++)  {
        a[NR, i] = $i
    }
}
NF > p { p = NF }
END {    
    for (j = 1; j <= p; j++) {
        str = a[1, j]
        for (i = 2; i <= NR; i++){
            str = str " " a[i, j]
        }
        print str
    }
}' file.txt
```
