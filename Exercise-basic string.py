
# coding: utf-8

# In[1]:

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


# In[20]:

#A. donuts
def donuts(count):
    first='Number of donuts: '
    if count>=10:
        last="many"
    else:
        last=count
    return first+str(last)


# In[21]:

#example
test(donuts(4), 'Number of donuts: 4')
test(donuts(9), 'Number of donuts: 9')
test(donuts(10), 'Number of donuts: many')
test(donuts(99), 'Number of donuts: many')


# In[22]:

#b.both_ends
def both_ends(s):
    if len(s)<2:
        both_end=''
    else :
        first_2=s[0:2]
        last_2=s[-2:]
        both_end=first_2+last_2

    return both_end


# In[23]:

#example
test(both_ends('spring'),'spng')
test(both_ends('Hello'),'Helo')
test(both_ends('a'),'')
test(both_ends('xyz'),'xyyz')


# In[24]:

#c.mixup
def mix_up(a,b):
    blank=' '
    if len(a)>=2 and len(b)>=2:
        mix_up=b[:2]+a[2:]+blank+a[:2]+b[2:]
    else:
        mix_up=''
    return mix_up


# In[25]:

#example
test(mix_up('mix','pod'),'pox mid')
test(mix_up('dog','dinner'),'dig donner')
test(mix_up('gnash','sport'),'spash gnort')
test(mix_up('pezzy','firm'),'fizzy perm')


# In[26]:

#d.verbing
def verbing(s):
    ing='ing'
    ly='ly'
    if len(s)<3:
        verbing=s
    elif s[-3:]=='ing':
        verbing=s+ly
    else:
        verbing=s+ing
    return verbing


# In[27]:

#example
test(verbing('hail'), 'hailing')
test(verbing('swiming'), 'swimingly')
test(verbing('do'), 'do') 


# In[28]:

#e.not_bad
def not_bad(s):
    find_bad=s.find('bad')
    find_not=s.find('not')
    # if don't fine word, return value,-1
    if (find_bad==-1 or find_not==-1):
        return s
    # Only change good for "not ~ bad"
    elif find_not<find_bad:
        find_bad=find_bad+3
        return s.replace(s[find_not:find_bad],'good')
    else :
        return s


# In[29]:

#example
test(not_bad('This movie is not so bad'), 'This movie is good')
test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
test(not_bad('This tea is not hot'), 'This tea is not hot')
test(not_bad("It's bad yet not"), "It's bad yet not")


# In[32]:

#f.front_back
def front_back(a,b):
    front=[]
    back=[]
    for i in [a,b]:
        if len(i)%2==0:
            front.append(i[:len(i)/2])
            back.append(i[len(i)/2:])   
        else :
            front.append(i[:int(len(i)/2)+1])
            back.append(i[int(len(i)/2)+1:])
    
    front_back=front[0]+front[1]+back[0]+back[1]
    return front_back


# In[33]:

#example
test(front_back('abcd', 'xy'), 'abxcdy')
test(front_back('abcde', 'xyz'), 'abcxydez')
test(front_back('Kitten', 'Donut'), 'KitDontenut')

