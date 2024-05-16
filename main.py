# with open("example.txt", encoding="utf-8", mode = "x") as data:
    # data.write("The weather is so cold today \n so that I wanna wear thick clothes)")
   
with open("example.txt", encoding="utf-8", mode = "r") as file:
    content = file.read()
    
with open("second.txt", encoding = "utf-8", mode = "w") as second:
    second.write(content)
    
with open("second.txt", encoding="utf-8", mode = 'r') as second:
    print(second.read())


