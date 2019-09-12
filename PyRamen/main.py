#This is the main script to run analysis
from pathlib import Path
import csv
class ProductAnalyzer:
    def __init__(self,menuDataPath,salesDataPath):
        self.menuSourceFilePath=Path(menuDataPath)
        self.salesSourceFilePath=Path(salesDataPath)
        self.menuItems=[]
        self.sales=[]
        self.report={}
        self.itemDetails={}
        self.missingItems=[]

    def ReadMenuData(self):
        with open(self.menuSourceFilePath,'r') as menuCSV:
            menuCSV=csv.reader(menuCSV,delimiter=',')
            #Skip Header Row
            next(menuCSV)
            for row in menuCSV:
                self.menuItems.append(row)

    def ReadSalesData(self):
        with open(self.salesSourceFilePath,'r') as salesCSV:
            salesCSV=csv.reader(salesCSV,delimiter=',')
            #Skip Header Row
            next(salesCSV)
            for row in salesCSV:
                self.sales.append(row)
    
    def GetMenuItemDetails(self):
        for item in self.menuItems:
            self.itemDetails[str(item[0])]={
                'Price':float(item[3]),
                'Cost':float(item[4])
            }

    def GenerateSalesReport(self,items={}):
        for salesData in self.sales:
            _menu_item=salesData[4]
            if _menu_item in items.keys():
                _quantity=int(salesData[3])
                _price=items[_menu_item]['Price']
                _cost=items[_menu_item]['Cost']
                _profit=_price-_cost
                if self.report.get(_menu_item)==None:
                    #First Instance of the menu item
                    reportDetails={
                        "01-count": _quantity,
                        "02-revenue": _price * _quantity,
                        "03-cogs": _cost * _quantity,
                        "04-profit": _profit * _quantity
                    }
                    self.report[_menu_item]=reportDetails
                else:
                    #Add to the previous data
                    self.report[_menu_item]["01-count"] +=_quantity
                    self.report[_menu_item]["02-revenue"] += (_price * _quantity)
                    self.report[_menu_item]["03-cogs"] += (_cost * _quantity)
                    self.report[_menu_item]["04-profit"] += (_profit * _quantity)
            else:
                self.missingItems.append(_menu_item)
            
            

            

            
            
            
            
            
            



