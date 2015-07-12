import fresh_tomatoes
import media

#enter your movies data to movie class
toy_story = media.Movie("Toy Story",
                        "1995",
                        "81",
                        "tt0114709",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "2009",
                     "162",
                     "tt0499549",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

mad_max_fr = media.Movie("Mad Max Fury Road",
                         "2015",
                         "120",
                         "tt1392190",
                         "The great return of Mad Max",
                         "https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
                         "https://www.youtube.com/watch?v=vjBb4SZ0F6Q")
                     
prisoners = media.Movie("Prisoners",
                        "2013",
                        "153",
                        "tt1392214",
                        "Desperate parents want to retrieve their daughters",
                        "https://upload.wikimedia.org/wikipedia/en/6/63/Prisoners2013Poster.jpg",
                        "https://www.youtube.com/watch?v=bpXfcTF6iVk")

there_will_be_blood = media.Movie("There will be blood",
                                  "2007",
                                  "158",
                                  "tt0469494",
                                  "The birth of a petrol magnate",
                                  "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg",
                                  "https://www.youtube.com/watch?v=FeSLPELpMeM")


#create collection of movies
movies = [toy_story, avatar, mad_max_fr, prisoners, there_will_be_blood]

#sort by alphabetical order
movies.sort()

fresh_tomatoes.open_movies_page(movies)