import random
score = 1000

def printGraphic(name):
    if name == "rock":
        print("""
                 *@@@#                    
               %,      &@@@@(             
               @        %     .@           
             &        /       *,          
             ,*       #        .,  .@      
         .*@       @         @     @*    
      *@      .%. &         .       @    
      @              /       .      .  @  
     @                #     /       &   @ 
    ./                     %       &    @ 
    &       %         *   %       &    #/ 
    @           ,&/.,@  ,.       #     @  
    /*                 @(      &      @   
     @                 (  #( &      ,#    
      @                         ,. @      
      ##                         #*      
       @%                      @,       
            @@*      .        ,@(         
                 @ @ @ @@ ./%#,          
        """)
    elif name == "scissors":
        print(""" 
                  .                    
               #.   .#         @,  *(  
               (     %        %      % 
               *     *       @      @  
               @      *     &      &   
               ./     @    /      ,    
                %     *   ..      &    
                 /     %  #      (     
           .#   .@ .*,,,@(       @     
      #.   &     @          (@   @     
      *    (     %              @&     
      #     &      @/            */    
      ,.     #     ,    **         ,   
       @#     #     ,  #,          &   
       # &.   #(@@#   *           ..   
        &                        ,(    
         #                      (.     
          %                   */       
            ,@             /%     
        """)
    elif name == "paper":
        print("""
                 // ,#                 
        ,@@(     /   /                 
       /    %   .,   /      #@,        
        /   (   *    (    .*   %       
        &    /  (    %    (   *        
/ **    ,    &  %    &   #    (        
    @    /   ,. &    /  %    &         
&    (   %    & &   *  %    @          
 %    *. &                 &           
  %    **#                &            
   #              ,%      /            
    /          /&    *&.  &      /@%#&*
     &   *%@*      &       @.*      .
     #            &                  &,
      *          %               ,@    
      &          #            ##       
       /         /          .*         
        #                  ,*          
         #.              .&   
        """)
    elif name == "gameover":
        print("""
                @@@@                    @@@@               
                @@@@                    @@@@               
                   @@@@            (@@@&                   
                   @@@@            (@@@&                   
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
           @@@@@@@@ ** @@@@@@@@@@@@@ @ &@@@@@@@@           
           @@@@@@@@@  @@@@@@@@@@@@@@@  @@@@@@@@@           
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
       @@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@       
       @@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@       
       @@@@    @@@@                     @@@@    @@@@       
       @@@@    @@@@                     @@@@    @@@@       
                   &&&&&&&&    %&&&&&&&&      
                   @@@@@@@@    &@@@@@@@&                   
                   ########    (#######(             

                                                         
   @@@@@@@@#     @@@@@@@@     @@@@@@ @@@@@@  @@@@@@@@@@   
  @@@@          @@@#   @@@@   @@@ @@@@ @@@@  @@@
  @@@@ @@@@@@   @@@#   @@@@   @@@ @@@@ @@@@  @@@@@@@@@@   
  @@@@   @@@@   @@@@@@@@@@@   @@@ @@@@ @@@@  @@@         
   @@@@@@@@@    @@@(   @@@@   @@@ @@@@ @@@@  @@@@@@@@@@   
                                                          
     @@@@@@@@    @@@@   @@@@   @@@@@@@@@@@   @@@@@@@@@     
   &@@@   @@@@   @@@@   @@@@   @@@@          @@@    @@@    
   &@@@   @@@@   @@@@   @@@@   @@@@@@@@@@@   @@@@@@@@@     
   &@@@   @@@@   @@@@@ @@@@@   @@@@          @@@    @@@    
     @@@@@@@@        @@@       @@@@@@@@@@@   @@@    @@@   
          """)
    elif name == "allIn":
        print("""
                  %$$$$$$$$$$$$$$$$$$$$%                                        
                  $$$ $$$$$$$$$$$$$$$$$$                  
                  $$*  $$$$$$$$$$$$$$$$$                  
                  $ $$  $$$$$$$$$$$$$$$$                  
                  $$$$$$$$$$$$$$$$$$$$$$                  
                  $$   $$$$$$$$$$$$$$$$$                 
                  $$ /  $$$*   $$$$$$$$$                 
                  $$$$$$$#       $$$$$$$                  
                  $$$$$$          $$$$$$                  
                  $$$$$%           $$$$$                  
                  $$$$$$$   @ %  &$$  $$                  
                  $$$$$$$$$$  /@$$$$   $                  
                  $$$$$$$$$$$$$$$$$$  $$                  
                  $$$$$$$$$$$$$$$$$$$$$$                  
                  $$$$$$$$$$$$$$$$$..  $                  
                  $$$$$$$$$$$$$$$$$$, $$                  
                  %$$$$$$$$$$$$$$$$$$$$%                   
                                                           
                                                           
      @@@@@&   @@@@    (@@@@        @@@@ @@@@. @@@@#   @@  
      @@@@@    @@@      @@@          @@@  @@@@@ @@@    @@  
     @@@ @@@   @@@      @@@          @@@  @@@@@@@@@    @@  
    @@@@@@@@@  &@@      @@@          @@@  @@@(@@@@@     
   @@@@   @@@@ @@@@@@@@(@@@@@@@@    @@@@ @@@@* @@@@#   @@ 
   ....   .... ........ ........    .... ....   ...  
            """)

play = True
while play :

    #player_choice
    print ("Your point is: " + str(score))
    betting = input("How much are you betting? Enter the amount less than your points: ")
    while (betting > score):
        betting = input("Enter the amount less than your points: ")
    if (betting == score):
        printGraphic("allIn")
    else:
        print("You are betting " + str(betting) + " points.")
    player = raw_input("Enter your choice (rock/paper/scissors): ")
    while (player != "rock" and player != "paper" and player != "scissors"):
        player = raw_input("Enter your choice (rock/paper/scissors): ")

    print("You:")
    printGraphic(player)
    
    #computer_random
    myList = ["rock", "paper", "scissors"]
    computer = random.choice(myList)
    print("Computer:")
    printGraphic(computer)
    #result
    if (player == computer):
        print("Draw!")

    elif player == "rock" and computer == "scissors":
        print("You Won")
        score = score + betting
        print ("Your point is: " + str(score))

    elif player == "scissors" and computer == "paper":
        print("You Won")
        score = score + betting
        print ("Your point is: " + str(score))

    elif player == "paper" and computer == "rock":
        print("You Won")
        score = score + betting
        print ("Your point is: " + str(score))

    else:
        print("You lose")
        score = score - betting
        print ("Your point is: " + str(score))

    #restart
    if (score == 0):
      printGraphic("gameover")
      play = False

    else:
      userInput = raw_input("Another Round? yes or no: ")
      if (userInput == "no"):
          play = False
          print("See you later.")
      else:
          play = True



 