#Iterables and iterators

#Iterables->Something that can be looped over e.g. a list

random_numbers=[1,2,3,4,5]

for number in random_numbers:
    print(number)
    
#for something to be iterable it needs to have the __iter__()

print(dir(random_numbers))


#Iterator->An object with a state that remembers where it is during iterations, they get their next element using the __next__(), when we run out of iteration it throws the StopIteration method, iterators can only go forward

#Why does this really matter

class Range:
    def __init__(self, start_range, end_range):
        self.start_range=start_range
        self.end_range=end_range
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start_range>=self.end_range:
            raise StopIteration
        current_value=self.start_range
        self.start_range+=1
        return current_value
    
    
nums=Range(0,11)

for num in nums:
    print(nums)
    
#Calling next manually

print(next(nums))



