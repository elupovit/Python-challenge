{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "_________________________________________________\n",
      "Total Votes: 3521000\n",
      "_________________________________________________\n",
      "Khan,2218231,(63.0%)\n",
      "Correy,704200,(20.0%)\n",
      "Li,492940,(14.0%)\n",
      "O'Tooley,105629,(3.0%)\n",
      "_________________________________________________\n",
      "Winner: Khan\n",
      "_________________________________________________\n"
     ]
    }
   ],
   "source": [
    "#imports\n",
    "import os\n",
    "import csv\n",
    "import operator\n",
    "import sys\n",
    "\n",
    "#set path\n",
    "votes_csv = os.path.join('..','PyPoll','election_data.csv')\n",
    "\n",
    "#open and read csv\n",
    "csv = open(votes_csv, newline=\"\").readlines()\n",
    "\n",
    "#variables\n",
    "votes_casted = 0\n",
    "candidates = {}\n",
    "percentages = {}\n",
    "final = {}\n",
    "\n",
    "\n",
    "for i in range(1,(len(csv[1:]))):\n",
    "    id, county, candidate = csv[i].strip().split(',')\n",
    "    #vote counter\n",
    "    votes_casted = votes_casted+1\n",
    "    \n",
    "    #capture unique candidates into dictionary with values being vote count\n",
    "    if candidate not in candidates.keys():\n",
    "        candidates[candidate] = 1\n",
    "        percentages[candidate] = 1\n",
    "        \n",
    "    #Add to counters\n",
    "    elif candidate in candidates.keys():\n",
    "        candidates[candidate] = candidates[candidate] + 1\n",
    "        percentages[candidate] = percentages[candidate] + 1\n",
    "\n",
    "#Calculate percentages of votes[candidate]\n",
    "percentages_list = list(percentages.values())\n",
    "per = [(a/votes_casted)*100 for a in percentages_list]\n",
    "per_rounded = [round(elem, 4) for elem in per]\n",
    "p = \"%\"\n",
    "final_percentages = [str(x) + p for x in per_rounded]\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(\"_________________________________________________\")\n",
    "print(\"Total Votes: \" + str(votes_casted))\n",
    "print(\"_________________________________________________\")\n",
    "\n",
    "#Combine candidates dictionary with the final percentages calculations\n",
    "for (k,v),x in zip(candidates.items(), final_percentages):\n",
    "    print(f'{k},{v},({x})')\n",
    "\n",
    "print(\"_________________________________________________\")\n",
    "\n",
    "stats = candidates\n",
    "\n",
    "print(f'Winner: {max(stats.items(), key=operator.itemgetter(1))[0]}')\n",
    "\n",
    "print(\"_________________________________________________\")\n",
    "\n",
    "\n",
    "#sys.stdout = open('/dev/stdout', 'w')\n",
    "\n",
    "#output as txt.file"
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
