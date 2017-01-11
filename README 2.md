# CS-C3170 Web Software Development Project Plan


## 1. Team  
428022 Elis Viitanen  
605311 Bingjing Xu  
502841 Teo Mertanen


## 2. Goal  
The goal of the project is to create an online game store for JavaScript games.  
Users should be able to log in as either developers, who can add their games to the service and set prices for them or players, who can purchase these games and play them.


## 3. Plans


Subsystems:  
* Authentication and registration  
* Buying games  
* Playing purchased games  
* Sending messages to game  
* Receiving messages from game  
* High scores  
* Adding, editing and removing games, setting prices  
* (Optional, if time permits) RESTful API  


The detailed technical implementations of these features will be discussed in the first meeting on 02.01.2016. 

![Alt text](/diagram1.png)
   
Diagram 1. Basic outline of required database models.


Django will be used for the server logic. The client will be a multi-page web app with HTML generated dynamically by Django, with CSS and Bootstrap for styling, and JavaScript with jQuery and possibly Underscore.js for client-side scripting.


### URL scheme:


/login - Default page when not logged in.  
/register - Create a new account.  
/index - Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  
/games - As a developer, see all the games you’ve created, or add and price a new game.  
/games/id - As a player, play a game. As a developer, edit a game or remove it.  
/games/id/highscores - See the highscore table for a particular game. 
/users/id - Public profile of players where other players can view their highscores.


## 4. Process and time schedule


We will communicate using Telegram and email regularly when working remotely, and meet in person starting on Jan 2nd (week 1). Git will be used for version control, and Google Docs for collaborating on documentation.


Week 1 - meeting 1, building the framework of the web application and work allocation;  
Week 2 - meeting 2, implement authentication and registration and buying games;  
Week 3 - meeting 3, implement playing purchased games, sending messages to game;  
Week 4 - meeting 4, implement receiving messages from game, high scores;  
Week 5 - meeting 5, implement adding, editing and removing games;  
Week 6 - meeting 6, implement setting prices, RESTful API;  
Week 7 - meeting 7, system testing, polish and demo practice;  
End of week 7 - Final submission on Sunday Feb 19th  
Project demonstration later, no date yet.


## 5. Testing  
Testing shall be mainly system testing. Each feature shall be thoroughly tested in the week after it is implemented and reviewed in the team meeting. Google Chrome/Chromium shall be used as the target browser platform on which all testing is conducted, as it has the largest amount of supported features[1], and creating workarounds in less modern browsers such as Edge would create significant additional workload.


HTML and CSS will be validated using W3C’s validator service.


[1] Can I use - browser scores, http://caniuse.com/




## 6. Risk analysis  
Based on warnings in the project description, security should be given consideration as data tampering and script injections are implied to be part of the grading tests.  
On a practical project level, the biggest risk is to failing to meet in person, causing momentum to be lost and work to be ignored and testing to be forgotten, which will eventually cause features being late and deadlines missed.
