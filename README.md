# time-bandits
Learn To Think Like A Computer Scientist.

World Wide Technology's Network Solutions Team meeting is in August 2017 and is attended by network engineers from Sales, Business Development, IT and Professional Services.

My presentation (18 minute TED talk format) is titled, _Learn To Think Like A Computer Scientist_, the goal is to introduce network engineers to the development of algorithms necessary to effectively interface with a device API. The slide deck is available on Slideshare [learn-to-think-like-a-computer-scientist](https://www.slideshare.net/joelwking/learn-to-think-like-a-computer-scientist). 

To demonstrate a real-world use case, we have the following requirement.

## Programming exercise
The security operations center (SOC) wishes to query Tetration for flows between two points in time spanning several months. The times are represented in iso8601 format, "2017-05-27T09:00:00-0700". Tetration API can query based either  iso8601 or epoch time in the API call. However, Tetration only allows querying maximum time range of 1 day per request. If a user wants to query a longer time range, they need to split that time range into 1 day time periods and query separately for each period.
 
Write an algorithm which accepts a start and end time in iso8601 format, e.g. "2017-03-27T09:00:00-0700" to "2017-05-27T09:00:00-0700" and outputs a list of start/stop times which comprise the entire timeframe specified by the SOC, but does not exceed the 1 day limitation imposed by the API.

## Outcome
I am soliciting solutions to this problem in various programming languages. Thanks for those who contributed.
