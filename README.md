# coronavisiion map project
The idea for this project is to have users submit there own data to track the coronavirus.
Users are able to indicate their condition and the locations they have been and when. This 
way, it would be possible to identify spots where many people overlapped and warn others 
who may have been in that area.

## structure 
The project was built using AWS and openmaps. We stored user data via dynamoDB. We then 
used the stream functionality of dynamoDB and a lambda to trigger an aws firehose that used
glue crawlers/table to format the data into parquet form for analysis. I worked primarily on 
setting up the dynamoDB stream->lambda->firehose->s3 +glue crawler. (and the scripts in here)
                             
                              
## assuming the website is live still 
http://static-website-covid19.s3-website-us-east-1.amazonaws.com
This was part of the devpost pandemic response hackathon. Our submission can be found here:
https://devpost.com/software/predicting-covid19-map
