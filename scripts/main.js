let playerOneName = "";
let playerOneScore = 0;

let playerTwoName = "";
let playerTwoScore = 0;

function generateNumberforP1() {
  let randnum = Math.floor(Math.random() * 6 + 1);
  if (randnum % 2 == 0) {
    playerOneScore += 10;
  } else {
    playerOneScore -= 5;
  }
  playerOneScore += randnum;
  playerOneScore = Math.max(playerOneScore, 0);
  console.log(playerOneName + " rolled " + randnum);
  console.log(playerOneName + "score is " + playerOneScore);
  const playerOneScoreDiv = document.getElementById("p1score");
  playerOneScoreDiv.innerHTML =
    playerOneName + " 's score is " + playerOneScore;
}

function generateNumber(player) {
  let scoreChange = 0;
  let randomNumber = Math.floor(Math.random() * 6 + 1);

  if (randomNumber % 2 == 0) {
    scoreChange += 10;
  } else {
    scoreChange -= 5;
  }

  if (player === 1) {
    playerOneScore += scoreChange;
    playerOneScore = Math.max(playerOneScore, 0);
    console.log(playerOneName + " rolled " + randomNumber);
    console.log(playerOneName + "score is " + playerOneScore);
    const playerOneScoreDiv = document.getElementById("p1score");
    playerOneScoreDiv.innerHTML =
      playerOneName + " 's score is " + playerOneScore;
  }

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

function generateNumberforP2() {
  let randnum2 = Math.floor(Math.random() * 6 + 1);
  if (randnum2 % 2 == 0) {
    playerTwoScore += 10;
  } else {
    playerTwoScore -= 5;
  }
  playerTwoScore += randnum2;
  playerTwoScore = Math.max(playerTwoScore, 0);
  console.log(playerTwoName + " rolled " + randnum2);
  console.log(playerTwoName + " score is " + playerTwoScore);
  const playerTwoScoreDiv = document.getElementById("p2score");
  playerTwoScoreDiv.innerHTML =
    playerTwoName + " 's score is " + playerTwoScore;
}

function storeName() {
  const input = document.getElementById("myInput");
  const inputValue = input.value;
  playerOneName = inputValue;
}

function storeNameP2() {
  const input2 = document.getElementById("myInput2");
  const inputValue2 = input2.value;
  playerTwoName = inputValue2;
}
