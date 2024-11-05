# CENG 435 - Programming Assignment Phase 1

This repository includes the "sender" and "reciever" docker files and the Python files for the assignment requirements.

## Group Information

Student 1: Çağatay Kayman - 2310225 </br>
Student 2: İrem Sezgi Kılıçdoğan - 2380632 </br>
Group ID: 56 </br>
Github repository link: https://github.com/ckayman/covertovert

## Sender and Receiver Modules

Our ICMP sender module sends an ICMP packet to the reciever container. Instead of a static IP address, hostname is used as IP address to make script work in case of dynamic IP assignment.

Our ICMP receiver module awaits an ICMP packet with TTL value of 1. It does not print packets other than ICMP and TTL=1. After it receives the first correct packet successfully, it terminates.
