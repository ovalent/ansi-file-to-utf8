#code for python 3
import sys

###funtions(s)##############################################

def encode_utf8(file_path):

    #check source language in title's filename and set the correct encoding
    if ("CHS" in file_path.upper()) or ("CN" in file_path.upper()):
        source_encoding = "gb2312"
    if ("GB" in file_path.upper()):
        source_encoding = "gb18030"
    if ("CHT" in file_path.upper()):
        source_encoding = "cp950"
    if ("FR" in file_path.upper()) or ("FRENCH" in file_path.upper()) or ("FRE" in file_path.upper()) or ("FRA" in file_path.upper()):
        source_encoding = "latin_1"

    #set the utf8 file name
    file_path_utf8 = file_path.replace(".srt", "_UTF8.srt")
    
    #open and encode the original content
    file_source = open(file_path, mode='r', encoding=source_encoding, errors='ignore')
    file_content = file_source.read()
    file_source.close

    #write the UTF8 file with the encoded content
    file_target = open(file_path_utf8, mode='w', encoding='utf-8')
    file_target.write(file_content)
    file_target.close

    return file_path_utf8

###Main##############################################

#check there is argument(s)
if len(sys.argv) == 0:
    sys.exit("argument needed: please input path")

#process the files
i = 1
while i < len(sys.argv):
    file_path = sys.argv[i]
    
    #call function
    file_encoded = encode_utf8(file_path)
    print(file_encoded)
    
    i = i + 1



print("UTF8 encoding done for "+ str(i-1) + " file(s).")
#quit()
