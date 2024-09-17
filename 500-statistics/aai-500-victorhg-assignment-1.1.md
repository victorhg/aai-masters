---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: masters
    language: python
    name: masters
---

# Assignment 1.1


Name:  Victor Hugo Germano
Date: 09/05/2024

```python
import pandas as pd
import numpy as np
from sklearn.neighbors import KernelDensity
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec
import math
import scipy.stats as st
```

For this assignment, you will refer to the textbook to solve the practice exercises. **Use Python to answer any coding problems (not R, even if indicated in your textbook).** Use Jupyter Notebook, Google Colab, or a similar software program to complete your assignment. Submit your answers as a **PDF or HTML** file. As a best practice, always label your axes and provide titles for any graphs generated on this assignment. Round all quantitative answers to 2 decimal places.


## **Problem # 1.1.** 
In the 2018 election for Senate in California, a CNN exit poll of 1882 voters stated that 52.5% voted for the Democratic candidate, Diane Feinstein. Of all 11.1 million voters, 54.2% voted for Feinstein.

(a) What was the (i) subject, (ii) sample, (iii) population? 



`(a) Your answer goes here`

```python
subject_candidate = "Diane Feinstein"

total_population = 11,100,000

sample_population = 1882

```

## **Problem # 1.2.** 
The `Students` data file at [http://stat4ds.rwth-aachen.de/data/Students.dat](http://stat4ds.rwth-aachen.de/data/Students.dat) responses of a class of 60 
social science graduate students at the University of Florida to a questionnaire that asked about *gender* (1 = female, 0 = male), *age*, *hsgpa* = high school GPA (on a four-point scale), cogpa = college GPA, *dhome* = distance (in miles) of the campus from your home town, *dres* = distance (in miles) of the classroom from your current residence, *tv* = average number of hours per week that you watch TV, *sport* = average number of hours per week that you participate in sports or have other physical exercise, *news* = number of 
times a week you read a newspaper, *aids* = number of people you know who have died from AIDS or who 
are HIV+, *veg* = whether you are a vegetarian (1 = yes, 0 = no), *affil* = political affiliation (1 = Democrat, 2 
= Republican, 3 = independent), *ideol* = political ideology (1 = very liberal, 2 = liberal, 3 = slightly liberal, 4 
= moderate, 5 = slightly conservative, 6 = conservative, 7 = very conservative), *relig* = how often you 
attend religious services (0 = never, 1 = occasionally, 2 = most weeks, 3 = every week), *abor* = opinion 
about whether abortion should be legal in the first three months of pregnancy (1 = yes, 0 = no), *affirm* = 
support affirmative action (1 = yes, 0 = no), and *life* = belief in life after death (1 = yes, 2 = no, 3 = 
undecided). You will use this data file for some exercises in this book. 



(a) Practice accessing a data file for statistical analysis with your software by going to the book’s 
     website and copying and then displaying this data file.



### (a) Accessing the Students file and showing the first few lines

```python

# Read in the Students data file
students = pd.read_csv('https://stat4ds.rwth-aachen.de/data/Students.dat', sep=r'\s+')

# View the first few rows of the dataset
students.head()
```

(b) Using responses on *abor*, state a question that could be addressed with (i) descriptive 
     statistics, (ii) inferential statistics.



A question about abortion looking at the dataset: 

**What's the distribution of people in favor of abortion being legal in the first three months, and how that can be an estimation about the opinion within the university?**

---



## **Problem # 1.3.** 
Identify each of the following variables as categorical or quantitative: (a) Number of smartphones that you own; (b) County of residence; (c) Choice of diet (vegetarian, nonvegetarian); (d) Distance, in kilometers, commute to work


| variable | data type | why? |
| --- |  --- | --- |
| Number of smartphones you own | Quantiative | countable |
| Country of Residence | Categorical  | non countable |
| Choice of diet |  Categorical | non countable |
| Distance commute to work |  Quantitative | countable |

---


## **Problem # 1.4.** 
Give an example of a variable that is (a) categorical; (b) quantitative; (c) discrete; (d) continuous


Examples of variables:

- Categorical
  - Eye Collors
  - Place of Origin
- Quantitative
  - Monthly Salary
  - Restaurant Capacity
- Discrete
  - Units Sold
  - Number of Attendees
- Continuous
  - Oil Prices
  - Temperature Outsite

---


# Define Methods to be used on the next problems

```python
# Plotting function for histogram
def histogram_plot(ylabel, xlabel, dataset, column, bins=10):
    gs = gridspec.GridSpec(1,1)
    fig = plt.figure(figsize=(5,3))
    ax = fig.add_subplot(gs[0])
    ax.set_xlabel(xlabel)
    dataset[column].hist(ax=ax, grid=False, bins = bins)
    fig.supylabel(ylabel)
    plt.show()


def print_summary(Min_value, Max_value, median, Lower_quartile, Upper_quartile):
    print("Five-number summary: min:%.2f max:%.2f median:%.2f lower q:%.2f upper q:%.2f"% (Min_value, Max_value, median, Lower_quartile, Upper_quartile)) 
    
def calculate_five_number_summary(array):
    # Extreme Values
    Max_value = array.max()
    Min_value = array.min()
    
    # Lower and upper Quartiles
    Lower_quartile = np.percentile(array, 25)
    Upper_quartile = np.percentile(array, 75)
    
    # Median
    median = np.median(array)

    return Min_value, Max_value, median, Lower_quartile, Upper_quartile
```

## **Problem # 1.10.** 
Analyze the `Carbon_West` ([http://stat4ds.rwth-aachen.de/data/Carbon_West.dat](http://stat4ds.rwth-aachen.de/data/Carbon_West.dat)) data file at the book’s website by **(a)** constructing a frequency distribution and  a histogram, **(b)** finding the mean, median, and standard deviation. Interpret each.


`(a)`

```python
# Reading file
carbon_west = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Carbon_West.dat', sep=r'\s+')
carbon_west.head()
```

```python

#freq_table = pd.crosstab(carbon_west['CO2'], 'CO2 Production') 

# Generate Histogram
histogram_plot("Number of Countries", "CO2 Emission", carbon_west, "CO2")
```

`(b) Your answer goes here`

```python
countries = carbon_west["Nation"]
co2 = carbon_west["CO2"]
plt.scatter(co2, countries)

plt.xlabel('Countries')
plt.ylabel('CO2 Emission')
plt.title('Countries')
plt.show()

# Print mean, median, and standard deviation
print('CO2 Emissions: Mean=%.2f, Median=%.2f, Std Dev=%.2f' % (np.mean(co2), np.median(co2), np.std(co2)))


```

### Data Interpretation 

The data presents the CO2 emission for a list of countries in europe, north america and australia, and the data extracted from the file can be interpreted as:

Mean
- The average CO2 emissions for any given country in the list is 6.72kt

Median
- If we were to split the list in two buckets, the value in the middle that defines a side would be 5.9kt

Stand Deviation
- Given any of the countries in the list, their co2 emission would be distant from the average emissons of the list by 3.31kt. Even though this is information is important, it also hides the outliers in the list with emission beyond 15kt, that contribute to a higher general avarage

---



## **Problem # 1.11.** 
According to Statistics Canada, for the Canadian population having income in 2019, annual income had a median of `$`35,000 and mean of `$`46,700. What would you predict about the shape of the distribution? Why?



## Answer 1.11

Given the difference between the median and the mean values on income for Canada, we can expect to see a distribution with a large range of income between the lower and high end of income values, possibily representing a larger population on the lower income quadrant, and a large variation of higher income, pushing the mean value up

We can also expect a large standad deviation, and a desproportionated large number of individuals on the lower income quadrant.

The representation of the bell shaped curve distribution will be skewed in this case.

---


## **Problem # 1.13.**
A report indicates that public school teacher’s annual salaries in New York city have an approximate  mean of `$`69,000 and standard deviation of `$`6,000. If the distribution has approximately a bell shape, report intervals that contain about (a) 68%, (b) 95%, (c) all or nearly all salaries. Would a salary of  `$`100,000 be unusual? Why? 


<!-- #region -->

Assuming the three sigma rule, we very unlikely expect to see a salary of `$`100,000 in a bell have distribution, given that nearly all salaries would fall below `$`90,000. One could say it is almost impossible to this salary be represented in the sample.

a) 68% confidence level (between -1sigma and +1sigma )
- We can expect a salary from `$`63,000 to `$`75,000 covering 68% of the sample


b) 95% confidence level (between -2sigma and +2sigma)
- We can expect a salary from `$`57,000 to `$`81,000 covering 95% of the sample 


c) 99.7% confidence level (between -3sigma and +3sigma)
- We can expect a salary from `$`51,000 to `$`87,000 covering 99.7% of the sample 
  

