#!/usr/bin/env python
# coding: utf-8

# # The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per

# In[1]:


unit = int(input("Enter your unit"))
total_bills = 0
if unit <= 100:
    total_bills = unit * 4.5
elif unit <= 200:
    total_bills = 100 * 4.5 + (units-100) * 6
elif unit <= 300:
    total_bills = 100 * 4.5 + 100 * 6 + (unit - 200) * 10
else:
    total_bills = 100 * 4.5 + 100 * 6 + 200 * 10 + (unit - 300) * 20
print(f"The total electricity bill for {unit} units is: Rs. {total_bills}")


# # Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each

# In[2]:


number= []
for num in range(1,101):
    cube = num **3
    if cube %4==0 or cube %5==0:
        number.append(num)
print("Numbers whose cubes are divisible by 4 or 5 (using for loop):", number)
        
    


# # While Loop

# In[ ]:


number = []
num = 1
while num <= 100:
    cube = num **3
    if cube %4==0 or cube %5==0:
        number.append(num)
        num = num +1 
print("Numbers whose cubes are divisible by 4 or 5:", number)
        
    


# # Write a program to filter count vowels in the below-given string.
# 
# 

# In[ ]:


string = "I want to become a data scientist"
vowel_count = 0
for char in string:
    if char.lower() in 'aeiou':
        vowel_count += 1
print("Number of vowels:", vowel_count) 


# In[ ]:




