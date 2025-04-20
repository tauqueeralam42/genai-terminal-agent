from openai import OpenAI
from dotenv import load_dotenv
import subprocess
import os
import json
import requests
import json
import time
import webbrowser


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# ------------------ Tool Functions ------------------ #
def get_weather(city_name):
    print(f"🔨 Getting weather for: {city_name}")
    url = f"https://wttr.in/{city_name}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city_name} is {response.text.strip()}."
    return "⚠️ Something went wrong while fetching weather."

def run_command(command):
    print(f"💻 Running command: {command}")
    return os.popen(command).read()

def create_python_file(params):
    print(f"🐍 Creating Python file...")
    try:
        data = json.loads(params) if isinstance(params, str) else params
        file_name = data.get("file_name", "script.py")
        code_raw = data.get("code", "print('Hello from Python')")

        # Decode escaped newlines and tabs properly
        code = bytes(code_raw, "utf-8").decode("unicode_escape")

        with open(file_name, "w") as f:
            f.write(code)
        return f"✅ Python file `{file_name}` created successfully."
    except Exception as e:
        return f"❌ Failed to create Python file: {e}"

def create_web_project(folder_name):
    print(f"📁 Creating web project folder: `{folder_name}`...")
    os.makedirs(folder_name, exist_ok=True)

    # HTML
    print("📄 Creating HTML file...")
    time.sleep(2)
    html_code = """<!DOCTYPE html>
<html>
<head>
    <title>My Web Project</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello from HTML!</h1>
    <script src="script.js"></script>
</body>
</html>"""
    with open(os.path.join(folder_name, "index.html"), "w") as f:
        f.write(html_code)
    print("✅ HTML file created!")

    # CSS
    print("🎨 Creating CSS file...")
    time.sleep(2)
    css_code = """body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    text-align: center;
}"""
    with open(os.path.join(folder_name, "style.css"), "w") as f:
        f.write(css_code)
    print("✅ CSS file created!")

    # JS
    print("🧠 Creating JavaScript file...")
    time.sleep(2)
    js_code = """console.log('Hello from JavaScript!');"""
    with open(os.path.join(folder_name, "script.js"), "w") as f:
        f.write(js_code)
    print("✅ JavaScript file created!")

    print("🎉 Your HTML project is ready!")
    return f"🚀 Project successfully created at `{folder_name}`"

def git_push(params):
    print(f"📤 Preparing to push code to GitHub...")
    try:
        data = json.loads(params) if isinstance(params, str) else params
        folder = data.get("folder", ".")
        commit_msg = data.get("message", "🚀 Auto commit from terminal agent")

        cwd = os.getcwd()
        os.chdir(folder)

        print("🔍 Staging changes...")
        os.system("git add .")

        print(f"📝 Committing with message: '{commit_msg}'")
        os.system(f'git commit -m "{commit_msg}"')

        print("☁️ Pushing to remote...")
        os.system("git push")

        os.chdir(cwd)
        return "✅ Code successfully pushed to GitHub! 🎉"
    except Exception as e:
        return f"❌ Git push failed: {e}"

import os
import time

def create_tic_tac_toe_project(folder_name):
    print(f"🎮 Starting Tic-Tac-Toe game setup in: `{folder_name}`")
    os.makedirs(folder_name, exist_ok=True)
    
    # Step 1: Creating HTML
    print("📄 Creating `index.html`...")
    time.sleep(2)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tic Tac Toe</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Tic Tac Toe</h1>
  <div class="board" id="board"></div>
  <button onclick="resetGame()">Reset Game</button>
  <script src="script.js"></script>
</body>
</html>"""
    with open(os.path.join(folder_name, "index.html"), "w") as f:
        f.write(html)
    print("✅ `index.html` created successfully.\n")

    # Step 2: Creating CSS
    print("🎨 Creating `style.css`...")
    time.sleep(2)
    css = """body {
  height: 100vh;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
}

h1 {
  margin-bottom: 20px;
}

.board {
  display: grid;
  grid-template-columns: repeat(3, 100px);
  gap: 5px;
}

.board div {
  width: 100px;
  height: 100px;
  background: #fff;
  border: 2px solid #333;
  font-size: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
}

