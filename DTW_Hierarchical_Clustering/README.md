# Dynamic Time Warping(DTW) and Hierarchical Clustering
- Calculated DTW for all repo and returned a DTW distance matrix
- Used PCA to lower the dimensionality of the matrix
- Fed the matrix into the Hierarchical Clustering model
- Compared and Analyze the cluster

# Pickled DataFrame
- cluster_1000 : Is a dataframe of repos with the cluster label
- dtw_1000: Is a dataframe with only the DTW distance matrix
- merge_df2: Merged data containing all 1000 repo's info/data
- df_repo_5000: 5000 repo names and general data(totalCommits, totalStars, totalIssues, totalPullRequests, etc...)
- features-and-dtw_1000: Is a dataframe with the dtw distance matrix and features combined

# Future Ideas
- Run DTW on issue and pull request association and see if it'll generate different results when clustering
- Run DTW on sentiment to confirm if average sentiment per cluster to check if the results were meaningful
- Run DTW on different time periods and check if better clusters are formed
- Gather more data and run different models(Neural Networks or other unsupervised learning models)
- Investigate sub cluster within each cluster
- Run other NLP methods like: Topic Modeling - Context of the corpus(all comments in issues or pull request)
- Run NLP on tweets or reddit if the repo has one
- Binning by features(age or repo, stars, issues, commits, pull requests etc...) and run a cluster model
