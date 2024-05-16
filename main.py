with open("input.txt", encoding = "utf-8", mode = "x") as file:
    file.writelines(["1.Hello world ", "\n2.I'm the second line", "\nI'm the 3rd line"])



with open("input.txt","r") as f:
    line = f.readline()
    formatted_line = line.upper()
    

 
with open("output.txt", "w") as g:
    g.write(formatted_line)
