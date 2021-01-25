import random #for creating order ID of the product

item_list = [] #List to store the items for the restaurant

#quickSort code for sorting the newly added customers
#Time complexity worst O(n^2); Space complexity: O(logn)
#def quicksort(arr, p, r):
#    if p < r:
#        q = partition(arr, p, r)
#        quicksort(arr, p, q-1)
#        quicksort(arr, q+1, r)

#supporting partion code for quicksort 
#def partition(arr, p, r):
#    x = arr[r].phone
#    i = p-1
#    for j in range(p, r):
#        if arr[j].phone <= x:
#            i+=1
#            arr[i], arr[j] = arr[j], arr[i]
#    arr[i+1], arr[r] = arr[r], arr[i+1]
#    return i+1

#Using MergeSort to sort the customer's list
# Time complexity: O(nlogn); Space Complexity: O(n)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
 
        mergeSort(Left)
        mergeSort(Right)
 
        i = j = k = 0
        while i < len(Left) and j < len(Right):
            if Left[i].phone < Right[j].phone:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
 
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
 
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

#binary search code for the findCustomer() method; O(logn) complexity
#Seaching based on phone number 
def binarySearch(arr,phone,lower,upper):
    if lower<=upper:
      mid = ((lower + upper)//2)
      if int(phone) == int(arr[mid].phone):
        return mid
      elif phone > arr[mid].phone:
        return binarySearch(arr,phone,mid+1,upper)
      elif phone < arr[mid].phone:
        return binarySearch(arr,phone,lower,mid-1)
      else:
        return -1
      return -1

# Restaurant class for the following functions:
#   addItem() Adds up an Item to the menu
#   addCustomer() Adds up a new Customer
#   findCustomer() Finds a new customer based on phone number
#   findPremiumCustomer() Finds premium customers
class Restaurant():

  def __init__(self):
    self.existing_customer = []

  max_seats=50
  unavailable_seats=0
  
  def addItem(self,item):
    global item_list
    item_list.append(item)

  #customers who've spent more than a specified amount qualify as
  #premium customers  
  def findPremiumCustomer(self):
    print("Premium Customer(s):")
    for i in self.existing_customer:
      if(sum((i.order_history.values())) > 750):
        print("Name: "+i.name+"\t\tContact No: "+str(i.phone))
      else:
        pass  

  #Finds and Prints an existing customer using the phone number provided
  def findCustomer(self):
    phone = int(input("Enter the contact number of customer: "))
    result = binarySearch(self.existing_customer,phone,0,len(self.existing_customer))
    if(result==(-1)):
      print("No Record Found!\n")
    else:
      print("Record Found!\n")
      print("Name: "+self.existing_customer[result].name+"\nContact Number: "+str(self.existing_customer[result].phone))
    
  #Adds a new customer
  def addCustomer(self,customer):
    self.existing_customer.append(customer) 
#    quicksort(self.existing_customer,0,len(self.existing_customer)-1)
    mergeSort(self.existing_customer)
      

# Customer class for the following functions:
#   book_seat()
#   place_order()
#   generate_bill()
#   search_Item()
class Customer(Restaurant):
  def __init__(self,name,phone):
    self.name = name
    self.phone = phone
    self.order_history = {}
    self.order_no = 0
  # Checks availability of seats, books seat if available and proceeds
  # to order
  def book_seat(self):
    no_of_guests = int(input("Enter Number Of People:"))
    if((Restaurant.unavailable_seats+no_of_guests)<Restaurant.max_seats):
        Restaurant.unavailable_seats=Restaurant.unavailable_seats+no_of_guests
        print("Seats are available!")
        self.place_order(no_of_guests)
    else:
      print("Sorry, seats are not available!")
  #Function to place order for customer
  def place_order(self,guest):
    ordereditems=[]
    choice=1
    print("------------Today's Menu--------------")
    for i in item_list:
        print(str(i.item_id)+"\t"+str(i.name)+"\t"+str(i.price))
    print("--------------------------------------\n")
    self.order_no = random.randint(10,1000)    
    while(choice==1):
      order = int(input("Enter your choice: "))
      ordereditems.append(item_list[order-1])
      item_list[order-1].frequency_of_item+=1
      choice=int(input("Do you want to add more items?(Yes(1)/No(0)):"))
    self.generate_bill(ordereditems,guest,self.order_no)

  #Generates the bill for the order placed by the customer
  def generate_bill(self,ordereditems,guest,order_no):
    total_amount=0
    for i in ordereditems:
      total_amount+=i.price
    print("\n-----------------BILL-----------------\n")
    for i in ordereditems:
      print(i.name+" "+str(i.price)+"Rs"+"\n")  
    print("Total Bill Amount: Rs"+str(total_amount))
    print("\n--------------------------------------\n")
    self.order_history[order_no]=total_amount
    Restaurant.unavailable_seats=Restaurant.unavailable_seats-guest

  #Searches for the specified item
  def search_Item(self):
    name=input("Input Name of Item to be searched: ")
    for i in item_list:
      if(name==i.name):
        k=i
      else:
        pass
    print("Name:"+k.name+"\nFrequency:"+str(k.frequency_of_item)+"\nIngredients Present:"+k.ingredients)
        
    
# The Item class to store attributes of any item     
class Item(Restaurant):
    def __init__(self,item_id, name, price, frequency_of_item, ingredient):
        self.name = name
        self.price = price
        self.frequency_of_item = 0
        self.ingredients = ingredient
        self.item_id=item_id
        

#Default objects to demonstrate the working of the following functions
my_restaurant = Restaurant()
demo_customer_1 = Customer("A", 90)
demo_customer_2 = Customer("B", 78)
demo_customer_3 = Customer("C", 56)
#Adding customer 
my_restaurant.addCustomer(demo_customer_1)
my_restaurant.addCustomer(demo_customer_2)
my_restaurant.addCustomer(demo_customer_3)


item1 = Item(1,"Toast",200,0,"Bread, lettuce, Cheese")
item2 = Item(2,"Pizza",400,0,"Bread, Cheese, Olives, Onion, Chilli")
item3 = Item(3,"Combo",500,0,"Bread, Cheese, Olives, Onion, Chilli, Soda Water")
item4 = Item(4,"Sweet",200,0,"Milk, Chocolate")
#Adding items to the restaurants 
my_restaurant.addItem(item1)
my_restaurant.addItem(item2)
my_restaurant.addItem(item3)
my_restaurant.addItem(item4)

#Run code/queries below this:
demo_customer_1.book_seat()
demo_customer_2.book_seat()
my_restaurant.findPremiumCustomer()



