# Initiation
   ## Installing required modules
  
    pip install -r requirements.txt
   
   ## Run the Main File, [ Binary Format ]
    .\StockAverage.cpython-310.pyc
    




# About Vega
Vega is a CopyTrading Program, which is really helpful when you needs to train yourself in StockMarket. In this you can do copy trading. Simply run this software in your system, and pin the program window one of the sides of your screen, and then you simply choose any of your favorate stock. And when your technical analysis says, its time to buy the stock, you simply have to put that particular stock current price to this program and then press 'enter'. And then it will ask for close price, where you feel its time to sell your stock, you type the price where you feel the share needs to be sold. And then it asks you more questions. Like how many indicators you used during this trade and the name of the stock and at the end it asks you, whether you want's to continue or exit. 

# Main Functionality

Here when, you type "c", it repeats the same process. And when you type "e", it exits. But it gives you output data, about total profit and loss and there averages.

It helps us, in condition, whether our progress in terms of trading, overall it guides us with data and graph that whether your trading is progressive or imprgrassive.

# Core Functionality

It shows us, different graphs, with each specific data with it's label and colors, to differenciate, our different kind of progress. It stores the data in MongoDB Database.


# Database

We have used here 2 - formats:

First one, MongoDB
And,
Second one, JSON Format. 

(Why JSON format. Answered below in "Data-Backups Section" , no worries, as your mind is damn itchy and curious to know about it.)

# Data Back-ups

We are using 3 kinds of functionality here.

@ First One: Storing in LocalMongoDB
@ Second One: Storing in MongoDB Cloud Server
@ Third One: Storing in JSON Files.


# The Intelligence of the Program
The Major Feature of this program is, it never steps back to loss your important trades data at all. It as Mentioned earlier, It stores Data in 3 Formats.

1) MongoDB in your Local Computer.
2) MongoDB in the Server.
3) In JSON Files.


# Data Intelligence

## When you run the Program, It checks with 3 Params which are, (InternetConnectionStatus, JSON, LocalMongoDB).
###### Where, InternetConnectionStatus checks if your Device is connected to Interent, So it store the Data on Cloud.
###### And in, JSON. Data is Stored in JSON, If Your Device is not connected to internet and also your LocalMachine, doesn't have installed Mongo Database in Local Machine.
###### And in LocalMongoDB, It stores data in LocalMongoDB, if Your Device is not Connected to Internet. 

Note: We are Storing Data in JSON Files, Because in the end Condition. If Your Device is Neither Connected to Internet nor you have Mongo DB Installed in your Computer. So You can store and retrive data.


# Graphs

## Main Functionality Which Helps User to Study their Trading Performance, Whether the User is Being Mastered and Progressing and Making Profits in Trading or Lossing at all.

It Shows Various Varities of Graph, Including 

1) Your Today's Profit, Your Today's Progress
2) Your Average Profit and Loss Today. 
3) Your Average Profit and Loss of All Time.
4) Your All time Number of Winnings and Loss in Trading, By calculating the 1 and -1 numbers. Which referes, 1 for Profit, and -1 for Loss.
5) Graph on Number of Indicators you Use During Trade.
6) It stores data on How many times you use which-which kind of Indicators.
7) It's Scalable, It can show you the Histograph, where you can check How much success you achieved by using specific trade. So you can work on you weak indicator knowledge to avoid next time trade loss. 

# I have Provided Apache 2.0 License. So Suggest if, more Functionalities can be added.
## I am Curious for your new suggestions, and Ideas Regarding Performance, adding more detailed graph, data handling and more...

# Contact Me at: 
## mailto: karmarahul67@gmail.com

# At the End, Self Destruction Mode
## In this Mode, If I Give My Server a Command, So never time if you run the StockAverage.py Program. It will be Self Destructed. (Also If Internet Connection is On! To get Command from My Server to the Program)

@Copyright 2022. All Rights Reserved to Rahul Vishwakarma. In Terms of Selling Promoting to Your Name or Company's Name or Neighbours Name.
