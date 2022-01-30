def hist_h(name, sirname, year, city, email, phone_number):
    return f'{name} {sirname} {year} {city} {email} {phone_number}'

n = input("Your name is:")
s = input("Your sirname is:")
y = input("You born in ... year:")
c = input("You live in:")
e = input("Your email is:")
p = input("Your phone number is:")

res = hist_h(name=n,sirname=s,year=y,city=c,email=e,phone_number=p)
print(res)
