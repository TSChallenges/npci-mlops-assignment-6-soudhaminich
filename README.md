# Assignment-6
## CI/CD Pipeline for Bank Marketing Data using GitHub Actions

##  Project Overview  
This project implements a **CI/CD pipeline using GitHub Actions** to process **bank marketing data** and train a machine learning model to predict if the client will subscribe a term deposit (variable y).

The pipeline includes:  
- **Data Preprocessing**: Cleaning & transforming raw data.  
- **Model Training**: Training a classification model.  
- **Automated Testing**: Using `pytest` for test cases.  
- **CI/CD Integration**: Automating workflow using GitHub Actions.  

### Dataset Descrption
The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.

#### Column Description:
- age - Age of the client
- job - Job type or profession of the client
- marital - Marital status of the client
- education - Education level of the client
- balance - Average yearly balance in euros
- default - Indicates if the client has credit in default (yes/no)
- housing - Indicates if the client has a housing loan (yes/no)
- loan - Indicates if the client has a personal loan (yes/no)
- day - Last contact day of the month
- month - Last contact month
- duration - Duration of the last contact in seconds
- campaign - Number of contacts performed during this campaign for this client
- pdays - Number of days since the client was last contacted (or -1 if not previously contacted)
- previous - Number of contacts performed before this campaign
- y Target variable: Whether the client subscribed to the product (yes=1, no=0)

---
 
## Assignment Tasks

**1. Understanding the given files**

You are provided with the following:
* **Dataset (`data/bank_marketing.csv`)**: Required for preprocessing and model training.
* **Preprocessing script (`preprocessing.py`)**: Cleans and prepares the data.
* **Model training script (`train_model.py`)**: Trains and saves a machine learning model.
* **Test scripts (`tests/test_pipeline.py`)**: Validates the preprocessing and model performance.

**2. Setting Up the CI/CD Pipeline**

You need to create a GitHub Actions workflow to automate the ML pipeline when code is pushed to the main branch or a pull request is made.

**Steps to Include in ml_pipeline.yml**
* Trigger the Workflow: Run the pipeline on push and pull requests to the main branch.
* Set Up the Environment: Use Ubuntu-latest as the runner.
* Setup Python 3.8 and install required dependencies (pandas, numpy, scikit-learn, pytest).
* **Run Preprocessing**: Execute `preprocessing.py` to clean and transform the dataset.
* **Train the Model**: Run `train_model.py` to train and save the model.
* **Run Test Cases**: Use `pytest` to verify correctness.

**3. Implementing the Workflow**

You need to define the `ml_pipeline.yml` file in the `.github/workflows/` directory, ensuring it includes:

* Checking out the repository
* Setting up python
* Installing dependencies
* Running preprocessing and model training
* Executing tests

---

## Submission Guidelines
After completing the assignment and developing the solution code in your system, commit and push the changes to this repository. 
  - Stage your changes and commit the files:
    ```
    git add .
    git commit -m "Completed playground challenge"
    ```
  - Push your changes to the GitHub repository:
    ```
    git push
    ```

Good luck, and happy coding!
