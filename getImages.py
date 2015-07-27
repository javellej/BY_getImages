#!/usr/bin/python

# import libraries
import os
import sys
import urllib
# import my_tools
from my_tools import reportError, printUsage, readFromFile, fileNameWithoutPath, addLog, urlExists, rename, removeFromHistory

def removeFile( filePath):
    # Step 1 : remove file
    try:
        os.remove( filePath)
    except Exception:
        reportError( "file \"%s\" not found" % filePath)
    # Step 2 : update image origins file
    removeFromHistory( fileNameWithoutPath( filePath))

# download a single file at a specific URL
def getFile( srcUrl, dstPath):
    try:
        if not urlExists( srcUrl):
            i = 1
            while ( os.path.isfile( dstPath) ):
                dstPath = rename( dstPath, i)
                i += 1
            urllib.urlretrieve( srcUrl, dstPath)
            addLog( "Logs/logOK", "\"%s\" downloaded" % srcUrl)
            addLog( "Logs/imageOrigins", "%s %s" % ( fileNameWithoutPath( dstPath), srcUrl))
    except Exception:
        reportError( "problem while downloading \"%s\"" % srcUrl)

def downloadImages( fileName):
    #   get images
    urlImages = ""
    try:
        urlImages = readFromFile( fileName)
    except:
        reportError( "file \"%s\" was not found" % fileName)
    print "BEGIN downloading files"
    for url in urlImages:
        url = url[:-1]
        getFile( url, "Output/" + str( fileNameWithoutPath( url)))
    print "END downloading files"

# main program
#   create output directory and log files
if not os.path.exists( "Output"):
    os.makedirs( "Output")
if not os.path.exists( "Logs"):
    os.makedirs( "Logs")
open( "Logs/logOK", 'a').close()
open( "Logs/logKO", 'a').close()
open( "Logs/imageOrigins", 'a').close()
#   get arguments
args = sys.argv
if ( len( args) == 3 ):
    if ( (args[1] == "-input") or (args[1] == "-i") ):
        downloadImages( args[2])
    elif ( (args[1] == "-remove") or (args[1] == "-rm") ):
        removeFile( args[2])
    else:
        reportError( "invalid argument")
        printUsage()
        quit()
if ( (len( args)==2) and ((args[1]=="-help") or (args[1]=="-h")) ):
    printUsage()
    quit()
else:
    reportError( "invalid command")
    printUsage()
    quit()

