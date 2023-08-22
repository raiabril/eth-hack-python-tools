# Scapy cheatsheet

    ls() 														# Protocols supported by scapy
    lsc() 														# List the commands available
    conf 														# configuration file
    help(rdpcap) 												# Help documentation
    pack_ = IP(dst="dgtsec.com", ttl=10) 						# Create a sample packet
    pack_.show() 												# Display the packet
    conf.color_theme=ColorOnBlackTheme()						# Change the color theme.
    IFACES 														# To see the list of interfaces available
    sniffer_ = sniff(iface="Intel(R) Wireless ...", count=15)	# Sniff 15 packet in the interface selected
    sniffer_.show() 											# See the packages received in the sniffer
    sniffer_[5].show() 											# See the package at index 5.
    hexdump(sniffer_[5].load)									# Hexdump of the load of the packet
    hexdump(sniffer_[5])										# Hexdump of the packet
	sniffer = sniff(filter="port 443 and host 162.12.12.12", count=15, prn=lambda x:x.summary())
	wrpcap("dgt.cap", sniffer) # Write to a file the sniffer
	read_cap = rdpcap("dgt.cap") 								# Read cap file
	read_cap[5].show() 											# Show a packet
	packet_t = IP(dst="dgtsec.com")/ICMP()/"You are not secured"						# Create a ICMP packet
	resp = sr(packet_t) # To send the packet.
	resp[0].summary()	# See the details of the packet.