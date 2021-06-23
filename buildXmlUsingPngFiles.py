import os

#print(os.getcwd()) # current dir
    
begintxt=open("begin.txt", "r") #open existing file
endtxt=open("end.txt", "r") #open existing file

xmlfile= open("loadingscreens.xml","w+") #create xml file

#check that the file is in open mode. If yes, we proceed ahead
if begintxt.mode == 'r' and endtxt.mode == 'r': 
    xmlfile.write( begintxt.read()  ) #appent start
    
    directory = r'' + os.getcwd() + '/nyashicons'
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            xmlfile.write('\n' + '\t\t\t' + '<Image id="seq_bg" class="SeqBg" src="file://{images}/loadingscreens/' + os.path.join(filename) + '" />' ) #print(os.path.join(directory, filename))
    xmlfile.write('\n')
    
    xmlfile.write( endtxt.read()  ) #appent end
    xmlfile.close()     