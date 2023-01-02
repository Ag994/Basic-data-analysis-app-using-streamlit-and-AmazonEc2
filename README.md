# Welcome to my Data Analysis App!

This app is designed to allow users to input and analyze data sets. It is currently deployed on an Amazon Web Services (AWS) Elastic Compute Cloud (EC2) instance.

To use the app, simply follow the prompts on the homepage to upload your data set. The app will then provide various analysis options, including visualizations and statistical analysis.

Please note that this app is still in development and may have bugs or issues. If you encounter any problems, please feel free to open an issue on the GitHub repository for this project.

## Getting Started
   To use this app, follow these steps:
   
   1. Make sure you have Python and pip installed on your machine. You can check if you have these installed by 
   running the following commands in your terminal:
   
   
   ```python
   python --version
   pip --version
   ```
   
   If you do not have Python or `pip` installed, you can install them by following the instructions [here](https://realpython.com/installing-python/)
   
   2. Clone this repository and navigate to the root directory of the project.
   
   
   ```python
   git clone https://github.com/Ag994/tweets-analysis-app.git
   cd tweet-analysis-app
   ```
   
   3. Install the required dependencies.
   

   ```python
   pip install -r requirements.txt
   ```
   
   This will install the `nltk` and `streamlit` libraries, which are needed to run the app.
   
   4. Launch the app by running the following command from the root directory of the project:
   
   
   ```python
   streamlit run app.py
   ```
   
   This will open the app in your default web browser. From there, you can enter a Twitter handle and click the "Analyze" button to see the sentiment analysis of the user's recent tweets.
   
   ## Sentiment Analysis
   
   The sentiment analysis is performed using NLTK's built-in sentiment analysis tool. It assigns a polarity score is a value between -1 (very negative) and 1 (very positive), and the subjectivity score is a value between 0 (very objective) and 1 (very subjective). to each tweet based on the words used, with positive words increasing the polarity score and negative words decreasing it.
   
   
   ## Future Work
   
   There are many ways that this app could be improved and expanded upon. Some ideas for future work include:
   
   * Adding more advanced sentiment analysis techniques, such as using machine learning models to classify tweets.
   * Adding additional analysis options, such as word frequency or topic modeling.
   * Implementing user authentication and the ability to save and compare analyses for different users.
   


Thank you for using my Data Analysis App!

































http://3.82.155.40:8501/
