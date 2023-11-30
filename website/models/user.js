const mongoose = require("mongoose");

const userSchema = new mongoose.Schema({
    username: String,
    selectedThemes: [{
      type: String,
      enum: ['1_Blockchain', '2_DevOps', '3_Fintech', '4_Gaming', '5_AR/VR', '6_Machine Learning/AI', '7_IoT', '8_Voice skills', 
            '9_Cybersecurity', '10_Communication', '11_Productivity', '12_Lifehacks', '13_Social Good', '14_COVID-19', '15_Music/Art', 
            '16_Health', '17_Low/No Code', '18_Design', '19_Education', '20_E-commerce/Retail','21_Enterprise', '22_Open Ended', 
            '23_Beginner Friendly', '24_Quantum', '25_Web', '26_Mobile', '27_Robotic Process Automation', '28_Databases'],
    }],
  });
  
const User = mongoose.model('User', userSchema);
  
module.exports = User;