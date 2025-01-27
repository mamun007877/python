# Date and Time
- Python is having built in modules that are related to date and time they are datetime, time and calendar
## datetime module
- This module contains classes like datetime ,date , time , time delta , tzip

- datetime - d / m / y , hours : minutes : seconds : millisecond
    - it also gives timezone

- date - date / month / year

- time - hours : minutes : seconds : millisecond

- timedelta - difference between 2 times , d2 - d1 it also gives day , hour, minutes ,second

- tzone. - IST ,GMT

- If you want know the current date and time we have many functions for that

- The starting point for time for any watch is taken as 1 jan 1970, this is also known as epoch time .

- The time.time( ) will give you the time elapsed from epoch time

        import time
        time.time()//1647342625.926307


- The time.localtime( ) will give you all the values of current date and time including year , month , monthly , weekday etc.

- "lt" is variable for local time , type of lt is structured time , you can also get the particular data of your choice like year , day and hour etc…

- Some other function to know current date and time are
    - time.ctime( ) - string form of current date and time
    
    - time.now( ) - will give object of date and time only

    - time.today( ) - same as now( )

## Create date object and time object
### datetime
- datetime class
- date class
- time class
#### datetime
- For this we have to import the datetime module , it contains both date and time object
    
- We have taken example as dt1 and dt2 we can also give keyword argument so we don’t have to give time in ordered form

- In this we can subtract dt2-dt1 , we can also find which is greater( > ) and lesser (<) between dt1 and dt2 it will return it in boolean form
#### date and time :
- A date object represents a date (year, month and day).

- A time object instantiated from the time class represents the local time.

- We can subtract dat2-dat1 but not tim2-tim1

- We can find both greater and less than for both date and time

- By using this classes we can create specific date and time
