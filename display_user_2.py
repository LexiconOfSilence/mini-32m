def get_movie_title(desired_movie_id, movie_title_filename):
    infile = open( movie_title_filename)
    header = infile.readline()
    for line in infile:
        row = line.removesuffix("\n").split("\t")
        assert len(row) == 3
        movie_id = int(row[0])
        title = row[1]
        if desired_movie_id == movie_id:
            infile.close()
            return title
    infile.close()
    return None

def get_movie_title(desired_movie_id, movie_ids, movie_titles): 
    for i in range(len(movie_ids)): # allows us to iterate through the list 
        movie_id = movie_ids[i]
        if desired_movie_id == movie_id: 
            movie_title = movie_titles[i]
            return movie_title
    return None 


def get_movie_table(movie_tsv_filename):
    infile = open(movie_tsv_filename)
    header = infile.readline()
    movie_ids = []
    titles = []
    genres = []
    for line in infile:
        fields = line.removesuffix("\n").split("\t")
        assert len(fields) == 3
        movie_id = int(fields[0])
        movie_title = fields[1]
        movie_genres = fields[2]
        movie_ids.append(movie_id)
        titles.append(movie_title)
        genres.append(movie_genres)
    infile.close()
    return movie_ids, titles, genres

def main():
    # goal is to display ratings of user_id 81287 with movie titles
    desired_user_id = 81287
    ratings_file = open("ratings.tsv")
    header = ratings_file.readline()
    for line in ratings_file:
        row = line.removesuffix("\n").split("\t")
        assert len(row) == 4
        user_id = int(row[0])
        movie_id = int(row[1])
        rating = float(row[2])
        if user_id == desired_user_id:
            movie_title = get_movie_title(movie_id, movie_ids, movie_titles)
            assert not (movie_title is None)
            print(f"user_id = {user_id}, movie_id = {movie_id}, title = {movie_title}, rating = {rating}")

    ratings_file.close()

if __name__ == "__main__":
    main()