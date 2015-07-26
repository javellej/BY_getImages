import re

def reportError( errorMessage):
    print "ERROR : %s" % errorMessage
    addLog( "Logs/logKO", errorMessage)

def printUsage( ):
    print "Usage: \"python getImages.py <-input|-i> <urlFileName>\" to download images"
    print "       \"python getImages.py <-remove|-rm> <filePath>\" to remove a downloaded file"

# read file contents
# return list of the line contents of the the input file
def readFromFile( fileName):
    f = open( fileName)
    lines = f.readlines()
    f.close()
    return lines

# extract file name from URL
def fileNameWithoutPath( url):
    fileName = re.sub( r'(.*)/(.*)', r'\2', url)
    return fileName

# add line to log file
def addLog( logFile, message):
    f = open( logFile, 'a')
    f.write( str( message) + "\n")
    f.close()

# parse image origins log and get original URL associated with file
def urlExists( url):
    associations = readFromFile( "Logs/imageOrigins")
    for pair in associations:
        line = pair.split( " ")
        line[0] = line[0][:-1]
        line[1] = line[1][:-1]
        if ( line[1] == url ):
            return True
    return False

def rename( filePath, i):
    pos1 = filePath.rfind( "_")
    pos2 = filePath.rfind( ".")
    if ( i==1 ):
        pos1 = pos2
    return filePath[:pos1] + "_%s"%i + filePath[pos2:]

def removeFromHistory( fileName):
    associations = readFromFile( "Logs/imageOrigins")
    # open log file back in write mode
    f = open( "Logs/imageOrigins", 'w')
    for pair in associations:
        line = pair.split( " ")
        if ( line[0] != fileName ):
            f.write( pair)

