const express = require('express');
const APP = express();
const PORT = 3000;

APP.get('/', (req, res) => res.send('<h1>Hello World!</h1>'));

APP.listen(PORT, () => console.log(`Listening on ${PORT}...`));