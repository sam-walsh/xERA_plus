README.md
Project Title: xERA_plus

This project is focused on improving the Expected Earned Run Average (xERA) metric. The project uses data from the years 2015 to 2023, and applies machine learning techniques to predict run values. It also differs from baseball-savants version of xERA by not using an xwOBA conversion as to [better capture the effect of double plays](https://sam-walsh.github.io/posts/double-plays/).

Data

The data used in this project is stored in CSV files, each representing a different year from 2015 to 2023. Each file contains detailed statistics for each game played in that year.
Libraries Used

- pandas
- numpy
- matplotlib
- seaborn
- sklearn
Files

- xERA_plus.ipynb: This is the main Jupyter notebook where all the analysis and computations are performed.
How to Run

1. Clone the repository to your local machine.
2. Install the necessary libraries mentioned above.
3. Open the xERA_plus.ipynb file in a Jupyter notebook environment.
4. Run the cells in order to perform the analysis.
Analysis

The analysis includes:

- Reading and concatenating data from multiple CSV files.
- Computing run values for each event in a game.
- Grouping data by different parameters and calculating mean run values.
- Predicting run values using a K-Nearest Neighbors Regressor model.
- Predicting run value leaders for different years.
Results

The results of the analysis are displayed in the notebook itself, with various tables showing the computed and predicted run values for different players and events.
Future Work

The project can be extended by incorporating more data, using different machine learning models for prediction, and performing more detailed analysis on the data.
Contact

For any queries or suggestions, please feel free to reach out.

---

Note: This is a basic template for your README. You may want to add more sections like 'Contributing', 'License', etc., depending on your project's needs.