{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '../Pybank_Completed/budget_data_copy.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-7-b98cba2a19e3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;31m#Open and read csv\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0mcsv\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbudget_path\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnewline\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m''\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreadlines\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;31m#Read the header row\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '../Pybank_Completed/budget_data_copy.csv'"
     ]
    }
   ],
   "source": [
    "#Imports for csvreader\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#Set path\n",
    "budget_path = os.path.join('..','Pybank_Completed','budget_data_copy.csv')\n",
    "\n",
    "#Open and read csv\n",
    "csv = open(budget_path, newline='').readlines()\n",
    "\n",
    "#Read the header row\n",
    "header = csv[0].strip().split(',')\n",
    "\n",
    "profit = 0 \n",
    "month_count = len(csv)-1\n",
    "max_diff = 0\n",
    "min_diff = 0\n",
    "average_change = 0\n",
    "\n",
    "for i in range(1,len(csv[1:])):\n",
    "    date, value = csv[i].strip().split(',')\n",
    "    profit += int(value)\n",
    "    \n",
    "rows = [row.strip().split(',') for row in csv[1:]]\n",
    "\n",
    "for i in range(len(rows)-1):\n",
    "    diff = int(rows[i+1][1])-int(rows[i][1])\n",
    "    profit += int(value)\n",
    "    average_change += diff\n",
    "    if diff > max_diff:\n",
    "        max_diff_i = i+1\n",
    "    if diff < min_diff:\n",
    "        min_diff_i = i+1\n",
    "    max_diff = max(max_diff, diff)\n",
    "    min_diff = min(min_diff, diff)\n",
    "\n",
    "\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------------------------------\")\n",
    "print(f\"Total Months: {month_count}\")\n",
    "print(\"Total: %s\"%(profit))\n",
    "print(f\"Average Change: ${(average_change/(float(month_count)-1))}\")\n",
    "print(f\"Greatest Increase in Profits: {(rows[max_diff_i])}\")\n",
    "print(f\"Greatest Decrease in Profits: {(rows[min_diff_i])}\")\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
