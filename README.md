# Python Programming - Basic to Advanced

Create a file script.py

```py
print("hello world")
```

In your prompt command/terminal:

```sh
> python script.py
```

##### Lists ( a type of collections)

Let´s create a list of health foods:

```py
healthy = ['pizza', "Frozen Custard"]
```

This list is an object, and whenever we´re working with objects, we can use a dot to access it´s elements.

Also, a list is python is naturally dynamic, it can grown or shrink.

```py
healthy.append("apple crips") #method

print(healthy)

```

A method is just a function that is attached to an object. A method is different from an standalone function because a standalone function is not attached to any specific object.

ex:

```py
length = len(healthy) #a function
print(length) #function print() that receives arguments.
```

ex:

```py
print("length:", length)
```

- `Check if item in List`

```py
healthy = ['pizza', 'frozen custard', 'apple crips']
print("chicken pot pie" in healthy)
#result: false
```

Adding a condition:

```py
if "pizza" in healthy:
    print("Eating the pizza!")
```

- `Working with lists`

```py
healthy = ['kale chips', 'broccoli']
backpack = ['pizza', 'frozen custard', 'apple crips', 'kale chips']
```

Now i want to remove food from the backpack only if is not healthy

```py
backpack.remove("pizza")
print(backpack)
```

But what if healthy has hundreds of items, i don´t wanna use my eyeballs to look through that, i wanna check if is unhealthy and if is not unhealthy, and then remove it.

```py
if "pizza" not in healthy:
    backpack.remove("pizza")
print(backpack)
```
