#!/usr/bin/bash

#实现1+...+100的求和
sum=0

for i in `seq 1 100`
do 
  sum=$[$i+$sum]
done

echo $sum
