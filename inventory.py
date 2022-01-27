# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mysql.connector as sqlconn
import matplotlib.pyplot as pl
import pandas as pd
import numpy as np

cn = sqlconn.connect(database="Inventory", host="localhost", user="root", password="1234")
if cn.is_connected() == False:
    print("CONNECTION FAILED")
else:
    cursor = cn.cursor(buffered=True)
    ch = 0
    while ch != 7:
        print("*" * 205)
        print(
            "                                                                          Welcome to IMS                                                             ")
        print("*" * 205)
        print(
            "                                                                               Menu                                                                  ")
        print("*" * 205)
        print("1. Add Details")
        print("2. Update Details")
        print("3. Delete a Record")
        print("4. Search for a Record")
        print("5. Visualize Data")
        print("6. Display all the Data")
        print("7. Quit")
        ch = int(input("Enter your choice(1-7):"))
        # Adding Deatils
        if ch == 1:
            print("What You Want to Add?")
            print("*" * 205)
            print("1. Product details")
            print("2. Supplier details")
            print("3. Customer details")
            print("4. Order Details")
            print("5. Purchase Details")
            print("6. Exit")
            print("*" * 180)
            a = int(input("Enter your choice(1-6):"))
            print(" ")
            # Product Details
            if a == 1:
                Product_Id = int(input("Enter the product id:"))
                Unit_Price = int(input("Enter the item price:"))
                Item_Qty = int(input("Enter the item quantity:"))
                Item_Name = input("Enter the name of the item:")
                Product_Received = input("Is product delivered(Yes/No)?")
                Product_Shipped = input("Is Product Shipped(Yes/No)?")
                Minimum_Required = int(input("Enter the quantity required:"))
                MfgDate = input("Enter the manufacturing date of product(YYYY-MM-DD):")
                ExpDate = input("Enter the expiry date of product(YYYY-MM-DD):")
                GST_tax = float(input("Enter the GST on product:"))
                sql1 = "insert into product values(" + str(Product_Id) + "," + str(Unit_Price) + "," + str(
                    Item_Qty) + ",'" + Item_Name + "','" + Product_Received + "','" + Product_Shipped + "'," + str(
                    Minimum_Required) + ",'" + MfgDate + "','" + ExpDate + "'," + str(GST_tax) + ")"
                cursor.execute(sql1)
                cn.commit()
                print("Record Added!")
                cursor.close()
                cn.close()
            # Supplier Details
            elif a == 2:
                Supplier_Name = input("Enter the Supplier Name :")
                Supplier_Id = int(input("Enter the Supplier Id :"))
                Contact_Details = int(input("Enter the Contact Details of Supplier:"))
                S_Address = input("Enter the supplier's address:")
                GSTNo = input("Enter the GSTNo:")
                sql2 = "insert into supplier values('{}',{},{},'{}','{}')".format(Supplier_Name, Supplier_Id,
                                                                                  Contact_Details, S_Address, GSTNo)
                cursor.execute(sql2)
                cn.commit()
                print("Record Added!")
                cursor.close()
                cn.close()
            # Customer Deatils
            elif a == 3:
                Cust_Id = int(input("Enter the customer id:"))
                CustName = input("Enter the customer name:")
                C_Address = input("Enter the customer's address:")
                Phone = int(input("Enter the phone number of customer:"))
                Email = input("Enter the Email id of customer:")
                C_GSTNo = input("Enter the GST number(for customer):")
                sql3 = "insert into customers values({},'{}','{}',{},'{}','{}')".format(Cust_Id, CustName, C_Address,
                                                                                        Phone, Email, C_GSTNo)
                cursor.execute(sql3)
                cn.commit()
                print("Record Added!")
                cursor.close()
                cn.close()
            # Order Details
            elif a == 4:
                O_Id = int(input("Enter the order id:"))
                Product_Id = int(input("Enter the product id:"))
                Cust_Id = int(input("Enter the customer id:"))
                Qty_Ordered = int(input("Enter the quantity ordered:"))
                Order_Date = input("Enter the date of placing the order(YYYY-MM-DD):")
                Status = input("Enter the order status:")
                sql4 = "insert into orders values({},{},{},{},'{}','{}')".format(O_Id, Product_Id, Cust_Id, Qty_Ordered,
                                                                                 Status)
                cursor.execute(sql4)
                cn.commit()
                print("Record Added!")
                cursor.close()
                cn.close()
            # Purchase Deatils
            elif a == 5:
                P_Id = int(input("Enter the purchase id:"))
                Product_Id = int(input("Enter the product id:"))
                Supplier_Id = int(input("Enter the Supplier Id :"))
                Number_received = int(input("Enter the quantity received:"))
                Purchase_Date = input("Enter the date of purchase(YYYY-MM-DD):")
                P_Status = input("Enter the purchase status ")
                sql5 = "insert into purchase values({},{},{},{},'{}','{}')".format(P_Id, Product_Id, Supplier_Id,
                                                                                   Number_received, Purchase_Date,
                                                                                   P_Status)
                cursor.execute(sql5)
                cn.commit()
                print("Record Added!")
                cursor.close()
                cn.close()
            elif a == 6:
                continue

        # Updating Details
        elif ch == 2:
            print("What You Want to Update?")
            print("*" * 205)
            print("1. Product details")
            print("2. Supplier details")
            print("3. Customer details")
            print("4. Order Details")
            print("5. Purchase Details")
            print("6. Exit")
            print("*" * 205)
            b = int(input("Enter your choice(1-6):"))
            # Product Details
            if b == 1:
                print("*" * 205)
                pr_update = 0
                while pr_update != 10:
                    print(" What do u want to update?")
                    print("*" * 205)
                    print(
                        "1.Unit_Price \n2.Item_Qty\n3.Item_Name\n4.Product_received\n5.Product_Shipped\n6.Minimum_Required\n7.MfgDate\n8.ExpDate\n9.GST_tax\n10.Exit")
                    print("*" * 205)
                    pr_update = int(input("Enter your choice(1-10): "))
                    if pr_update == 1:
                        Product_Id = int(input("Enter the product id:"))
                        Unit_Price = int(input("Enter the Item Price(per unit):"))
                        sql6 = "Update product set Unit_Price ={} Where Product_Id= {}".format(Unit_Price, Product_Id);
                    elif pr_update == 2:
                        Product_Id = int(input("Enter the product id:"))
                        Item_Qty = int(input("Enter the Item Quantity:"))
                        sql6 = "Update product set Item_Qty= {} Where Product_Id={}".format(Item_Qty, Product_Id);
                    elif pr_update == 3:
                        Product_Id = int(input("Enter the product id:"))
                        Item_Name = input("Enter the name of item:")
                        sql6 = "Update product set Item_Name = '{}' Where Product_Id={}".format(Item_Name, Product_Id);
                    elif pr_update == 4:
                        Product_Id = int(input("Enter the product id:"))
                        Product_received = input("Is product delivered(Yes/No)?")
                        sql6 = "Update product set Product_received = '{}' Where Product_Id={}".format(Product_received,
                                                                                                       Product_Id);
                    elif pr_update == 5:
                        Product_Id = int(input("Enter the product id:"))
                        Product_Shipped = input("Is product shipped(Yes/No)?")
                        sql6 = "Update  product set  Product_Shipped = '{}' Where Product_Id={}".format(Product_Shipped,
                                                                                                        Product_Id);
                    elif pr_update == 6:
                        Product_Id = int(input("Enter the product id:"))
                        Minimum_Required = int(input("Enter the Minimum quantity required:"))
                        sql6 = "Update  product set  Minimum_Required = {} Where Product_Id={}".format(Minimum_Required,
                                                                                                       Product_Id);
                    elif pr_update == 7:
                        Product_Id = int(input("Enter the product id:"))
                        MfgDate = input("Enter the manufacturing date(YYYY-MM-DD):")
                        sql6 = "Update  product set  MfgDate = '{}' Where Product_Id={}".format(MfgDate, Product_Id);
                    elif pr_update == 8:
                        Product_Id = int(input("Enter the product id:"))
                        ExpDate = input("Enter the expiry date(YYYY-MM-DD):")
                        sql6 = "Update  product set  ExpDate = '{}' Where Product_Id={}".format(ExpDate, Product_Id);
                    elif pr_update == 9:
                        Product_Id = int(input("Enter the product id:"))
                        GST_tax = float(input("Enter the GST tax:"))
                        sql6 = "Update  product set  GST_tax = {} Where Product_Id={}".format(GST_tax, Product_Id);
                    elif pr_update == 10:
                        break
                    cursor.execute(sql6)
                    cn.commit()
                    print("Updation Completed!")
                    cursor.close()
                    cn.close()
            # Supplier Details
            elif b == 2:
                sp_update = 0
                while sp_update != 5:
                    print("*" * 205)
                    print(" What do u want to update?")
                    print("*" * 205)
                    print("1.Supplier_Name\n2.S_Address\n3.Contact_Details\n4.GSTNo\n5.Exit")
                    print("*" * 205)
                    sp_update = int(input("Enter your choice(1-5): "))
                    if sp_update == 1:
                        Supplier_Id = int(input("Enter the Supplier Id :"))
                        Supplier_Name = input("Enter the Supplier Name:")
                        sql7 = "Update Supplier set Supplier_Name = '{}' Where Supplier_Id={}".format(Supplier_Name,
                                                                                                      Supplier_Id);
                    elif sp_update == 2:
                        Supplier_Id = int(input("Enter the Supplier Id :"))
                        S_Address = input("Enter the Supplier's Address:")
                        sql7 = "Update Supplier set S_Address = '{}' Where Supplier_Id={}".format(S_Address,
                                                                                                  Supplier_Id);
                    elif sp_update == 3:
                        Supplier_Id = int(input("Enter the Supplier Id :"))
                        Contact_Details = int(input("Enter the Contact Details:"))
                        sql7 = "Update Supplier set Contact_Details = {} Where Supplier_Id={}".format(Contact_Details,
                                                                                                      Supplier_Id);
                    elif sp_update == 4:
                        Supplier_Id = int(input("Enter the Supplier Id :"))
                        S_GSTNo = input("Enter the GSTNo(for supplier):")
                        sql7 = "Update Supplier set GSTNo = '{}'Where Supplier_Id={}".format(S_GSTNo, Supplier_Id);
                    elif sp_update == 5:
                        break
                    cursor.execute(sql7)
                    cn.commit()
                    print("Updation Completed!")
                    cursor.close()
                    cn.close()
            # Customer Details
            elif b == 3:
                c_update = 0
                while c_update != 6:
                    print("*" * 205)
                    print(" What do u want to update?")
                    print("*" * 205)
                    print("1.CustName\n2.C_Address\n3.Phone\n4.GSTNo\n5.Email\n6.Exit")
                    print("*" * 205)
                    c_update = int(input("Enter your choice(1-6): "))
                    if c_update == 1:
                        CustId = int(input("Enter the customer id:"))
                        CustName = input("Enter the customer Name:")
                        sql8 = "Update Customer set CustName = '{}' Where CustId={}".format(CustName, Cust_Id);
                    elif c_update == 2:
                        CustId = int(input("Enter the customer id:"))
                        C_Address = input("Enter the Customer's Address:")
                        sql8 = "Update Customer set C_Address = '{}' Where Cust_Id={}".format(C_Address, Cust_Id);
                    elif c_update == 3:
                        CustId = int(input("Enter the customer id:"))
                        Phone = int(input("Enter the phone number of customer:"))
                        sql8 = "Update Customer set  Phone = {} Where Cust_Id={}".format(Phone, Cust_Id);
                    elif c_update == 4:
                        CustId = int(input("Enter the customer id:"))
                        GSTNo = input("Enter the GSTNo:")
                        sql8 = "Update Customer set GSTNo = '{}' Where CustId={}".format(GSTNo, Cust_Id);
                    elif c_update == 5:
                        CustId = int(input("Enter the customer id:"))
                        Email = input("Enter the Email id of customer:")
                        sql8 = "Update Customer set Email = '{}' Where CustId={}".format(Email, Cust_Id);
                    elif c_update == 6:
                        break
                    cursor.execute(sql8)
                    cn.commit()
                    print("Updation Completed!")
                    cursor.close()
                    cn.close()
            # Order Details
            elif b == 4:
                o_update = 0
                while o_update != 4:
                    print("*" * 205)
                    print(" What do u want to update?")
                    print("*" * 205)
                    print("1.QtyOrdered\n2.OrderDate\n3.O_Status\n4.Exit")
                    o_update = int(input("Enter your choice(1-4): "))
                    if o_update == 1:
                        O_Id = int(input("Enter the order id:"))
                        QtyOrdered = int(input("Enter the quantity ordered:"))
                        sql9 = "Update Orders set Qty_Ordered = {} Where O_Id={}".format(QtyOrdered, O_Id);
                    elif o_update == 2:
                        O_Id = int(input("Enter the order id:"))
                        OrderDate = input("Enter the Order Date(YYYY-MM-DD):")
                        sql9 = "Update Orders set Order_Date = '{}' Where O_Id={}".format(OrderDate, O_Id);
                    elif o_update == 3:
                        O_Id = int(input("Enter the order id:"))
                        O_Status = input("Enter the order status:")
                        sql9 = "Update Orders set Status = '{}' Where O_Id={}".format(O_Status, O_Id);
                    elif o_update == 4:
                        break
                    cursor.execute(sql9)
                    cn.commit()
                    print("Updation Completed!")
                    cursor.close()
                    cn.close()
            # Purchase Details
            elif b == 5:
                pu_update = 0
                while pu_update != 4:
                    print("*" * 205)
                    print(" What You want to update?")
                    print("*" * 205)
                    print("1. Number_received\n2.Purchase_date\n3.Status\n4.Exit")
                    pu_update = int(input("Enter your choice(1-4): "))
                    if pu_update == 1:
                        P_Id = int(input("Enter the purchase id:"))
                        Number_recieved = int(input("Enter the Number recieved:"))
                        sql10 = "Update Purchase set Number_recieved = {} Where Id={}".format(Number_recieved, Id);
                    elif pu_update == 2:
                        P_Id = int(input("Enter the purchase id:"))
                        Purchase_date = input("Enter the date of purchase(YYYY-MM-DD):")
                        sql10 = "Update Purchase set Purchase_date= '{}' Where Id={}".format(Purchase_date, Id);
                    elif pu_update == 3:
                        P_Id = int(input("Enter the purchase id:"))
                        P_Status = input("Enter the  current Status :")
                        sql10 = "Update Purchase set P_Status = '{}' Where Id={}".format(P_Status, Id);
                    elif pu_update == 4:
                        break
                    cursor.execute(sql10)
                    cn.commit()
                    print("Updation Completed!")
                    cursor.close()
                    cn.close()
            elif b == 6:
                continue
        # Deleting Record
        elif ch == 3:
            print("What You Want to Remove?")
            print("*" * 205)
            print("1. Product details")
            print("2. Supplier details")
            print("3. Customer details")
            print("4. Order Details")
            print("5. Purchase Details")
            print("6. Exit")
            print("*" * 205)
            c = int(input("Enter your choice(1-6):"))
            if c == 1:
                st = pd.read_sql("select* from product", cn)
                Product_Id = int(input("Enter the product id to be removed:"))
                if Product_Id in st.values:
                    sql11 = "Delete from product where Product_Id={}".format(Product_Id);
                    cursor.execute(sql11)
                    cn.commit()
                    print("Record Removed Successfully!")
                    cursor.close()
                    cn.close()
                else:
                    print("This Product Id does not exist.")
            elif c == 2:
                supp = pd.read_sql("Select* from supplier", cn)
                Supplier_Id = int(input("Enter the supplier id to be removed:"))
                if Supplier_Id in supp.values:
                    sql12 = "Delete from Supplier where Supplier_Id={}".format(Supplier_Id);
                    cursor.execute(sql12)
                    cn.commit()
                    print("Record Removed Successfully!")
                    cursor.close()
                    cn.close()
                else:
                    print("This Supplier Id does not exist.")
            elif c == 3:
                cust = pd.read_sql("Select* from customers", cn)
                CustId = int(input("Enter the customer id to be removed:"))
                if CustId in cust.values:
                    sql13 = "Delete from Customer where CustId={}".format(CustId);
                    cursor.execute(sql13)
                    cn.commit()
                    print("Record Removed Successfully!")
                    cursor.close()
                    cn.close()
                else:
                    print("This Customer Id does not exist.")
            elif c == 4:
                order = pd.read_sql("Select* from orders", cn)
                O_Id = int(input("Enter the order id to be removed:"))
                if O_Id in order.values:
                    sql14 = "Delete from Orders where O_Id={}".format(O_Id);
                    cursor.execute(sql14)
                    cn.commit()
                    print("Record Removed Successfully!")
                    cursor.close()
                    cn.close()
                else:
                    print("This Order Id does not exist.")
            elif c == 5:
                purch = pd.read_sql("Select* from purchase", cn)
                Id = int(input("Enter the purchase id to be removed:"))
                if Id in purch.values:
                    sql15 = "Delete from Purchase where Id={}".format(Id);
                    cursor.execute(sql15)
                    cn.commit()
                    print("Record Removed Successfully!")
                    cursor.close()
                    cn.close()
                else:
                    print("This Purchase Id does not exist.")
            elif c == 6:
                continue
        # Searching for a Record
        elif ch == 4:
            print("Want To Search For?")
            print("*" * 205)
            print("1. Product details")
            print("2. Supplier details")
            print("3. Customer details")
            print("4. Order Details")
            print("5. Purchase Details")
            print("6. Exit")
            print("*" * 205)
            d = int(input("Enter Your Choice(1-6):"))
            if d == 1:
                st = pd.read_sql("select* from product", cn)
                Product_Id = int(input("Enter the product id to search for a record:"))
                if Product_Id in st.values:
                    sql16 = "Select * from product where Product_Id={}".format(Product_Id);
                    df1 = pd.read_sql(sql16, cn)
                    cursor.execute(sql16)
                    cn.commit()
                    print(df1)
                    cursor.close()
                    cn.close()
                else:
                    print("This Product Id does not exist.")
            elif d == 2:
                supp = pd.read_sql("Select* from supplier", cn)
                Supplier_Id = int(input("Enter the supplier id to search for a record :"))
                if Supplier_Id in supp.values:
                    sql17 = "Select * from supplier where Supplier_Id={}".format(Supplier_Id);
                    df2 = pd.read_sql(sql17, cn)
                    cursor.execute(sql17)
                    cn.commit()
                    print(df2)
                    cursor.close()
                    cn.close()
                else:
                    print("This Supplier Id does not exist.")
            elif d == 3:
                cust = pd.read_sql("Select* from customers", cn)
                CustId = int(input("Enter the customer id to search for a record:"))
                if CustId in cust.values:
                    sql18 = "Select * from customers where CustId={}".format(CustId);
                    df3 = pd.read_sql(sql18, cn)
                    cursor.execute(sql18)
                    cn.commit()
                    print(df3)
                    cursor.close()
                    cn.close()
                else:
                    print("This Customer Id does not exist.")
            elif d == 4:
                order = pd.read_sql("Select* from orders", cn)
                O_Id = int(input("Enter the order id to search for a record:"))
                if O_Id in order.values:
                    sql19 = "Select * from orders where O_Id={}".format(O_Id);
                    df4 = pd.read_sql(sql19, cn)
                    cursor.execute(sql19)
                    cn.commit()
                    print(df4)
                    cursor.close()
                    cn.close()
                else:
                    print("This order Id does not exist.")
            elif d == 5:
                purch = pd.read_sql("Select* from purchase", cn)
                Id = int(input("Enter the purchase id to search for a record:"))
                if Id in purch.values:
                    sql20 = "Select * from purchase where P_Id={}".format(Id);
                    df5 = pd.read_sql(sql20, cn)
                    cursor.execute(sql20)
                    cn.commit()
                    print(df5)
                    cursor.close()
                    cn.close()
                else:
                    print("This purchase Id does not exist.")
            elif d == 6:
                continue
        # Visualizing Data
        elif ch == 5:
            print("*" * 205)
            print("Wants to see the?")
            print("1. Stock\n2. Orders Placed\n3. Purchases Made\n4. Price of each Item\n5. Exit")
            print("*" * 205)
            e = int(input("Enter your choice(1-5):"))
            print("Want to visualize data in the form of-\n1. Bar Graphs\n2. Line Chart\n3. Scatter Chart")
            if e == 1:
                f = int(input("Enter your choice(1-3):"))
                st = pd.read_sql("select* from product", cn)
                name = st.Item_Name
                qty = st.Item_Qty
                if f == 1:
                    x = np.arange(len(name))
                    pl.bar(name, qty)
                    for i in range(len(name)):
                        pl.annotate(qty[i], xy=(x[i], qty[i]))
                    pl.title("STOCK")
                    pl.ylabel("Item Quantity")
                    pl.xlabel("Item Name")
                    pl.show()
                elif f == 2:
                    pl.plot(name, qty, 'r', linestyle='dotted', marker='D', markersize=5, markeredgecolor='red')
                    pl.ylabel("Item Quantity")
                    pl.xlabel("Item Name")
                    pl.show()
                elif f == 3:
                    pl.scatter(name, qty, color='m')
                    pl.show()
            elif e == 2:
                f = int(input("Enter your choice(1-3):"))
                od = pd.read_sql("Select* from orders", cn)
                st = pd.read_sql("select* from product", cn)
                name = st.Item_Name
                qt_od = od.Qty_Ordered
                if f == 1:
                    x = np.arange(len(name))
                    pl.bar(name, qt_od)
                    for i in range(len(name)):
                        pl.annotate(qt_od[i], xy=(x[i], qt_od[i]))
                    pl.xlabel("Product Name")
                    pl.ylabel("Quantity Ordered")
                    pl.title("Orders Placed")
                    pl.show()
                elif f == 2:
                    pl.plot(name, qt_od, 'g', linestyle='dashed', marker='^', markeredgecolor='red')
                    pl.xlabel("Product Name")
                    pl.ylabel("Quantity Ordered")
                    pl.show()
                elif f == 3:
                    pl.scatter(name, qt_od, color='c')
                    pl.show()
            elif e == 3:
                f = int(input("Enter your choice(1-3):"))
                pu = pd.read_sql("Select* from purchase", cn)
                nu = pu.Number_received
                st = pd.read_sql("select* from product", cn)
                name = st.Item_Name
                if f == 1:
                    x = np.arange(len(name))
                    pl.bar(name, nu)
                    for i in range(len(name)):
                        pl.annotate(nu[i], xy=(x[i], nu[i]))
                    pl.xlabel("Product Name")
                    pl.ylabel("Number Received")
                    pl.title("Purchases")
                    pl.show()
                elif f == 2:
                    pl.plot(name, nu, 'red', marker='d', markeredgecolor='k')
                    pl.xlabel("Product Name")
                    pl.ylabel("Number Received")
                    pl.show()
                elif f == 3:
                    pl.scatter(name, nu, color='k')
                    pl.show()
            elif e == 4:
                f = int(input("Enter your choice(1-3):"))
                st = pd.read_sql("select* from product", cn)
                name = st.Item_Name
                price = st.Unit_Price
                if f == 1:
                    x = np.arange(len(name))
                    pl.bar(name, price)
                    for i in range(len(name)):
                        pl.annotate(price[i], xy=(x[i], price[i]))
                    pl.xlabel("Product Name")
                    pl.ylabel("Unit Price")
                    pl.title("Cost Of Each Product")
                    pl.show()
                elif f == 2:
                    pl.plot(name, price, 'm', marker='x', markeredgecolor='k')
                    pl.xlabel("Product Name")
                    pl.ylabel("Unit Price")
                    pl.show()
                elif f == 3:
                    pl.scatter(name, price, c='m', marker=',')
                    pl.show()
            elif e == 5:
                continue
        # Displaying the data
        elif ch == 6:
            print("Want To Display The Data For -?")
            print("*" * 205)
            print("1. Products \n2. Suppliers\n3. Customers\n4. Orders\n5. Purchases\n6. Exit")
            print("*" * 205)
            g = int(input("Enter your choice(1-6):"))
            if g == 1:
                prod = pd.read_sql("select*from product", cn)
                print(prod)
            elif g == 2:
                supp = pd.read_sql("Select* from supplier", cn)
                print(supp)
            elif g == 3:
                cust = pd.read_sql("Select* from customers", cn)
                print(cust)
            elif g == 4:
                orders = pd.read_sql("Select* from orders", cn)
                print(orders)
            elif g == 5:
                purc = pd.read_sql("Select* from purchase", cn)
                print(purc)
            elif g == 6:
                continue
        elif ch == 7:
            print("-" * 205)
            print("*\n" * 20)
            print(
                "*                                                                               THANK YOU                                                                                   ")
            print(
                "*                                                                             FOR USING OUR                                                                                 ")
            print(
                "*                                                                               PROGRAME                                                                                    ")
            print("*\n" * 20)
            print("-" * 205)






































