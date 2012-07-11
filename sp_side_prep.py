#
#  Makes the rest of ISSN<TAB>TITLE from
#  from 
#  holdings_brock.txt
#
print("Working...")
f_in = open("holdings_brock.txt","r");
f_out = open("ready.txt","w+");

for line in f_in:
    data = line.split("\t")

    
    issn = data[3].replace("-","")    
    title = data[1]
    if(len(issn) != 8):
        continue
    f_out.write(issn + "\t" + title + "\n")

f_in.close();
f_out.close();
print("Done\n")
