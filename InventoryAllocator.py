#Assignment for FreeD Group 
__author__ = "Kyungtaek Oh"
__email__ = "Kyungtaek95@gmail.com"

global warehouse
global order
global allocatedInventory
global notEnough

#Class of Warehouse
class Warehouse:
    def __init__(self, warehouse_name, inventory_list):
        self.name = warehouse_name
        self.inv = inventory_list

    def getInventoryKeys(self):
        return list(self.inv.keys())

    def getInventoryValues(self):
        return list(self.inv.values())

    def getInventoryCount(self, inv_name):
        return self.inv[inv_name]

    def checkNameInWarehouse(self, inv_name):
        if inv_name in self.getInventoryKeys():
            return True
        else: return False

    def checkInventoryLeft(self):
        cnt = 0
        for i in self.getInventoryValues():
            cnt += i
        if cnt == 0: return True
        else: return False

#Class of Order     
class Order:
    def __init__(self, order_name, order_cnt):
        self.name = order_name
        self.cnt = order_cnt

#save allocated
def saveInventory(saved, wh_name, inv_name, count):
    if wh_name not in list(saved.keys()):
        saved[wh_name] = {inv_name:count}
    else:
        if inv_name not in list(saved[wh_name].keys()):
            saved[wh_name][inv_name] = count
        else:
            saved[wh_name][inv_name] += count

#printers        
def printInfo(orders,warehouses):
    print("--------------"*10)
    print("order: ", orders)
    print("warehouse: ", warehouses)
def printOut(notEnough, warehouse, saved):  
    if notEnough:
        print("Not Enough Inventory!")
    elif len(warehouse) == 0:
        print("Happy Case!")
    else:print("splited!")
    print("output: ", saved)
    
# main allocating function
def inventoryAllocator(orders, warehouses):
    #declare
    order = [Order(i,orders[i]) for i in orders]
    warehouse = [Warehouse(i['name'],i['inventory']) for i in warehouses]
    allocatedInventory = {}
    notEnough = False
    printInfo(orders,warehouses)

    # going through orders to check if there are enough spaces
    for i in order:
        #if there are no more space then break
        if notEnough == True or not warehouse: 
            notEnough = True
            break
        
        j = 0
        # checking cheapest warehouse first, allocate order untill it is done
        while warehouse:
            if i.cnt == 0: break #if no more to allocate, then next
            if j==len(warehouse): #if no more space in warehouse, then it's over
                notEnough = True
                break

            #if inventory name is in the warehouse, continue
            if warehouse[j].checkNameInWarehouse(i.name):
                #if warehouse has enough space
                if warehouse[j].getInventoryCount(i.name) >= i.cnt:
                    saveInventory(allocatedInventory, warehouse[j].name, i.name, i.cnt)
                    warehouse[j].inv[i.name]-=i.cnt
                    i.cnt = 0
                #warehouse has less space
                elif i.cnt >= warehouse[j].getInventoryCount(i.name) and warehouse[j].getInventoryCount(i.name) > 0:
                    saveInventory(allocatedInventory, warehouse[j].name, i.name, warehouse[j].getInventoryCount(i.name))
                    i.cnt -= warehouse[j].getInventoryCount(i.name)
                    warehouse[j].inv[i.name] = 0
            
            #check space left, if not pop out of the line
            if warehouse[j].checkInventoryLeft():
                warehouse.pop(0)
            else: j+=1
        #if cnt has left, then not enough space
        if i.cnt > 0: notEnough = True
    
    #print result
    printOut(notEnough, warehouse, allocatedInventory)


#test case#1 (Happy case)
orders1, warehouses1 = { 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }] 
orders2, warehouses2 = { 'apple': 5, 'banana': 5}, [{ 'name': 'owd', 'inventory': { 'apple': 3 } }, { 'name': 'dm', 'inventory': { 'apple': 2, 'banana':5 }}] 
orders3, warehouses3 = { 'apple': 10, 'banana': 10, 'orange':10 }, [{ 'name': 'owd', 'inventory': { 'apple': 6 } }, { 'name': 'dm', 'inventory': { 'apple': 4, 'banana':5 }}, { 'name': 'tr', 'inventory': { 'banana':5, 'orange': 10 }}] 

#test case#2 (Not enough inventory)
orders4, warehouses4 = { 'apple': 1}, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }] 
orders5, warehouses5 = { 'apple': 5, 'banana': 5}, [{ 'name': 'owd', 'inventory': { 'apple': 3 } }, { 'name': 'dm', 'inventory': { 'apple': 2, 'banana':1 }}] 
orders6, warehouses6 = { 'apple': 10, 'banana': 10, 'orange':10 }, [{ 'name': 'owd', 'inventory': { 'banana': 15 } }, { 'name': 'dm', 'inventory': { 'apple': 11, 'banana':1 }}, { 'name': 'tr', 'inventory': { 'orange': 9, 'banana':5 }}] 

#test case#3 (Should be splited)
orders7, warehouses7 = { 'apple': 10}, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}] 
orders8, warehouses8 = { 'apple': 10, 'banana': 10}, [{ 'name': 'owd', 'inventory': { 'apple': 3 , 'banana': 10 } }, { 'name': 'dm', 'inventory': { 'apple': 7, 'banana': 1 }}] 
orders9, warehouses9 = { 'apple': 10, 'banana': 10, 'orange':10 }, [{ 'name': 'owd', 'inventory': { 'apple': 9 } }, { 'name': 'dm', 'inventory': { 'apple': 4, 'banana': 5 }}, { 'name': 'tr', 'inventory': { 'orange': 15, 'banana': 12 }}] 


inventoryAllocator(orders1,warehouses1)
inventoryAllocator(orders2,warehouses2)
inventoryAllocator(orders3,warehouses3)
inventoryAllocator(orders4,warehouses4)
inventoryAllocator(orders5,warehouses5)
inventoryAllocator(orders6,warehouses6)
inventoryAllocator(orders7,warehouses7)    
inventoryAllocator(orders8,warehouses8)    
inventoryAllocator(orders9,warehouses9)