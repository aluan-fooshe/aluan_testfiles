myfile = open(str(input()))
mycontents = myfile.read()

#print(mycontents)

titles = []
years = []
my_dict = {}

my_list = mycontents.split('\n')
#print(my_list)

for element in my_list:
    dict_term = element.split(' |')
#    print(title)
#    print(dict_term)
    titles.append(dict_term[0])
    years.append(dict_term[1])
    years.sort()
#    print(dict_term[1], dict_term[0], "\n")
    my_dict = dict(zip(years, titles))

for element in sorted(my_dict):
    print(element, my_dict[element])