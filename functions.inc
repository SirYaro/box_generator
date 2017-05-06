#!/bin/bash

function CheckScreen()
{
if [ -z "$STY" ]; then
    echo -e "Run script in screen session. Exiting."; exit 1
fi
}

function CheckDeps()
{
for DEP in $DEPS; do
    echo "Checking for ${DEP}..."
    which $DEP >> /dev/null
    if [ $? -eq 1 ]; then
	echo -ne "Missing required dependency: \"$DEP\". Exiting."; exit 1
    fi
done

}

function Wait()
{
    if [ $1 -eq 6 ]; then echo "Can't wait any longer. Something is wrong. Exiting." exit 1; fi	# don't wait more than 150 sec (10+20+30+40+50)
    echo "Waiting $(( 10 * $1 )) sec"
    sleep $(( 10 * $1 ))
}

function ProcessingTime()
{
time2=$(date +%s.%N)
dt=$(echo "$time2 - $time1" | bc)
dd=$(echo "$dt/86400" | bc)
dt2=$(echo "$dt-86400*$dd" | bc)
dh=$(echo "$dt2/3600" | bc)
dt3=$(echo "$dt2-3600*$dh" | bc)
dm=$(echo "$dt3/60" | bc)
ds=$(echo "$dt3-60*$dm" | bc)

printf "Total runtime: %d:%02d:%02d:%02.4f\n" $dd $dh $dm $ds
}
