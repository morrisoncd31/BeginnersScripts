global_var = 5
changed_global_var = 20

def local_change():
    global_var = 10
    print("inside function global_var's value is: ", global_var)
    global changed_global_var
    changed_global_var += 5
    print("inside function changed_global_var's value: ", changed_global_var)

local_change()

print("outside function global_var's value: ")
print("outside function global_var's value: ", changed_global_var)
