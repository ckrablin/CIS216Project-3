from datetime import datetime

def CreateUsers():
  print('##### Create users, passwords, and roles #####')
  UserFile = open("Users.txt", "a+")
  while True:
    username = GetUserName()
    if (username.upper() == "END"):
      break
    userpwd = GetUserPassword()
    userrole = GetUserRole()
    UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
    UserFile.write(UserDetail)
  UserFile.close()
  printuserinfo()
def GetUserName():
  username = input("Enter user name or 'End' to quit: ")
  return username
def GetUserPassword():
  pwd = input("Enter password: ")
  return pwd
def GetUserRole():
  userrole = input("Enter role (Admin or User): ")
  while True:
    if (userrole.upper() == "ADMIN" or userrole.upper() =="USER"):
      return userrole
    else:
      userrole = input("Enter role (Admin or User): ")
def printuserinfo():
  UserFile = open("Users.txt", "r")
  while True:
    UserDetail = UserFile.readline()
    if not UserDetail:
      break
    UserDetail = UserDetail.replace("\n", "")
    UserList = UserDetail.split("|")
    username = UserList[0]
    userpassword = UserList[1]
    userrole = UserList[2]
    print("User Name: ", username, " Password: ", userpassword, "Role: ", userrole) 

def Login():
  UserFile = open("Users.txt", "r")
  UserList = []
  UserName = input("Enter User Name: ")
  UserPwd = input("Enter Password: ")
  UserRole = "None"
  while True:
    UserDetail = UserFile.readline()
    if not UserDetail:
      return UserRole, UserName
    UserDetail = UserDetail.replace("\n", "")
    UserList = UserDetail.split("|")
    if UserName == UserList[0] and UserPwd == UserList[1]:
      UserRole = UserList[2]
      return UserRole, UserName

  

def WorkingDates():
 while True:
  try:
      FromDate = input("Enter the Start Date in mm/dd/yyy Format: ")
      FromDate = datetime.strptime(FromDate,'%m/%d/%Y')
      FromDate = FromDate.date()
      break
  except: 
    print("Invalid Entry, enter in mm/dd/yyy Format")
    continue
 while True: 
  try: 
    ToDate = input("Enter the End Date mm/dd/yyy Format: ")
    ToDate = datetime.strptime(ToDate,'%m/%d/%Y')
    ToDate = ToDate.date()
    break
  except:
    print("Invalid Entry, enter in mm/dd/yyy Format")
    continue
 return FromDate, ToDate

def GetEmployeeName():
  while True:
    try:
      FirstName = str(input('What is the Employee\'s First Name?: '))
      break
    except:
      print ("incorrect format try again")
      continue
  while True:  
    try:
      LastName=str(input('What is the Employee\'s Last Name: '))
      break
    except:
      print ("incorrect format try again")
      continue
  EmployeeName=LastName.capitalize() +', '+ FirstName.capitalize()
  return EmployeeName

def GetHoursWorked():
  while True:
    try:
      HoursWorked = float(input('How many hours did the employee work?: '))
      break
    except:
      print ("incorrect format try again")
      continue
  return HoursWorked

def GetPayRate():
  while True:
    try:
      PayRate = float(input('What is the employee\'s hourly rate?: '))
      break
    except:
      print ("incorrect format try again")
      continue 
  return PayRate

def GetTaxRate():
  while True:
    try:
      TaxRate = float(input('What is the employee\'s tax rate?: '))
      break
    except:
      print ("incorrect format try again")
      continue  
  TaxRate = TaxRate / 100
  return TaxRate

def EmployeeOutputCalc(HoursWorked,PayRate,TaxRate):
  GrossPay = (HoursWorked * PayRate)
  IncomeTax= (GrossPay * TaxRate)
  NetPay = (GrossPay - IncomeTax)
  return GrossPay,IncomeTax,NetPay

