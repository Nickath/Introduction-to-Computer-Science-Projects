number = int(raw_input("Please enter an integer number of your choice : "));
itis = None
for i in range(1,number):
    if (number % i ) ==0 :
        if(i*i == number):
           print("Yes, number {} is number {} in the exponent of 2 ".format(number,i))
           itis = True;
if(itis is None):
    print('Your number is not the exponent of 2 of any number')
