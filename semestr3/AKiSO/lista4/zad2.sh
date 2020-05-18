#!/bin/bash

#echo -e 'nazwa\tpid\tppid\tstatus\tilosc_otwartych_plikow'
		printf "%-0s%-25s nazwa"
		printf "%-0s%-7s pid"
		printf "%-0s%-6s ppid"
		printf "%-0s%-14s status"
		printf "%-5s ilosc_plikow\n"

for i in $(sudo ls /proc | awk '/[0-9]+/{print}' ); do
	if [ -d "/proc/$i" ]; then

		nazwa=$(echo $(awk 'FNR == 1' /proc/$i/status | cut -d":" -f2))
		pid=$(echo $(awk 'FNR == 6' /proc/$i/status | cut -d":" -f2))
		ppid=$(echo $(awk 'FNR == 7' /proc/$i/status | cut -d":" -f2))		
		status=$(echo $(awk 'FNR == 3' /proc/$i/status | cut -d":" -f2))
		ilosc_plikow=$(echo $(sudo ls -l /proc/$i/fd | wc -l))

		#echo -e "$nazwa\t$pid\t$ppid\t$status\t$ilosc_plikow"
		printf "%-0s%-$((30-${#nazwa}))s $nazwa"
		printf "%-0s%-$((10-${#pid}))s $pid"
		printf "%-0s%-$((10-${#ppid}))s $ppid"
		printf "%-0s%-$((20-${#status}))s $status"
		printf "%-5s $ilosc_plikow\n"
	fi
done
