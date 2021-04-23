import shutil
a=0
readDir = "newcorpus1.txt"  #old
writeDir = "newcorpus.txt" #new
# txtDir = "/home/Administrator/Desktop/１"
lines_seen = set()
outfile = open(writeDir, "w",encoding="utf-8")
f = open(readDir, "r",encoding="utf-8")
for line in f:
  if line not in lines_seen:
    a+=1
    outfile.write(line)
    lines_seen.add(line)
    print(a)
    print('\n')
outfile.close()
print("success")
