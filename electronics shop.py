#Before Running This Electronic Shop Application, First Read Instructions Given In The Report
#There Is A Password For Admin or User Both Without That The Application Won't Run



class Electronics:
    print('WELCOME TO LSD ELECTRONICS')
    def __init__(self):        
        self.items=['TeleVision','Refrigerator','Air Conditioner','Washing Machine','Grinder','Vaccuum Cleaner','MicroWave','Sewing Machine','Tea Maker','Stove']
        self.quant=[3,3,3,3,3,3,3,3,3,3]
        self.price=[70000,50000,80000,40000,5000,10000,15000,7000,6000,12000]
    def __str__(self):
        F=Filing()
        strg='PRODUCTS                 QUANTITY       PRICE'
        for i in range(len(self.items)):
            strg+=f'\n{self.items[i]:25}{str(self.quant[i]):15}Rs.{self.price[i]}/-'
        F.save_to_file(strg,'products.txt','w')
        return strg

class Shopping(Electronics):
    cart=[]
    TotalBill=0
    def __init__(self):
        super().__init__()
    def add_to_cart(self):
        buyTV=input('\nWould you like to buy Television from our shop? YES/NO: ')
        if buyTV.upper()=='YES':
            TVsp=Specifications(1)
            self.TVquantity=int(input('\nHow many TelseVision you wanna buy?: '))
            if self.TVquantity<=self.quant[0]:
                self.quant[0]-=self.TVquantity
                TVprice=self.price[0]*self.TVquantity
                self.cart.append([self.items[0],self.TVquantity,TVprice])
                Shopping.TotalBill+=TVprice
            else:
                print(f'SORRY \nWe have only {self.quant[0]} TV left')

        buyREF=input('\nWould you like to buy Refrigerator from our shop? YES/NO: ')
        if buyREF.upper()=='YES':
            REFsp=Specifications(2)
            self.REFquantity=int(input('\nHow many Refrigerator you wanna buy?: '))
            if self.REFquantity <= self.quant[1]:
                self.quant[1]-=self.REFquantity
                REFprice=self.price[1]*self.REFquantity
                self.cart.append([self.items[1],self.REFquantity,REFprice])
                Shopping.TotalBill+=REFprice
            else:
                print(f'SORRY \nWe have only {self.quant[1]} refrigerator left')

        buyAC=input('\nWould you like to buy Air Conditioner from our shop? YES/NO: ')
        if buyAC.upper()=='YES':
            ACsp=Specifications(3)
            self.ACquantity=int(input('\nHow many Air Conditioner you wanna buy?: '))
            if self.ACquantity <= self.quant[2]:
                self.quant[2]-=self.ACquantity
                ACprice=self.price[2]*self.ACquantity
                self.cart.append([self.items[2],self.ACquantity,ACprice])
                Shopping.TotalBill+=ACprice
            else:
                print(f'SORRY \nWe have only {self.quant[2]} AC left')

        buyWM=input('\nWould you like to buy Washing Machine from our shop? YES/NO: ')
        if buyWM.upper()=='YES':
            WMsp=Specifications(4)
            self.WMquantity=int(input('\nHow many Washing Machine you wanna buy?: '))
            if self.WMquantity <= self.quant[3]:
                self.quant[3]-=self.WMquantity
                WMprice=self.price[3]*self.WMquantity
                self.cart.append([self.items[3],self.WMquantity,WMprice])
                Shopping.TotalBill+=WMprice
            else:
                print(f'SORRY \nWe have only {self.quant[3]} washing machine left')

        buyGR=input('\nWould you like to buy Grinder from our shop? YES/NO: ')
        if buyGR.upper()=='YES':
            GRsp=Specifications(5)
            self.GRquantity=int(input('\nHow many Grinder you wanna buy?: '))
            if self.GRquantity <= self.quant[4]:
                self.quant[4]-=self.GRquantity
                GRprice=self.price[4]*self.GRquantity
                self.cart.append([self.items[4],self.GRquantity,GRprice])
                Shopping.TotalBill+=GRprice
            else:
                print(f'SORRY \nWe have only {self.quant[4]} grinder left')

        buyVC=input('\nWould you like to buy Vaccuum Cleaner from our shop? YES/NO: ')
        if buyVC.upper()=='YES':
            VCsp=Specifications(6)
            self.VCquantity=int(input('\nHow many Vaccuum Cleaner you wanna buy?: '))
            if self.VCquantity <= self.quant[5]:
                self.quant[5]-=self.VCquantity
                VCprice=self.price[5]*self.VCquantity
                self.cart.append([self.items[5],self.VCquantity,VCprice])
                Shopping.TotalBill+=VCprice
            else:
                print(f'SORRY \nWe have only {self.quant[5]} Vaccuum Cleaner left')

        buyMW=input('\nWould you like to buy Micro Wave from our shop? YES/NO: ')
        if buyMW.upper()=='YES':
            MWsp=Specifications(7)
            self.MWquantity=int(input('\nHow many Micro wave you wanna buy?: '))
            if self.MWquantity <= self.quant[6]:
                self.quant[6]-=self.MWquantity
                MWprice=self.price[6]*self.MWquantity
                self.cart.append([self.items[6],self.MWquantity,MWprice])
                Shopping.TotalBill+=MWprice
            else:
                print(f'SORRY \nWe have only {self.quant[6]} Micro wave left')

        buySM=input('\nWould you like to buy Sewing Machine from our shop? YES/NO: ')
        if buySM.upper()=='YES':
            SMsp=Specifications(8)
            self.SMquantity=int(input('\nHow many Sewing Machine you wanna buy?: '))
            if self.SMquantity <= self.quant[7]:
                self.quant[7]-=self.SMquantity
                SMprice=self.price[7]*self.SMquantity
                self.cart.append([self.items[7],self.SMquantity,SMprice])
                Shopping.TotalBill+=SMprice
            else:
                print(f'SORRY \nWe have only {self.quant[7]} Sewing Machine left')

        buyTM=input('\nWould you like to buy Tea Maker from our shop? YES/NO: ')
        if buyTM.upper()=='YES':
            TMsp=Specifications(9)
            self.TMquantity=int(input('\nHow many Tea Maker you wanna buy?: '))
            if self.TMquantity <= self.quant[8]:
                self.quant[8]-=self.TMquantity
                TMprice=self.price[8]*self.TMquantity
                self.cart.append([self.items[8],self.TMquantity,TMprice])
                Shopping.TotalBill+=TMprice
            else:
                print(f'SORRY \nWe have only {self.quant[8]} Tea Maker left')

        buyST=input('\nWould you like to buy Stove from our shop? YES/NO: ')
        if buyST.upper()=='YES':
            STsp=Specifications(10)
            self.STquantity=int(input('\nHow many Stove you wanna buy?: '))
            if self.STquantity <= self.quant[9]:
                self.quant[9]-=self.STquantity
                STprice=self.price[9]*self.STquantity
                self.cart.append([self.items[9],self.STquantity,STprice])
                Shopping.TotalBill+=STprice
            else:
                print(f'SORRY \nWe have only {self.quant[9]} Stove left')

    def remove_from_cart(self,product):
        if self.cart!=[]:
            for i in self.cart:
                if product in i:
                    self.cart.remove(i)
                    Shopping.TotalBill-=i[2]
        else:
            print('There\'s nothing in your cart!')
    def viewCart(self):
        if self.cart==[]:
            print('Your cart is empty')
        else:
            print("\nYOUR CART:")
            for i in self.cart:
                print(i)
    def changeQuantity(self,product):
        if self.cart!=[]:
            quant=int(input('Enter new quantity: '))
            for i in range(len(self.cart)):
                if product in self.cart[i]:
                    self.cart[i][1]=quant
                    Shopping.TotalBill-=self.cart[i][2]
                    self.cart[i][2]=quant*self.price[self.items.index(product)]
                    Shopping.TotalBill+=self.cart[i][2]
        else:
            print('There\'s nothing in your cart!')
    def CheckOut(self):
        if self.cart!=[]:
            F=Filing()
            Shopping.cart.append(self.cart)
            F.save_to_file(Shopping.cart,'shopping history.txt','w')
        else:
            print('There\'s nothing in your cart!')
    def cancelOrder(self):
        if self.cart!=[]:
            print('Your order has been cancelled')
            print('We wish to see you again on our shop')
            self.cart=[]
            F=Filing()
            Shopping.cart.append(self.cart)
            F.save_to_file(Shopping.cart,'shopping history.txt','w')
        else:
            print('There\'s nothing in your cart!')
            
