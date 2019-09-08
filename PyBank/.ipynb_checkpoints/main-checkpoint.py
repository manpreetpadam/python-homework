# This is main script for analysis
 
from pathlib import Path
import csv

class FinancialAnalyzer:
    def __init__(self,inputFilePath,outputFilePath):
        #Assign the relative path for the source csv file
        self.inputFilePath=Path(inputFilePath)

        #Assign the relative path for the output text file
        self.outPutFilePath=Path(outputFilePath)

        #Create empty lists to hold months and Profit/Loss data
        self.months=[]
        self.results=[]
        self.monthly_result_change=[]
    
    def ReadCsv(self):
        with open(self.inputFilePath,'r') as csvFile:
            _csvReader=csv.reader(csvFile,delimiter=',')
            _csvHeader=next(_csvReader)
            
            for row in _csvReader:
                self.months.append(row[0])
                self.results.append(float(row[1]))
    
    def CalculateTotalMonths(self):
        return len(self.months)

    def CalculateNetTotalPF(self):
        return round(sum(self.results),2)
    
    def CalculateAveragePF(self):
        for i in range(len(self.results)-1):
            self.monthly_result_change.append(self.results[i+1]-self.results[i])
        _avgPF=round(sum(self.monthly_result_change)/len(self.monthly_result_change),2)
        return _avgPF
    
    def GetMonthWithMaximumResult(self):
        _monthWithMaximumProfit={'Month':'','MaxValue':0}
        _monthWithMaximumProfit['MaxValue']=max(self.monthly_result_change)
        _monthWithMaximumProfit['Month']=self.monthly_result_change.index(_monthWithMaximumProfit['MaxValue'])+1
        return _monthWithMaximumProfit

    def GetMonthWithMinimumResult(self):
        _monthWithMinimumProfit={'Month':'','MinValue':0}
        _monthWithMinimumProfit['MinValue']=max(self.monthly_result_change)
        _monthWithMinimumProfit['Month']=self.monthly_result_change.index(_monthWithMinimumProfit['MinValue'])+1
        return _monthWithMinimumProfit

    def WriteResultsToTextFile(self,results):
        with open(self.outPutFilePath,'w') as textFile:
            textFile.write("Financial Analysis")
            textFile.write("\n")
            textFile.write("----------------------------")
            textFile.write("\n")
            textFile.write(f"Total Months: {results['Total_Months']}")
            textFile.write("\n")
            textFile.write(f"Total: ${results['Total_Amount']}")
            textFile.write("\n")
            textFile.write(f"Average Change: {results['Average_Change']}")
            textFile.write("\n")
            textFile.write(f"Greatest Increase in Profits: {results['Max_Month']} (${(str(results['Max_Value']))})")
            textFile.write("\n")
            textFile.write(f"Greatest Decrease in Profits: {results['Min_Month']} (${(str(results['Min_Value']))})")