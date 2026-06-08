# File objects

# Wrong way of reading a file
# file=open(r'test.txt','r')
# print(file.name)
# print(file.mode)
# file.close()


# Write way of reading from a file is using the context manager

# with open(r'test.txt','r') as file:
#     file_content=file.readlines()
#     print(file_content)

    
#.readline()->This graps the first line in the file

# with open(r'test.txt','r') as file:
#     character_limit=100
#     file_content=file.read(character_limit)
    
#     while len(file_content) > 0:
#         print(file_content, end='')
#         file_content=file.read(character_limit)
#.readlines()->Reads every line
#.read()->Reads the entire file, typically used for small files

#Reading the entire file using iteration

# with open(r'test.txt','r') as file:
#     for line in file:
#         print(line)
        
# This is efficient, we won't have to worry about memory

#.tell()->This is indicates the current position we in, like we have already read ten characters
# .seek()->This methods returns you to a specific position when reading in the file


#Writing to a file

with open(r'test2.txt', 'w') as file:
    file.write("This file  didn't exist, we are writing to this file for the first time")
    
# Reading and writing on multiple files
#Open the original file

with open(r'test.txt','r') as file_read, open(r'test3.txt','w') as file_write:
    for line in file_read:
        file_write.write(line)
        
        
#Appending to a file

with open(r'test3.txt','a') as file:
    file.write("We append this line as the last thing on the test3.txt file ")
    
with open(r'test4.txt', 'w') as file:
    file.write("Hello world , testing if i remember how to write on a file")
