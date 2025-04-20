const board = document.getElementById("board");
let currentPlayer = "X";
let cells = Array(9).fill(null);

function drawBoard() {
  board.innerHTML = "";
  cells.forEach((val, idx) => {
    const cell = document.createElement("div");
    cell.textContent = val;
    cell.addEventListener("click", () => handleMove(idx));
    board.appendChild(cell);
  });
}

function handleMove(i) {
  if (!cells[i]) {
    cells[i] = currentPlayer;
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    drawBoard();
    checkWinner();
  }
}

function checkWinner() {
  const wins = [
    [0,1,2], [3,4,5], [6,7,8],  // rows
    [0,3,6], [1,4,7], [2,5,8],  // cols
    [0,4,8], [2,4,6]            // diagonals
  ];
  for (const [a,b,c] of wins) {
    if (cells[a] && cells[a] === cells[b] && cells[a] === cells[c]) {
      alert(`${cells[a]} wins!`);
      return;
    }
  }
  if (!cells.includes(null)) {
    alert("It's a draw!");
  }
}

function resetGame() {
  cells = Array(9).fill(null);
  drawBoard();
}

drawBoard();