# Project: Can you recognize the emotion from an image of a face? 
<img src="figs/CE.jpg" alt="Compound Emotions" width="500"/>
(Image source: https://www.pnas.org/content/111/15/E1454)

### [Full Project Description](doc/project3_desc.md)

Term: Fall 2019

+ Team ## Section1-Group2
+ Team members
	+ Chen, Qichao qc2254@columbia.edu
        + Culver, Ashley alc2221@columbia.edu
        + Lee, Richard rl3079@columbia.edu
        + Zhang, Justine yz3420@columbia.edu
        + Zheng, Kaiyan kz2324@columbia.edu

+ Project summary: In this project, we created a classification engine for facial emotion recognition. We rewrite our baseline model(KNN) in python and improve accuracy by using PCA. Then we tried different ways to calculate distance to extract features and different models(Logistice Regression, Random Forest, GBM and XGboost) in order to improve the accuracy. Finally, we decided to use logistic model whose accuracy is around 50%. The final model is in under doc/.
	
**Contribution statement**: ([default](doc/a_note_on_contributions.md)) Kaiyan Zheng built the baseline model in python, improved the baseline model, tune parameters for improved models and made the presentation. Justine Zhang built the tested different features and imporved models, decided the final model. Qichao Chen worked on feature and KNN in R.  Ashley Culver analyzed the models on the basis of time, accuracy, and similarity between the train model accuracy and test model accuracy and contributed to the presentation slides. Richard implemented normalization code before processing them into the models, and he tested logistic regression with different parameters, c values, and used grid search to find the optimal parameter.

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
