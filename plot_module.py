import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler


def create_hist(data, transform=None, title=None, xlabel=None):
    '''This function creates an histogram. It can also accept transformation method to 
       create a histogram after the transoformation ('log', 'sqrt', 'cbrt')'''
    if transform == 'log':
        data = np.log(data)
    elif transform == 'sqrt':
        data = np.sqrt(data)
    elif transform == 'cube':
        data = np.cbrt(data)
    # create the plot

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(data, density=True)
    # add the labels
    ax.set_title(title)
    ax.set_ylabel('Frequency')
    ax.set_xlabel(xlabel)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return


def create_scatter(x, y, title, xlabel, ylabel):
    '''This function creates a scatter plot and saves the plot as png on your device.'''
    fig, ax = plt.subplots(figsize=(8, 5))
    # create the scatter
    ax.scatter(x, y, color="blue", alpha=0.3)

    # adds a title and axes labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # removing top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return


def CorrMtx(df, dropDuplicates=True, xrot=70, yrot=0, label='Variable'):
    '''This function accepts a correlation matrix of your data, returns a heat map and save
       the plot on your device'''

    # exclude duplicate correlations by masking uper right values
    if dropDuplicates:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

    # set background color / chart style
    sns.set_style(style='white')
    fig, ax = plt.subplots(figsize=(12, 10))

    # add diverging colormap from red to blue
    cmap = sns.diverging_palette(250, 10, as_cmap=True)
    # add titles
    plt.title("Correlation Heat Map")

    # draw correlation plot with or without duplicates
    if dropDuplicates:
        sns.heatmap(df, mask=mask, cmap=cmap,
                    square=True,
                    linewidth=.5, cbar_kws={"shrink": .5}, ax=ax)
        plt.xlabel(label)
        plt.ylabel(label)
        plt.xticks(rotation=xrot)
        plt.yticks(rotation=yrot)

    else:
        sns.heatmap(df, cmap=cmap,
                    square=True,
                    linewidth=.5, cbar_kws={"shrink": .5}, ax=ax)
        plt.xlabel(label)
        plt.ylabel(label)
        plt.xticks(rotation=xrot)
        plt.yticks(rotation=yrot)
    return


def get_pairs(data, dependent, features, n, fig_name=None):
    '''This function accepts a dataframe, the dependent variable name, list of feature names,
       number of plots per row and an optional figure name for saving the figure
    '''
    
    row_groups = [features[i:i+n] for i in range(0, len(features), n)]
    # create the plots
    for ind in row_groups:
        plot = sns.pairplot(x_vars=ind, y_vars=dependent,
                            data=data, kind="reg", height=3)
        if fig_name:
            plt.savefig(f"{fig_name}_{ind}.png")
    # save the file

    return


def checkresiduals(df, target, sm_model):
    ''' This function checks the model's homoscedasticity of a dataframe and saves the plot'''
    # checking for our model - Homoscedasticity,  Independence of residuals
    pred_val = sm_model.fittedvalues.copy()
    true_val = df[target].values.copy()
    residual = true_val - pred_val

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
#   fig, ax = plt.subplots(figsize=(8, 6))
    ax1.hist(residual, density=True, bins=30)
    ax2.scatter(df[target], residual)
    ax1.set_title('Residual Histogram')
    ax2.set_title('Residual Scatterplot')
    plt.show()
    return
