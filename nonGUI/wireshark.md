# Wireshark

> Source: https://www.wireshark.org/docs/man-pages/wireshark-filter.html

> Aliases: gui-tshark

$ Installation
    `Windows Installation          {{Download wireshark from https://www.wireshark.org/download.html and execute the installer file}} 
    `Ubuntu Installation           {{apt-get install wireshark}} 
    `Arch Linux Installation       {{pacman -Syu wireshark-qt}} 

$ Main Window Navigation
    ` Shift   Tab  /  Tab          {{Move between screen elements, e.g. from the toolbars to the packet list to the packet detail}} 
    ` ↓                            {{Move to the next packet or detail item}} 
    ` ↑                            {{Move to the previous packet or detail item}} 
    ` Ctrl   ↓  /  F8              {{Move to the next packet, even if the packet list isn’t focused}} 
    ` Ctrl   ↑  /  F7              {{Move to the previous packet, even if the packet list isn’t focused}} 
    ` Ctrl   .                     {{Move to the next packet of the conversation (TCP, UDP or IP)}} 
    ` Ctrl   ,                     {{Move to the previous packet of the conversation (TCP, UDP or IP)}} 
    ` ←                            {{In the packet detail, closes the selected tree item. If it’s already closed, jumps to the parent node}} 
    ` →                            {{In the packet detail, opens the selected tree item}} 
    ` Shift   →                    {{In the packet detail, opens the selected tree item and all of its subtrees}} 
    ` Ctrl   →                     {{In the packet detail, opens all tree items}} 
    ` Ctrl   ←                     {{In the packet detail, closes all tree items}} 
    ` Backspace                    {{In the packet detail, jumps to the parent node}} 
    ` Return  /  Enter             {{In the packet detail, toggles the selected tree item}} 

$ Comparison Operators Display Filter
    `eq /  ==                      {{Equal Ex: ip.src == 10.0.0.5}} 
    `ne /  !=                      {{Not Equal Ex: ip.src != 10.0.0.5}} 
    `gt /  >                       {{Greater than Ex: frame.len > 10}} 
    `lt /  <                       {{Less than Ex: frame.len < 128}} 
    `ge /  >=                      {{Greater than or equal to Ex: frame.len ge 0x100}} 
    `le /  <=                      {{Less than or equal to Ex: frame.len <= 0x20}} 
    `contains                      {{Protocol, field or slice contains a value Ex: http contains "https://www.wireshark.org"}} 
    `matches                       {{Protocol or text field matches Perl regualar expression Ex: wsp.user_agent matches "(?i)cldc"}} 
    `bitwise_and /  &              {{Compare bit field value Ex: tcp.flags & 0x02}} 

$ Field Types Display Filter
    `Unsigned/Signed integer       {{Can be 8, 16, 24, 32, or 64 bits (decimal,octal or hexadecimal) Ex: ip.len le 0x436}} 
    `Boolean                       {{It is present in the protocol decode only if its value is true Ex: +tcp.flags.syn+}} 
    `Text string                   {{ Strings are enclosed in double quotes Ex: http.request.method == "POST"}} 
    `Ethernet or MAC address       {{eth.len, eth.src, eth.dst, eth.addr,eth.lg, eth.type, eth.trailer Ex: eth.dst == ff:ff:ff:ff:ff:ff}} 
    `WLAN (802.11)                 {{wlan.addr, wlan.ra, wlan.ta, wlan.da, wlan.sa, wlan.fc.type, wlan.fc.type_subtype, wlan.bssid, wlan.aid}} 
    `IPv4 address                  {{ip.addr, ip.checksum, ip.dst, ip.flags, ip.fragment, ip.host, ip.len, ip.id, ip.src, ip.ttl Ex: ip.src == 192.168.0.1}} 
    `IPv6 address                  {{ipv6.addr, ipv6.dst, ipv6.class, ipv6.fragment, ipv6.host, ipv6.src, ipv6.nxt, ipv6.flow, ipv6.version Ex: ipv6.addr == ::1}} 
    `ARP filter                    {{arp.dst.hw_mac, arp.hw.size, arp.hw_type, arp.opcode, arp.proto.size, arp.proto.type, arp.src.hw_mac, arp.src.proto_ipv4}} 
    `TCP filter                    {{tcp.ack, tcp.checksum, tcp.dstport, tcp.flags, tcp.flags.ack, tcp.flags.syn, tcp.flags.reset, tcp.len, tcp.srcport, tcp.dstport, tcp.seq}} 
    `UDP filter                    {{udp.checksum, udp.dstport, udp.srcport, udp.port, udp.length, udp.checksum_good, udp.checksum_bad}} 
    `Frame relay                   {{fr.becn, fr.control, fr.control.ftype, fr.control.p, fr.dc, fr.cr, fr.de, fr.dlci, fr.ea, fr.snaptype, fr.nlpid, fr.fecn, fr.snap.pid}} 
    `PPP filter                    {{ppp.address, ppp.direction, ppp.control, ppp.protocol}} 
    `MPLS filter                   {{mpls.bottom, mpls.cw.control, mpls.exp, mpls.label, mpls.oam.frequency, mpls.oam.function_type, mpls.oam.defect_type, mpls.ttl}} 
    `ICMP filter                   {{icmp.checksum, icmp.code, icmp.checksum_bad, icmp.ident, icmp.seq, icmp.type, icmp.mtu}} 
    `VTP filter                    {{vtp.code, vtp.md, vtp.md5_digest, vtp.md_len, vtp.seq_num, vtp.version, vtp.vlan_info.len, vtp.vlan_info.mtu_size, vtp.vlan_info.vlan_type}} 
    `ICMPv6                        {{icmpv6.code, icmpv6.checksum, icmpv6.checksum_bad, icmpv6.comp, icmpv6.identifier, icmpv6.option, icmpv6.type, icmpv6.option.length}} 
    `RIP filter                    {{rip.auth.passwd, rip.ip, rip.netmask, rip.metric, rip.family, rip.next_hop, rip.version, rip.command, rip.route_tag}} 
    `HTTP filter                   {{http.accept, http.authbasic, http.cache_control, http.connection, http.cookie, http.host, http.request, http.response, http.user_agent}} 

$ Logical Operators Display Filter
    `and /  &&                     {{Logical AND Ex: ip.src==10.0.0.5 and tcp.flags.fin}} 
    `or /  ||                      {{Logical OR Ex: ip.scr==10.0.0.5 or ip.src==192.1.1.1}} 
    `xor /  ^^                     {{Logical XOR Ex: tr.dst[0:3] == 0.6.29 xor tr.src[0:3] == 0.6.29}} 
    `not /  !                      {{Logical NOT Ex: not llc}} 
    `...                           {{Substring Operator Ex: eth.src[0:3] == 00:00:83 Ex: eth.src[1-2] == 00:83 Ex: eth.src[:4] == 00:00:83:00 Ex: eth.src[4:] == 20:20}} 
    `in                            {{Membership Operator Ex: tcp.port in {80 443 8080}}} 

