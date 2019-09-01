Analysis of log file:- 
=======================

Assessment Criteria:-
---------------------
In no specific order:
* If your solution satisfies the requirements
* How the code and functionality is tested
* The understandability and maintainability of your code
* The cleanliness of design and implementation
* Time performance on a standard laptop
* Answers to the discussion questions.

Tasks-1:- 
-------

1. For a given time period:- 
    1. Create histogram for errors
    1. 50,90 and 95 percentile of Response time of successful request.

#### Assumptions :- 

1. Have to perform analysis on a static file 1.log 
1. file is in same directory as code
1. Log file is small size (there is only one log file at a time), so  that pandas lib based analysis can be performed.
1. Analysis is done on static file not on steam of logs.

   
####Questions :- 

1. Briefly describe the conceptual approach you chose! What are the trade-offs?

Answer:- 
    
    1. User of generator (to reduce memory complexity)
    2. Reduce use of regex instead used tuple unpacking/packing feature with string split function - Regex
    has exponential order of time complexity.
    3. used pandas libraries to reduce coding time
    
    
1. What's the runtime performance? What is the complexity? Where are the bottlenecks?

Answer:- 

    1. Time performance depends on number of lines (n) and number of worlds per line (k). its O(nk).
    1. Memory/space performance is also )(nk)
     
1. If you had more time, what improvements would you make, and in what order of priority?

Answer:- 

The answers can vary based on what exactly are requirements.

    1. Currently, histogram and 50,90 and 95 percentile is being create using pandas.
    Since I am converting entire dataset to Pandas dataframe that is a memory inefficient. 
    I would convert only required columns to PandasSeries. I Would like to take a divide and
    conqure approach for large datasets probably writing my own generator functions to 
    calculate 50, 90 and 95 percentiles.
    1. Converting it to an API (CLI) so that everyone can use it.
    1. Assuming we want to do Analysis kind of things on static dataset, Handling of large 
    multiple files is one feature that I would like to add. Addition of Parallelism/AsyncIO to handle it.
    
    1. To perform such analysis on a DataLake, will approach to distributed system like
    Spark etc. ( pointers -> ETL systems)
    1. 
    

Tasks-2:- 
-------

1. A service or script to consume Stream from logfile, and verify  followings rules:- 
    1. Response time > 100ms for more than 5 seconds
    1. number of errors > 5 in a minute
 
#### Assumptions :-


1. Log stream is being written on one file 1.log
1. Log file is never being rotated/trucated
1. Logs are being appended in log file


#### Questions :- 


1. Briefly describe the conceptual approach you chose! What are the trade-offs?

1. What's the runtime performance? What is the complexity? Where are the bottlenecks?

1. If you had more time, what improvements would you make, and in what order of priority?  
