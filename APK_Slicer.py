#!/usr/bin/env python3


#------------------------------------------------------#
#   Program Description: APK Slicer
#   Author: userHonest
#   Date: 02/11/22
#------------------------------------------------------#

import os
import subprocess
import sys
import re

print("    ___    ____  __ __     _____ ___               ")
print("   /   |  / __ \/ //_/    / ___// (_)_______  _____")
print("  / /| | / /_/ / ,<       \__ \/ / / ___/ _ \/ ___/")
print(" / ___ |/ ____/ /| |     ___/ / / / /__/  __/ /    ")
print("/_/  |_/_/   /_/ |_|____/____/_/_/\___/\___/_/     ")
print("                  /_____/                          ")

print("APK_SLicer")
print("HTTP Protocol Analyzer")
print("Author: userHonest")
print("\n")








def fnExtractApk(strApkPath, strOutputDir):
    try:
        subprocess.run(['apktool', 'd', strApkPath, '-o', strOutputDir], check=True)
    except subprocess.CalledProcessError:
        print("Error while extracting APK. Make sure apktool is installed and the APK file path is correct.")
        exit(1)

def lstScanForProtocols(strOutputDir):
    dctProtocolMatches = {}
    protocol_count = {'http': 0, 'https': 0}  # Initialize protocol counters

    for strRoot, lstDirs, lstFiles in os.walk(strOutputDir):
        for strFile in lstFiles:
            if strFile.endswith('.smali'):
                strFilepath = os.path.join(strRoot, strFile)
                with open(strFilepath, 'r', errors='replace') as objFile:
                    lstLines = objFile.readlines()
                    for intIndex, strLine in enumerate(lstLines):
                        # Check for both HTTP and HTTPS
                        for protocol in ['http://', 'https://']:
                            if protocol in strLine:
                                protocol_count[protocol.rstrip('://')] += 1
                                intStart = max(intIndex - 2, 0)
                                intEnd = min(intIndex + 3, len(lstLines))
                                strContext = "".join(lstLines[intStart:intEnd])

                                if strFilepath not in dctProtocolMatches:
                                    dctProtocolMatches[strFilepath] = []
                                dctProtocolMatches[strFilepath].append((intIndex + 1, strContext))

    return dctProtocolMatches, protocol_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python scan_apk.py <path_to_apk>")
        exit(1)

    strApkPath = sys.argv[1]
    strOutputDir = "decoded_apk"

    print(f"Decoding {strApkPath}...")
    fnExtractApk(strApkPath, strOutputDir)

    print("Scanning for protocols...")
    dctProtocolMatches, protocol_count = lstScanForProtocols(strOutputDir)

    if dctProtocolMatches:
        print("\nFound Protocols:")
        for strFilepath, lstDetails in dctProtocolMatches.items():
            print(f"\nIn file: {strFilepath}")
            for intLineNo, strContext in lstDetails:
                print(f"At line {intLineNo}:\n{strContext}\n{'-'*40}")
    else:
        print("\nNo protocols found.")

    # Print protocol counts
    print("\nProtocol Counts:")
    for protocol, count in protocol_count.items():
        print(f"{protocol.upper()}: {count}")

    # Clean up
    subprocess.run(['rm', '-rf', strOutputDir], check=True)

if __name__ == '__main__':
    main()
# --------- End of file --------------------------------#
