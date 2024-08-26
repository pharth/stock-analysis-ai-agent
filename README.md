
# Stock Analysis AI Agent



## Overview
This project is a Stock Analysis AI Agent that leverages multiple AI agents to perform comprehensive analysis of stock data, including technical analysis, sentiment analysis, and risk assessment. The app is built using Streamlit and integrates with OpenAI's GPT-3.5-turbo model.

## Features
Data Validation: Ensures correct company name, valid date ranges, and retrieves stock price data.
Technical Analysis: Analyzes stock data using technical indicators.
Sentiment Analysis: Analyzes documents and news articles to gauge public sentiment around the stock.
Risk Assessment: Provides detailed risk reports for short-term and long-term investments.
Investment Advice: Offers recommendations based on the comprehensive analysis.

## Tech Stack
Python
Streamlit: For the user interface.
OpenAI GPT-3.5-turbo: For managing and interacting with AI agents.
Serper API: For web scraping and Google Search.
Pandas: For data manipulation.
Custom AI Agents: Developed using crewai for specialized tasks.

## Installation
Clone the repository:

```bash
https://github.com/pharth/stock-analysis-ai-agent
cd stock-analysis-ai-agent
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```
Set up your environment variables:

OPENAI_API_KEY: Your OpenAI API key.
SERPER_API_KEY: Your Serper API key.


Run the Streamlit app:

```bash
streamlit run app.py
```
Enter your OpenAI and Serper API keys in the sidebar.

Provide the company name, start date, and end date.

Click on "Analyze" to get a detailed stock analysis.
