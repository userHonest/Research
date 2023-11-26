
import matplotlib.pyplot as plt
import numpy as np


lstCategories = ['HTTP Knowledge', 'HTTPS Programming', 'OWASP Awareness', 'Single Subject Course']
iTotalStudents = 4
lstValues = [4, 1, 0, 4]

lstPercentages = [(iValue / iTotalStudents) * 100 for iValue in lstValues]

fAveragePercentage = (3 / iTotalStudents) * 100
lstAverageLine = [fAveragePercentage] * len(lstCategories)

plt.figure(figsize=(10, 6))
lstBars = plt.bar(lstCategories, lstPercentages, color='skyblue')
plt.axhline(y=fAveragePercentage, color='r', linestyle='-', label='Average Trend Line (75%)')

for bar in lstBars:
    fYVal = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, fYVal, round(fYVal, 2), va='bottom', ha='center')

plt.xlabel('Categories')
plt.ylabel('Percentage of Students (%)')
plt.title('Student Knowledge and Experience')
plt.legend()

plt.show()

