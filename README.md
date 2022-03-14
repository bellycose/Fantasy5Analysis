# Fantasy 5 Analysis
### Contact
|Name|Email|Github|Website|
|----|-----|------|-------|
Donald Cao|cao.donald89@gmail.com|[bellycose](https://github.com/bellycose "github")|

### Purpose
The purpose for this project is to extricate targeted data from API on CA-Lottery webstite into csv/xlxs file and by using Baysian Probability Statistics to develop a prediction of the next winning calls.

### Softwares
- Python 3.10.x
- Microsoft Excel 2019

### Dependencies
- Request 2.27
- Glom
- Pandas

---
### Program Process
1. Data extraction from API/XHR
2. Data wrangled with glom.
3. Data further cleaned and saved as csv and xlxs.
4. Statistic analysis, starting with descriptive and then exploratory analysis.
5. Guess future calls with probability and cross reference with frequency and positions.

---
### Note
This portfolio is a longitudinal study (on-going). As of 03/07/2022, only 202 calls were available to be acquired. By having low amount of sample size, "Winning Draws", only limited the use of predictive models. Therefore, the approach with exploratory analysis will be by simple predictive models for accuracy. Hence, the predictive model will be conditional probability for picking numbers and Bayes Theorem for validation. Valid is when the probability of the number matches with Bayes Theorem.
