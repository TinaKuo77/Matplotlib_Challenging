{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Observations and Insights "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mouse ID</th>\n",
       "      <th>Drug Regimen</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age_months</th>\n",
       "      <th>Weight (g)</th>\n",
       "      <th>Timepoint</th>\n",
       "      <th>Tumor Volume (mm3)</th>\n",
       "      <th>Metastatic Sites</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>0</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>38.825898</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>10</td>\n",
       "      <td>35.014271</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>15</td>\n",
       "      <td>34.223992</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>k403</td>\n",
       "      <td>Ramicane</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>16</td>\n",
       "      <td>20</td>\n",
       "      <td>32.997729</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1888</th>\n",
       "      <td>z969</td>\n",
       "      <td>Naftisol</td>\n",
       "      <td>Male</td>\n",
       "      <td>9</td>\n",
       "      <td>30</td>\n",
       "      <td>25</td>\n",
       "      <td>63.145652</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1889</th>\n",
       "      <td>z969</td>\n",
       "      <td>Naftisol</td>\n",
       "      <td>Male</td>\n",
       "      <td>9</td>\n",
       "      <td>30</td>\n",
       "      <td>30</td>\n",
       "      <td>65.841013</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1890</th>\n",
       "      <td>z969</td>\n",
       "      <td>Naftisol</td>\n",
       "      <td>Male</td>\n",
       "      <td>9</td>\n",
       "      <td>30</td>\n",
       "      <td>35</td>\n",
       "      <td>69.176246</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1891</th>\n",
       "      <td>z969</td>\n",
       "      <td>Naftisol</td>\n",
       "      <td>Male</td>\n",
       "      <td>9</td>\n",
       "      <td>30</td>\n",
       "      <td>40</td>\n",
       "      <td>70.314904</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1892</th>\n",
       "      <td>z969</td>\n",
       "      <td>Naftisol</td>\n",
       "      <td>Male</td>\n",
       "      <td>9</td>\n",
       "      <td>30</td>\n",
       "      <td>45</td>\n",
       "      <td>73.867845</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1893 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Mouse ID Drug Regimen   Sex  Age_months  Weight (g)  Timepoint  \\\n",
       "0        k403     Ramicane  Male          21          16          0   \n",
       "1        k403     Ramicane  Male          21          16          5   \n",
       "2        k403     Ramicane  Male          21          16         10   \n",
       "3        k403     Ramicane  Male          21          16         15   \n",
       "4        k403     Ramicane  Male          21          16         20   \n",
       "...       ...          ...   ...         ...         ...        ...   \n",
       "1888     z969     Naftisol  Male           9          30         25   \n",
       "1889     z969     Naftisol  Male           9          30         30   \n",
       "1890     z969     Naftisol  Male           9          30         35   \n",
       "1891     z969     Naftisol  Male           9          30         40   \n",
       "1892     z969     Naftisol  Male           9          30         45   \n",
       "\n",
       "      Tumor Volume (mm3)  Metastatic Sites  \n",
       "0              45.000000                 0  \n",
       "1              38.825898                 0  \n",
       "2              35.014271                 1  \n",
       "3              34.223992                 1  \n",
       "4              32.997729                 1  \n",
       "...                  ...               ...  \n",
       "1888           63.145652                 2  \n",
       "1889           65.841013                 3  \n",
       "1890           69.176246                 4  \n",
       "1891           70.314904                 4  \n",
       "1892           73.867845                 4  \n",
       "\n",
       "[1893 rows x 8 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import scipy.stats as st\n",
    "\n",
    "# Study data files\n",
    "mouse_metadata_path = \"data/Mouse_metadata.csv\"\n",
    "study_results_path = \"data/Study_results.csv\"\n",
    "\n",
    "# Read the mouse data and the study results\n",
    "mouse_metadata = pd.read_csv(mouse_metadata_path)\n",
    "study_results = pd.read_csv(study_results_path)\n",
    "\n",
    "# Combine the data into a single dataset\n",
    "combined_study_data = pd.merge(mouse_metadata, study_results, on=\"Mouse ID\")\n",
    "\n",
    "# Display the data table for preview\n",
    "combined_study_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checking the number of mice.\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Optional: Get all the data for the duplicate mouse ID. \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a clean DataFrame by dropping the duplicate mouse by its ID.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checking the number of mice in the clean DataFrame.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Summary Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen\n",
    "\n",
    "# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: \n",
    "# mean, median, variance, standard deviation, and SEM of the tumor volume. \n",
    "# Assemble the resulting series into a single summary dataframe.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen\n",
    "\n",
    "# Using the aggregation method, produce the same summary statistics in a single line\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bar and Pie Charts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a bar plot showing the total number of measurements taken on each drug regimen using pandas.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a bar plot showing the total number of measurements taken on each drug regimen using pyplot.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using pandas\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a pie plot showing the distribution of female versus male mice using pyplot\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Quartiles, Outliers and Boxplots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the final tumor volume of each mouse across four of the treatment regimens:  \n",
    "# Capomulin, Ramicane, Infubinol, and Ceftamin\n",
    "\n",
    "# Start by getting the last (greatest) timepoint for each mouse\n",
    "\n",
    "\n",
    "# Merge this group df with the original dataframe to get the tumor volume at the last timepoint\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Put treatments into a list for for loop (and later for plot labels)\n",
    "\n",
    "\n",
    "# Create empty list to fill with tumor vol data (for plotting)\n",
    "\n",
    "\n",
    "# Calculate the IQR and quantitatively determine if there are any potential outliers. \n",
    "\n",
    "    \n",
    "    # Locate the rows which contain mice on each drug and get the tumor volumes\n",
    "    \n",
    "    \n",
    "    # add subset \n",
    "    \n",
    "    \n",
    "    # Determine outliers using upper and lower bounds\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a box plot of the final tumor volume of each mouse across four regimens of interest\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Line and Scatter Plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a line plot of tumor volume vs. time point for a mouse treated with Capomulin\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate a scatter plot of average tumor volume vs. mouse weight for the Capomulin regimen\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Correlation and Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the correlation coefficient and linear regression model \n",
    "# for mouse weight and average tumor volume for the Capomulin regimen\n"
   ]
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
  "anaconda-cloud": {},
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
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