.board div:hover {
  background: #ddd;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
"""
    with open(os.path.join(folder_name, "style.css"), "w") as f:
        f.write(css)
    print("✅ `style.css` created successfully.\n")

    # Step 3: Creating JS
    print("⚙️ Creating `script.js`...")
    time.sleep(2)
    js = """const board = document.getElementById('board');
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

renderBoard();"""
    with open(os.path.join(folder_name, "script.js"), "w") as f:
        f.write(js)
    print("✅ `script.js` created successfully.\n")

    # Final message
    time.sleep(1)
    print("🎉 Your Tic-Tac-Toe project has been set up successfully! Ready to play! 🚀")

# Example usage:
# create_tic_tac_toe_project("tic_tac_toe")


def create_snake_game_project(folder_name):
    print(f"🐍 Starting Snake Game project in: `{folder_name}`")
    os.makedirs(folder_name, exist_ok=True)

    # HTML
    print("📄 Creating `index.html`...")
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Snake Game</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Snake Game</h1>
  <button id="startBtn">Start Game</button>
  <canvas id="game" width="400" height="400"></canvas>
  <script src="script.js"></script>
</body>
</html>"""
    with open(os.path.join(folder_name, "index.html"), "w") as f:
        f.write(html)
    time.sleep(2)
    print("✅ `index.html` created.")

    # CSS
    print("🎨 Creating `style.css`...")
    css = """body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
  background-color: #f0f0f0;
  font-family: Arial, sans-serif;
}

h1 {
  margin-bottom: 20px;
}

canvas {
  background-color: #222;
  border: 2px solid #444;
  margin-top: 20px;
}

#startBtn {
  margin-bottom: 20px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

#startBtn:hover {
  background-color: #45a049;
}
"""
    with open(os.path.join(folder_name, "style.css"), "w") as f:
        f.write(css)
    time.sleep(2)
    print("✅ `style.css` created.")

    # JavaScript
    print("⚙️ Creating `script.js`...")
    js = """const canvas = document.getElementById("game");
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
"""
    with open(os.path.join(folder_name, "script.js"), "w") as f:
        f.write(js)
    time.sleep(2)
    print("✅ `script.js` created.")

    print("🎉 Snake Game setup complete! You’re ready to slither! 🐍🎮")

    return f"✅ Project created in `{folder_name}`"

    print(f"🐍 Creating Snake Game in folder: {folder_name}")
    os.makedirs(folder_name, exist_ok=True)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Snake Game</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Snake Game</h1>
  <button id="startBtn">Start Game</button>
  <canvas id="game" width="400" height="400"></canvas>
  <script src="script.js"></script>
</body>
</html>
"""

    css = """body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
  background-color: #f0f0f0;
  font-family: Arial, sans-serif;
}

h1 {
  margin-bottom: 20px;
}

canvas {
  background-color: #222;
  border: 2px solid #444;
  margin-top: 20px;
}

#startBtn {
  margin-bottom: 20px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

#startBtn:hover {
  background-color: #45a049;
}
"""

    js = """const canvas = document.getElementById("game");
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

// Start the game when the "Start Game" button is clicked
document.getElementById("startBtn").addEventListener("click", startGame);

// Start the game loop
function startGame() {
  document.getElementById("startBtn").style.display = "none"; // Hide the Start button once the game begins
  gameInterval = setInterval(gameLoop, 150);  // Start the game loop
}

// Game loop: Update and draw the game
function gameLoop() {
  update();
  draw();
}

// Update the snake's position and check for collisions
function update() {
  const head = {
    x: snake[0].x + direction.x,
    y: snake[0].y + direction.y
  };

  // Game over conditions (wall collision or self collision)
  if (
    head.x < 0 || head.y < 0 ||
    head.x >= tileCount || head.y >= tileCount ||
    snake.some(seg => seg.x === head.x && seg.y === head.y)
  ) {
    alert("Game Over!");
    clearInterval(gameInterval); // Stop the game loop
    resetGame(); // Reset the game state
    return;
  }

  snake.unshift(head);  // Add new head to snake

  // Check if snake eats the food
  if (head.x === food.x && head.y === food.y) {
    food = {
      x: Math.floor(Math.random() * tileCount),
      y: Math.floor(Math.random() * tileCount)
    };
  } else {
    snake.pop();  // Remove the last segment of the snake if it didn't eat food
  }
}

