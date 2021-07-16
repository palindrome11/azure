#!/usr/bin/env python3

'''
Go to Virtual Machine page in the portal (filter by Resource Group -- maybe) and save the Virtual machines to a .csv file

Use thge following shell command to get the first field (VM Name and place all of them one line)

In the example below ... the name AzureVirtualMachines.csv is what we called the export list.

cat AzureVirtualMachines.csv | cut -d "," -f1 | sed 's/^"//' | sed 's/"$//' | tr '\n' ',' >unordered_list_from_csv


The List:

Analytics2,mars,SteelConnect-EX_Analytics,SteelConnect-EX_Controller,SteelConnect-EX_Director


'''