# BtoothRangeExtension
An open-source Bluetooth Range Extension module that works in the application layer to achieve extension in the range of operation in Class 2 Bluetooth devices through single/multi-hop store and forward networking.

This repository (as of now) contains only the key file that I had coded myself by piecing together various algorithms I had learned to complete this project.

The file is a python script which checks a specified directory on a linux device for 'txt' files and then processes them to read the
first line containing source and destination MAC addresses (as required by design) and then proceeds to initiate a Bluetooth search 
for the destination device and the appropriate OBEX service. Upon a successful search, it sends the file to the destination device and
logs the metadata and deletes the file from the directory.

Other files used to complete this project such as the Linux service script for configuring Bluetooth device and port and setting it to
permanently listen for incoming files and other shell scripts used to automate the process and open new terminals have not been uploaded
as they are simple to code and don't require any guidance or time. I will upload them later when I get time to compile all the files
into one directory as my PC and Pi are still very much unsorted and I can't dedicate time to sort them out while focusing on my graduation.

Thank you. Do not hesitate to message me if have any questions or doubts about the code.