// Draw the game (snake and food)
function draw() {
  ctx.fillStyle = "#222";  // Background color
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Draw the snake
  ctx.fillStyle = "lime";
  snake.forEach(segment => {
    ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
  });

  // Draw the food
  ctx.fillStyle = "red";
  ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
}

// Listen for arrow keys to change snake's direction
document.addEventListener("keydown", e => {
  switch (e.key) {
    case "ArrowUp": if (direction.y === 0) direction = { x: 0, y: -1 }; break;
    case "ArrowDown": if (direction.y === 0) direction = { x: 0, y: 1 }; break;
    case "ArrowLeft": if (direction.x === 0) direction = { x: -1, y: 0 }; break;
    case "ArrowRight": if (direction.x === 0) direction = { x: 1, y: 0 }; break;
  }
});

// Reset game state after Game Over
function resetGame() {
  snake = [{ x: 10, y: 10 }];
  direction = { x: 1, y: 0 };  // Reset direction to the right
  food = {
    x: Math.floor(Math.random() * tileCount),
    y: Math.floor(Math.random() * tileCount)
  };
  document.getElementById("startBtn").style.display = "block"; // Show the start button again
}
"""

    with open(os.path.join(folder_name, "index.html"), "w") as f:
        f.write(html)
    with open(os.path.join(folder_name, "style.css"), "w") as f:
        f.write(css)
    with open(os.path.join(folder_name, "script.js"), "w") as f:
        f.write(js)

    return f"✅ Snake game created in folder `{folder_name}`"

def run_html_project(params):
    try:
        data = json.loads(params) if isinstance(params, str) else params
        folder = data.get("folder", ".")
        port = data.get("port", 8000)

        print(f"🚀 Serving HTML project from: `{folder}` on port {port}...")

        # Use subprocess to start the server
        subprocess.Popen(f'start cmd /k "cd {folder} && python -m http.server {port}"', shell=True)

        url = f"http://localhost:{port}"
        time.sleep(2)
        webbrowser.open(url)

        return f"🌍 Project is live at: {url}"
    except Exception as e:
        return f"❌ Failed to run project: {e}"


# ------------------ Tool Registry ------------------ #
available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as input and returns the current weather.",
    },
    "run_command": {
        "fn": run_command,
        "description": "Executes a system command and returns the output.",
    },
    "create_web_project": {
        "fn": create_web_project,
        "description": "Creates a folder with HTML/CSS/JS template.",
    },
    "create_python_file": {
    "fn": create_python_file,
    "description": "Creates a Python file with given name and code content. Input must be a JSON with 'file_name' and 'code'."
    },
    "git_push": {
        "fn": git_push,
        "description": "Commits and pushes code in the given folder. Input must be JSON with 'folder' and optional 'message'."
    },
    "create_tic_tac_toe_project": {
    "fn": create_tic_tac_toe_project,
    "description": "Creates a web-based Tic Tac Toe game in HTML/CSS/JS. Input is the folder name as string."
    },
    "create_snake_game_project": {
    "fn": create_snake_game_project,
    "description": "Creates a Snake Game using HTML/CSS/JS. Input is the folder name."
    },
    "run_html_project": {
    "fn": run_html_project,
    "description": "Serves a static HTML/CSS/JS project using Python's HTTP server. Input must be JSON with 'folder' and optional 'port'."
    }


}

# ------------------ System Prompt ------------------ #
system_prompt = """
    you are a helpfull AI assistant who is specialized in resolving user query
    you work on start,plan,action,observe mode.
    for the given user query and available tools, plan the steps by step execution based on planning,
    select the relevant tool from the available tool and based on the tool selection you perform an action to call the tool
    wait for the observation and based on the observation from the tool resolve user query.
    
    Rules:
    - Follow the output JSON format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query
    
    Available Tools:
    - get_weather : Take a city name as an input and returns the current weather of city,
    - run_command : Take system command and run it and return output of it,
    - create_web_project : Creates a folder with HTML/CSS/JS template.
    - git_push : Pushes code in a folder to GitHub (repo must already be initialized).
    - create_python_file : Creates a Python file with given name and code content. Input must be a JSON with 'file_name' and 'code'.
    - create_tic_tac_toe_project : Creates a web-based Tic Tac Toe game in HTML/CSS/JS. Input is folder name.
    - create_snake_game_project : Creates a Snake Game using HTML/CSS/JS. Input is the folder name.
    - run_html_project : Serves a static HTML/CSS/JS project using Python's HTTP server. Input must be JSON with 'folder' and optional 'port'.
    
    Output Format:
    {
        "step": "string",
        "content": "string",
        "function": "the name of function if step is action",
        "input": "the input parameter for function"
    }
    
    Example:
    user query : What is the weather of new york?
    Output: {"step": "plan", "content": "The user is interested in weather data of new york"}
    Output: {"step": "plan", "content": "From the available tool I should call the get_weather"}
    Output: {"step": "action", "function": "get_weather","input":"new york"}
    Output: {"step": "observation", "output": "12 degree C"}
    Output: {"step": "output", "content": "the weather for new york seems to be 12 degree."}
    
    // USER QUERY:
    Create a Python program that adds two numbers and save it in a file

    // LLM OUTPUT EXAMPLES:
    {"step": "plan", "content": "The user wants a Python program to add numbers saved in a file."}
    {"step": "action","function": "create_python_file","input": "{\"file_name\": \"add_numbers.py\", \"code\": \"def add(a, b):\\n  return a + b\\n\\nnum1 = 5\\nnum2 = 3\\nsum_result = add(num1, num2)\\nprint(f'{num1} + {num2} = {sum_result}')\"}"}
    {"step": "observation", "output": "✅ Python file `add_numbers.py` created successfully."}
    {"step": "output", "content": "Your Python file has been created."}
    
        // USER QUERY:
    Now commit and push that file to my repo

    // LLM OUTPUT EXAMPLES:
    {"step": "plan", "content": "User wants to push changes to Git."}
    {"step": "action", "function": "git_push", "input": "{\"folder\": \".\", \"message\": \"Added add_numbers.py\"}"}
    {"step": "observation", "output": "✅ Code pushed to GitHub."}
    {"step": "output", "content": "Your code is now pushed to GitHub."}
    
    // USER QUERY:
    Create a Tic-Tac-Toe game using html css and js

    // LLM OUTPUT EXAMPLE:
    {"step": "plan", "content": "The user wants a Tic-Tac-Toe game in HTML, CSS, and JS."}
    {"step": "action", "function": "create_tic_tac_toe_project", "input": "tic_tac_toe"}
    {"step": "observation", "output": "✅ Tic-Tac-Toe game project created in `tic_tac_toe`"}
    {"step": "output", "content": "Your Tic-Tac-Toe game project is ready in the folder `tic_tac_toe`."}

    // USER QUERY:
    Create a snake game in html css and js

    // LLM OUTPUT EXAMPLE:
    {"step": "plan", "content": "User wants a Snake Game built with HTML/CSS/JS."}
    {"step": "action", "function": "create_snake_game_project", "input": "snake_game"}
    {"step": "observation", "output": "✅ Snake game created in folder `snake_game`"}
    {"step": "output", "content": "Your Snake game is ready in the folder `snake_game`."}


"""
# ------------------ Initialize Conversation ------------------ #
messages = [{"role": "system", "content": system_prompt}]

# ------------------ Interaction Loop ------------------ #
print("💬 Hey Tauqueer! 😊 What would you like me to help you with today? Just type your message below and I’ll do my magic! ✨")
while True:
    user_input = input("🧑‍💻 -> ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    while True:
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            response_format={"type": "json_object"},
            messages=messages
        )
        # print(response.choices[0].message.content)
        parsed_output = json.loads(response.choices[0].message.content)
        messages.append({"role": "assistant", "content": json.dumps(parsed_output)})

        step = parsed_output.get("step")

        if step == "plan":
            print(f"🧠 Plan: {parsed_output.get('content')}")
            continue

        if step == "action":
            fn_name = parsed_output.get("function")
            fn_input = parsed_output.get("input")

            if fn_name in available_tools:
                result = available_tools[fn_name]["fn"](fn_input)
                messages.append({
                    "role": "assistant",
                    "content": json.dumps({"step": "observation", "output": result})
                })
                continue

        if step == "output":
            print(f"🤖 Output: {parsed_output.get('content')}")
            break
