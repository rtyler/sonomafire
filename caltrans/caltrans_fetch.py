

import sys, re, os, pdb, csv
import pandas as pd
from datetime import datetime

fields = [ 'closureID', 'typeOfClosure', 'typeOfWork', 'beginLocationName',
          'travelFlowDirection', 'beginFreeFormDescription',
          'endFreeFormDescription', 'beginRoute', 'endRoute', ]

#'beginLatitude', 'endLatitude', 'beginLongitude', 'endLongitude'

# later not all fields will get written in the header
header=[ 'latitude','longitude','title', 'date']+fields

def process_file(file):
    """ process a caltran file and return something, not sure what yet"""

    print "processing ", file
    lst = pd.read_csv(file)
    for key in lst.keys():

        print key,"\t:", lst[key][1]
    print
    now = datetime.now()
    for i in range(len(lst)):
        dt = datetime.strptime("%s %s" % (lst.closureStartDate[i], lst.closureStartTime[i]), "%Y-%m-%d %H:%M:%S")

        row=[]

        if lst.typeOfClosure[i] == 'Full' and dt < now:
            for fld in fields:
                # print lst[fld][i],
                val = str(lst[fld][i])
                if val=='nan':
                    val = ''
                row.append(val)

            try:
                lat1 = "%8.5f" % float(lst.beginLatitude[i])
                lat2 = "%8.5f" % float(lst.endLatitude[i])
                lng1 = "%8.5f" % float(lst.beginLongitude[i])
                lng2 = "%8.5f" % float(lst.endLongitude[i])
            except:
                lat1 =''
                lng1 =''
                lat2 = ''
                lng2 = ''

            title = "%s to %s" % (lst.beginLocationName[i], lst.endLocationName[i])
            date = "%s %s" % (lst.closureStartDate[i], lst.closureStartTime[i])

            writer.writerow( [lat1, lng1, title, date]+row)
            if lat1 != lat2 or lng1 != lng2:
                writer.writerow( [lat2, lng2, title, date]+row)


ofile  = open('road_closure.csv', "wb")

writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(header)


urls = ['http://www1.dot.ca.gov/cwwp2/data/d1/lcs/lcsStatusD01.csv', 'http://www1.dot.ca.gov/cwwp2/data/d3/lcs/lcsStatusD03.csv', 'http://www1.dot.ca.gov/cwwp2/data/d4/lcs/lcsStatusD04.csv']
for filename in urls:
    # print "processing: ",filename
    process_file(filename)

# for filename in os.listdir(os.getcwd()):
# if re.search('^lcs.+csv$', filename):
#     # print "processing: ",filename
#     process_file(filename)
# else:
#     print "not a csv: ", filename

ofile.close()
