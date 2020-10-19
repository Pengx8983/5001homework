#!/bin/bash
mkdir DDM{1..100}
touch DDM{1..100}/time_till_now.txT
for i in {1..100}; do
    	echo 'nanoseconds since 1970-01-01 00:00:00 UTC:'>>./DDM$i/time_till_now.txT
	echo '<'`date "+%s%N"`'>'>>./DDM${i}/time_till_now.txT
done

