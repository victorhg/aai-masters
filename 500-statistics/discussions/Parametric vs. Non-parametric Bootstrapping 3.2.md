# What to do
Prior to completing this discussion forum, read the Sampling Distributions and the Bootstrap article. Respond to the following prompt by Day 4 of the learning week. Cite resources and references appropriately in APA format.

Discuss the differences between a parametric and a non-parametric bootstrap, as discussed in the Sampling Distributions and the Bootstrap article you read this week. Provide real-world examples of when and how you would use each method.


# Answer

Bootstrapping provides a practical way to analyze stability and variability in estimates derived from limited data

**Parametric Bootstrap**: This approach assumes a specific statistical model (like a negative binomial distribution) based on the sample data. New samples are generated from this model, which can produce values outside the range of observed data. This method works well if the model accurately represents the underlying data distribution.

It is important to note that the definition of a parametric bootstrap does need a deep understanding of the data distribution to allow for best possible results. 

In [@boyntonParametricBootstrapEvaluate2018], in order to create a parametric model to evaluate asset portfolio allocation methods, the researchers assumed that the returns of the assets are multivariate normal, and that it is possible to predict the Sharpe Ratio [@sharpeMutualFundPerformance1966] to reach a better predictive investment performance.  Although the model was not perfect for all scenarios, compared with established approaches, it showed its value to the investor.

**Non-parametric Bootstrap**: This method does not rely on any assumptions about the underlying distribution. Instead, it randomly samples with replacement from the observed data to create new samples of the same size. This approach is generally safer when there is uncertainty about the source distribution but may underestimate variability when sample sizes are small.

The article [[@kulesaSamplingDistributionsBootstrap2015]] illustrates these concepts using the Luria-Delbrück experiment, which investigated mutation mechanisms in bacteria. And I would like to present three examples to illustrate the use of parametric and non-parametric bootstrap.

In [@anhalCausalityGDPEnergy2013] the strategy of analyzing the correlation between energy and coal consumption in India and the relationship with GDP growth in order to establish a  possible causality between growth-energy connection for the Indian Economy, important to policy and any commitments to reduce carbon emissions, given the possible Impact in economic growth. In order to arrive at the direction of causality between real GDP and final energy and coal consumption, a non-parametric approach methodology was used, based on the nature of the problem described and since the researchers make no assumptions about the nature of the distribution of the variables analyzed, the cumulative density function (CDF) was unknown.

Understanding both methods of bootstrapping will help future statistics work to improve our ability to create statistical model to analyze data.


# References 

Anhal, R. (2013). _Causality between GDP, Energy and Coal Consumption in India, 1970-2011: A Non-parametric Bootstrap Approach_. 434–446. [https://www.proquest.com/docview/1448347920?pq-origsite=primo&sourcetype=Scholarly%20Journals](https://www.proquest.com/docview/1448347920?pq-origsite=primo&sourcetype=Scholarly%20Journals)

Boynton, W., & Chen, F. (2018). A parametric bootstrap to evaluate portfolio allocation models. _Finance Research Letters_, _25_, 76–82. [https://doi.org/10.1016/j.frl.2017.10.009](https://doi.org/10.1016/j.frl.2017.10.009)

Kulesa, A., Krzywinski, M., Blainey, P., & Altman, N. (2015). Sampling distributions and the bootstrap. _Nature Methods_, _12_(6), 477–478. [https://doi.org/10.1038/nmeth.3414](https://doi.org/10.1038/nmeth.3414)
