
healthy = ['kale chips', 'broccoli']
backpack = ['pizza', 'frozen custard', 'apple crips', 'kale chips']
# Wanna remove food from the backpack only if is not healthy
#Remove Elements from a list
backpack.remove("pizza")
print(backpack)
#What if healthy has hundreds of items, i don´t wanna use my eyeballs to look through that, i wanna check if is unhealthy and if is not unhealthy, then remove it.
if "pizza" not in healthy:
    backpack.remove("pizza")
print(backpack)

    
