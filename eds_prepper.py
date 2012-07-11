#
#  Makes ISSN<TAB>TITLE from
#  from 
#  #ISSN	eISSN	ISBN	eISBN	LCCN	LOCAL	OBJECT_ID	TITLE	TARGET_INTERNAL_NAME	TARGET_PUBLIC_NAME	TARGET_SERVICE	AVAILABILITY	PARSER	PARSE_PARAM	THRESHOLD_ACTIVE	THRESHOLD_GLOBAL	CATEGORIES	PUBLISHER	NOTE	AUTHENTICATION	LANGUAGE	TITLE_MAIN	INSTITUTE
#  and
#  Makes the rest of ISSN<TAB>TITLE from
#  from 
#  holdings_brock.txt
#
print("Working...")
f_in = open("export_portfolios.txt","r")
f_out = open("ready.txt","w")

#SFX Gen'd info
#toss intro line
f_in.readline()

for line in f_in:
    data = line.split("\t")

    if (data[0] == "\t" or data[0] == "" or data[1] == "\t" or data[1] == " "):
        continue
    
    issn = data[0].replace("-","")
    if (len(issn) != 8):
        print "bad one: " + issn
    
    title = data[7]
    f_out.write(issn + "\t" + title + "\n")

f_in.close();

#SP Title info
f_in = open("holdings_brock.txt","r");


for line in f_in:
    data = line.split("\t")

    
    issn = data[3].replace("-","")    
    title = data[1]
    if(len(issn) != 8):
        continue
    f_out.write(issn + "\t" + title + "\n")


f_out.close();
print("Done\n")


