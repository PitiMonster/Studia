#!/bin/bash

barWidth=$1
barHeight=$2
barAmount=$3

if(( $# != 3)); then
	echo "enter correct number of parameters"
	echo "1 - barWidth, 2 - barHeight, 3 - barAmount"
	exit
fi

# setting colors value
downloadColor=$(tput setaf 2)
uploadColor=$(tput setaf 4)
normal=$(tput sgr0)

downloadArray=()
uploadArray=()
downloadHeightArray=()
uploadHeightArray=()

# filling arrays with 0s value
for (( i=0; i<$barAmount; i++)); do
	downloadArray+=(0)
	uploadArray+=(0)
	downloadHeightArray+=(0)
	uploadHeightArray+=(0)
done

maxDownload=${downloadArray[0]}
maxUpload=${uploadArray[0]}

downloadAvg=0
uploadAvg=0

numOfDev=$(ls /sys/class/net | wc -w)

trap ctrl_c INT
stty -ctlecho

# executing after pressing ctrl+c
function ctrl_c() {
	temp=$(echo "16 + $barHeight * 2" | bc)
	for (( i=0; i<$temp; i++ )); do
		echo ""
	done

	tput cnorm
	stty ctlecho
	clear
	exit
}

# calculating curren speed
function calculateSpeed {
	rec1=0
	t1=0
	for (( i=0; i<$numOfDev; i++ )); do
		index=$(($i + 3))
		tempRec=$(awk -v i=$index 'FNR == i {print $2}' /proc/net/dev)
		tempT=$(awk -v i=$index 'FNR == i {print $10}' /proc/net/dev)
		rec1=$(($rec1 + $tempRec))
		t1=$(($t1+$tempT))
	done

	sleep "1"

	rec2=0
	t2=0
    for (( i=0; i<$numOfDev; i++ )); do
		index=$(($i + 3))
		tempRec=$(awk -v i=$index 'FNR == i {print $2}' /proc/net/dev)
		tempT=$(awk -v i=$index 'FNR == i {print $10}' /proc/net/dev)
		rec2=$(($rec2 + $tempRec))
		t2=$(($t2+$tempT))
	done
	
	download=$(($rec2-$rec1))
	upload=$(($t2-$t1))
}

# setting correct unit of bites amount
function setUnit {
	local speedValue=$1
	local unitsNames=(B KB MG GB TB)
	local i=0
	while (($speedValue>=1000)); do
		speedValue=$(echo "$speedValue/1000" | bc)
		i=$(($i+1))
	done

	echo -e "$speedValue ${unitsNames[$i]}/s"
}
# calculating average speed
function calculateAverage {
	local avg=0
	for(( i=0; i<${#downloadArray[@]}; i++)); do
		liczba=${downloadArray[$i]}
		avg=$(($avg+$liczba))	
	done
	
	downloadAvg=$(echo "$avg/$barAmount" |bc)
	
	avg=0
	for(( i=0; i<${#uploadArray[@]}; i++)); do
		liczba=${uploadArray[$i]}
		avg=$(($avg+$liczba))	
	done
	
	uploadAvg=$(echo "$avg/$barAmount" |bc) 
}
# showing system uptime
function showSystemTime {
	totalSeconds=$(awk '{print $1}' /proc/uptime)

	intervalsNames=(seconds minutes hours days)
	intervalsDuration=(1 60 60 24 1)
	intervalCount=()

	
	for(( i=0; i<${#intervalsNames[@]}; i++)); do
		
		totalSeconds=$(echo "$totalSeconds/${intervalsDuration[$i]}" | bc)
		intervalCount[$i]=$(echo "$totalSeconds%${intervalsDuration[$i+1]}" | bc)
	done

	for(( i=$((${#intervalsNames[@]}-1)); i>=0; i--)); do
		echo -n "${intervalCount[$i]} ${intervalsNames[$i]} "
	done
	echo ""
}
# showing current battery state
function showBatteryState {
	if [ -f /sys/class/power_supply/BAT0/uevent ]; then
		battery=$(cat /sys/class/power_supply/BAT0/uevent | grep -oP '(?<=POWER_SUPPLY_CAPACITY=).*')
		echo "battery level: $battery                     "
	fi
}
# showing /proc/loadavg
function showSystemLoadavg {
	echo "loadavg: $(cat /proc/loadavg)                         "
}
# adding current speed to array 
function addToArray {
	local -n tmpArray=$1
	local tmpArraySize=${#tmpArray[@]}

	for (( i=0; i<$tmpArraySize; i++ )); do
        tmpArray[$i]=${tmpArray[(($i+1))]}
    done
    
	tmpArray[-1]=$2
}
# setting current max download and upload speed
function setMax {
	maxDownload=${downloadArray[0]}
	maxUpload=${uploadArray[0]}

	for (( i=1; i<${#downloadArray[@]}; i++ )); do
		if (( ${downloadArray[$i]} > $maxDownload )); then
            maxDownload=${downloadArray[$i]}
        	fi
		
		if (( ${uploadArray[$i]} > $maxUpload )); then
            maxUpload=${uploadArray[$i]}
        	fi
	
   	done
}
# calculating height of the plot
function calculateHeight {
	local -n arr=$1
	local -n heightArray=$2
	local scale=$(echo "$3/$barHeight" | bc)
	local arrSize=${#arr[@]}

	for (( i=0; i<$arrSize; i++ )); do
		if (( $scale == 0 )); then
			heightArray[$i]=0
		else
			heightArray[$i]=$(echo "${arr[$i]}/$scale" | bc) 
		fi
	done 
}
# showing plot
function showPlot {
	local -n heightArray=$1
	local color=$2
	printf "%-$(($(($(($barWidth+1))*$barAmount))/2))s $3                       \n"
	for (( i=1; i<=$barHeight; i++ )); do
		echo -n -e "\u2551"
		for (( j=1; j<=$barAmount; j++ )); do
			if (( $(($barHeight-$i)) < ${heightArray[$(($j-1))]} )); then
				bar=""
				for (( k=0; k<$barWidth; k++ )); do 
					bar+="\u2588"
				done
				echo -n -e " ${color}$bar${normal}"
			else
				echo -n " "
				for (( k=0; k<$barWidth; k++ )); do 
					echo -n " "
				done
			fi
		done
		
		echo -e "\u2551"
		
	done
}

#clearing terminal and making cursor invisible
clear
tput civis

# executing all functions every seconds indefinitely
while(true); do
tput cup 0 0
showSystemLoadavg
echo "system uptime: $(showSystemTime)"
showBatteryState
calculateSpeed

addToArray downloadArray $download
addToArray uploadArray $upload

calculateAverage
echo "download present speed: $(setUnit $download)                                     "
echo "upload present speed: $(setUnit $download)                                       "
echo "average download speed: $(setUnit $downloadAvg)                                  "
echo "average upload speed: $(setUnit $uploadAvg)                                      "

setMax
calculateHeight downloadArray downloadHeightArray $maxDownload
calculateHeight uploadArray uploadHeightArray $maxUpload


showPlot downloadHeightArray $downloadColor $maxDownload
showPlot uploadHeightArray $uploadColor $maxUpload
 
done
