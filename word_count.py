
countries = ["India", "Srilanka", "Canada", "Ireland", "US", "Germany", "Iceland", "Italy", "Iran", "UK"]

#count the countries which are starting with "I"
#Also print all the countries with "I"


counter = 0
output = []
for country in countries:
    #if country[0] == "I":  #instead of this we can write as below
    if country.startswith("I"):
        counter += 1
        output.append(country)
print(counter)
print(output)