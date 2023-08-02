""""
Nour owns a computer that she uses to learn programming. This computer has a maximum storage capacity of X GB. You want
Noor stores a number of files of 𝑁, each of
them 𝑌 gigabytes in size. Will the storage capacity of the Noor device be enough to store files or not?
no?
Input Description:
The input is a single line containing three integers, in order: computer space X, number of files N, and file size
The one Y.
"""
storage_size = int(input("Enter size of storage: "))
file_num = int(input("Enter number of files: "))
file_size = int(input("Enter size of files: "))
total_size = file_num * file_size
if total_size <= storage_size:
    print("Yes file can be stored")
else:
    print("No file can not be stored")