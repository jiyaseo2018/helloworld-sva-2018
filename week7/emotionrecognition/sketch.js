var songAngry;
var songSad;
var songHappy;

function preload(){
    songAngry = loadSound("sz.wav");
    songSad = loadSound("sad.mp3");
    songHappy = loadSound("applause.wav");
}


function setup() {
    loadCamera();
    loadTracker();
    loadCanvas(800,600);
}

function draw() {
    getPositions();
    getEmotions();
    
    clear();
    
    noStroke();
    fill(0,150);
    rect(0,0,width,height);
    
    drawPoints();

    if (emotions) {
        // angry=0, sad=1, happy=2
        for (var i = 0;i < predictedEmotions.length;i++) {

            rect(i * 110+20, height-80, 30, -predictedEmotions[i].value * 30);
            setAudio();

              
        }
    }


    // loop();
    
    text("ANGRY", 20, height-40);
    text("SAD", 130, height-40);
    text("HAPPY", 220, height-40);



}


 function setAudio(){    

    var happyV = predictedEmotions[2].value
    var angryV = predictedEmotions[0].value 
    var sadV = predictedEmotions[1].value 


    if(angryV > happyV && angryV > sadV ){
        songAngry.setVolume(0.002);
        songAngry.play();
        // songAngry.setLoop(false);
        songHappy.stop();
        songSad.stop();
    }

     if(sadV > happyV && sadV > angryV ){
        songSad.setVolume(0.002);
        songSad.play();
        songHappy.stop();
        songAngry.stop();
    }

     if(happyV > angryV && happyV > sadV ){
        songHappy.setVolume(0.002);
        songHappy.play();
        songAngry.stop();
        songSad.stop();
    }

    // noLoop();

}


function drawPoints() {
    fill(255);
    for (var i=0; i<positions.length -3; i++) {
        ellipse(positions[i][0], positions[i][1], 2, 2);
    }
}