import mysql.connector
import datetime

def db_connect():
    try:
        db = mysql.connector.connect(
            host='localhost', 
            password='admin', # change to your password
            user='root', # change to your user
            database = 'testdb', # change name to your database
        )
        return db
    except mysql.connector.Error as err:
        return err

def convert(x):
    converted = ''
    for i in x:
        converted += i
    return converted

def get_low_stock(cursor):
    query = "SELECT b.BrandName FROM productname p INNER JOIN Brand b ON b.BrandID = p.BrandID WHERE p.StockQuantity < 25;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nItems Low In Stock:")
    for x in cursor:
        print("◦ " + str(convert(x)).strip() + " 🔴")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_total_purchased(cursor):
    query = "SELECT b.BrandName, SUM(ip.PurchasedQuantity) AS TotalPurchasedQuantity FROM brand b INNER JOIN productname p ON p.BrandID = b.BrandID INNER JOIN itempurchased ip ON ip.ProductID = p.ProductID GROUP BY b.BrandName;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nBrand Name: Total Purchased")
    for x in cursor:
        print("◦ " + str(x[0]).strip() + ": " + str(x[1]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def check_acc_mutation(cursor, startDate, endDate):
    if startDate == None: startDate = datetime.date(2023, 11, 1)
    if endDate == None: endDate = datetime.date(2023, 12, 1)
    query = "SELECT salestransaction.TransactionDate FROM salestransaction WHERE salestransaction.TransactionDate >= %s AND salestransaction.TransactionDate < %s"
    cursor.execute(query, (startDate, endDate))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nAccount Mutation From " + str(startDate) + " To " + str(endDate))
    for x in cursor:
        print("◦ " + str(x[0]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def employee_sales(cursor):
    query = "SELECT e.EmployeeID, e.EmployeeName, SUM(st.TotalAmount) AS TotalRevenue FROM Employee e LEFT JOIN salestransaction st ON e.EmployeeID = st.EmployeeID GROUP BY e.EmployeeID, e.EmployeeName;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[Employee ID] Employee Name: Sales Generated")
    for x in cursor:
        print("◦ " + "[" + str(x[0]) + "] " + str(x[1]) + ": Rp" + "{:,}".format(float(x[2])))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_recent_transactions(cursor):
    query = "SELECT * FROM salestransaction WHERE salestransaction.TransactionDate >= DATE_SUB(CURDATE(), INTERVAL 1 WEEK)"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[Employee ID] Employee Name: Sales Generated")
    for x in cursor:
        print(x)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_shelf_location(cursor, product):
    query = "SELECT b.BrandName, i.ShelfLocation FROM productname p INNER JOIN inventory i ON p.ProductID = i.ProductID INNER JOIN brand b ON b.BrandID = p.BrandID WHERE b.BrandName = %s;"
    cursor.execute(query, (product,))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nBrand Name: Shelf Location")
    for x in cursor:
        print("◦ " + str(x[0]) + ": " + str(x[1]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_employees_info(cursor):
    query = "SELECT employee.EmployeeName, employee.ContactInformation FROM employee;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nEmployee Name: Phone Number")
    for x in cursor:
        print("◦ " + str(x[0]) + ": " + str(x[1]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_unsuccessful_transactions(cursor):
    query = "SELECT * FROM salestransaction WHERE salestransaction.PaymentStatus = 'Unsuccessful';"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[Transaction ID] Transaction Date | Employee ID | Total Amount | Payment Status")
    for x in cursor:
        print("◦ " + "[" + str(x[0]) + "]" + " | " + str(x[1]) + " | " + str(x[2]) + " | " + str(x[3]) + " | " + str(x[4]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_most_sales_brand(cursor):
    query = "SELECT b.BrandName, SUM(ip.PurchasedQuantity) AS TotalQuantitySold FROM brand b INNER JOIN productname p ON b.BrandID = p.BrandID INNER JOIN itempurchased ip ON p.ProductID = ip.ProductID GROUP BY b.BrandName ORDER BY TotalQuantitySold DESC LIMIT 1;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nBrand Name: Sales")
    for x in cursor:
        print("◦ " + str(x[0]) + ": " + str(x[1]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_total_revenue(cursor):
    query = "SELECT p.Category, SUM(ip.Subtotal) AS TotalRevenue FROM productname p INNER JOIN itempurchased ip ON p.ProductID = ip.ProductID GROUP BY p.Category;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nProduct Category: Total Revenue")
    for x in cursor:
        print("◦ " + str(x[0]) + ": Rp" + "{:,}".format(float(x[1])))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_average_transaction(cursor):
    query = "SELECT CONCAT('Rp', FORMAT(AVG(TotalAmount), 0)) AS AverageTransactionAmount FROM salestransaction;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nAverage Transaction")
    for x in cursor:
        print("◦ " + str(x[0]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def get_no_sales(cursor):
    query = "SELECT p.ProductID, b.BrandName FROM productname p LEFT JOIN itempurchased ip ON p.ProductID = ip.ProductID INNER JOIN brand b ON b.BrandID = p.BrandID WHERE ip.PurchasedID IS NULL;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[Product ID] Brand Name")
    for x in cursor:
        print("◦ " + "[" + str(x[0]) + "] " + str(x[1]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
def retrieve_all_products(cursor):
    query = "SELECT b.BrandName FROM productname p INNER JOIN inventory i ON p.ProductID = i.ProductID INNER JOIN brand b ON b.BrandID = p.BrandID;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[Product ID] Brand Name")
    for x in cursor:
        print("◦ " + str(x[0]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def update_product_price(cursor):
    query = "UPDATE productname SET productname.Price = productname.Price * 1.1;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nSuccessfully updated prices of all products by 1.1%\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def receive_latest_restock_dates(cursor):
    query = "SELECT p.ProductID, b.BrandName, MAX(i.RestockDate) AS LatestRestockDate FROM productname p INNER JOIN inventory i ON p.ProductID = i.ProductID INNER JOIN brand b ON b.BrandID = p.BrandID GROUP BY p.ProductID, b.BrandName;"
    cursor.execute(query)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[Product ID] Brand Name | Date Restocked")
    for x in cursor:
        print("◦ " + "[" + str(x[0]) + "] " + str(x[1]) + " | " + str(x[2]))
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def prompt_return():
    print("Return to menu? Y/N")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    while True:
        selected = input("Your input: ")
        if str.upper(str(selected)) == "Y":
            break
        if str.upper(str(selected)) == "N":
            print("Exiting program")
            exit(1)
        else:
            print("Invalid input. Please retry.")

def main():
    db = db_connect()
    cursor = db.cursor()
    print("Welcome to StockUp (Grocery Management System)")
    while True:
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("What would you like to do?")
        print("◦ [0] Exit Program\n◦ [1] Get Items Low In Stuck\n◦ [2] Get Total Purchased\n◦ [3] Check Account Mutation\n◦ [4] Calculate Sales By Each Employee\n◦ [5] Retrieve Recent Transactions\n◦ [6] Find Shelf Locations Of Specific Product\n◦ [7] Employees List\n◦ [8] Get Unsuccessful Transaction\n◦ [9] Get Brand With Most Sales \n◦ [10] Total Revenue For Each Category\n◦ [11] Average Transaction Amount\n◦ [12] Products With No Sales\n◦ [13] All Products In Inventory\n◦ [14] Update Product Prices by 1.1%\n◦ [15] Latest Restock Dates")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        selected = int(input("Your input: "))
        match selected:
            case 0:
                print("Exiting program")
                exit(1)
            case 1:
                get_low_stock(cursor)
                prompt_return()
            case 2:
                get_total_purchased(cursor)
                prompt_return()
            case 3:
                check_acc_mutation(cursor, None, None)
                prompt_return()
            case 4:
                employee_sales(cursor)
                prompt_return()
            case 5:
                get_recent_transactions(cursor)
                prompt_return()
            case 6:
                retrieve_all_products(cursor)
                print("Which product would you like to find the location of?")
                selected = str(input("Your input: "))
                get_shelf_location(cursor, selected)
                prompt_return()
            case 7:
                get_employees_info(cursor)
                prompt_return()
            case 8:
                get_unsuccessful_transactions(cursor)
                prompt_return()
            case 9:
                get_most_sales_brand(cursor)
                prompt_return()
            case 10:
                get_total_revenue(cursor)
                prompt_return()
            case 11:
                get_average_transaction(cursor)
                prompt_return()
            case 12:
                get_no_sales(cursor)
                prompt_return()
            case 13:
                retrieve_all_products(cursor)
                prompt_return()
            case 14:
                update_product_price(cursor)
                prompt_return()
            case 15:
                receive_latest_restock_dates(cursor)
                prompt_return()
            case _:
                print("Invalid input. Please retry.")
                prompt_return()
    
main()