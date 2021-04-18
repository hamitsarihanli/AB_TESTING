import pandas as pd
from scipy.stats import shapiro
from scipy import stats

df_ = pd.read_excel(".../ab_testing_data.xlsx",
                    sheet_name="Control Group")
df2_ = pd.read_excel(".../ab_testing_data.xlsx",
                    sheet_name="Test Group")

df_control = df_.copy()
df_test = df2_.copy()

#####################
### 1. AB Testing ###
#####################

###############################
### 1.1. Assumption Control ###
###############################

##################################
#>>>  1.1.1 Normality assumption #
##################################

test_statistics, pvalue = shapiro(df_control["Purchase"])
print('Test Statistics is = %.4f, p-value = %.4f' % (test_statistics, pvalue))
# Test Statistics = 0.9773, p-value = 0.5891

# If the p-value < 0.05, H0 is rejected.
# If the p-value > 0.05, H0 can not be rejected.


test_statistics, pvalue = shapiro(df_test["Purchase"])
print('Test Statistics is = %.4f, p-value = %.4f' % (test_statistics, pvalue))
# Test Statistics = 0.9589, p-değeri = 0.1541

# If the p-value < 0.05, H0 is rejected.
# If the p-value > 0.05, H0 can not be rejected.

#################################
#>>> 2.1.2 Variance Homogeneity #
#################################

# H0: Variances Are Homogeneous
# H1: Variances Are Not Homogeneous


stats.levene(df_control["Purchase"],
             df_test["Purchase"])

#LeveneResult(statistic=2.6392694728747363, pvalue=0.10828588271874791)
# H0 was not rejected because the p-value was not less than 0.05.
# Variances are homogeneous.

########################################
### 2. Application of the Hypothesis ###
########################################

# Independent two-sample t test if assumptions are provided (parametric test)
# H0: M1 = M2 (There is no statistically significant difference between the two group averages.)

# H1: M1! = M2 (There is a statistically significant difference between the two group averages)

# H0 Rejected if p-value <0.05.
# If p-value> 0.05, H0 Cannot be denied.

test_statistics, pvalue = stats.ttest_ind(df_control["Purchase"],
                                           df_test["Purchase"],
                                           equal_var=True)

print('Test Statistics is  %.4f, p-value is %.4f' % (test_statistics, pvalue))

# Test Statistics = -0.9416, p-value = 0.3493
# H0 was not rejected because the p value was not less than 0.05.

# No statistically significant difference was observed between the means of the two groups.
