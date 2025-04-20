const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const gridSize = 20;
const tileCount = canvas.width / gridSize;

let snake = [{ x: 10, y: 10 }];
let direction = { x: 1, y: 0 };  // Start moving to the right
let food = {
  x: Math.floor(Math.random() * tileCount),
  y: Math.floor(Math.random() * tileCount)
};

let gameInterval; // To store the game loop interval

document.getElementById("startBtn").addEventListener("click", startGame);

function startGame() {
  document.getElementById("startBtn").style.display = "none";
  gameInterval = setInterval(gameLoop, 150);
}

function gameLoop() {
  update();
  draw();
}

function update() {
  const head = {
    x: snake[0].x + direction.x,
    y: snake[0].y + direction.y
  };

  if (
    head.x < 0 || head.y < 0 ||
    head.x >= tileCount || head.y >= tileCount ||
    snake.some(seg => seg.x === head.x && seg.y === head.y)
  ) {
    alert("Game Over!");
    clearInterval(gameInterval);
    resetGame();
    return;
  }

  snake.unshift(head);

  if (head.x === food.x && head.y === food.y) {
    food = {
      x: Math.floor(Math.random() * tileCount),
      y: Math.floor(Math.random() * tileCount)
    };
  } else {
    snake.pop();
  }
}

function draw() {
  ctx.fillStyle = "#222";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = "lime";
  snake.forEach(segment => {
    ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
  });

  ctx.fillStyle = "red";
  ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
}

document.addEventListener("keydown", e => {
  switch (e.key) {
    case "ArrowUp": if (direction.y === 0) direction = { x: 0, y: -1 }; break;
    case "ArrowDown": if (direction.y === 0) direction = { x: 0, y: 1 }; break;
    case "ArrowLeft": if (direction.x === 0) direction = { x: -1, y: 0 }; break;
    case "ArrowRight": if (direction.x === 0) direction = { x: 1, y: 0 }; break;
  }
});

function resetGame() {
  snake = [{ x: 10, y: 10 }];
  direction = { x: 1, y: 0 };
  food = {
    x: Math.floor(Math.random() * tileCount),
    y: Math.floor(Math.random() * tileCount)
  };
  document.getElementById("startBtn").style.display = "block";
}
