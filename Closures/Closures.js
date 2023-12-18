const increaseCount = (function() {
  let count = 0;

  return function updateClickCount() {
    count++;
    console.log(`Click count: ${count}`);
  };
})();

// Simulating button clicks
increaseCount(); // Click count: 1
increaseCount(); // Click count: 2
increaseCount(); // Click count: 3
