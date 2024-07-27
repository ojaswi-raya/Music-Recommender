from flask import Flask, request, jsonify, render_template, url_for
import random

app = Flask(__name__)

recommendations = {
    "pop": [
        "Blinding Lights - The Weeknd", "Watermelon Sugar - Harry Styles",
        "Levitating - Dua Lipa", "Save Your Tears - The Weeknd",
        "Good 4 U - Olivia Rodrigo", "Positions - Ariana Grande",
        "drivers license - Olivia Rodrigo", "Peaches - Justin Bieber",
        "Montero (Call Me By Your Name) - Lil Nas X", "Kiss Me More - Doja Cat",
        "Stay - The Kid LAROI, Justin Bieber", "Heat Waves - Glass Animals",
        "deja vu - Olivia Rodrigo", "Shivers - Ed Sheeran",
        "Easy On Me - Adele", "bad guy - Billie Eilish",
        "Don't Start Now - Dua Lipa", "Senorita - Shawn Mendes, Camila Cabello",
        "Circles - Post Malone", "Say So - Doja Cat",
        "Memories - Maroon 5", "Someone You Loved - Lewis Capaldi",
        "Break My Heart - Dua Lipa", "Good As Hell - Lizzo",
        "Stuck With U - Ariana Grande, Justin Bieber", "Adore You - Harry Styles",
        "Willow - Taylor Swift", "Holy - Justin Bieber",
        "Mood - 24kGoldn ft. Iann Dior", "Therefore I Am - Billie Eilish",
        "Savage Love - Jawsh 685, Jason Derulo", "Butter - BTS",
        "Life Goes On - BTS", "Lonely - Justin Bieber, Benny Blanco",
        "Dynamite - BTS", "Intentions - Justin Bieber, Quavo",
        "Kings & Queens - Ava Max", "Blinding Lights - The Weeknd",
        "Heartbreak Anniversary - Giveon", "Peach - Justin Bieber",
        "Levitating (Remix) - Dua Lipa ft. DaBaby", "deja vu - Olivia Rodrigo",
        "Before You Go - Lewis Capaldi", "WAP - Cardi B ft. Megan Thee Stallion",
        "You Right - Doja Cat, The Weeknd", "Industry Baby - Lil Nas X, Jack Harlow",
        "Woman - Doja Cat", "Take My Breath - The Weeknd",
        "Ghost - Justin Bieber", "Love Again - Dua Lipa",
        "Happier Than Ever - Billie Eilish", "Brutal - Olivia Rodrigo",
        "Good Without - Mimi Webb", "Good Things Fall Apart - ILLENIUM, Jon Bellion",
        "Lost Cause - Billie Eilish", "Beautiful Mistakes - Maroon 5, Megan Thee Stallion",
        "Build a B*tch - Bella Poarch", "Your Power - Billie Eilish",
        "Leave the Door Open - Silk Sonic", "Favorite Crime - Olivia Rodrigo",
        "Best Friend - Saweetie ft. Doja Cat", "My Ex's Best Friend - Machine Gun Kelly, Blackbear",
        "Talking to Yourself - Carly Rae Jepsen", "Kiss My (Uh Oh) - Anne-Marie, Little Mix",
        "No Tears Left To Cry - Ariana Grande", "Electric - Katy Perry",
        "Cardigan - Taylor Swift", "Willow - Taylor Swift",
        "De Una Vez - Selena Gomez", "Boyfriend - Ariana Grande, Social House",
        "Lover - Taylor Swift", "Daisies - Katy Perry",
        "Good Time - Carly Rae Jepsen, Owl City", "Without You - The Kid LAROI",
        "Be Kind - Marshmello, Halsey", "Over Now - Calvin Harris, The Weeknd",
        "In Your Eyes - The Weeknd", "Wonder - Shawn Mendes",
        "Treat People With Kindness - Harry Styles", "Holy - Justin Bieber",
        "Anyone - Justin Bieber", "No Time To Die - Billie Eilish",
        "Bad Habits - Ed Sheeran", "Visiting Hours - Ed Sheeran",
        "Love Not War (The Tampa Beat) - Jason Derulo x Nuka",
        "Monsters - All Time Low ft. Demi Lovato, Blackbear",
        "What Other People Say - Sam Fischer, Demi Lovato",
        "Telepatía - Kali Uchis", "You - Regard, Troye Sivan, Tate McRae",
        "Afterglow - Ed Sheeran", "At My Worst - Pink Sweat$",
        "Hold On - Justin Bieber", "Girl Like Me - Black Eyed Peas, Shakira",
        "Save Your Tears (Remix) - The Weeknd ft. Ariana Grande",
        "Don't Go Yet - Camila Cabello", "My Head & My Heart - Ava Max",
        "Boys - Lizzo ft. DaBaby", "Smile - Katy Perry",
        "Take You Dancing - Jason Derulo", "Rare - Selena Gomez"
    ],
    "rock": [
        "Bohemian Rhapsody - Queen", "Stairway to Heaven - Led Zeppelin",
        "Hotel California - Eagles", "Sweet Child O' Mine - Guns N' Roses",
        "Back In Black - AC/DC", "Livin' On A Prayer - Bon Jovi",
        "Smells Like Teen Spirit - Nirvana", "Paint It Black - The Rolling Stones",
        "Dream On - Aerosmith", "We Will Rock You - Queen",
        "Enter Sandman - Metallica", "Don't Stop Believin' - Journey",
        "Paradise City - Guns N' Roses", "Highway to Hell - AC/DC",
        "Under Pressure - Queen & David Bowie", "Wonderwall - Oasis",
        "November Rain - Guns N' Roses", "Kashmir - Led Zeppelin",
        "Sweet Emotion - Aerosmith", "Jump - Van Halen",
        "Back for Good - Take That", "You Really Got Me - The Kinks",
        "The Final Countdown - Europe", "Thunderstruck - AC/DC",
        "More Than a Feeling - Boston", "Zombie - The Cranberries",
        "The Middle - Jimmy Eat World", "I Love Rock 'N' Roll - Joan Jett",
        "Black Hole Sun - Soundgarden", "Smells Like Teen Spirit - Nirvana",
        "Creep - Radiohead", "Numb - Linkin Park", "In The End - Linkin Park",
        "Killing In The Name - Rage Against The Machine", "One - Metallica",
        "New Year's Day - U2", "Boulevard of Broken Dreams - Green Day",
        "Basket Case - Green Day", "Ironic - Alanis Morissette",
        "You Oughta Know - Alanis Morissette", "Alive - Pearl Jam",
        "Jeremy - Pearl Jam", "Rooster - Alice In Chains", "Man In The Box - Alice In Chains",
        "Plush - Stone Temple Pilots", "Interstate Love Song - Stone Temple Pilots",
        "Are You Gonna Go My Way - Lenny Kravitz", "American Idiot - Green Day",
        "Everlong - Foo Fighters", "Learn To Fly - Foo Fighters",
        "The Pretender - Foo Fighters", "Radioactive - Imagine Dragons",
        "Demons - Imagine Dragons", "Counting Stars - OneRepublic",
        "Ride - Twenty One Pilots", "Heathens - Twenty One Pilots",
        "Believer - Imagine Dragons", "Sex On Fire - Kings Of Leon",
        "Use Somebody - Kings Of Leon", "Toxicity - System Of A Down",
        "Chop Suey! - System Of A Down", "Take Me Out - Franz Ferdinand",
        "I Bet You Look Good On The Dancefloor - Arctic Monkeys",
        "Do I Wanna Know? - Arctic Monkeys", "R U Mine? - Arctic Monkeys",
        "No One Knows - Queens Of The Stone Age", "Go With The Flow - Queens Of The Stone Age",
        "Aerials - System Of A Down", "My Own Worst Enemy - Lit",
        "Jumper - Third Eye Blind", "Semi-Charmed Life - Third Eye Blind",
        "Hard To Handle - The Black Crowes", "She Talks To Angels - The Black Crowes",
        "All The Small Things - Blink-182", "What's My Age Again? - Blink-182",
        "Miss You - Blink-182", "The Anthem - Good Charlotte",
        "Lifestyles Of The Rich & Famous - Good Charlotte",
        "I Write Sings Not Tragedies - Panic! At The Disco",
        "I Write Sings Not Tragedies - Panic! At The Disco",
        "Welcome To The Black Parade - My Chemical Romance", "Helena - My Chemical Romance",
        "I'm Not Okay (I Promise) - My Chemical Romance", "Teenagers - My Chemical Romance",
        "Sugar, We're Goin Down - Fall Out Boy", "Dance, Dance - Fall Out Boy",
        "Thnks fr th Mmrs - Fall Out Boy", "I Believe In A Thing Called Love - The Darkness",
        "Wonderful Tonight - Eric Clapton", "Layla - Derek And The Dominos",
        "Wonderful Tonight - Eric Clapton", "Sunshine Of Your Love - Cream",
        "White Room - Cream", "Crossroads - Cream", "Badge - Cream"
    ],
    "hiphop": [
        "Sicko Mode - Travis Scott", "God's Plan - Drake", 
        "Rockstar - Post Malone", "HUMBLE. - Kendrick Lamar",
        "Old Town Road - Lil Nas X", "Bad and Boujee - Migos", 
        "Sicko Mode - Travis Scott", "I Like It - Cardi B", 
        "Mo Bamba - Sheck Wes", "Money Trees - Kendrick Lamar",
        "Mask Off - Future", "Lucid Dreams - Juice WRLD", 
        "The Box - Roddy Ricch", "Life Goes On - BTS",
        "Savage Remix - Megan Thee Stallion", "WAP - Cardi B feat. Megan Thee Stallion",
        "Sunflower - Post Malone & Swae Lee", "Hotline Bling - Drake", 
        "HUMBLE. - Kendrick Lamar", "In My Feelings - Drake", 
        "Nonstop - Drake", "All The Stars - Kendrick Lamar", 
        "Bodak Yellow - Cardi B", "Trap Queen - Fetty Wap", 
        "Bad Guy - Billie Eilish", "Roses - SAINt JHN", 
        "What's Poppin - Jack Harlow", "For The Night - Pop Smoke",
        "Gonna Love Me - Teyana Taylor", "Stir Fry - Migos", 
        "Suge - DaBaby", "No Role Modelz - J. Cole", 
        "Goosebumps - Travis Scott", "Pick Up The Phone - Young Thug & Travis Scott",
        "Gummo - 6ix9ine", "Antidote - Travis Scott", 
        "Broccoli - DRAM feat. Lil Yachty", "Congratulations - Post Malone", 
        "Bank Account - 21 Savage", "Butterfly Effect - Travis Scott",
        "Black Beatles - Rae Sremmurd", "Lean On - Major Lazer & DJ Snake",
        "Pick It Up - Famous Dex", "Lemonade - Internet Money & Gunna",
        "Dior - Pop Smoke", "Racks In The Middle - Nipsey Hussle",
        "Sucker For Pain - Lil Wayne, Wiz Khalifa, Imagine Dragons",
        "Panda - Desiigner", "Rockstar - Post Malone", "XO TOUR Llif3 - Lil Uzi Vert",
        "Uptown Funk - Mark Ronson feat. Bruno Mars", "HUMBLE. - Kendrick Lamar",
        "Mosh Pit - Juice WRLD", "Migos - Narcos", 
        "Energy - Drake", "Sicko Mode - Travis Scott", "Money Longer - Lil Uzi Vert",
        "Numb - XXXTentacion", "Butterfly Effect - Travis Scott", 
        "Lose Control - Meduza, Becky Hill, Goodboys", "Mask Off - Future",
        "Slide - Calvin Harris", "Going Bad - Meek Mill feat. Drake",
        "The Middle - Zedd, Maren Morris, Grey", "Shallow - Lady Gaga, Bradley Cooper",
        "Wake Me Up - Avicii", "Never Forget You - Zara Larsson",
        "New Rules - Dua Lipa", "God Is A Woman - Ariana Grande",
        "Havana - Camila Cabello", "Nonstop - Drake", "I Like It - Cardi B",
        "Lucid Dreams - Juice WRLD", "Racks - Yung Bans",
        "Dior - Pop Smoke", "On The Regular - The Old G",
        "Hotel Room Service - Pitbull", "Dynamite - BTS"
    ],
    "edm": [
        "Wake Me Up - Avicii", "Titanium - David Guetta feat. Sia", 
        "Closer - The Chainsmokers feat. Halsey", "Lean On - Major Lazer & DJ Snake",
        "Don't You Worry Child - Swedish House Mafia", "Turn Down for What - DJ Snake & Lil Jon",
        "Animals - Martin Garrix", "Levels - Avicii", "Starboy - The Weeknd", 
        "Strobe - Deadmau5", "Wake Me Up - Avicii", "Uptown Funk - Mark Ronson feat. Bruno Mars",
        "Party Rock Anthem - LMFAO", "Scream & Shout - will.i.am feat. Britney Spears", 
        "Shut Up & Dance - WALK THE MOON", "Firestone - Kygo feat. Conrad Sewell",
        "Gold Skies - Zedd feat. Aleesia", "Summer - Calvin Harris", "I Could Be The One - Avicii vs Nicky Romero",
        "Despacito (Remix) - Luis Fonsi, Daddy Yankee feat. Justin Bieber", "Go! - The Chemical Brothers",
        "All We Know - The Chainsmokers feat. Phoebe Ryan", "Be Right There - Jax Jones & MNEK", 
        "Roses - SAINt JHN", "Rise - Jonas Blue feat. Jack & Jack", "You Don't Know Me - Jax Jones feat. RAYE", 
        "Happier - Marshmello feat. Bastille", "Bury Me - Don Diablo", "Piece Of Your Heart - Meduza feat. Goodboys",
        "Lose Control - Meduza, Becky Hill & Goodboys", "No Tears Left To Cry - Ariana Grande", 
        "Dusk Till Dawn - Zayn feat. Sia", "Don't Let Me Down - The Chainsmokers feat. Daya",
        "Cold Water - Major Lazer feat. Justin Bieber", "Something Just Like This - The Chainsmokers & Coldplay",
        "This Is What You Came For - Calvin Harris feat. Rihanna", "Hymn For The Weekend - Coldplay",
        "Stay - Zedd & Alessia Cara", "Solo - Clean Bandit feat. Demi Lovato", "New Rules - Dua Lipa",
        "In My Mind - Ivan Gough & Feenixpawl", "Intoxicated - Martin Solveig & GTA", 
        "Lush Life - Zara Larsson", "Shivers - Ed Sheeran", "Havana - Camila Cabello",
        "The Middle - Zedd, Maren Morris & Grey", "No Money - Galantis", "I Like Me Better - Lauv",
        "Rockabye - Clean Bandit feat. Sean Paul & Anne-Marie", "Let Me Love You - DJ Snake feat. Justin Bieber",
        "Waiting For Love - Avicii", "Faded - Alan Walker", "Hey Mama - David Guetta feat. Nicki Minaj",
        "Sweet Lovin' - Sigala", "Beautiful Now - Zedd", "Fireball - Pitbull feat. John Ryan",
        "Memories - David Guetta feat. Kid Cudi", "Don't Let Me Down - The Chainsmokers feat. Daya",
        "Party Rock Anthem - LMFAO", "One Kiss - Calvin Harris & Dua Lipa", "Bad Guy - Billie Eilish",
        "Dance Monkey - Tones and I", "Old Town Road - Lil Nas X", "Everything I Wanted - Billie Eilish",
        "Starlight - The Supermen Lovers", "I Wanna Know - Alesso feat. Nico & Vinz", 
        "High Hopes - Panic! At The Disco", "Scared to Be Lonely - Martin Garrix & Dua Lipa",
        "Attention - Charlie Puth", "Rockstar - Post Malone feat. 21 Savage", "No Tears Left To Cry - Ariana Grande",
        "Only Want You - Rita Ora", "Giant - Calvin Harris & Rag'n'Bone Man"
    ],
    "country": [
        "The Dance - Garth Brooks", "Tennessee Whiskey - Chris Stapleton", 
        "Take Me Home, Country Roads - John Denver", "Jolene - Dolly Parton",
        "Ring of Fire - Johnny Cash", "Friends in Low Places - Garth Brooks", 
        "Before He Cheats - Carrie Underwood", "Wagon Wheel - Darius Rucker", 
        "Your Man - Josh Turner", "Where the Green Grass Grows - Tim McGraw", 
        "Coal Miner's Daughter - Loretta Lynn", "I Walk the Line - Johnny Cash", 
        "Live Like You Were Dying - Tim McGraw", "The Gambler - Kenny Rogers", 
        "Need You Now - Lady A", "Die a Happy Man - Thomas Rhett", "Blue Ain't Your Color - Keith Urban", 
        "Girl Crush - Little Big Town", "Chicken Fried - Zac Brown Band", 
        "Dirt Road Anthem - Jason Aldean", "Highway Don't Care - Tim McGraw feat. Taylor Swift", 
        "Kiss an Angel Good Mornin' - Charley Pride", "God's Country - Blake Shelton", 
        "House Party - Sam Hunt", "Humble and Kind - Tim McGraw", "Sand in My Boots - Morgan Wallen",
        "Good Vibes - Chris Janson", "Single Man's Party - Blake Shelton", 
        "The Only Way I Know - Jason Aldean, Luke Bryan & Eric Church", 
        "Big Green Tractor - Jason Aldean", "Some Beach - Blake Shelton", 
        "Fast Car - Tracy Chapman", "I Hold On - Dierks Bentley", 
        "Drink a Beer - Luke Bryan", "My Front Porch Looking In - Lonestar", 
        "I Love This Life - LOCASH", "Riser - Dierks Bentley", "Wagon Wheel - Old Crow Medicine Show",
        "Bless the Child - Keith Urban", "American Honey - Lady A", "Blue Bayou - Linda Ronstadt", 
        "Boys 'Round Here - Blake Shelton", "Living in Fast Forward - Kenny Chesney",
        "More Than a Memory - Garth Brooks", "Just a Kiss - Lady A", "Fastest Girl in Town - Miranda Lambert",
        "Holes in the Floor of Heaven - Steve Wariner", "Cuz I Like It - Rachelle Ann Go",
        "Whiskey Lullaby - Brad Paisley & Alison Krauss", "T-shirt - Thomas Rhett", 
        "She Got the Best of Me - Luke Combs", "I Don't Want This Night to End - Luke Bryan",
        "I’m Comin’ Over - Chris Young", "This Is Country Music - Brad Paisley", 
        "Every Little Thing - Carly Pearce", "Riot - The Band Perry", 
        "Shallow - Lady Gaga & Bradley Cooper", "In Case You Didn’t Know - Brett Young",
        "Heartache Medication - Jon Pardi", "Hometown Girl - Josh Turner", 
        "Breaking Up Was Easy in the 90s - Sam Hunt", "Small Town Boy - Dustin Lynch", 
        "When It Rains It Pours - Luke Combs", "Drinkin’ Problem - Midland", 
        "Beautiful Crazy - Luke Combs", "I Was Jack (You Were Diane) - Jake Owen", 
        "The Middle - Zedd, Maren Morris & Grey", "Best Shot - Jimmie Allen",
        "Sangria - Blake Shelton", "You Broke Me First - Tate McRae", 
        "What Ifs - Kane Brown feat. Lauren Alaina", "Famous Friends - Chris Young & Kane Brown",
        "More Hearts Than Mine - Ingrid Andress", "Beer Can't Fix - Thomas Rhett feat. Jon Pardi",
        "One Margarita - Luke Bryan", "One Too Many - Keith Urban & Pink", 
        "Better Together - Jack Johnson", "The Good Ones - Gabby Barrett", 
        "Settling Down - Miranda Lambert", "Sand in My Boots - Morgan Wallen"
    ],
    "classical": [
        "Symphony No. 5 - Ludwig van Beethoven", "Clair de Lune - Claude Debussy", 
        "Eine kleine Nachtmusik - Wolfgang Amadeus Mozart", "The Four Seasons - Antonio Vivaldi",
        "Piano Concerto No. 21 - Wolfgang Amadeus Mozart", "Symphony No. 9 - Ludwig van Beethoven", 
        "Adagio for Strings - Samuel Barber", "Requiem - Wolfgang Amadeus Mozart", 
        "Boléro - Maurice Ravel", "The Nutcracker Suite - Pyotr Ilyich Tchaikovsky", 
        "Piano Sonata No. 14 (Moonlight Sonata) - Ludwig van Beethoven", "Carmen Suite - Georges Bizet",
        "Symphony No. 40 - Wolfgang Amadeus Mozart", "Rhapsody on a Theme of Paganini - Sergei Rachmaninoff",
        "Swan Lake - Pyotr Ilyich Tchaikovsky", "Concerto for Two Violins - Antonio Vivaldi", 
        "Symphony No. 6 (Pastoral) - Ludwig van Beethoven", "Largo from Xerxes - George Frideric Handel",
        "Prelude in C Major - Johann Sebastian Bach", "Hungarian Rhapsody No. 2 - Franz Liszt",
        "Pictures at an Exhibition - Modest Mussorgsky", "Piano Concerto No. 2 - Sergei Rachmaninoff",
        "Symphony No. 3 (Eroica) - Ludwig van Beethoven", "The Planets - Gustav Holst", 
        "Symphony No. 1 - Johannes Brahms", "Gymnopédies - Erik Satie", "Serenade for Strings - Antonín Dvořák",
        "Eine Alpensinfonie - Richard Strauss", "Piano Sonata No. 16 - Wolfgang Amadeus Mozart",
        "Concerto for Piano and Orchestra - Sergei Prokofiev", "The Rite of Spring - Igor Stravinsky",
        "Symphony No. 7 - Ludwig van Beethoven", "Piano Concerto No. 1 - Pyotr Ilyich Tchaikovsky", 
        "Messa da Requiem - Giuseppe Verdi", "Intermezzo from Cavalleria Rusticana - Pietro Mascagni",
        "Symphony No. 2 - Johannes Brahms", "Vocalise - Sergei Rachmaninoff", "Symphony No. 4 - Ludwig van Beethoven",
        "Symphony No. 8 - Franz Schubert", "Don Giovanni - Wolfgang Amadeus Mozart", 
        "Träumerei from Kinderszenen - Robert Schumann", "The Emperor Concerto - Ludwig van Beethoven",
        "Sinfonia Concertante - Wolfgang Amadeus Mozart", "Concierto de Aranjuez - Joaquín Rodrigo",
        "Symphony No. 9 (Choral) - Ludwig van Beethoven", "Allegro from Symphony No. 40 - Wolfgang Amadeus Mozart",
        "Pavane pour une infante défunte - Maurice Ravel", "L'Arlésienne Suite - Georges Bizet",
        "Requiem Mass in D Minor - Wolfgang Amadeus Mozart", "Violin Concerto - Jean Sibelius",
        "Prelude and Fugue in C Minor - Johann Sebastian Bach", "Ode to Joy - Ludwig van Beethoven", 
        "Symphony No. 5 - Gustav Mahler", "Song of the Night - Richard Strauss", 
        "Intermezzo from Cavalleria Rusticana - Pietro Mascagni", "Adagio - Tomaso Albinoni",
        "Allegro from The Four Seasons - Antonio Vivaldi", "Lament for a Soldier - Samuel Barber",
        "Symphony No. 3 - Gustav Mahler", "Piano Quartet in G Minor - Maurice Ravel",
        "Sonata No. 1 for Violin and Piano - Johannes Brahms", "Sonata for Cello and Piano - Dmitri Shostakovich",
        "Concerto for Violin - Felix Mendelssohn", "Nocturnes - Claude Debussy", "Rhapsody in Blue - George Gershwin",
        "Serenade for Strings in E Major - Antonín Dvořák", "Serenade for Winds - Wolfgang Amadeus Mozart",
        "Carmen - Georges Bizet", "Fantasia on a Theme by Thomas Tallis - Ralph Vaughan Williams",
        "The Barber of Seville - Gioachino Rossini", "Toccata and Fugue in D Minor - Johann Sebastian Bach",
        "Liederkreis - Robert Schumann", "Piano Concerto No. 5 - Ludwig van Beethoven", 
        "Nimrod from Enigma Variations - Edward Elgar", "The Firebird Suite - Igor Stravinsky",
        "Hungarian Dance No. 5 - Johannes Brahms", "Rhapsody on a Theme of Paganini - Sergei Rachmaninoff",
        "Symphony No. 1 - Sergei Prokofiev", "Meditation from Thaïs - Jules Massenet", 
        "Piano Concerto No. 3 - Sergei Rachmaninoff", "The Merry Widow - Franz Lehár"
    ],
    "jazz": [
        "Take Five - Dave Brubeck", "So What - Miles Davis", "My Favorite Things - John Coltrane",
        "Strange Fruit - Billie Holiday", "Sing, Sing, Sing - Benny Goodman", "All The Things You Are - Ella Fitzgerald",
        "In a Sentimental Mood - Duke Ellington & John Coltrane", "Take the 'A' Train - Duke Ellington",
        "Autumn Leaves - Cannonball Adderley", "Round Midnight - Thelonious Monk", "A Love Supreme - John Coltrane",
        "Misty - Erroll Garner", "Maiden Voyage - Herbie Hancock", "Watermelon Man - Herbie Hancock",
        "Blue in Green - Miles Davis", "Freddie Freeloader - Miles Davis", "Summertime - Ella Fitzgerald & Louis Armstrong",
        "You Don't Know What Love Is - Billie Holiday", "Goodbye Pork Pie Hat - Charles Mingus",
        "Moanin' - Charles Mingus", "Blue Monk - Thelonious Monk", "Mercy, Mercy, Mercy - Cannonball Adderley",
        "The Girl from Ipanema - Stan Getz & João Gilberto", "Desafinado - Stan Getz & João Gilberto",
        "Witch Hunt - Wayne Shorter", "Song for My Father - Horace Silver", "Cantaloupe Island - Herbie Hancock",
        "Night in Tunisia - Dizzy Gillespie", "Confirmation - Charlie Parker", "Ornithology - Charlie Parker",
        "A Night in Tunisia - Dizzy Gillespie", "Giant Steps - John Coltrane", "Nostalgia in Times Square - Charles Mingus",
        "The Sidewinder - Lee Morgan", "One O'Clock Jump - Count Basie", "Just Friends - John Coltrane",
        "Chameleon - Herbie Hancock", "Lullaby of Birdland - George Shearing", "Stolen Moments - Oliver Nelson",
        "Blue Train - John Coltrane", "Django - Modern Jazz Quartet", "Killer Joe - Benny Golson",
        "Parker's Mood - Charlie Parker", "C Jam Blues - Duke Ellington", "Straight, No Chaser - Thelonious Monk",
        "Lush Life - Billy Strayhorn", "Airegin - Sonny Rollins", "Poinciana - Ahmad Jamal",
        "Satin Doll - Duke Ellington", "Misty Blue - Erroll Garner", "I Get a Kick Out of You - Cole Porter",
        "Tenor Madness - Sonny Rollins", "In the Mood - Glenn Miller", "The Preacher - Horace Silver",
        "Night Train - Jimmy Forrest", "Blues for Alice - Charlie Parker", "Boplicity - Miles Davis",
        "Waltz for Debby - Bill Evans", "C-Jam Blues - Duke Ellington", "Ruby My Dear - Thelonious Monk",
        "Body and Soul - Coleman Hawkins", "Haitian Fight Song - Charles Mingus", "Some Day My Prince Will Come - Bill Evans",
        "Lover Man - Billie Holiday", "You Go to My Head - Billie Holiday", "Stompin' at the Savoy - Benny Goodman",
        "What a Wonderful World - Louis Armstrong", "Mood Indigo - Duke Ellington", "Skylark - Hoagy Carmichael",
        "On Green Dolphin Street - Miles Davis", "Desafinado - Stan Getz & João Gilberto", "It Don't Mean a Thing - Duke Ellington",
        "Autumn Leaves - Eva Cassidy", "Songbird - Kenny G", "Wave - Antonio Carlos Jobim", "Breezin' - George Benson",
        "Blue Skies - Ella Fitzgerald", "The Look of Love - Dusty Springfield", "Cheek to Cheek - Ella Fitzgerald & Louis Armstrong",
        "In Your Own Sweet Way - Dave Brubeck", "All of Me - Billie Holiday", "Cry Me a River - Julie London",
        "Take Five - Dave Brubeck", "Moanin' - Charles Mingus", "How High the Moon - Ella Fitzgerald",
        "Ain't Misbehavin' - Fats Waller", "Comin' Home Baby - Mel Tormé", "Perdido - Duke Ellington",
        "Lover Man - Sarah Vaughan", "Fine and Mellow - Billie Holiday", "Night and Day - Frank Sinatra", 
        "Let’s Fall in Love - Ella Fitzgerald", "Fever - Peggy Lee", "April in Paris - Count Basie", 
        "On the Sunny Side of the Street - Louis Armstrong"
    ],
    "blues": [
        "The Thrill Is Gone - B.B. King", "Sweet Little Angel - B.B. King", "Pride and Joy - Stevie Ray Vaughan",
        "Crossroad Blues - Robert Johnson", "Hoochie Coochie Man - Muddy Waters", "Mannish Boy - Muddy Waters",
        "Stormy Monday - T-Bone Walker", "Born Under a Bad Sign - Albert King", "I’d Rather Go Blind - Etta James",
        "Boom Boom - John Lee Hooker", "Wang Dang Doodle - Koko Taylor", "Muddy Waters Blues - Muddy Waters",
        "Spoonful - Howlin' Wolf", "Hoochie Coochie Man - Howlin' Wolf", "Little Red Rooster - Howlin' Wolf",
        "Dust My Broom - Elmore James", "The Sky Is Crying - Elmore James", "Good Morning Little Schoolgirl - Donny Hathaway",
        "Key to the Highway - Big Bill Broonzy", "Rock Me Baby - B.B. King", "I Can't Quit You Baby - Otis Rush",
        "Lonesome Bedroom - Buddy Guy", "I Got My Mojo Working - Muddy Waters", "Trouble in Mind - Richard M. Jones",
        "Goin' Down Slow - St. Louis Jimmy", "It Hurts Me Too - Elmore James", "The House of the Rising Sun - The Animals",
        "Red House - Jimi Hendrix", "Little Wing - Jimi Hendrix", "I'm a King Bee - Slim Harpo", "Love Struck Baby - Stevie Ray Vaughan",
        "Texas Flood - Stevie Ray Vaughan", "The Blues Is Alright - Little Milton", "I'm in the Mood - John Lee Hooker",
        "You Shook Me - Willie Dixon", "My Babe - Little Walter", "Juke - Little Walter", "One Bourbon, One Scotch, One Beer - George Thorogood",
        "Messin' with the Kid - Junior Wells", "Killing Floor - Howlin' Wolf", "She's Nineteen Years Old - B.B. King",
        "Sittin' on Top of the World - Howlin' Wolf", "Shake Your Money Maker - Elmore James", "The Comeback - Freddie King",
        "Blues Before Sunrise - Elmore James", "Boom Boom (Out Go the Lights) - Little Walter", "Hoochie Coochie Man - Muddy Waters",
        "No Money Down - Chuck Berry", "Every Day I Have the Blues - B.B. King", "Love in Vain - Robert Johnson",
        "Rollin' and Tumblin' - Muddy Waters", "Blues in My Heart - T-Bone Walker", "Baby Please Don't Go - Big Joe Williams",
        "I'd Rather Be Blind - Etta James", "I Want to Be Loved - Muddy Waters", "My Little Machine - Albert King",
        "Sweet Home Chicago - Robert Johnson", "Last Night - The Mar-Keys", "Ain't No Sunshine - Bill Withers",
        "Going Down to Main Street - Charlie Musselwhite", "Slam Jam - Magic Sam", "Come On In My Kitchen - Robert Johnson",
        "Killing Floor - Howlin' Wolf", "Goodbye Blues - Memphis Slim", "Unchain My Heart - Ray Charles",
        "I Found My Baby - Little Walter", "Juke Joint Jump - Little Richard", "Forty Four - Howlin' Wolf",
        "Rough Stuff - Buddy Guy", "Wang Dang Doodle - Koko Taylor", "I Can't Stand It - Walter Horton",
        "Mean Old World - T-Bone Walker", "I Walk the Line - Johnny Cash", "Someday - Freddie King", "Driftin' Blues - Charles Brown",
        "Walking by Myself - Jimmy Rogers", "Blues with a Feeling - Little Walter", "Bad Luck - Junior Wells",
        "Blues with a Feeling - Little Walter", "Can't Quit the Blues - George Thorogood", "I'm Tore Down - Freddie King",
        "Down Home Blues - Z.Z. Hill", "Hoodoo Man Blues - Junior Wells", "She's a Good 'Un - Albert King",
        "Bourbon Street Blues - Eddie Cleanhead Vinson", "Gonna Quit You Baby - Otis Rush", "Woke Up This Morning - B.B. King",
        "Got My Mojo Working - Muddy Waters", "What's the Matter with the Mill - Little Walter"
    ],
    "reggae": [
        "The Thrill Is Gone - B.B. King", "Sweet Little Angel - B.B. King", "Pride and Joy - Stevie Ray Vaughan",
        "Crossroad Blues - Robert Johnson", "Hoochie Coochie Man - Muddy Waters", "Mannish Boy - Muddy Waters",
        "Stormy Monday - T-Bone Walker", "Born Under a Bad Sign - Albert King", "I’d Rather Go Blind - Etta James",
        "Boom Boom - John Lee Hooker", "Wang Dang Doodle - Koko Taylor", "Muddy Waters Blues - Muddy Waters",
        "Spoonful - Howlin' Wolf", "Hoochie Coochie Man - Howlin' Wolf", "Little Red Rooster - Howlin' Wolf",
        "Dust My Broom - Elmore James", "The Sky Is Crying - Elmore James", "Good Morning Little Schoolgirl - Donny Hathaway",
        "Key to the Highway - Big Bill Broonzy", "Rock Me Baby - B.B. King", "I Can't Quit You Baby - Otis Rush",
        "Lonesome Bedroom - Buddy Guy", "I Got My Mojo Working - Muddy Waters", "Trouble in Mind - Richard M. Jones",
        "Goin' Down Slow - St. Louis Jimmy", "It Hurts Me Too - Elmore James", "The House of the Rising Sun - The Animals",
        "Red House - Jimi Hendrix", "Little Wing - Jimi Hendrix", "I'm a King Bee - Slim Harpo", "Love Struck Baby - Stevie Ray Vaughan",
        "Texas Flood - Stevie Ray Vaughan", "The Blues Is Alright - Little Milton", "I'm in the Mood - John Lee Hooker",
        "You Shook Me - Willie Dixon", "My Babe - Little Walter", "Juke - Little Walter", "One Bourbon, One Scotch, One Beer - George Thorogood",
        "Messin' with the Kid - Junior Wells", "Killing Floor - Howlin' Wolf", "She's Nineteen Years Old - B.B. King",
        "Sittin' on Top of the World - Howlin' Wolf", "Shake Your Money Maker - Elmore James", "The Comeback - Freddie King",
        "Blues Before Sunrise - Elmore James", "Boom Boom (Out Go the Lights) - Little Walter", "Hoochie Coochie Man - Muddy Waters",
        "No Money Down - Chuck Berry", "Every Day I Have the Blues - B.B. King", "Love in Vain - Robert Johnson",
        "Rollin' and Tumblin' - Muddy Waters", "Blues in My Heart - T-Bone Walker", "Baby Please Don't Go - Big Joe Williams",
        "I'd Rather Be Blind - Etta James", "I Want to Be Loved - Muddy Waters", "My Little Machine - Albert King",
        "Sweet Home Chicago - Robert Johnson", "Last Night - The Mar-Keys", "Ain't No Sunshine - Bill Withers",
        "Going Down to Main Street - Charlie Musselwhite", "Slam Jam - Magic Sam", "Come On In My Kitchen - Robert Johnson",
        "Killing Floor - Howlin' Wolf", "Goodbye Blues - Memphis Slim", "Unchain My Heart - Ray Charles",
        "I Found My Baby - Little Walter", "Juke Joint Jump - Little Richard", "Forty Four - Howlin' Wolf",
        "Rough Stuff - Buddy Guy", "Wang Dang Doodle - Koko Taylor", "I Can't Stand It - Walter Horton",
        "Mean Old World - T-Bone Walker", "I Walk the Line - Johnny Cash", "Someday - Freddie King", "Driftin' Blues - Charles Brown",
        "Walking by Myself - Jimmy Rogers", "Blues with a Feeling - Little Walter", "Bad Luck - Junior Wells",
        "Blues with a Feeling - Little Walter", "Can't Quit the Blues - George Thorogood", "I'm Tore Down - Freddie King",
        "Down Home Blues - Z.Z. Hill", "Hoodoo Man Blues - Junior Wells", "She's a Good 'Un - Albert King",
        "Bourbon Street Blues - Eddie Cleanhead Vinson", "Gonna Quit You Baby - Otis Rush", "Woke Up This Morning - B.B. King",
        "Got My Mojo Working - Muddy Waters", "What's the Matter with the Mill - Little Walter"
    ],
    "indian": [
        "Tum Hi Ho - Arijit Singh", "Tera Ban Jaunga - Akhil Sachdeva, Manj Musik", "Dil Dhadakne Do - Priyanka Chopra, Farhan Akhtar",
        "Channa Mereya - Arijit Singh", "Raabta - Arijit Singh", "Pehla Nasha - Udit Narayan, Sadhana Sargam", "Kal Ho Na Ho - Sonu Nigam",
        "Tum Mile - Neeraj Shridhar", "Kabira - Arijit Singh", "Tum Jo Aaye - Rahat Fateh Ali Khan, Sunidhi Chauhan", "Kabira (Reprise) - Arijit Singh",
        "Ae Mere Humsafar - Mansheel Gujral, Mithoon", "Pani Da Rang - Ayushmann Khurrana", "Tere Bina - A. R. Rahman", "Sun Saathiya - Priya Saraiya, Dev Negi",
        "Galliyan - Ankit Tiwari", "Janam Janam - Arijit Singh", "Tera Yaar Hoon Main - Arijit Singh", "Dilli Wali Girlfriend - Arijit Singh, Neeti Mohan",
        "Jeene Laga Hoon - Yasser Desai, Shreya Ghoshal", "Hasi - Ami Mishra", "Hasi Ban Gaye - Ami Mishra", "Tere Bina - A. R. Rahman",
        "Teri Galliyan - Ankit Tiwari", "Tum Hi Ho Bandhu - Neeraj Shridhar, Kavita Seth", "Kuch To Hai - Armaan Malik", "Chal Ghoom Dilli - Gippy Grewal",
        "Raabta - Arijit Singh", "Dilbaro - Harshdeep Kaur, Vibha Saraf", "Mere Rashke Qamar - Rahat Fateh Ali Khan", "O Saathi - Atif Aslam",
        "Ishq Sufiana - Kamran Ahmed", "Tera Mera Rishta - Lata Mangeshkar", "Agar Tum Mil Jao - Atif Aslam", "Agar Tum Mil Jao - Atif Aslam",
        "Dil Se - A. R. Rahman", "Tera Ban Jaunga - Akhil Sachdeva, Manj Musik", "Pani Da Rang - Ayushmann Khurrana", "Tere Bina - A. R. Rahman",
        "Teri Galliyan - Ankit Tiwari", "Tum Jo Aaye - Rahat Fateh Ali Khan", "Channa Mereya - Arijit Singh", "Ae Mere Humsafar - Mansheel Gujral, Mithoon",
        "Tum Mile - Neeraj Shridhar", "Galliyan - Ankit Tiwari", "Kabira (Reprise) - Arijit Singh", "Janam Janam - Arij Singh", "Pehla Nasha - Udit Narayan",
        "Pehla Nasha - Udit Narayan", "Sun Saathiya - Priya Saraiya, Dev Negi", "Tere Bina - A. R. Rahman", "Chal Ghoom Dilli - Gippy Grewal",
        "Hasi - Ami Mishra", "Dilli Wali Girlfriend - Arijit Singh", "Tum Jo Aaye - Rahat Fateh Ali Khan", "Jeene Laga Hoon - Yasser Desai",
        "Hasi Ban Gaye - Ami Mishra", "Dil Dhadakne Do - Priyanka Chopra, Farhan Akhtar", "Kabira - Arijit Singh", "Pehla Nasha - Udit Narayan",
        "Tum Mile - Neeraj Shridhar", "Dil Se - A. R. Rahman", "O Saathi - Atif Aslam", "Teri Galliyan - Ankit Tiwari", "Channa Mereya - Arijit Singh",
        "Tere Bina - A. R. Rahman", "Tera Ban Jaunga - Akhil Sachdeva, Manj Musik", "Jeene Laga Hoon - Yasser Desai", "Galliyan - Ankit Tiwari",
        "Raabta - Arijit Singh", "Hasi Ban Gaye - Ami Mishra", "Dilli Wali Girlfriend - Arijit Singh", "Pani Da Rang - Ayushmann Khurrana",
        "Tum Hi Ho - Arijit Singh", "Kabira (Reprise) - Arijit Singh", "Teri Galliyan - Ankit Tiwari", "Dil Dhadakne Do - Priyanka Chopra",
        "Sun Saathiya - Priya Saraiya, Dev Negi", "Chal Ghoom Dilli - Gippy Grewal", "Tum Mile - Neeraj Shridhar", "Tere Bina - A. R. Rahman",
        "Janam Janam - Arijit Singh", "Kabira - Arijit Singh", "Galliyan - Ankit Tiwari", "Channa Mereya - Arijit Singh", "Tere Bina - A. R. Rahman"
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    music_type = data.get('music_type')
    num_songs = int(data.get('num_songs'))

    if music_type in recommendations:
        songs = random.sample(recommendations[music_type], num_songs)
        return jsonify({'songs': songs})
    else:
        return jsonify({'songs': []})

if __name__ == '__main__':
    app.run(debug=True)
