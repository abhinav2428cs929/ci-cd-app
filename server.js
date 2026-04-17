const express = require('express');
const app = express();

app.get('/health', (req, res) => {
  res.json({ status: "Server is running" });
});

app.listen(3001, () => {
  console.log("Server running on port 3001");
});
