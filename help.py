def helpMenu():
    return """
FortiDetect - An Intrusion Detection System
Usage: 

Arguments:
-h, --help: show the help message and exit
--start: start capturing network packets
--stop: stop capturing network packets
--logfile <PATH>: specify the file path where intrusion logs will be saved
--interface <INTERFACE>: specify the network interface to capture packets from
--threshold <VALUE>: set the threshold for triggering alerts based on suspicious activity
--model <PATH>: specify the path to the trained machine learning model
--features <METHOD>: choose  the method for extracting features from packets for anomaly detection
--viewlogs: display the intrusion logs
--dashboardport <PORT>: specify the port for web dashboard
"""