def PrintEmployeeInfo(EmployeeDetailList):
  TotalEmployees = 0
  TotalHours = 0.00
  TotalGrossPay = 0.00
  TotalTax = 0.00
  TotalNetPay = 0.00 

  for EmployeeList in EmployeeDetailList:
    FromDate = EmployeeList[0]
    EndDate = EmployeeList[1]
    EmployeeName = EmployeeList[2]
    HoursWorked = EmployeeList[3]
    PayRate = EmployeeList[4]
    TaxRate = EmployeeList [5]
    GrossPay, IncomeTax, NetPay = EmployeeOutputCalc(HoursWorked, PayRate, TaxRate)

    print (FromDate, EndDate, EmployeeName, f"{HoursWorked:,.2f}",
    f"{PayRate:,.2f}", f"{GrossPay:,.2f}", f"{TaxRate:,.1%}",
    f"{IncomeTax:,.2f}", f"{NetPay:,.2f}")

    TotalEmployees += 1
    TotalHours += Hours
    TotalGrossPay += GrossPay
    TotalTax  += IncomeTax
    TotalNetPay  += NetPay

  EmployeeTotals["TotalEmp"] = TotalEmployees
  EmployeeTotals["TotalHours"] = TotalHours
  EmployeeTotals["TotalGross"] = TotalGrossPay
  EmployeeTotals["TotalTax"] = TotalTax 
  EmployeeTotals["TotalNet"] = TotalNetPay 

def PrintTotals(EmployeeTotals):
  print(".........................................")
  print(f'Total Number Of Employees: {EmployeeTotals["TotalEmp"]}')
  print(f'Total Hours Of Employees: {EmployeeTotals["TotalHours"]}')
  print(f'Total Gross Pay Of Employees: ${EmployeeTotals["TotalGross"]:,.2f}')
  print(f'Total Tax Of Employees: ${EmployeeTotals["TotalTax"]:,.2f}')
  print(f'Total Net Pay Of Employees: ${EmployeeTotals["TotalNet"]:,.2f}')
  print(("........................................."))

def WriteEmployeeInformation(employee):
  file = open("employeeinfo.txt", "a")
  file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5]))

def GetFromDate():
  valid = False
  fromdate = ""
  while not valid:
    fromdate = input("Enter From Date (yyyy/dd/mm): ")
    if (len(fromdate.split('/')) != 3 and fromdate.upper() !='ALL'):
      print("Invalid Date Format: ")
    else:
      valid = True
      if fromdate.upper() != 'ALL':
          fromdate = datetime.strptime(fromdate, '%m/%d/%Y').date()
          fromdate = str(fromdate)
      else:
          fromdate = fromdate.upper()
      return fromdate
  
def ReadEmployeeInformation(fromdate):
  EmployeeDetailList = []
  file = open("employeeinfo.txt", "r")
  data = file.readlines()
  condition = True
  print(fromdate)
  print("FromDate Check")
  
  if fromdate == 'ALL':
    print(fromdate)
    condition = False
  
  for employee in data:
    employee = [x.strip() for x in employee.strip().split("|")]
    if not condition:
      EmployeeDetailList.append([employee[0],employee[1],employee[2],float(employee[3]),float(employee[4]),float(employee[5])])
    else:
      if fromdate == employee[0]:
        EmployeeDetailList.append([employee[0],employee[1],employee[2],float(employee[3]),float(employee[4]),float(employee[5])])
  return EmployeeDetailList


def addanother():
  AddAnother = str(input("Do you want to add another employee? Y/N "))
  AddAnother = AddAnother.upper()
  return AddAnother

if __name__=="__main__":
  CreateUsers()
  print()
  print("##### Data Entry #####")
  UserRole, UserName = Login()
  DetailsPrinted = False
  EmpTotals = {}
  if (UserRole.upper() == "NONE"):
    print(UserName, " is invalid.")
  else:
    if (UserRole.upper() == "ADMIN"):
      EmpFile = open("Employees.txt", "a+")
      while True:
        
        EmployeeDetailList = []
        EmployeeTotals = {}
        AddAnother = 'Y'

        print("\n\n....................Welcome to the Payroll System..........................\n\n")
        while AddAnother == 'Y':
          EmployeeName = GetEmployeeName()
          FromDate, ToDate = WorkingDates()
          Hours=GetHoursWorked()
          PayRate = GetPayRate()
          TaxRate = GetTaxRate()
          EmployeeDetail = [FromDate, ToDate, EmployeeName, Hours, PayRate,TaxRate]
          WriteEmployeeInformation(EmployeeDetail)
          AddAnother = addanother()
        print((".........................................\n"))
        fromdate = GetFromDate()
        EmployeeDetailList = ReadEmployeeInformation(fromdate)
        PrintEmployeeInfo(EmployeeDetailList)
        PrintTotals(EmployeeTotals)
        print ("\nThank You for Using the System!\n\n")

  
  
  
  
  
  







