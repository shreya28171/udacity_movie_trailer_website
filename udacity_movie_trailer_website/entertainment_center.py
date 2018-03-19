import media
import fresh_tomatoes

""" Creating instances of class Movie to hold details of my favourite movies"""
in_time = media.Movie("In Time",
                      "A world where time has become the ultimate currency.",
                      "119 minutes",
                      "Justin Timberlake, Amanda Seyfried",
                      "https://goo.gl/WG2asf",
                      "https://www.youtube.com/watch?v=fdadZ_KrZVw")

arjun_reddy = media.Movie("Arjun Reddy",
                          "A troubled young surgeon begins to self-destruct.",
                          "182  minutes",
                          "Vijay Deverakonda, Shalini Pandey, Amit Sharma",
                          "https://goo.gl/66SV3G",
                          "https://youtu.be/JMU0KE-7FVI")

wonder_woman = media.Movie("Wonder woman",
                           "Princess Diana fought a war to end all the wars.",
                           "141 minutes",
                           "Gal Gadot, Chris Pine, Robin Wright",
                           "https://goo.gl/NVqc52",
                           "https://www.youtube.com/watch?v=5lGoQhFb4NM")

the_shape_of_water = media.Movie("The Shape of Water",
                                 "A lady forms a unique link with a creature.",
                                 "123 minutes",
                                 "Sally Hawkins, Michael Shannon",
                                 "https://goo.gl/vWxhzj",
                                 "https://www.youtube.com/watch?v=XFYWazblaUA")
gravity = media.Movie("Gravity",
                      "Two astronauts got stranded in space.",
                      "91 minutes",
                      "Sandra Bullock, George Clooney, Ed Harris ",
                      "https://goo.gl/CyCScX",
                      "https://youtu.be/OiTiKOy59o4")

titanic = media.Movie("Titanic",
                      "An unsinkable ship sinks when hits an iceberg.",
                      "194 minutes",
                      "Leonardo DiCaprio, Kate Winslet, Billy Zane",
                      "https://goo.gl/mctTJM",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

pink = media.Movie("Pink",
                   "A lawyer steps forward to help 3 women clear their crime.",
                   "136 minutes",
                   "Amitabh Bachchan, Tapsee, Kirti Kulhari, Andrea Tariang",
                   "https://goo.gl/6nkg3V",
                   "https://www.youtube.com/watch?v=AL2TShb6fFs")

coco = media.Movie("Coco",
                   "A boy enters the Land of the Dead.",
                   "105 minutes",
                   "Anthony Gonzalez, Gael García Bernal, Benjamin Bratt",
                   "https://goo.gl/W174Uw",
                   "https://www.youtube.com/watch?v=zNCz4mQzfEI")

jumanji = media.Movie("Jumanji: Welcome To The Jungle",
                      "Four teenagers are sucked into a magical video game.",
                      "119 minjutes",
                      "Dwayne Johnson, Karen Gillan, Kevin Hart",
                      "https://goo.gl/xsMLRF",
                      "https://www.youtube.com/watch?v=2QKg5SZ_35I")

# Add the instances to a list
movies = [
    in_time,
    arjun_reddy,
    wonder_woman,
    the_shape_of_water,
    gravity,
    titanic,
    pink,
    coco,
    jumanji
    ]

# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)
