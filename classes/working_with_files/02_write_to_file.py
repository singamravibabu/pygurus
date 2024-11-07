# WRITE TO FILE
f = open("sample.txt", "w")
f.write("Good morning!")
f.close()

# WRITE TO A FILE THAT DOESN'T EXISTS CREATES ONE
f = open("Year_2024.txt", "w")
f.write("Year 2024 is below average for me.")
f.close()