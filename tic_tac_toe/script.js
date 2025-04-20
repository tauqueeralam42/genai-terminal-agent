const board = document.getElementById('board');
let currentPlayer = 'X';
let cells = Array(9).fill(null);

function renderBoard() {
  board.innerHTML = '';
  cells.forEach((cell, index) => {
    const cellDiv = document.createElement('div');
    cellDiv.textContent = cell;
    cellDiv.addEventListener('click', () => makeMove(index));
    board.appendChild(cellDiv);
  });
}

function makeMove(index) {
  if (!cells[index]) {
    cells[index] = currentPlayer;
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    renderBoard();
    checkWinner();
  }
}

function resetGame() {
  cells = Array(9).fill(null);
  currentPlayer = 'X';
  renderBoard();
}

function checkWinner() {
  const winningCombos = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
  ];
  
  for (const combo of winningCombos) {
    const [a,b,c] = combo;
    if (cells[a] && cells[a] === cells[b] && cells[a] === cells[c]) {
      alert(`${cells[a]} wins!`);
      resetGame();
      return;
    }
  }

  if (!cells.includes(null)) {
    alert("It's a draw!");
    resetGame();
  }
}

renderBoard();