class billing(Shopping):                                        #object will be created when user checks out
    def __init__(self):
        C=customer()
        self.name=C.name
        self.number=C.num
        self.date=input('Enter the date: ')
        self.day=input('Enter the day: ')
        self.address=input('Enter your address: ')
        self.bill=Shopping.TotalBill
        self.review=input('Enter the review for our products: ')
        self.fName=self.name+'.txt'
    def printBillingInfo(self):
        F=Filing()
        F.save_to_file(self.cart,self.fName,'a')
        print(f'Name                Date      Day       Number       Address                  Bill')
        print(f'{self.name:20}{self.date:10}{self.day:10}{self.number:13}{self.address:25}{str(self.bill)}')
        print('YOUR REVIEW:  ',self.review)


class Specifications:
    def __init__(self,sp):
        print('\nBefore buying, review the specifications of the products.')
        if sp==1:
            print('\nWe sell TVs of,\nModel: \'EE-20018\' \nColor: Black')
        elif sp==2:
            print('\nWe sell Refrigerators of,\nModel: \'RF-34TH\' \nColor: Grey')
        elif sp==3:
            print('\nWe sell ACs of,\nModel: \'AC-OP123\' \nColor: White')
        elif sp==4:
            print('\nWe sell Washing Machines of,\nModel: \'WM-123wm\' \nColor: White')
        elif sp==5:
            print('\nWe sell Grinders of,\nModel: \'GG-123er\' \nColor: Black')
        elif sp==6:
            print('\nWe sell Vaccuum Cleaner of,\nModel: \'VC-20021\' \nColor: Navy Blue')
        elif sp==7:
            print('\nWe sell Micro wave of,\nModel: \'MW-56v\'\nColor: Black')
        elif sp==8:
            print('We sell Sewing Machine of,\nModel: \'SM009\' \nColor: Grey')
        elif sp==9:
            print('\nWe sell Tea Maker of,\nModel: \'TM20233\' \nColor: White')
        elif sp==10:
            print('\nWe sell Stove of,\nModel: \'ST-912\' \nColor: Black')
            
    
