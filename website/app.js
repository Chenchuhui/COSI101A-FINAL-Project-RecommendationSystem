const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const User = require("./models/user");
const ejs = require('ejs');

const app = express();
const PORT = 3000;

app.set('view engine', 'ejs');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/rsapp', { useNewUrlParser: true, useUnifiedTopology: true });

// Middleware
app.use(bodyParser.json());

// Serve EJS template
app.get('/', (req, res) => {
  res.render('index');
});

// Handle user survey submission
app.post('/survey', (req, res) => {
    const { username, selectedThemes } = req.body;
  
    const user = new User({ username, selectedThemes });
  
    user.save()
    .then(() => {
        res.send('User survey submitted successfully!');
    })
    .catch((err) => {
        console.error(err);
        res.status(500).send('Error saving user and survey response');
    });
      
  });

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
