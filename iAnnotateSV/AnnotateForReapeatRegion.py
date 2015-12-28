'''
Created on 12/23/2015
@Ronak Shah

'''

from collections import defaultdict

# Gives elements at particular index in list
getVar = lambda searchList, ind: [searchList[i] for i in ind]

def ReadRepeatFile(file, verbose):
    if(verbose):
        print ("Reading & Storing Repeat TSV file as dictionary")
    # Initialize dictionary of lists 
    dataDict = defaultdict(list)
    with open(file, 'r') as filecontent:
        header = filecontent.readline()
        for line in filecontent:
            data = line.rstrip('\n').split('\t')
            processedData = (data[0].replace('chr', ''))
            slicedData = data[1:]
            joinedData = '\t'.join(slicedData)
            dataDict[processedData].append(joinedData)    
    return dataDict        

def AnnotateRepeatRegion (verbose, count, sv, rrDict):
    if(verbose):
        print ("Checking Entry in Repeat data")
    # Initialize List to store repeat annotation
    list_svloc1 = []
    list_svloc2 = []
    # Read SV Data
    sv_chr1 = str(sv.loc['Chr1'])
    sv_pos1 = int(sv.loc['Pos1'])
    sv_chr2 = str(sv.loc['Chr2'])
    sv_pos2 = int(sv.loc['Pos2'])
    # Traverse through Repeat Data Dict
    list_loc1 = rrDict.get(sv_chr1, "None")  # Get the values for the chromosome
    if(list_loc1 != "None"):  # Check if there are no keys with a particular chromosome
        for loc in list_loc1:  # For each location in all values check the overlap
            data = loc.split('\t') 
            rr_pos1 = int(data[0])
            rr_pos2 = int(data[1])
            if (rr_pos1 <= sv_pos1 <= rr_pos2):
                slicedData = data[2:]
                joinedData = '-'.join(slicedData)
                list_svloc1.append(joinedData)
    else:
        if(verbose):
            print "Chromosome ", sv_chr1, " is not there in the repeat dictionary"
    list_loc2 = rrDict.get(sv_chr2, "None")
    if(list_loc2 != "None"):
        for loc in list_loc2:
            data = loc.split('\t') 
            rr_pos1 = int(data[0])
            rr_pos2 = int(data[1])
            if (rr_pos1 <= sv_pos2 <= rr_pos2):
                slicedData = data[2:]
                joinedData = '-'.join(slicedData)
                list_svloc2.append(joinedData)
    else:
        if(verbose):
            print "Chromosome ", sv_chr2, " is not there in the repeat dictionary" 
    return (list_svloc1, list_svloc2)  