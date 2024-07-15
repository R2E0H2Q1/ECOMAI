#input product prices from the user, float
#until the total price exceed 1000
#print the avg price of the products
#print how many products you have purchased
#print how much beyond 1000 you reached
#i.e. 1900 then print
#you went 900 beyond 1000

#start
price: float = 0;
total: int = 0;
count: int = 0;
while total <= 1000:
    price = float(input("Please enter the item price: "));
    total = total + price;
    count = count + 1;
    exceed: float = total - 1000;
avg: float = total / count
print(f"The average is {avg}")
print(f"You have purchased {count} items");
print(f"You exceed your budget by {exceed}");
#end
