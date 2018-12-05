#!/usr/bin/env python
# coding: utf-8

# # This is my first python notebook
# (yes that is how it is spelled and capitalized)
# 

# # Heading 1
# ## Heading 2
# ### Heading 3
# #### Heading 4
# ##### Heading 5
# I didn't really need that comment!

# ## This is a bulleted list
# * Item 1
# * Item 2
#     * Item 2a
#     * Item 2b
#         * Item 2ba
#     * Item 2c
# * Item 3

# ### This is a numbered list
# 1. Item 1
# 2. Item 2
# 7. Item 3
# 15. Item 4
#     * Item 4a
#     * Item 4b
#     

# ### Let's look at bold and italics
# In this line of text *this item will be in italics* while this will not. By the same token _this will be_ but this won't. In this line of text **this item will be bold** while this will not. By the same token __this will be but__ this won't. This would be **bold and *italics* text**.

# # My Temperature Conversion Script
# In this exercise, I want to enter a temperature in degrees Fahrenheit and have the code calculate degrees in Celsius.

# In[4]:


f = float(input("Enter the temperatures in degrees Fahrenheit? "))
c = (f-32)*5/9
c
print()
print("The temperature " + str(f) + " degrees Fahrenheit is " + str(round((c),2)) + " degrees Celsius") 


# In[ ]:




