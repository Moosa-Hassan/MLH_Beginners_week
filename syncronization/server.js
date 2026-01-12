const express = require("express");
const http = require("http");
const WebSocket = require("ws");

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

let poll = { yes: 0, no: 0 };

app.use(express.static("public"));

wss.on("connection", (ws) => {
  // Send current poll state to new user
  ws.send(JSON.stringify(poll));

  ws.on("message", (msg) => {
    const vote = msg.toString();
    if (vote === "yes") poll.yes++;
    if (vote === "no") poll.no++;

    // Broadcast update to all users
    wss.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify(poll));
      }
    });
  });
});

server.listen(3000, () =>
  console.log("Server running on http://localhost:3000")
);
