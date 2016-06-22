In order to get the desired output for the questions 1 to 4, the code needs to be run in the following manner:

1. The input file for all the three files is the raw unzipped passwords file with the entire set of passwords provided with the homework. Due to its large size it has not been added directly to the folder. The zip file provided has instead been added and that should be unzipped to get the actual passwords file with all the data before running any code files.

2. The unzipped file(size close to 3 GB) should be placed in the same folder as the one that contains the python code files.

3. For getting the output of question 1, simply run the file ‘cse664spring16hw3question1.py’ and the generated output file is a .txt file with two columns, the first column containing the frequency of the password which itself is present in the second column.
The file is sorted based on the frequency in decreasing order and among the entries with the same frequency the passwords are in the reverse alphabetical order.

4. For the outputs of questions 2 and 3, run the file, ‘cse664spring16hw3question2question3.py’. It outputs two .txt files both in similar format. The files have 2 columns First one contains the entropy value and the second contains the password corresponding to it. The files are sorted in reverse order of the entropy values. For question 2 the base considered is the original set of passwords(including duplicates) and for the question 3 the base for calculation is the unique set of passwords.

5. For the output of question 4, run the file ‘cse664spring16hw3question4.py’. It outputs a .txt file which has 2 columns, the first is the hash value and the second is the password corresponding  to the hash value. 