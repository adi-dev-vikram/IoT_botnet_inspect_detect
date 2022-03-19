from prettytable import PrettyTable
%matplotlib inline
def read_pcap():
  pcap_read = rdpcap('suspicious.pcap')
  for pkt in pcap_read:
    if pkt.haslayer(DNSQR):
        query = pkt[DNSQR].qname
        print(query)
    if pkt.haslayer(IP):
      pckt_src=pkt[IP].src
      pckt_dst=pkt[IP].dst
      pckt_ttl=pkt[IP].ttl
      print("IP Packet: {} is going to {} and has ttl value {}".format(pckt_src,pckt_dst,pckt_ttl))

def process_src_IP():
  packets = rdpcap('suspicious.pcap')
  srcIP=[]
  for pkt in packets:
    if IP in pkt:
      try:
        srcIP.append(pkt[IP].src)
        #print(srcIP)
      except:
        pass
  
  cnt=Counter()
  for ip in srcIP:
    cnt[ip] += 1
  xData=[]
  yData=[]
  for ip, count in cnt.most_common():
    xData.append(ip)
    yData.append(count)

  table= PrettyTable(["IP", "Count"])
  for ip, count in cnt.most_common():
    table.add_row([ip, count])
  print(table)
  plt.bar(xData,yData)
  plt.title("Src IP count")
  plt.xlabel("Src IPs ")
  plt.ylabel("Number of times it occuered ")
  #plt.setp(plt.get_xticklabels(), rotation=30, horizontalalignment='right')
  plt.xticks(xData, rotation='vertical')
  plt.show()

def main():
  #read_pcap()
  process_src_IP()



if __name__=='__main__':
  main()

#interface = "eth0"
#def print_packet(packet):
# ip_layer = packet.getlayer(IP)
# print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src,
#dst=ip_layer.dst))
#print("[*] Start sniffing...")
#sniff(iface=interface, filter="ip", prn=print_packet)
#print("[*] Stop sniffing")
