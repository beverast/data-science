# GitHub Analysis

To analyze open source projects and determine common features that influence the continued growth in contributions and popularity.

## Contributors


|                                       [Patrick Wilky](https://github.com/PWalis)                                        |                                       [Joseph Wagner](https://github.com/beverast)                                        |                                       [Dustin Yang](https://github.com/dustiny5)                                        |                                       [Patrick Steveson](https://github.com/Mrsteveson)                                        |                                       
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
|                      [<img src="https://avatars0.githubusercontent.com/u/48426713?s=400&v=4" width = "200" />](https://github.com/)                       |                      [<img src="https://avatars3.githubusercontent.com/u/15187637?s=400&v=4" width = "200" />](https://github.com/)                       |                      [<img src="https://avatars3.githubusercontent.com/u/46609531?s=400&v=4" width = "200" />](https://github.com/)                       |                      [<img src="https://avatars2.githubusercontent.com/u/46543946?s=400&v=4" width = "200" />](https://github.com/)                       |                     
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/PWalis)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/beverast)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/dustiny5)            |          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Mrsteveson)           |            
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/patrick-wilky-a434aa184/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/joseph-wagner-67a710b2/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/dustin-yang-a30489184/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/patricktsteveson/) | 



![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)

## Project Overview

[Trello Board](https://trello.com/b/aMs5qF5U/labs-15-github-commit)

[Product Canvas](https://www.notion.so/Github-Commit-Analysis-9f39d9567c494a29b3084bf5014b1da2)


**Why: What value can the consumer get from this?**

- Gain insight to what makes a GitHub repository successful.
- Avoid the pitfalls of an unsuccessful GitHub repository.
- Monitor repo success metrics (whatever those are)

**How do we know something is successful? How do we measure success?**

- Funding, Contributors, Bug Fixes, Pull Requests
- General outreach
    - marketing
    - social media
    - workshops
    - newsletters
- user adoption

### Tech Stack

- Pandas - Data organization, wranging, cleaning
- tslearn - Calculate dtw values of each repo
- scipy - Run PCA and hierarchical clustering
- scikit-learn - Run clustering models and preprocessing
- numpy - organize and clean data
- requests - Access APIs
- os - Access repo data files
- zipfile - Zip a file
- category_encoders - Encode categorical variables into ordinal variables

### Predictions
Initial Assumptions:
Run hierarchcial clustering on Dynamic Time Warping values of the repo to check if there are unique clusters of successful and unsuccessful repo.

Results:
Two main clusters: 1 cluster showed more activity then the other. This does not mean it is more successful than the other. More analysis required to confirm our assumptions.

Future Ideas:
- Run DTW on issue and pull request association and see if it'll generate different results when clustering
- Run DTW on sentiment to confirm if average sentiment per cluster to check if the results were meaningful
- Run DTW on different time periods and check if better clusters are formed
- Gather more data and run different models(Neural Networks or other unsupervised learning models)
- Investigate sub cluster within each cluster
- Run other NLP methods like: Topic Modeling - Context of the corpus(all comments in issues or pull request)
- Run NLP on tweets or reddit if the repo has one
- Binning by features(age or repo, stars, issues, commits, pull requests etc...) and run a cluster model

### Explanatory Variables

- Used unsupervised learning and did not have explanatory variables
- Used data from issues, pull request, stars, and commits to feed into our unsupervised clustering model

### Data Sources

-   [GraphQL](https://developer.github.com/v4/explorer/)
-   [Twitter]( https://developer.twitter.com/)
-   [Reddit](https://www.reddit.com/wiki/api)

### Python Notebooks

[Dyanmic Time Warping and Hierarchical Clustering](https://github.com/labs15-github-commit/data-science/blob/master/DTW_Hierarchical_Clustering/DTW_Clustering.ipynb)

[Srape Github's Data using GraphQL](https://github.com/labs15-github-commit/data-science/blob/master/GithubGraphQL/GithubGraphQL_All.ipynb)

[Python Notebook 3](🚫add link to python notebook here)

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).
