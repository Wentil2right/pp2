def im_5(movie1):
    return movie1["imdb"]>5

movie1= {
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
}


result = im_5(movie1)
print(result)