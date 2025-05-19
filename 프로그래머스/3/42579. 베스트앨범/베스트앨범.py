def solution(genres, plays):
    genre_songs = {}
    genre_plays = {}
    
    for idx in range(len(genres)):
        genre = genres[idx]
        play = plays[idx]
        
        #노래 목록 저장
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, idx))
        
        #재생 수 저장
        if genre not in genre_plays:
            genre_plays[genre] = 0
        genre_plays[genre] += play
        
        
    sorted_genres = sorted(genre_plays, key = lambda g: genre_plays[g], reverse = True)
    
    answer = []
    
    for genre in sorted_genres:
        songs = sorted(genre_songs[genre], key = lambda x: (-x[0], x[1]))
        
        for song in songs[:2]:
            answer.append(song[1])
    
    return answer