{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b95ac170",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "import os\n",
    "\n",
    "flight_data=pd.read_csv('flight_data12.csv')\n",
    "\n",
    "counter=13\n",
    "directory = r'/Users/moritz/Desktop/private_repository/flight_analysis/flight_data'\n",
    "for entry in os.scandir(directory):\n",
    "    if entry.path.endswith(\".csv\") and entry.is_file():\n",
    "        csv_data=pd.read_csv(entry)\n",
    "        flight_data=pd.concat([flight_data,csv_data],axis=0, sort=False)\n",
    "        flight_data.to_csv(f'flight_data{counter}.csv')\n",
    "        print (counter)\n",
    "        print ('\\n')\n",
    "        print (entry)\n",
    "        counter+=1"
   ]
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
