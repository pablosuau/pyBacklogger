#Post mortem: pyBacklogger

    Pablo Suau - pablosuau AT gmail.com

This is a [post mortem](http://www.pixelprospector.com/the-big-list-of-postmortems/) of pyBacklogger, a personal project I've been working on for about two years, which is now ready to be released and used by other users. In this document I will summarise what my objectives were when I started the project, and which things went well/bad.

## The objective

When I first started working on pyBacklogger I was going through a series of changes in my career. One of the consequences of these changes was that I wanted/needed to learn Python. More specifically, I wanted to learn Python in the context of manipulating data, even if it was in a very simple form. In order to motivate myself, it was clear that my project had to be about something I am passionate about, or at least, something that would be useful for me. And this is how the idea of pyBacklogger came up.

I like video games, but I do not have much time to play video games (isn't this a common problem in the first world?) The list of games I'd like to play keeps growing and growing, and it is always hard to decide what to play next. There are, of course, many backlog management applications out there, but there was one single feature that I always wanted to have but never found: weighted scores. I am referring here to the way [IMDB ratings](https://math.stackexchange.com/questions/169032/understanding-the-imdb-weighted-rating-function-for-usage-on-my-own-website) work. Weighted scores are both a measure of how good and how popular a game is. A game has a high weighted score when many people think that it is a good game. 

Once I decided to work on such an application, there was an important issue to consider: where to get the data from. I wanted immediate results, I was not planning on creating a platform that would attract thousands of users so that I could get millions of ratings and therefore be able to access significant and useful weighted scores. That would just take too much time. Instead, I decided to make use of data available out there: the [GameFAQs database](https://www.gamefaqs.com). The advantage of GameFAQs over other video game databases is that it contains a remarkably larger number of titles and user ratings.  However, GameFAQs does not provide an API to access their data with. They are, in fact, quite protective with their data. It was in that moment when I decided to make us of web scrapping in my tool, so that I could make use of such a rich source of data. This proved to be a big issue later during the project, as I explain in another section below.

I also wanted to include some simple statistics in pyBacklogger: how far I am to my objective of completing my backlog? Which platform is the one in which I beat more games? How many JRPGs in my backlog remain to be completed? I really enjoy looking at this numbers and use them to take decisions about what to play next. These statistics also give me motivation to keep grinding through my backlog. At first I was planning to even include plots with this data, but I abandoned de idea once the tool was useful enough for me.

## What didn't go well

* **Scrapping data**: scrapping the whole GameFAQs data would have taken much time, and I was only going to use a very small fraction of it, so I designed my application so that scrapping is done  on demand. This means that you only scrap GameFAQs website whenever you want to add a new game to your backlog or synchronise the game scores with the values on the website. I learned, the hard way, that this solution left me in a very vulnerable position. At one point during the development GameFAQs underwent some changes on their web structure. The consequence of this is that several components of my application became useless and I had to make many changes in my code. There has not been changes on the website for a long time now, but this could change in the future, and my application will not be usable again. What I learned from this experience is that I cannot depend on other people's data. I have to collect and build my own database. Scrapping may be useful as a first step, but absolutely not on demand.

* **Scrapping data (2)**: well, this is embarrassing, but my IP was banned from GameFAQs once while I was implementing the score updating option. I was not careful, I made too many requests in a very short period of time, and I had to use a proxy for a couple of weeks to be able to keep developing the updating functionality. This made things much slower. At least, after this experience, I was able to learn how to scrap websites in a sustainable and rational way.
 
* **Much time wasted on refactoring**: my application is designed to follow the MVC pattern. But this is not the way I started building up the application. At the beginning I mixed all the code together in the same module: design of the graphical interface, logical control and data models. I decided to refactor my code so that it would follow the MVC pattern at a very advanced stage. And this refactoring process took way too long. I should have thought about the application architecture before actually starting coding. 

* **Desktop vs. online application**: I use pyBacklogger very often at home, and I it is really useful for me. But... I can only use it at home, because it is a desktop application, and I only keep my saved backlog in my personal computer. What if I want to check my backlog from the office? I'd have to share my backlog data through Dropbox or Google Drive, and then download both the application code and the data to my office's computer. It is not impossible, but having to do so prevented me to use my tool in other locations. The era of desktop applications is long gone now. By implementing a solution in the cloud I'd have allowed myself to use it everywhere. If other people decide to use the application, it would be easier for them, and there may not be so much need of scrap data from GameFAQs if such data was already in my application's database. 

* **IDE**: I used [Spyder](https://github.com/spyder-ide/spyder) to code pyBacklogger. The reason I chose Spyder is because it was part of the Python distribution I was using at work when I first started using Python ([Python(x,y)](https://python-xy.github.io/)). However, using Spyder turned out to make things harder. In my opinion (and this is my opinion) Spyder is bloated and slow, full of features that I did not use during the development of pyBacklogger. As my laptop became older and older I had to wait a long time just to boot the editor and start typing code. In the meantime, new IDEs were released and I started experimenting with other solutions. I am now using [Sublime](https://www.sublimetext.com/) at work. Sublime is not really and IDE, but a text editor. However, it has all the functionalities I need. It is powerful, fast and easy to use. Bye bye Spyder!

## What did go well

* **I achieved my objectives**: I am fluent in Python now and I made a useful tool that I use (almost) every day. These were exactly the reasons why I started working on pyBacklogger. 

* **I learned about how to properly scrap data**: this is a skill that may be useful in my professional life, as well as in any possible future project related with data I decide to embark in. 

* **I completed a project from beginning to end**: this is the very first personal project I complete. I can't describe with words how excited I feel about this. I feel encouraged now to keep working on personal projects to both improve my personal technical skills and provide other people with useful tools. 

## Conclusions 

I would say that the outcome of this project has been positive. Not only have I improved my Python coding skills, but also I have learned some data and software engineering related skills. The ending result is far from perfect, but it is useful enough for me the way it is. 

The fact that this is a post mortem document does not mean that I will stop maintaining pyBacklogger. I still use this tool, and until I do not find/implement a replacement for it, I will make sure that it keeps working. But I will not add new features from now on. I hope that pyBacklogger may be useful for other people as well.

