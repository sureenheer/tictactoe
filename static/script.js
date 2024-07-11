document.addEventListener('DOMContentLoaded', () => {
  const board = document.getElementById('board');
  const resetButton = document.getElementById('resetButton'); // Get the reset button element

  const createBoard = (boardState) => {
      board.innerHTML = ''; // Clear the current board
      for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 3; j++) {
              const cell = document.createElement('div');
              cell.textContent = boardState[i][j];
              cell.addEventListener('click', () => makeMove(i, j)); // Add event listener to each cell
              board.appendChild(cell);
              console.log("boxes are being made")
          }
      }
  };

  const makeMove = (x, y) => {
      fetch('/move', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ x, y }) // Send the cell coordinates to the server
      })
      .then(response => response.json()) // Parse the JSON response
      .then(data => {
          if (data.success) {
              createBoard(data.board); // Update the board with the new state
              if (data.winner) {
                  alert(`Player ${data.winner} won!`); // Notify if there's a winner
              }
          } else {
              alert(data.message); // Show an error message if the move was invalid
          }
      });
  };

  const resetGame = () => {
      fetch('/reset', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              createBoard(data.board); // Reset the board to its initial state
          }
      });
  };

  resetButton.addEventListener('click', resetGame); // Add event listener for reset button

  createBoard([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]); // Initialize the board
});