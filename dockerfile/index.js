const express = require('express');
const path = require('path');
const fs = require('fs');
const APP = express();
const PORT = 3000;

APP.get('/', (req, res) => {
    const CACHE = path.join(__dirname, "cache");
    const INDEX = path.join(CACHE, "index.html");

    if(!fs.existsSync(INDEX)){
        // Simulating a process with a delay
        fs.mkdirSync(CACHE, { recursive: true });
        setTimeout(() => {
            fs.writeFileSync(INDEX, '<h1>Hello, World!</h1>', { encoding: "utf-8" });
            res.sendFile(INDEX);
        }, 3000);
    }
    else res.sendFile(INDEX);
});

APP.listen(PORT, () => console.log(`Listening on ${PORT}...`));