class Filing:
    def save_to_file(self,details,file,file_mode):
        f = open(file,file_mode)
        f.write(str(details))
        f.close()
    def read_file(self,file):
        f = open(file)
        print(f.read())
        f.close()

from abc import ABC, abstractmethod
class User(ABC):
    F=Filing()
    def __init__(self):
        self.name=input('Enter your name: ')
        self.email=input('Enter your email: ')        
    @abstractmethod
    def ViewShoppingHistory(self):
        pass

class customer(User):    
    def __init__(self):
        super().__init__()
        self.pwd=input('Enter password: ')
        self.num=input('Enter your phone number: ')
        super().F.save_to_file([self.name,self.email,self.pwd,self.num],'users.txt','a')
    def ViewShoppingHistory(self):
        fName=self.name+'.txt'
        super().F.read_file(fName)

class Admin(User):
    e=Electronics()
    def __init__(self):
        super().__init__()        
    def changeQuantity(self,item,q):
        self.e.quant[self.e.items.index(item)]=q
        print('Modified Product Details:')
        print(self.e)
    def changePrice(self,item,pr):
        self.e.price[self.e.items.index(item)]=pr
        print('Modified Product Details:')
        print(self.e)
    def ViewAccounts(self):        
        super().F.read_file('users.txt')
    def ViewShoppingHistory(self):
        super().F.read_file('shopping history.txt')

class UserError(Exception):
    def __init__(self):
        super().__init__('No Such User Found')

#DRIVER CODE
def Menu(user):
    print("\n=====================")
    print("\nEnter valid choices from Menu or else you will LOG OUT!!!!! \n")
    if user == 'A':
        print("1.Display Products and details")
        print("2.View Users")
        print("3.Shopping History")
        print("4.Change Price")
        print("5.Change Quantity")
    elif user == 'C':        
        print("1.Display Products")
        print("2.Start Shopping") 
        print("3.View My Cart")
        print("4.Remove From Cart")
        print("5.Change Quantity ")
        print("6.Place order")
        print("7.Cancel order")
        print("8.View My Shopping History")

E=Electronics()
S=Shopping()

#EXCEPTION HANDLING
try:    
    loginAs = input('Press A to login as Admin, C for Customer: ')
    if loginAs.upper() == 'A':
        A=Admin()
        passwordA = 'itsadmin'
        password = input('Enter password for Admin: ')
        if  password == passwordA:
            while True:
                Menu('A')
                choice = int(input('\nEnter choice from menu: '))
                if choice == 1:                    
                    print(E)
                elif choice == 2:
                    A.ViewAccounts()
                elif choice == 3:
                    A.ViewShoppingHistory()
                elif choice == 4:
                    prod=input('Enter name of the product to change its price: ')
                    cost=int(input('Enter new price: '))
                    A.changePrice(prod,cost)
                elif choice == 5:
                    prod=input('Enter name of the product to change its quantity: ')
                    quant=int(input('Enter new quantity: '))
                    A.changeQuantity(prod,quant)
                elif not (1<=choice<=5):
                    raise ValueError
        else:
            print('invalid password')
            

    elif loginAs.upper() == 'C':
        Cus=customer()
        while True:
            Menu('C')
            choice = int(input('\nEnter choice from menu: '))
            if choice == 1:
                    print(E)
            elif choice == 2:
                    S.add_to_cart()
            elif choice == 3:
                    S.viewCart()
            elif choice == 4:
                    prod=input('Which product do you want to remove?: ')
                    S.remove_from_cart(prod)
            elif choice == 5:
                    prod=input('Which product\'s quantity do you want to change?: ')
                    S.changeQuantity(prod)
            elif choice == 6:
                    S.CheckOut()
                    b=billing()
                    b.printBillingInfo()
            elif choice == 7:
                    S.cancelOrder()
            elif choice == 8:
                    Cus.ViewShoppingHistory()
            elif not (1<=choice<=8):
                    raise ValueError

    elif loginAs.upper() != 'A' and loginAs.upper() != 'C':
        raise UserError

except ValueError:
    print('You pressed a key other than the given menu, logging out....') 

except UserError as U:
    print(U)

except FileNotFoundError:
    if loginAs.upper()=='C':
        print('You haven\'t bought anything from here before!!')
    if loginAs.upper()=='A':
        if choice == 2:
            print("No customer has logged in yet")
        elif choice == 3:
            print('No one has placed an order yet')

##except:
##    print('There was an error')
