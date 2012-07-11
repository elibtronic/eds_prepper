#
#  Makes ISSN<TAB>TITLE from
#  from 
#  #ISSN	eISSN	ISBN	eISBN	LCCN	LOCAL	OBJECT_ID	TITLE	TARGET_INTERNAL_NAME	TARGET_PUBLIC_NAME	TARGET_SERVICE	AVAILABILITY	PARSER	PARSE_PARAM	THRESHOLD_ACTIVE	THRESHOLD_GLOBAL	CATEGORIES	PUBLISHER	NOTE	AUTHENTICATION	LANGUAGE	TITLE_MAIN	INSTITUTE
#
print("Working...")
f_in = open("export_portfolios.txt","r");
f_out = open("ready.txt","w");

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
f_out.close();
print("Done\n")
