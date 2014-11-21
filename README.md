RunsTest
========

This is a short implementation of the runs test suitable for multi-categorical data sequences. It is an adaption of the original Wald-Wolfowitz runs test and works with a linear combination of the weighted variances of run lengths.

One should note that the test has some limitations: there have to be more than one run length for an element, more than one run and  the number of occurrences minus the number of runs of an element has to exceed one. For details about these limitations please refer to the code or to [1]. Hence, I would only recommend to perform the test on somewhat longer sequences with more runs. I have included several warnings and exceptions into the code which should make it easier to catch the issues.

If you use the code, please cite:

Simon Walk, Philipp Singer and Markus Strohmaier,
Sequential Action Patterns in Collaborative Ontology Engineering Projects: A Case-study in the Biomedical Domain,
23rd ACM Conference on Information and Knowledge Management, Shanghai, China, 2014

[1] P. C. O'Brien and P. J. Dyck. A runs test based on run lengths. Biometrics, pages 237-244, 1985.
