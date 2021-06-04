# Excellence Technosoft Pvt. Ltd.
## Interview test questions

#### Question 4(a)

In this folder I have created a `flask` api with five endpoints
    -`/add_candidate`
    -`/candidate`
    -`/add_score`
    -`/highest_score`
    -`/average`

**/add_candidate** type `post`
expect json schema 
```
{
    "name":"Candidate Name",
    "email":"Candidate@Email.com"
}
```

**/candidate** type `get`
expect `query parameter` `email = candidate@email.com`

**/add_score** type `post`
expect json schema 
```
{
    "candidate_id": 4,
    "tests": {
        "test_1":{
            "name": "first_round",
            "score": int
        },
        "test_2":{
            "name": "second_round",
            "score": int
        },
        "test_3":{
            "name": "third_round",
            "score": int
        }
    }
}
```

**/highest_score** type `get`
return highest scoring candidate with total marks

**/average** type `get`
return average score of all candidate
