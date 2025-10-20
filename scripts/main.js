let playerOneName = "";
let playerOneScore = 0;

let playerTwoName = "";
let playerTwoScore = 0;

function end() {
  // This is how the winner is decided
  const btn = document.getElementById("play");
  btn.disabled = true;
  console.log(" The Game has been Stopped ");
  const game_winner = document.getElementById("Winner");
  if (playerOneScore > playerTwoScore) {
    game_winner.innerHTML = playerOneName + " wins! ";
  } else {
    game_winner.innerHTML = playerTwoName + " wins! ";
  }
  if (playerOneScore === playerTwoScore) {
    game_winner.innerHTML = " its a tie ";
  }
}
// This is how a player rolls a number and also how their score is worked out
function generateNumber(player) {
  let scoreChange = 0;
  let randomNumber = Math.floor(Math.random() * 6 + 1);
  // We do * 6 since our dice is 6 sided and use the
  // math.floor to truncate the random number to a whole number and + 1
  // so that our numbers are generated from 1-6 instead of 1-5.

  if (randomNumber % 2 == 0) {
    scoreChange += 10;
  } else {
    //This is the logic for adding 10 or -5 from the score
    scoreChange -= 5;
  }

  if (player === 1) {
    playerOneScore += scoreChange;
    playerOneScore = Math.max(playerOneScore, 0);
    console.log(playerOneName + " rolled " + randomNumber);
    console.log(playerOneName + " score is " + playerOneScore);
    const playerOneScoreDiv = document.getElementById("p1score");
    playerOneScoreDiv.innerHTML =
      playerOneName + " 's score is " + playerOneScore;
  }
  // I did this so that there wouldnt be two seperate functions for each player,
  // preventing any duplication of code and making it look much cleaner and easier to read.
  if (player === 2) {
    playerTwoScore += scoreChange;
    playerTwoScore = Math.max(playerTwoScore, 0);
    console.log(playerTwoName + " rolled " + randomNumber);
    console.log(playerTwoName + " score is " + playerTwoScore);
    const playerTwoScoreDiv = document.getElementById("p2score");
    playerTwoScoreDiv.innerHTML =
      playerTwoName + " 's score is " + playerTwoScore;
  }
}

function storeName() {
  const input = document.getElementById("myInput");
  const inputValue = input.value;
  playerOneName = inputValue;
}
//These functions are used to store the names of the players
function storeNameP2() {
  const input2 = document.getElementById("myInput2");
  const inputValue2 = input2.value;
  playerTwoName = inputValue2;
}
function hiderules() {
  document.getElementById("rulestext").style.display = "none";
}
