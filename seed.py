import models

def seed():
    movie1 = models.Movie(
        title = "SCP: Overlord",
        description = "A secret NGO investigates the home of an esoteric cult on suspicion that they are more than meets the eye.  Directed by Stephen Hancock. Written by Evan Muir",
        movie_src = "https://youtube.com/embed/EOxarwd3eTs",
        movie_cover = "https://i.imgur.com/VoRt5NG.jpg",
        rating = 0
    )



    movie2 = models.Movie(
        title = "Dig Your Own Grave",
        description = "A man is forced to dig his own grave in the desert, but the ground is to hard.",
        movie_src = "https://youtube.com/embed/hrtf5AR5e-Y",
        movie_cover = "https://i.imgur.com/rNMZQGK.jpg",
        rating = 0
    )

    movie3 = models.Movie(
        title = "Feeling Through",
        description = "A homeless teen meets a deaf-blind man who changes his life forever...",
        movie_src = "https://youtube.com/embed/h1CqzntEZZ8",
        movie_cover = "https://i.imgur.com/VfDFr8J.jpg",
        rating = 0
    )

    movie4 = models.Movie(
        title = "The Narrow World",
        description = "A giant alien creature comes to Earth, But its reasons for arriving are unknown.",
        movie_src = "https://youtube.com/embed/o8bSNGy8vMw",
        movie_cover = "https://i.imgur.com/JkPyPJ0.jpg",
        rating = 0
    )

    movie5 = models.Movie(
        title = "1500 Words",
        description = "A man with 1500 words left to live, struggles to keep his marriage and himself alive.",
        movie_src = "https://youtube.com/embed/-waMtGtxAdg",
        movie_cover = "https://i.imgur.com/ZZ4ScWb.jpg",
        rating = 0
    )

    movie6 = models.Movie(
        title = "Darth Maul: Apprentice",
        description = "Star Wars: Fan-Film",
        movie_src = "https://youtube.com/embed/Djo_91jN3Pk",
        movie_cover = "https://i.imgur.com/zbj9n9M.jpg",
        rating = 0
    )

    movie7 = models.Movie(
        title = "Laazy Boy",
        description = "A man discovers his La-Z-Boy recliner is a 1-minute time machine.",
        movie_src = "https://youtube.com/embed/qHp7ngBVnQs",
        movie_cover = "https://i.imgur.com/JMgbxDH.jpg",
        rating = 0
    )

    movie8 = models.Movie(
        title = "Turning Tide",
        description = "A young boy encounters a downed German pilot after witnessing a large aerial battle.",
        movie_src = "https://youtube.com/embed/6eYOZNjUqp4",
        movie_cover = "https://i.imgur.com/UmcBfil.jpg",
        rating = 0
    )

    movie9 = models.Movie(
        title = "SCP: Dollhouse",
        description = "",
        movie_src = "https://youtube.com/embed/xVx2jyDPinw",
        movie_cover = "https://i.imgur.com/zZv8LwY.jpg",
        rating = 0
    )

    movie10 = models.Movie(
        title = "Holding",
        description = "A man calls a suicide hotline and gets put on hold. He finds his neighbor is on hold too.",
        movie_src = "https://youtube.com/embed/KLc3_MlCzIM",
        movie_cover = "https://i.imgur.com/sHeEHhX.jpg",
        rating = 0
    )

    movie11 = models.Movie(
        title = "The Scorpion's Tale",
        description = "A hitman on death row gets one last visit from his son.",
        movie_src ="https://youtube.com/embed/761IajDS8SM",
        movie_cover = "https://i.imgur.com/UhOmgL0.jpg",
        rating = 0
    )

    movie12 = models.Movie(
        title = '096 | SCP',
        description = 'SCP #096 escapes containment.',
        movie_src = 'https://youtube.com/embed/MEOZkf4imaM',
        movie_cover = 'https://i.imgur.com/OCTbEGP.jpg',
        rating = 0
    )

    movie13 = models.Movie(
        title = 'Astartes',
        description = 'Astartes parts 1-5',
        movie_src = 'https://youtube.com/embed/DVXEYksoE6c',
        movie_cover = 'https://i.imgur.com/v1uRw1s.jpg',
        rating = 0
    )

    movie14 = models.Movie(
        title = 'Spawn: The Recall',
        description = 'Spawn Fan-Film',
        movie_src = 'https://youtube.com/embed/f5tCbd4fgkw',
        movie_cover = 'https://i.imgur.com/vFAItb0.jpg',
        rating = 0
    )

    models.db.session.add(movie1)
    models.db.session.add(movie2)
    models.db.session.add(movie3)
    models.db.session.add(movie4)
    models.db.session.add(movie5)
    models.db.session.add(movie6)
    models.db.session.add(movie7)
    models.db.session.add(movie8)
    models.db.session.add(movie9)
    models.db.session.add(movie10)
    models.db.session.add(movie11)
    models.db.session.add(movie12)
    models.db.session.add(movie13)
    models.db.session.add(movie14)

    models.db.session.commit()
    print(models.Movie.query.filter_by(title='SCP: Overlord').first().to_json()['id'])
    movie_filter = models.Movie.query.filter_by

    tag1 = models.Tag(
        movie_id = models.Movie.query.filter_by(title='SCP: Overlord').first().to_json()['id'],
        genre = 'Thriller'
    )

    tag2 = models.Tag(
        movie_id = movie_filter(title='SCP: Overlord').first().to_json()['id'],
        genre = 'Action'
    )

    tag3 = models.Tag(
        movie_id = movie_filter(title='Dig Your Own Grave').first().to_json()['id'],
        genre = 'Comedy'
    )

    tag4 = models.Tag(
        movie_id = movie_filter(title='Feeling Through').first().to_json()['id'],
        genre = 'Drama'
    )

    tag5 = models.Tag(
        movie_id = movie_filter(title='Feeling Through').first().to_json()['id'],
        genre = 'Adventure'
    )

    models.db.session.add(tag1)
    models.db.session.add(tag2)
    models.db.session.add(tag3)
    models.db.session.add(tag4)
    models.db.session.add(tag5)



    models.db.session.commit()
