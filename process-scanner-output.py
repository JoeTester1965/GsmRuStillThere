import sys

with open(sys.argv[1]) as kal_input:
    kal_input.readline()

    ppm = sys.argv[2]

    power_threshold = sys.argv[3]
    
    print("#!/bin/bash")
    print("")
    
    print("if [[ $(/usr/bin/id -u) -ne 0 ]]; then")
    print("echo 'Not running as root'")
    print("exit")
    print("fi")
    print("")

    print("rm -f imsi.csv")
    print("")

    print("echo 'Control-C to stop looping round GSM channels'")
    print("sleep 1 ")
    print("pkill -f grgsm_livemon_headless")
    print("pkill -f tshark")
    print("sudo stdbuf -i0 -o0 -e0 tshark -i lo -Y e212.imsi -T fields -e e212.imsi -e frame.time -E separator=, -E quote=d -E occurrence=f >> imsi.csv 2>/dev/null &")
    print("")

    print("while [ 1 ]")
    print("do")
    average_ppm_offset = 0.
    valid_stations = 0
    for line in kal_input:
        if "chan:" in line:
            frequency=line.split("(")[1][0:6]
            power=line.split(":")[2].lstrip().rpartition('.')[0]
            if (int(power) > int(power_threshold)):
                print("echo 'Processing " + frequency + "'")            
                print(" grgsm_livemon_headless -p " + ppm + " -g 40 -s 2000000 -f " 
                                    + frequency + " > /dev/null 2>&1 < /dev/null &")
                print(" sleep 600")
                print(" pkill -f grgsm_livemon_headless")

    print("done")
