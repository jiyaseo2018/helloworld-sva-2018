const ballSpeed = 6;
const BALL_RADIUS = 15;

const PADDLE_WIDTH = 15;
const PADDLE_HEIGHT = 100;

var player1Position, player2Position;
var player1Velocity, player2Velocity;
var player1Score, player2Score;

var ball, ballVelocity;

function setup() {

  createCanvas(800, 400);

  player1Position = player2Position = height / 2 - 50; 

  player1Velocity = player2Velocity = 0;
  player1Score = player2Score = 0;

  ball = createVector(width / 2, height / 2); 
  ballVelocity = createVector(random(-1, 1), random(-1, 1)); 
  ballVelocity.setMag(ballSpeed); 
  
  textAlign(CENTER);
  textSize(30);
  fill(255);
}

function draw() {

  background(210, 80, 80)
  line(width / 2, 60, width / 2, height);
  stroke(126);
  rect(PADDLE_WIDTH * 2, player1Position, PADDLE_WIDTH, PADDLE_HEIGHT);
  rect(width - (PADDLE_WIDTH * 3), player2Position, PADDLE_WIDTH, PADDLE_HEIGHT);
  ellipse(ball.x, ball.y, BALL_RADIUS);
  text(player1Score + "  :  " + player2Score, width / 2, 40);
  handlePaddles();
  handleBall();
  gameOver();
}


function handlePaddles() {

  if (keyIsDown(87)) {
    player1Velocity -= 5;
  } else if (keyIsDown(83)) {
    player1Velocity += 5;
  }

  if (keyIsDown(UP_ARROW)) {
    player2Velocity -= 5;
  } else if (keyIsDown(DOWN_ARROW)) {
    player2Velocity += 5;
  }

  player1Position += player1Velocity;
  player2Position += player2Velocity;

  player1Velocity *= 0.6;
  player2Velocity *= 0.6;

  player1Position = constrain(player1Position, 0, height - PADDLE_HEIGHT);
  player2Position = constrain(player2Position, 0, height - PADDLE_HEIGHT);
}


function handleBall() {

  ball.x += ballVelocity.x;
  ball.y += ballVelocity.y;

  if (ball.y > height || ball.y < 0)
    ballVelocity.y *= -1; 

  if (ball.x <= PADDLE_WIDTH * 3) { 
    if (ball.x <= PADDLE_WIDTH) {

      player2Score++;
      reset();
      return;
    }

    if (ball.y > player1Position && ball.y < player1Position + PADDLE_HEIGHT) {
      if (ballVelocity.x < 0) { 
        ballVelocity.x *= -1;
        ballVelocity.mult(random(1, 1.1));
      }
    }

  } else if (ball.x >= width - (PADDLE_WIDTH * 3)) { 
    if (ball.x >= width - PADDLE_WIDTH) { 
      player1Score++;
      reset();
      return;
    }
    if (ball.y > player2Position && ball.y < player2Position + PADDLE_HEIGHT) {
      if (ballVelocity.x > 0) {
        ballVelocity.x *= -1;
        ballVelocity.mult(random(1, 1.1));
      }
    }

  }

}

function reset() {
  ballVelocity.setMag(ballSpeed);
  ball = createVector(width / 2, height / 2); 
}

function gameOver() {
  if (player1Score == 5) {
    noLoop();
    player1Score == "Player1 Win!";
    }
    else if (player2Score == 5) {
    noLoop();
    player2Score == "Player2 Win!";
    }
}