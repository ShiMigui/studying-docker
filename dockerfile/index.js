const express = require('express');
const path = require('path');
const fs = require('fs');
const APP = express();
const PORT = 3000;

APP.get('/', (req, res) => res.send("<h1>Hello world!</h1><a href='./duck'>Duck</a>"));

const LINK = 'https://hips.hearstapps.com/hmg-prod/images/how-to-keep-ducks-call-ducks-1615457181.jpg';
APP.get('/duck', (req, res) => res.send(`<img src='${LINK}' alt='A duck image'/><h1>I am a duck! Quack</h1><a href='../'>Home</a>`));

APP.listen(PORT, () => console.log(`Listening on ${PORT}...`));