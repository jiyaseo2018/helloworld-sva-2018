let snowflakes = [];
var serial;
var latestData = "waiting for data"; // you'll use this to write incoming data to the canvas

function setup() {
  createCanvas(500, 600);

  // STEP 1 Instantiate our SerialPort object
  serial = new p5.SerialPort();
	
  // STEP 2 Set port (Get this from p5 serial control app!)
  serial.open("/dev/cu.usbserial-DN051BSQ");

  // STEP 3 set up a callback to read data
  serial.onData(gotData);
  
  fill(240);
  noStroke();

}

// Ok here comes daya!
function gotData() {
  // Step 4a: read the data
  var currentString = serial.readLine(); // read the incoming string
  if (!currentString) return; // if the string is empty, do no more
  latestData = Number(currentString); // save it for the draw method
}

function draw() {
  background('Maroon');
  let t = frameCount / map(latestData, 0, 1023, 10, 200); // update time

  // create a random number of snowflakes each frame
  for (var i = 0; i < random(5); i++) {
    randSize = map(latestData, 0, 1023, 4, 10);
    snowflakes.push(new snowflake(randSize)); // append snowflake object
  }

  // loop through snowflakes with a for..of loop
  for (let flake of snowflakes) {
    flake.update(t); // update snowflake position
    flake.display(); // draw snowflake
  }
  
}
function snowflake(randSize) {
  // initialize coordinates
  this.posX = 0;
  this.posY = random(-50, 0);
  this.initialangle = random(0, 2 * PI);
  this.size = randSize;

  // radius of snowflake spiral
  // chosen so the snowflakes are uniformly spread out in area
  this.radius = sqrt(random(pow(width / 2, 2)));

  this.update = function(time) {
    // x position follows a circle
    let w = 0.6; // angular speed
    let angle = w * time + this.initialangle;
    this.posX = width / 2 + this.radius * sin(angle);

    // different size snowflakes fall at slightly different y speeds
    this.posY += pow(this.size, 0.5);

    // delete snowflake if past end of screen
    if (this.posY > height) {
      let index = snowflakes.indexOf(this);
      snowflakes.splice(index, 1);
    }
  };

  this.display = function() {
    ellipse(this.posX, this.posY, this.size);
  };
}