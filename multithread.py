import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of: ', self.infile)

background = AsyncZip('mydata.txt', 'mydata_archive.zip')
background2 = AsyncZip('input.txt', 'input_archive.zip')
background.start()
background2.start()
print("Main continues on foreground")

print("main program doing things in foreground")
print(sum([1, 2, 3]))

background.join()
background2.join()

print('Main waited until background was done')