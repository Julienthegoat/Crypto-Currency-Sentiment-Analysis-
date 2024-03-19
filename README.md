# Cryptocurrency Sentiment Analysis

This project utilizes Streamlit to create a web application that analyzes the sentiment of cryptocurrency-related posts on Reddit. By leveraging the CryptoBERT model, the app can determine whether the overall sentiment of a post is bullish, neutral, or bearish. This tool can be invaluable for traders, investors, and cryptocurrency enthusiasts who want to gauge market sentiment and make informed decisions.

## Features

- **Search by Token**: Allows users to enter a cryptocurrency symbol (e.g., $BTC, $ETH, $ADA) to fetch and analyze sentiment from relevant Reddit posts.
- **Search by SubReddit**: Users can specify a subreddit and optionally filter by a keyword to analyze sentiment in posts.
- **Global Trends**: Offers an overview of the global sentiment towards cryptocurrencies based on the latest posts from selected subreddits.

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Transformers (Hugging Face)
- PRAW (Python Reddit API Wrapper)

## Setup and Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all necessary Python packages including Streamlit, Pandas, Matplotlib, Transformers, and PRAW.

3. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

    Replace `app.py` with the name of your main Python script.



## How to Use
Use the sidebar to navigate through the app and select from various analysis options. Input the necessary details according to your chosen option and click the "Analyze Sentiment" button to get the analysis results.

## Contribution
Avalanche 🔺 Adress for Contributiuons : 
````bash
0xe5d5D0078E3a5afE22727F9c16dc545Ae3CA0046
````

## License
This project is made available under the MIT License.

Acknowledgements
Our project leverages CryptoBERT, a specialized NLP model for analyzing cryptocurrency sentiment, created by ElKulako. For more information, see: ElKulako (2022), "CryptoBERT: A Pre-trained NLP Model for Cryptocurrency Sentiment Analysis," available on IEEE Xplore.

Disclaimer
This software is provided for informational purposes only and should not be used as financial advice.
