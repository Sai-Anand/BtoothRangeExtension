# BtoothRangeExtension
An open-source Bluetooth Range Extension module that works in the application layer to achieve extension in the range of operation in Class 2 Bluetooth devices through single/multi-hop store and forward networking. This is just the script for the PoC prototype I built as a part of my Senior Capstone Project in the final year of my undergraduation in Electronics & Communication Engineering at Vellore Institute of Technlogy (2017).

This repository contains only the key algorithm/code that I wrote myself by stitching together functions and services from the various packages I used in this project.

The main file is a Python script which checks a specified directory on a Linux device (the hop module) for 'TXT' files and then processes them to read the first line containing source and destination MAC addresses (as required by design). It then proceeds to initiate a Bluetooth search for the destination device and checks for a OBEX service that supports file exchange. Upon a successful search, it sends the file to the destination device, logs the metadata, and deletes the file from the source directory.

Other scripts used to complete this project such as the Linux service script for configuring the device's Bluetooth service, port and setting it to permanently listen for incoming files; and shell scripts (if any, I can't recall) used to automate the process and open new terminals can be founnd in the Thesis document. These are fairly simple to code and don't require specific assistance when exposed to Linux/Debian.

Thank you. Do not hesitate to message me if have any questions or doubts about the code.
