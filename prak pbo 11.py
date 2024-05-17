
def add_title(title):
    def decorator(func):
        def wrapper(first_name, last_name, nim):
            full_name = func(first_name, last_name)
            return f"{title} {full_name}, NIM: {nim}"
        return wrapper
    return decorator


@add_title("Mr.")
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


@add_title("Ms.")
def full_name_ms(first_name, last_name):
    return f"{first_name} {last_name}"


first_name = "Rafael gala "
last_name = "Herlambang"
nim = "064002300036"

print("full name:",full_name(first_name, last_name, nim))  

first_name_female = "Naomi ivo saskia"
last_name_female = "Ambri"
nim_female = "064002300065"

print("full name:",full_name_ms(first_name_female, last_name_female, nim_female)) 
