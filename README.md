# Twitter Sentiment Analysis for Brand Recognition

## Inspiration
The solution for evaluating Twitter data to perform better business decisions is to keep tracking all relevant Twitter content about a brand in real-time and perform analysis as topics or issues emerge. By monitoring brand mentions on Twitter, brands could inform enagement and deliver better experiences for their customers across the world.

## Technical Approach
1. Extracting streaming Twitter Data
2. Preprocessing data and storing in MySQL
3. Perform data analysis to explore the insights (In Progress)
4. Connect with real-time Plotly|Dash for data visualization based on time series (In Progress)
5. Publish the visualization on github.io (In Progress)

## Second Version ( ~ Aug 20)
Build ETL pipelines based on stream processing using Kafka, and fully automate ETL using automated data management

## Get Started
### Pre-installation
```
pip install -r requirements.txt
```
### Set-up
Create a file called ```credentials.py``` and fill the context in below
```
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you
API_KEY = "XXXXXXXXXXXXXX"
API_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
ACCESS_TOEKN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

### Run
Run ```Main.ipynb``` to start scraping data on Jupter Notebook. (Note: Because it extracts streaming data from Twitter, you need to manually press STOP button to stop the streaming process.)
Run ```Analysis.ipynb``` to perform data analysis and visualization
