import csv
import random

records=100000
print("Making %d records\n" % records)

fieldnames=['Name','email','password','message']
writer = csv.DictWriter(open("test.csv", "w"), fieldnames=fieldnames)

Name=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
email=['deep2000@gmail.com', 'sangworld@gmail.com', 'Mayuri@gmail.com', 'regina@gmail.com']
pass_w=['whlle','apple','orange','amrina','amen','ladem']
message=['hurray','have a nice','Good day','Happy','made my day']

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('Name', random.choice(Name)),
    ('email',random.choice(email)),
    ('password',random.choice(pass_w)),
    ('message', random.choice(message))]))
