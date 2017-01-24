"""
import_legacy.py
CIS 322 - Assignment 2
Author - Cole Vikupitz
-----------------------------------------------------------------
Imports the downloaded legacy data into the specified database.

Usage:
    >> python3 import_legacy.py [database] [port_number]

Files:
    aquisitions.csv
    convoys.csv
    DC_inventory.csv
    HQ_inventory.csv
    MB005_inventory.csv
    NC_inventory.csv
    product_list.csv
    security_compartments.csv
    security_levels.csv
    SPNV_inventory.csv
    transit.csv
    vendors.csv
"""

import sys

def acquisitions():
    """
    Imports legacy data from aquisitions.csv
    """    
    ### FIXME
    print("Imported acquisitions.csv")


def convoys():
    """
    Imports legacy data from convoys.csv
    """    
    ### FIXME
    print("Imported convoys.csv")


def DC_inventory():
    """
    Imports legacy data from DC_inventory.csv
    """    
    ### FIXME
    print("Imported DC_inventory.csv")


def HQ_inventory():
    """
    Imports legacy data from HQ_inventory.csv
    """    
    ### FIXME
    print("Imported HQ_inventory.csv")


def MB005_inventory():
    """
    Imports legacy data from MB005_inventory.csv
    """    
    ### FIXME
    print("Imported MB005_inventory.csv")
    

def NC_inventory():
    """
    Imports legacy data from NC_inventory.csv
    """    
    ### FIXME
    print("Imported NC_inventory.csv")


def product_list():
    """
    Imports legacy data from product_list.csv
    """    
    ### FIXME
    print("Imported product_list.csv")


def security_compartments():
    """
    Imports legacy data from security_compartments.csv
    """
    ### FIXME
    print("Imported security_compartments.csv")
    

def security_levels():
    """
    Imports legacy data from security_levels.csv
    """
    ### FIXME
    print("Imported security_levels.csv")
    

def SPNV_inventory():
    """
    Imports legacy data from SPNV_inventory.csv
    """
    ### FIXME
    print("Imported SPNV_inventory.csv")


def transit():
    """
    Imports legacy data from transit.csv
    """    
    ### FIXME
    print("Imported transit.csv")


def vendors():
    """
    Imports legacy data from vendors.csv
    """    
    ### FIXME
    print("Imported vendors.csv")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage:")
        print("\t>> python3 import_legacy.py [database_name] [port_number]")
        sys.exit()

    print("Not implemented yet....")
    acquisitions()
    convoys()
    DC_inventory()
    HQ_inventory()
    MB005_inventory()
    NC_inventory()
    product_list()
    security_compartments()
    security_levels()
    SPNV_inventory()
    transit()
    vendors()
    print("***** Legacy data imported successfully *****")
