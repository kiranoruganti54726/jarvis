'''
modes are w=write,r=read,a=append
opening and closing of file is must
content.read() for mode r
content.write for mode w
content.write() for mode a also append ki separate ga function undadhu
write method ye vadtham just mode a ki chabge chestam
'''


a=open("D:\python\-filehandling notepad file.txt",mode='a')
content=a.write("\nthis is append adds data to existing file")
print(content)
a.close()