# live code performance
## parsons dt spring 2025 final project
### five dollars are five dollars - mac sanmiguel

[link to video demonstration](https://vimeo.com/1083566309?share=copy)

## process/challenges

For this project, I decided to use a live coding library for python to arrange and perform one of my original songs. After experimenting with a few different libraries, I decided on [sardine](https://github.com/Bubobubobubobubo/sardine). Something that was very challenging was installing sardine along with all of its dependencies and getting it to work on my device. Getting sardine to consistently work was the first big task, and took me hours to figure out. Once I had that taken care of, I had to learn sardine's unique syntax and figure out what it was capable of. I ended up writing a few different scripts to test some of sardine's features out, and ran into a lot of challenges along the way. Initially, I wanted to use a midi controller to send an input to sardine that would act like a synthesizer, but I wasn't able to get that to work out. I ended up deciding to use ableton live as my instrument that I would be able to play like a piano keyboard. I ended up putting these together to plan a live performance that uses sardine's capabilities for changing what I had written, along with ableton to play melodies on top.

## code breakdown
```
# five dollars are five dollars 
# mac sanmiguel

clock.tempo = 135

rev0 = {'room':5, 'size':0.5, 'dry':0.25}

del0 = {'delay':1, 'delaytime':0.75, 'delayfeedback':0.2}

Pa * zd('gtr', 'h. ^4 e E h. ^2 e r e ^6 q. ^7 e ^6 e ^4 q r e ^E q ^^4 q ^^2 q ^7 e ^9 q ^9 w r h. r e r e ^7 q ^6 e ^4 e ^2 h r h. r e ^1 q ^6 q ^4 q 9 e E q E w r h. r e E q. ^2 e 9 e 7 h r w r', scale='chromatic')

Pb * zd('superpiano', 'h. _0_7_E4 e r w __6_3_92 e r w __4_2_E7 h __9_704 h _4_E27 h.. _7_E69 w _1_T49 e r h. __E_926 w __4__E_6_92 q r h __E_926 h __6_1_94 h.. __2_0_4_7_E w __5_0_3_9 e r h. _4_7269 w _2_5047 q r', scale='chromatic')

Pc * d('ab:4 ab:4 ab:9 ab:9 ab:4 ab:10 ab:10 ab:9', gain=1.5, p=0.5, rate=1)


silence()
```
Code for sardine is not run from top to bottom like regular python code. The code is actually sent as individual lines by the user into the sardine interpreter. As a result of this feature, changes can be made to each line and they can be sent into the interpreter to alter the track that is already playing.
At the top of my code, I have the line 'clock.tempo = 135' which can be sent to the interpreter to set the tempo of the song. the next two lines, 'rev0 = {'room':5, 'size':0.5, 'dry':0.25}' and 'del0 = {'delay':1, 'delaytime':0.75, 'delayfeedback':0.2}' are effect presets. These are effects that I can put on any of the tracks, with the parameters predetermined by myself, so I can add them easily to whichever track I want during the performance. The next three lines contain the actual song itself. Each of these lines start with either "Pa", "Pb", or "Pc". These are "players" and like the name suggests, they act like individuals that play their part of the larger composition. The asterisk signifies that the player will repeat what has been written indefinitely, and the following "zd" or "d" is the "pattern language" that the following melodic/rhythmic information is written in. For the first two tracks, I'm using the "ziffers" syntax. In ziffers, each note is interpreted as a pair, separated by spaces, in a string of characters. the first part of the string is the rhythm, with each rhythm having a specified character, and the second part is the pitch content, which is written as the number which would be the index of the pitch in the selected scale. Pitches can be combined to make chords, and they can also be put up and down octaves by using "^" and "_" respectively. Also, the first and last parameters are the sample/instrument being used, and the scale. The third track, "Pc" is my drum track, and I decided this would be easier to write in sardine pattern language (d). For the sardine pattern language, the first parameter is a string, which is the pitch/rhythm content and the sample that is being used. I am using the "ab" sample set, which is a drum kit, and choosing the individual sample by using a colon and the index of whichever sample I need. The other important parameters in sardine pattern language are "p" and "rate". These parameters both have to do with the rhythm that the string will be played in. "p" is the "period" of the string, and is basically the speed at which the string will be played. I start out with it being set to 0.5, which would be eighth notes, because it's half the value of the default "1" which is quarter notes. "rate" is the amount of times each individual part of the string is played. If "rate" is 1, then each part of the string will be played once. 

## what i learned
Because of how difficult the setup was, I learned a lot about managing python versions and working with VSCode. There were also a lot of issues with the library I chose, but I think it was probably the best option for me to use with python. Because of that, another takeaway is that python is probably not the best language for live coding. If I were to do this again, I would probably want to use javascript, with the strudel library, which seems like a much better live coding tool.