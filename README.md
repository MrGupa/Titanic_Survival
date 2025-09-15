# Titanic Survival Prediction Project

This project aims to predict the survival of passengers on the Titanic using machine learning techniques. The model is trained using a Decision Tree Classifier and is deployed as a web application using Streamlit.

## Project Structure

- **Titanic_Survival.ipynb**: Jupyter notebook containing the complete code for data preprocessing, model training, and evaluation.
- **app.py**: Streamlit application that allows users to input their details and predict their survival on the Titanic.
- **deployment.pkl**: Serialized model and label encoders used for making predictions in the Streamlit app.
- **requirements.txt**: Lists all necessary Python packages required to run the project.
- **README.md**: Documentation for the project.

## Installation

To set up the project, clone the repository and navigate to the project directory. Then, install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

After installing the required packages, you can run the Streamlit application with the following command:

```
streamlit run app.py
```

This will start the application, and you can access it in your web browser.

## Usage

1. Select your class (Pclass) from the dropdown.
2. Choose your gender (Sex) from the dropdown.
3. Enter your age (Age).
4. Select your embarkation point (Embarked) from the dropdown.
5. Click on the "Survival Probability" button to see if you are predicted to survive.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.