# assignment 7 - web scraping artist images
## mac sanmiguel

this week i decided to go to the web archive/catalog of smalls (an nyc jazz club) to see if i could scrape the images of each musician of a certain instrument. because i'm a pianist, i decided i would filter the results in their catalog by pianists, and download those images. 
at first, i tried the method we used in class, with requests and bs4. after debugging for a while, i realized that i would need to use another library that would allow me to make a script that can interact with the web browser. by default, the smalls website only loads a few of the results, and the rest of the results can be loaded by pressing the "show more" button. there are a lot of results, so i had to make the script press the button over and over, until all of the results were loaded. after that, i could use beautifulsoup like normal and download the images. 
here's some fun visuals i made of the process/result:
![gif](smalls_piano_scrape.gif)

![collage](smalls_piano_scrape.png)