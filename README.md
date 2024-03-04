# SW_pokerstreaming
 
A system that can be used to stream poker games to a website and calculate the odds of winning for each player. The system is based on a Raspberry Pi 3B+ and a couple of webcams. The system is based on the following software:

https://github.com/EdjeElectronics/OpenCV-Playing-Card-Detector (OpenCV-Playing-Card-Detector)
We use the code from this repository to detect the cards on the table. The code is modified to work with two webcams. We also trained a new model to detect our cards using the code from the repository.


https://github.com/elleklinton/PiedPoker (Package to run simulations of poker games and calculate the odds of winning)


Software that has to run on the Raspberry Pi is in the folder "server". "CardDetectorServer.py" is the code that sends community cards. For each player, there should be a copy of "severp1.py" and "severp2.py" with a changed port and camera number that sends the cards of the player. 

The code for the website is in the file website.py. Before running the website you have to run appropriate client for the community cards and each player's hand. The website is based on Flask. Clients use web sockets to communicate with the server and save information about the game in text files. 

![Alt text](/screenshot.png?raw=true "Website screenshot")