<!-- #endregion -->

## **Problem # 1.17.** 
From the `Murder` data file ([http://stat4ds.rwth-aachen.de/data/Murder.dat](http://stat4ds.rwth-aachen.de/data/Murder.dat)) at the book’s website, use the variable murder, which is the murder rate (per 100,000 population) for each state in the U.S. in 2017 according to the FBI Uniform Crime Reports. At first, do not use the observation for D.C. (DC). Using software:  
(a) Find the mean and standard deviation and interpret their values.  
(b) Find the five-number summary, and construct the corresponding box plot. Interpret.  
(c) Now include the observation for D.C. What is affected more by this outlier: The mean or the median? The range or the inter-quartile range?


**Answer:**


`(a) Your answer goes here` 

```python
# Method definitions to be reused

def print_murder_rates(numbers):
    print('Murder rates by State: Mean=%.2f, Std Dev=%.2f, Median=%.2f' % (np.mean(numbers), np.std(numbers), np.median(numbers)))

    

```

```python

murder_rates = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Murder.dat', sep=r'\s+')

# Remove DC from murder rates
no_DC = murder_rates.drop(murder_rates.index[(murder_rates["state"] == "DC")],axis=0)
murder_numbers_no_dc = no_DC["murder"]


histogram_plot("Number of States", "Murder Rates ber 100k", no_DC, "murder")

print_murder_rates(murder_numbers_no_dc)

```

### Interpretation

Given the data provided, we conclude that there are an avarege of 4.87 murders per 100,000 in the US, with a variation of 2.5. As we plot an histogram represeting the data, it is possible to see an skewed distribution of a bell shape 



`(b) Your answer goes here`

```python
### Five-number summary

five_numbers = calculate_five_number_summary(murder_numbers_no_dc)

print_summary(*five_numbers)


# Creating plot
fig = plt.figure(figsize =(5, 4))
plt.boxplot(murder_numbers_no_dc, vert=False)

# show plot
plt.show()

```

`(c) Your answer goes here` 

```python
# Redefining murder_numbers to include DC

murder_numbers = murder_rates["murder"]


histogram_plot("Number of States", "Murder Rates per 100k", murder_rates, "murder")

print("# Including DC:")
print_murder_rates(murder_numbers)
print_summary(*calculate_five_number_summary(murder_numbers))

```

## Interpretation of considering DC 

- It is clear that the inclusion of DC afects most results calculated before, specially moving the maximun value to 24.20, increasing the range 
- Mean and Median had an increase lower than 10% with Mean being more afected, with an increase of 7%
- The Standard Deviation changed more than 40%
- Upper quartile was more affected, increasing from 6.17 to 6.45
- Relative Standard Deviation (coefficient variation) changed from 52% to 70%
- Positively Skewed distribution, with a long tail

---



## **Problem # 1.18.**
The `Income` data file ([http://stat4ds.rwth-aachen.de/data/Income.dat](http://stat4ds.rwth-aachen.de/data/Income.dat)) at the book’s website reports annual income values in the U.S., in thousands of dollars.

(a) Using software, construct a histogram. Describe its shape.  
(b) Find descriptive statistics to summarize the data. Interpret them.  
(c) The kernel density estimation method finds a smooth-curve approximation for a histogram. At each value, it takes into account how many observations are nearby and their distance, with more weight given those closer. Increasing the bandwidth increases the influence of observations further away. Plot a smooth-curve approximation for the histogram of income values. Summarize the impact of increasing and of decreasing the bandwidth substantially from the default value.  
(d) Construct and interpret side-by-side box plots of income by race (B = Black, H = Hispanic, W = White).  Compare the incomes using numerical descriptive statistics

```python
# File Load
income_data = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Income.dat', sep=r'\s+')

```

**Answers:**


`(a) Your answer goes here`

```python

# Generate Histogram
histogram_plot("Individuals", "Income in thousands of dollars", income_data, "income", bins=30)

print("Income Curve information: Mean:%.2f"%(np.mean(income_data["income"])))
print_summary(*calculate_five_number_summary(income_data["income"]))

# Generate Histogram
histogram_plot("Individuals", "Education", income_data, "education")

print("Education Curve information: Mean:%.2f"%(np.mean(income_data["education"])))
print_summary(*calculate_five_number_summary(income_data["education"]))
```

<!-- #region -->
### Explanation

The Income histogram presents an Asymmetrical distribution, Positively Skewed with a long tail, meaning that most of the cluster is centered closed to the lower values, with frequency reducing as we move to higher salaries. 

We also notice that Mean and Median are far apart, with the value Mean 37.52 and Median 30

Important to note that this histogram considers the full dataset, without analyzing specific samples like race and education. Using these variations could change the representation of the graph, and subsequent analyzis 


---
<!-- #endregion -->

`(b) Your answer goes here`

```python
# Find descriptive statistics to summarize the data. Interpret them.

education = income_data["education"]
income = income_data["income"]
plt.figure(figsize=(5,3))
plt.scatter(education, income)
plt.xlabel('Education')
plt.ylabel('Income')
plt.title('Income x Education')
plt.show()

print(income_data.describe())
```

### Explanation & Description

Interesting to notice how the Median and Mean for Income distribution are far apart by more than 20%, as referenced on (a), and that can be confirmed looking at other information on the lower quartile and upper quartile, that are represented between 22k - 46k salary, with the maximum being 120k

Education on the other hand, is more simetrically distributed with a much smaller distance between Mean and Median



`(c) Your answer goes here`

```python
# The kernel density estimation method finds a smooth-curve approximation for a histogram. 
# At each value, it takes into account how many observations are nearby and their distance, with more weight given those closer. 
# Increasing the bandwidth increases the influence of observations further away. 
# Plot a smooth-curve approximation for the histogram of income values. 
# Summarize the impact of increasing and of decreasing the bandwidth substantially from the default value.

plt.figure(figsize=(5,3))
sns.histplot(income_data["income"], bins=30, kde=True, kde_kws={'bw_adjust':1})
 
# Adding labels and title

plt.xlabel('Salary in thousand')
plt.ylabel('Frequency')
plt.title('Income Salary and Density')


plt.show()
```

`(d) Your answer goes here`

```python
# Construct and interpret side-by-side box plots of income by race (B = Black, H = Hispanic, W = White). 
# Compare the incomes using numerical descriptive statistics

blacks = income_data[income_data.race.isin(["B"])]
hispanics = income_data[income_data.race.isin(["H"])]
whites = income_data[income_data.race.isin(["W"])]


box_data = pd.DataFrame({
        "Blacks": blacks["income"], 
        "Hispanics": hispanics["income"],
        "Whites": whites["income"]
        })

box_data.plot(kind='box', title='boxplot', showmeans=True, meanline=True)


# Display the figure
plt.show()
box_data.describe()
```

### Interpretation

The interesting aspect of the information is how distinct the data is presented once we separate by Race, that becomes more evident with the box-plot representation.

I noticed that the representation of whites (50) in the sample data far outnumbers hispanics (14) and blacks (16) together, given the general population distribution in the US. 

We can see that in every category there are outliers above the whiskers, with higher incomes overall in the Whites cathegory (120k).

The average income in the three categories presents an scenario where Whites mean of 42k is higher than hispanics top whisker, and the same as 75% of the blacks population. 

Even though the minimum values are closer between the three categories, whites still have a higher minimum value. On the upper quartile the difference is more evident, and the 75% mark with the highest difference between the groups with blacks, hispanics and whites represented at 31, 32, and 50, respectively.

Whites have the biggest standard deviation at 22k, and a longer upper quartile range. 

---



## **Problem # 1.19.** 
The `Houses` data file ([http://stat4ds.rwth-aachen.de/data/Houses.dat](http://stat4ds.rwth-aachen.de/data/Houses.dat)) at the book’s website lists the selling price (thousands of dollars), size (square feet), tax bill (dollars), number of bathrooms, number of bedrooms, and whether the house is new (1 = yes, 0 = no) for 100 home sales in Gainesville, Florida. Let’s analyze the selling prices. 

(a) Construct a frequency distribution and a histogram. Describe the shape.  
(b) Find the percentage of observations that fall within one standard deviation of the mean. Why is this not close to 68%?  
(c) Construct a box plot, and interpret.   
(d) Use descriptive statistics to compare selling prices according to whether the house is new. 





**Answer:**


`(a) Your answer goes here`

```python
# Method to plot variables both Discrete and Continuous
def plot_variables(df, columns, num_cols=3, img_height=3, img_width=10, discrete=False, continuous=False):
    n_plots = len(columns)
    n_cols = num_cols
    n_rows = int(math.ceil(n_plots/n_cols))
    gs = gridspec.GridSpec(n_rows, n_cols)
    fig = plt.figure(figsize=(img_width,img_height))
    for i in range(n_plots):
        ax = fig.add_subplot(gs[i])
        if discrete:
            df[columns[i]].value_counts().sort_index().plot(kind='bar', ax=ax)
        if continuous:
            df[columns[i]].hist(ax=ax, grid=False)
            ax.axvline(df[columns[i]].mean(), color='k', linestyle='dashed', linewidth=1, alpha=0.5)
            
            min_ylim, max_ylim = plt.ylim()
            ax.text(df[columns[i]].mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(df[columns[i]].mean()))
        
        ax.set_xlabel(columns[i])
    fig.tight_layout()
    fig.supylabel('Count')
    plt.show()
    
```

```python
# (a) Construct a frequency distribution and a histogram. Describe the shape. 
houses_data = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Houses.dat', sep=r'\s+')

#Plot discrete variables
plot_variables(houses_data, ["new", "bedrooms", "baths"], discrete=True)

#Plot continuous variables
plot_variables(houses_data, ["price", "size", "taxes"], continuous=True)

```

### Interpretation

- Positively Skewed distribution of house prices, size and taxes, presenting a correlation between size of a house, their relative price and the expected tax incurred on a purchase.
- 


`(b) Your answer goes here`


```python
# (b) Find the percentage of observations that fall within one standard deviation of the mean. 
# Why is this not close to 68%?  <<< Not normal distribution
 

price_mean= np.mean(houses_data["price"])
price_std= np.std(houses_data["price"])

print("House Prices data: \n Mean:%.2f | STD:%.2f"% (price_mean, price_std))

#Finding the total observations on 1sigma Empirical Rule
observations_one_sigma = houses_data[houses_data["price"].between((price_mean - price_std), (price_mean + price_std)) ]

percent_representation = (len(observations_one_sigma) / len(houses_data["price"])) * 100

print("Houses on 1sigma of the distribution:%.2f | Represents %.2f%%  of the sample"% (len(observations_one_sigma), percent_representation))


```

### Interpretation

Given the House Prices dataset do not represent a normal distribution, presented on (a), the Empirical Rule does not apply. In normal distribution we would have an close do equal of observations close to the mean, which is not the case for a Skewed Distribution.



`(c) Your answer goes here`

```python
#(c) Construct a box plot, and interpret.  
houses_data["price"].plot(kind='box', title='boxplot house prices', showmeans=True, meanline=True)

# Display the figure
plt.show()
```

### Interpretation

- The box represents how the prices distribution is accounted for. An interesting aspect is the fact that above house prices of `$`400k, the observations are all outliers, given that the top whisker is set at this value.
- The 75% population of prices is set at `$`254K, and the box plot show clearly that the median value is around $200k
- Outliers spread from just above `$`400, up to the maximum of `$`880k



`(d) Your answer goes here`

```python
#(d) Use descriptive statistics to compare selling prices according to whether the house is new. 
houses_data.describe()

# defining data
three_bed_houses = houses_data[houses_data["bedrooms"] == 3]
two_bath_houses = houses_data[houses_data["baths"] == 2]
new_houses = houses_data[houses_data["new"] == 1]
old_houses = houses_data[houses_data["new"] == 0]


fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)
labels = ['new houses', 'old houses']

# defining plots for new and old houses using the defined variable (bedrooms or bathrooms)
# histogram for new and old houses
ax0.boxplot(
    [new_houses["price"], 
    old_houses["price"]],
    meanline=True, showmeans=True, tick_labels=labels)
ax0.set_title('General Old and New Houses')
ax0.set_ylabel('Prices')

ax1.boxplot(
    [two_bath_houses[two_bath_houses["new"] == 1]["price"], 
    two_bath_houses[two_bath_houses["new"] == 0]["price"]],
    meanline=True, showmeans=True, tick_labels=labels)
ax1.set_title('Houses with 2 bathrooms')
ax1.set_ylabel('Prices')


ax2.boxplot(
    [three_bed_houses[three_bed_houses["new"] == 1]["price"], 
    three_bed_houses[three_bed_houses["new"] == 0]["price"]],
    meanline=True, showmeans=True, tick_labels=labels)
ax2.set_title('Houses with 3 bedrooms')
ax2.set_ylabel('Prices')




fig.suptitle('House prices', fontsize=16)

fig.tight_layout()
fig.set_figwidth(11)
plt.show() 

print("Old Houses Summary")
print(old_houses.describe())

print("\nNew Houses Summary")
print(new_houses.describe())

```

<!-- #region -->
### Interpretation

I decided to use two variables (number of bedrooms and number of bathrooms) to analyze the impact of house prices from new to old, to have more examples of how it affects the distribution.

When looking at the first graph, containing all houses divided between New & Old, we see an evident disparity in the Mean and Median values, with new houses accounting for over 100% the price average of an old house. Max price values for new and old house are similar (new: `$`866k, old: `$`800k), but the box graph show the evident outlier in the case of old house. The vast majority (top 75%) of old houses are bellow `$`240k  
 - Mean Price for New Houses: `$`436k
 - Mean Price for Old Houses: `$`208k


Using the discrete variable _Number of Bathrooms_, and a sample of all houses with 2 bathrooms, we see a similar average price of the houses in both cases, but the top whiskers of both old and new houses stayed close above `$`400K, even though new houses do have a higher Median and Mean value.

When looking at the mean price of houses with 3 bedrooms, the difference is more apparent, with the interquartile range for new houses being higher than the first graph 


<!-- #endregion -->

```python

```
