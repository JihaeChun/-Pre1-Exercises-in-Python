
# coding: utf-8

# In[2]:

def test(got, expected): 
     prefix = 'OK' if got == expected else ' X' 
     print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# In[26]:

#a.match_ends
def match_ends(words):
    list1=[]
    for i in words:
        if len(i)>=2:
            first=i[0]
            last=i[-1]
            if first==last:
                list1.append(i)
    n=len(list1)
    return n


# In[27]:

#example
test(match_ends(['aba','xyz','aa','x','bbb']), 3)
test(match_ends(['','x','xy','xyx','xx']), 2)
test(match_ends(['aaa','be','abc','hello']), 1)


# In[28]:

#b.front_x
def front_x(words):
    first_x=[]
    else_list=[]
    for i in words:
        if i[0:1]=='x':
            first_x.append(i)
        else:
            else_list.append(i)
    first_x1=sorted(first_x)
    else_list1=sorted(else_list)
    final_list=first_x1+else_list1
    return final_list


# In[29]:

#example
test(front_x(['bbb','ccc','axx','xzz','xaa']),['xaa','xzz','axx','bbb','ccc'])
test(front_x(['ccc','bbb','aaa','xcc','xaa']),['xaa','xcc','aaa','bbb','ccc'])
test(front_x(['mix','xyz','apple','xanadu','aardvark']),['xanadu','xyz','aardvark','apple','mix'])


# In[31]:

#c.sort_last
def sort_last(tuples):
    sorted_list=sorted(tuples, key=lambda x: x[-1])
    return sorted_list


# In[32]:

#example
test(sort_last([(1,7),(1,3),(3,4,5),(2,2)]),[(2,2),(1,3),(3,4,5),(1,7)])


# In[33]:

#d.remove_adjacent
def remove_adjacent(nums):
    if len(nums)>0 :
        remove_list=list(set(nums))
    else :
        remove_list=[]
    return remove_list


# In[34]:

#example
test(remove_adjacent([1,2,2,3]),[1,2,3])
test(remove_adjacent([2,2,3,3,3]),[2,3])
test(remove_adjacent([]), [])


# In[36]:

#e.linear_merge
def linear_merge(list1,list2):
    linear=sorted(list1+list2)
    return linear


# In[37]:

#example
test(linear_merge(['aa','xx','zz'], ['bb','cc']),['aa','bb','cc','xx','zz'])
test(linear_merge(['aa','xx'], ['bb','cc','zz']),['aa','bb','cc','xx','zz'])
test(linear_merge(['aa','aa'], ['aa','bb','bb']),['aa','aa','aa','bb','bb'])

