# Statistical Thinking and Data Analysis
# github.org - texts from diff books
# next.....think about comparing 3 texts
# which way will give best results
# look at distribution of letters, break word vectors into letter vectors
def textParse(fileName1, fileName2):
    import numpy as np
    import string
    import time

    start = time.time()
    # Read from Text File - need to make really large texts
    # 1st text file
    text1 = open(fileName1,'r')
    words1 = ((text1.read()).split()) # Create word array
    words1= [x.lower() for x in words1] # make case insensitive
    words1 = [x.translate(string.maketrans("",""),string.punctuation) for x in words1] #remove punctuation
    words1 = filter(None, words1) #filter empty strings from list array
    
    # 2nd text file
    text2 = open(fileName2,'r')
    words2 = ((text2.read()).split()) # Create word array
    words2= [x.lower() for x in words2] # make case insensitive
    words2 = [x.translate(string.maketrans("",""),string.punctuation) for x in words2] #remove punctuation
    words2 = filter(None, words2) #filter empty strings from list array
     # exclude any punctuation, make case-insensitive

    check1 = set(words1) # Set of unique words in 1st text file
    check2 = set(words2) # Set of unique words in 2nd text file
    master = check1.union(check2) # Union Set of all unique words - needs to be on the order of 10*exp(3)
    master = list(master)
    master = np.asarray(master) # Convert to numpy array
  
    # Array of frequencies of master word list in text 1
    #print(words2)
    freq1 = []
    freq2 = []
    for i in range(0,len(master)):
        freq1.append(words1.count(master[i]))
        freq2.append(words2.count(master[i]))
  
    # normalize
    freq1 = freq1/np.linalg.norm(freq1)
    freq2 = freq2/np.linalg.norm(freq2)
    # Find similarity
    similarity = float(np.dot(freq1,freq2)) # dot product
    print('Similarity between the two files is {similarity}.'.format(similarity = similarity))

    end = time.time()
    print('Script Execution Time: {time} seconds'.format(time = end-start))
# Call function
textParse("book1.txt","book2.txt")
