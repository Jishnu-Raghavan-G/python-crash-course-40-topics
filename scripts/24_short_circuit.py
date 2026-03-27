def check():
    print("Function called")
    return True

print(True or check())   # check() won't run
print(False and check()) # check() won't run
