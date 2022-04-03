n = int(input())
movie_count = 0
for i in range(n):
    while '666' not in str(movie_count):
        movie_count += 1
    movie_count += 1
print(movie_count-1)