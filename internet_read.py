from urllib.request import urlopen

# web_address = 'https://www.pinkbike.com/news/5-things-we-learned-at-ews-val-di-fassa-2019.html'
web_address = input("Enter web address: ")

try:
    with urlopen(web_address) as response:
        with open('output_file.html', 'w') as write_file:
            for line in response:
                line = line.decode('utf-8')
                write_file.write(line) 
                print(line)
except FileNotFoundError:
    print("address not found")



#        if 'published_time' in line:
#            print(line)

# instead of with could be response = urlopen('...')
# response.close()
# but with is generally better practice