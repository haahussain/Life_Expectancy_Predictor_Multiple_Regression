# Life Expectancy
### Project Description and Motivaton
Life expectancy is the average number of years that a group of persons in a population is expected to live. The intention of this project was to get a better understanding of the relationship between various public health factors and global life expectancy. How can countries better allocate their limited resources to improve their overall life expectancy. To answer that question A multiple linear regression model was created and then evaluated to determine if the approach was good. 

## Workflow

* Explore the Dataset
  * [Add Features](#new-features)
  * [Clean the Dataset](#cleaning-the-data)
* [Create Models](#results)
* [Evaluating Models](#train-test-split)
* [Recommendations](#take-home-message)


## Data Sources

The dataset was was collected from World Health Organization (WHO) and can be foud at [Kaggle](https://www.kaggle.com/kumarajarshi/life-expectancy-who "Kaggle"). The final dataset contains 2939 observations where each row represents a country for a specific year. THere are a total of 193 countries with data from years 2000 to 2015. The features include immunization factors, mortality factors, economic factors, social factors and other health related factors.

| Data                     | Data                             | Data                            |
| ------------------------ | -------------------------------- | ------------------------------- |
| Country                  | HIV\AIDS                         | Measles                         |
| Year                     | Hepatitis B                      | BMI                             |
| Life expectancy          | Polio                            | Status                          |
| Adult mortality          | Diphtheria                       | Prevalence for malnutrition 5-9 |
| Infant mortality         | GDP                              | Education                       |
| Alcohol consumpton       | Population                       | Total expenditre on health      |
| Expenditure on health (%)| Prevalence for malnutrition 1-19 |


## Technical Description

To achieve the goal we utilized various Python libraries such as [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html/ "Pandas") to clean and explore the data. [Numpy](https://www.numpy.org/ "Numpy"), [Scipy](https://www.numpy.org/ "Scipy"), and [Sklearn](https://scikit-learn.org/stable/ "Sklearn") for data analysis, descriptive statistics and modeling.

### New Features
Initially literature review and domain knowledge was used to select which predictors could have the greatest influence on life expectancy for the baseline model. Additionally, we created 4 more features that we beleived could affect life expectancy and better explain the data. These features include: 

1. Population Size - A population range was created which includes three catagories; Small, Medium, and Large.
2. Lifestyle - We created an interaction variable that takes alcohol consumption and BMI into consideration. 
3. Economy - A interaction variable between population and the gross domestic product (GDP).
4. Death ratio - The ratio between adult and infant mortality.

### Cleaning the Data

We began by removing all the fragmented observations from the dataset. We then checked if there was possible linearity between life expectancy and all features. When necessary certain features were transformed to achieve a more linear relationship and normal distribution.

<img src=Images/before_after_transform.JPG alt="Before and after GDP log transformation historgram" width="450"/>

Next we assessed the multicollinearity model assumption between the selected predictors by creating a correlation heatmap. A multicollinearity threshold was assigned at 0.8 which omitted alcohol consumption and GDP from the initial model.

![HeatMap](Images/heatmap.png)

We then proceeded to remove all possible outliers by looking at box-whisker plots and scatter plots. Extreme obserations that were skewing the data were removed.

<img src=Images/paired_before_lifestyle.png alt="Scatter Before removing outliers" width="350"/>


<img src=Images/paired_afte_lifestyle.png alt="Scatter Before removing outliers" width="350"/>

## Results

The first model we ran to predict life expectancy used the features; BMI, HIV, thinness 1-19, GDP, mortality ratio, lifestyle, education, infant mortality rate, economy, and population size. With R squared equal to 0.804, our initial model explains 80%~ of variation in life expectancy.

<img src=Images/init_summary.png alt="Initial model summary" width="450"/>

We ran the model again after scaling the data, and also removing predictors that were deemed insignificant (P-value > 0.05).

<img src=Images/scaled_model_summary.png alt="Scaled model summary" width="450"/>

To test the model, we looked at the distribution of residuals for homoscedasticity. The residuals although scattered did suggest a minor positive linear relationship. The heteroscedasticity is likely to due to one or more of the predictors' distribution being skewed or that there might be missing features our dataset does not have information on. 

<img src=Images/scaled_residuals.png alt="Residuals scatter plot and historgram" width="450"/>

We conducted a train, test split test using 80% of our data to predict the other 20%. The model's mean absolute error was 3.022

<img src=Images/model_final.png alt="Train test split model" width="450"/>

### Train Test Split
Additionally, we tested the model with all the features we previously excluded (BMI, alcohol, GDP, and population size). Expectedly, the model mean absolute error is slightly smaller (2.995). However, the deviation is still in years meaning the model has to be refined.

<img src=Images/model_all.png alt="Train test split model" width="450"/>

## Conclusion

Our suggestions for countries looking to increase their global life expectancy is to focus their resources mainly on program and policies that increase HIV awareness and prevention. Additionally, we recommend increasing developing policies that increase access to basic education. A possible next step would be to seperate developing and established countries as the public health factors effecting each type may be very different.
