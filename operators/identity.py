#Identity
# Both object should be same even if both varaibles have same value ie similar to === operator

a=['apple','banana'];
b=['apple','banana'];
c=a; print(a);
print(a is c);
print(a is b);
print(a is not b);
print(a==b);

a={'apple','banana'};
b={'apple','banana'};

c=a; print(a);
print(a is c);
print(a is b);
print(a is not b);
print(a==b);
