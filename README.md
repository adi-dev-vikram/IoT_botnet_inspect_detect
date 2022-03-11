# Botnet Detection using Machine learning on IoT devices

## About the project :

There has been a significant rise in IoT devices and since these devices are less secure and are vulnerable to DDoS attacks and often targeted by botnets. It could be advantageous to develop a machine learning model that predicts ddos attacks. Internet of Things (IoT) devices are widely used in modern homes and every part of our lives, because they are not that sophisticated, it becomes an easy target for Denial of service attack. One of the common ways in which attacks work is they propagate through the vulnerable IoT devices and infect them with malwares. These codes run and then C&C communication is established. Thus, they are used as part of DDoS attacks. For e.g Mirai.

## About the dataset :

The BoT-IoT dataset was created by cybersecurity lab in UNSW Canberra. The network environment incorporated a combination of benign and botnet or malicious traffic. I have combined the datasets into a single csv file. The files were separated, based on attack category and subcategory, to better assist in labeling process. we aimed at distinguishing between benign and Malicious traffic data by means of anomaly detection techniques.
It contains the following features like:- source ip, dest ip, src_port, dst_port and protocol, total_data, sent_data, recv_data etc.
In future the app would take input as pcap file or genrate pcap files, then convert them into CSV files and perform classification.

Another Data set that i will use : https://archive.ics.uci.edu/ml/datasets/detection_of_IoT_botnet_attacks_N_BaIoT (UCI Data)

Machine learning algorithms used :

* SVM
* ANN
* Random Forest

Classification Metrices :
Accuracy:
F1 Score: 
Precision: 
Recall: 

## Pcap Analyser tool :
We have implemented a web app and CLI tool that performs statistical analysis on the pcap file which gives valuable insights and saves time.
Used Scapy, pandas for this.
