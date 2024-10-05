
# What to do 

In Lab Presentation 2.1, you were introduced to Bayesian probability visa vie sepsis survival minimal clinical records Links to an external site. from the UCI Machine Learning Repository. Summarize the cohort selection, data mining methods, and algorithms used in the scientific paper Links to an external site. directly connected to this dataset.

# My Answer

Based on the analysis of (Chicco & Jurman, 2020), the article defines a primary cohort as the information about admissions and hospitalizations between 2011 and 2012 of people diagnosed with infections, SIRS, microbial sepsis or septic shock from the Norwegian Patient Registry and the Statistics Norway agency (Knoop et al., 2017), this data set is defined as Primary Cohort.

The article describes the classification process to organize the Primary Cohort into a subset called Study cohort:

As the study focuses on Sepsis, the data selection used the Sepsis-3 definition (Singer et al., 2016) to organize the Primary Cohort into a subset, containing 19,051 hospital admissions divided as 81.07% patients who survived (15,445 positives) and 18.93% who deceased (3,606 negatives).
To confirm their findings, a cohort of 137 patients with 1 or 2 septic episodes was chosen from the South Korean critically ill medical records from January 2007 and December 2015 (Lee et al., 2018), defined as Validation Cohort.

Biostatistics univariate tests were used to determine the statistical significance of the three variables used in the study (sex, age and septic episode) and the target (survival)

The article also described the Machine Learning algorithms used. As the use of function approximation methods (Esch, 1990) was not enough to solve the problem of survival prediction, five machine learning classifiers were tested:

Linear regression
Linear SVM
Radial SVM
Gradient boosting
Naïve Bayes
 

References

Chicco, D., & Jurman, G. (2020). Survival prediction of patients with sepsis from age, sex, and septic episode number alone. Scientific Reports, 10(1), 17156. https://doi.org/10.1038/s41598-020-73558-3 Links to an external site.
Esch, R. (1990). Functional Approximation. In C. E. Pearson (Ed.), Handbook of Applied Mathematics: Selected Results and Methods (pp. 928–987). Springer US. https://doi.org/10.1007/978-1-4684-1423-3_17 Links to an external site.
Knoop, S. T., Skrede, S., Langeland, N., & Flaatten, H. K. (2017). Epidemiology and impact on all-cause mortality of sepsis in Norwegian hospitals: A national retrospective study. PloS One, 12(11), e0187990. https://doi.org/10.1371/journal.pone.0187990 Links to an external site.
Lee, S. H., Lee, J. Y., Hong, T. H., Kim, B. O., Lee, Y. J., & Lee, J. G. (2018). Severe persistent hypocholesterolemia after emergency gastrointestinal surgery predicts in-hospital mortality in critically ill patients with diffuse peritonitis. PloS One, 13(7), e0200187. https://doi.org/10.1371/journal.pone.0200187 Links to an external site.
Singer, M., Deutschman, C. S., Seymour, C. W., Shankar-Hari, M., Annane, D., Bauer, M., Bellomo, R., Bernard, G. R., Chiche, J.-D., Coopersmith, C. M., Hotchkiss, R. S., Levy, M. M., Marshall, J. C., Martin, G. S., Opal, S. M., Rubenfeld, G. D., van der Poll, T., Vincent, J.-L., & Angus, D. C. (2016). The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA, 315(8), 801–810. https://doi.org/10.1001/jama.2016.0287 Links to an external site.
