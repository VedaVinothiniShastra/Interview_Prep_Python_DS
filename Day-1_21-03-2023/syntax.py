a=['a','b','c','d','e']
t=('i','j','k')
d = {
  'name':'John Doe',
  'job title':'software engineer',
  'country':'USA'
}
print("Accessing the data with index known",a[2]) 
for i in a: 
    print(i)

r=10
for i in range(r):  # range(value)
    print(i)
for i in range(5,15): # range(start , stop)
    print(i)
for i in range(5,15,2): #range(start , stop , step) print only 2 value from start to stop
    print(i)

for i in "Unikaksha":
    print(i)

for i in t:
    print(i)

for key , value in d.items():
    print(key)
    print(value)
 

for i in 'Unikecdccccccccccccccccccccccccccc':
    if(i=='i'):
        print('Found i')
        break 


for i in 'Unikecdccccccccccccccccccccccccccc':
    if(i=='i'):
        print('Found i')
        continue
    print(i)

for i in 'Unikecdccccccccccccccccccccccccccc':
    if(i=='i'):
        print('Found i')
        pass
    print(i)

w=1
while (w<5):  #5<5 -> false
    print(w) #1, 2, 3, 4
    w=w+1 #w=2,w=3,w=4,w=5