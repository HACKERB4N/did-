#!/data/data/com.termux/files/usr/bin/python3
from flask import Flask, render_template_string, jsonify, send_file
import random
import datetime
import os

app = Flask(__name__)

# Check if your image exists
IMAGE_PATH = "5955.jpg"
HAS_IMAGE = os.path.exists(IMAGE_PATH)

# Birthday database
BIRTHDAY_DATA = {
    "name": "My Dear Sister (Didi)",
    "date": "18th December",
    "year": 2024,
    "wishes": [
        "May your birthday be as wonderful as you are! 🌟",
        "Wishing you endless joy and happiness! 😊",
        "May all your dreams come true this year! ✨",
        "You deserve the world and more! 🌍",
        "Another year of amazing memories! 💫"
    ],
    "gifts": ["Virtual Hugs 🤗", "Endless Love 💕", "Sweet Memories 📸", "Future Adventures 🚀"],
    "surprises": ["🎂 Cake Time!", "🎉 Party Mode!", "🎁 Gift Unlocked!", "✨ Magic Moment!"],
    "has_image": HAS_IMAGE
}

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎉 Amazing Birthday for Didi! 🎂</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #ff6b6b;
            --secondary: #4ecdc4;
            --accent: #ffe66d;
            --dark: #2d3436;
            --light: #f9f9f9;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            min-height: 100vh;
            color: white;
            overflow-x: hidden;
            padding: 20px;
        }
        
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Header Styles */
        .header {
            text-align: center;
            padding: 30px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
            border: 3px solid gold;
            animation: pulse 2s infinite;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }
        
        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 0 20px gold; }
            50% { transform: scale(1.02); box-shadow: 0 0 40px gold; }
            100% { transform: scale(1); box-shadow: 0 0 20px gold; }
        }
        
        .title {
            font-size: 4em;
            background: linear-gradient(45deg, gold, orange, red);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 5px 15px rgba(0,0,0,0.5);
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 1.8em;
            color: var(--accent);
            margin-bottom: 20px;
        }
        
        /* Photo Gallery */
        .photo-gallery {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 40px 0;
        }
        
        .main-photo-frame {
            width: 100%;
            max-width: 600px;
            margin: 20px auto;
            border: 20px solid;
            border-image: linear-gradient(45deg, gold, orange, red) 1;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 25px 50px rgba(0,0,0,0.5);
            position: relative;
            animation: photoFloat 6s ease-in-out infinite;
        }
        
        @keyframes photoFloat {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            25% { transform: translateY(-10px) rotate(1deg); }
            50% { transform: translateY(-5px) rotate(-1deg); }
            75% { transform: translateY(-10px) rotate(1deg); }
        }
        
        .main-photo-frame::before {
            content: '✨ SPECIAL MOMENT ✨';
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            color: gold;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            z-index: 2;
        }
        
        .main-photo-frame img {
            width: 100%;
            height: 400px;
            object-fit: cover;
            display: block;
            transition: transform 0.5s;
        }
        
        .main-photo-frame:hover img {
            transform: scale(1.05);
        }
        
        .photo-caption {
            text-align: center;
            margin-top: 15px;
            font-size: 1.3em;
            color: var(--accent);
            font-style: italic;
        }
        
        .thumbnail-container {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        
        .thumbnail {
            width: 80px;
            height: 80px;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            border: 3px solid transparent;
            transition: all 0.3s;
        }
        
        .thumbnail:hover {
            transform: scale(1.1);
            border-color: gold;
        }
        
        .thumbnail.active {
            border-color: var(--primary);
            box-shadow: 0 0 15px var(--primary);
        }
        
        .thumbnail img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        /* Countdown Timer */
        .countdown-container {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            margin: 30px 0;
            backdrop-filter: blur(5px);
        }
        
        .countdown {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        
        .countdown-item {
            background: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 15px;
            min-width: 100px;
            text-align: center;
            animation: float 3s infinite;
        }
        
        .countdown-value {
            font-size: 3em;
            font-weight: bold;
            color: gold;
        }
        
        .countdown-label {
            font-size: 1em;
            color: #ccc;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        /* Interactive Cards */
        .cards-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin: 40px 0;
        }
        
        .card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
            cursor: pointer;
            transition: all 0.3s ease;
            min-height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        .card:hover {
            transform: translateY(-10px) scale(1.05);
            background: rgba(255, 255, 255, 0.25);
            border-color: gold;
            box-shadow: 0 15px 30px rgba(0,0,0,0.4);
        }
        
        .card-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .card-title {
            font-size: 1.5em;
            margin-bottom: 10px;
            color: var(--accent);
        }
        
        /* Message Box */
        .message-box {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 20px;
            padding: 30px;
            margin: 30px 0;
            text-align: center;
            border: 2px dashed gold;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .message-box:hover {
            background: rgba(0, 0, 0, 0.7);
            transform: scale(1.02);
        }
        
        #messageText {
            font-size: 1.8em;
            min-height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Controls */
        .controls {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin: 30px 0;
        }
        
        .btn {
            padding: 18px 35px;
            font-size: 1.2em;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        
        .btn:hover {
            transform: translateY(-5px) scale(1.1);
            box-shadow: 0 15px 30px rgba(0,0,0,0.3);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        /* Floating Elements */
        .floating-elements {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }
        
        .floating {
            position: absolute;
            font-size: 2em;
            animation: floatAround 20s linear infinite;
        }
        
        @keyframes floatAround {
            0% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(100vw, 25vh) rotate(90deg); }
            50% { transform: translate(50vw, 75vh) rotate(180deg); }
            75% { transform: translate(0, 50vh) rotate(270deg); }
            100% { transform: translate(0, 0) rotate(360deg); }
        }
        
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
        }
        
        .hearts {
            font-size: 2em;
            animation: heartbeat 1s infinite;
        }
        
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.2); }
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .title { font-size: 2.5em; }
            .countdown { flex-wrap: wrap; }
            .countdown-item { min-width: 80px; padding: 15px; }
            .countdown-value { font-size: 2em; }
            .btn { padding: 15px 25px; font-size: 1em; }
            .main-photo-frame { max-width: 95%; }
            .main-photo-frame img { height: 300px; }
        }
        
        /* Image Status */
        .image-status {
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            text-align: center;
            font-weight: bold;
        }
        
        .status-success {
            background: rgba(46, 204, 113, 0.3);
            color: #2ecc71;
        }
        
        .status-warning {
            background: rgba(241, 196, 15, 0.3);
            color: #f1c40f;
        }
    </style>
</head>
<body>
    <div class="floating-elements" id="floatingElements"></div>
    
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1 class="title">🎂 HAPPY BIRTHDAY DIDI! 🎉</h1>
            <p class="subtitle">The Most Amazing Sister in the World! 💖</p>
            <p style="font-size: 1.5em;">📅 Celebrating on <strong>18th December</strong></p>
            
            <!-- Image Status -->
            <div class="image-status {{ 'status-success' if has_image else 'status-warning' }}">
                {% if has_image %}
                ✅ Your personal photo is loaded successfully!
                {% else %}
                ⚠️ Using default photo (Add 5955.jpg to same directory)
                {% endif %}
            </div>
        </div>
        
        <!-- Photo Gallery Section -->
        <div class="photo-gallery">
            <h2 style="text-align: center; margin-bottom: 20px; font-size: 2em;">📸 Birthday Memories</h2>
            
            <div class="main-photo-frame">
                {% if has_image %}
                <img src="/get_photo" alt="Happy Birthday Didi!" id="mainPhoto">
                {% else %}
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80" 
                     alt="Birthday Celebration" 
                     id="mainPhoto">
                {% endif %}
            </div>
            
            <div class="photo-caption" id="photoCaption">
                {% if has_image %}
                💝 My beautiful sister on her special day! 💝
                {% else %}
                🎉 Celebrating the amazing person you are! 🎉
                {% endif %}
            </div>
            
            <!-- Thumbnails (for multiple photos if added later) -->
            <div class="thumbnail-container">
                <div class="thumbnail active" onclick="changePhoto('/get_photo', '💝 My beautiful sister! 💝')">
                    {% if has_image %}
                    <img src="/get_photo?thumb=true" alt="Didi">
                    {% else %}
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=100&q=80" alt="Default">
                    {% endif %}
                </div>
                <!-- Add more thumbnails here if you have more photos -->
            </div>
        </div>
        
        <!-- Countdown Timer -->
        <div class="countdown-container">
            <h2 style="text-align: center; margin-bottom: 20px;">⏳ Birthday Countdown</h2>
            <div class="countdown">
                <div class="countdown-item">
                    <div class="countdown-value" id="hours">00</div>
                    <div class="countdown-label">Hours</div>
                </div>
                <div class="countdown-item">
                    <div class="countdown-value" id="minutes">00</div>
                    <div class="countdown-label">Minutes</div>
                </div>
                <div class="countdown-item">
                    <div class="countdown-value" id="seconds">00</div>
                    <div class="countdown-label">Seconds</div>
                </div>
            </div>
        </div>
        
        <!-- Interactive Cards -->
        <div class="cards-container">
            <div class="card" onclick="showSurprise('cake')">
                <div class="card-icon">🎂</div>
                <div class="card-title">Virtual Cake</div>
                <p>Cut the birthday cake with Didi!</p>
            </div>
            
            <div class="card" onclick="showSurprise('gift')">
                <div class="card-icon">🎁</div>
                <div class="card-title">Open Gifts</div>
                <p>Special gifts for special sister!</p>
            </div>
            
            <div class="card" onclick="showSurprise('music')">
                <div class="card-icon">🎵</div>
                <div class="card-title">Birthday Music</div>
                <p>Play happy birthday song!</p>
            </div>
            
            <div class="card" onclick="showSurprise('photo')">
                <div class="card-icon">📸</div>
                <div class="card-title">Photo Album</div>
                <p>View more memories!</p>
            </div>
        </div>
        
        <!-- Message Box -->
        <div class="message-box" onclick="changeMessage()">
            <h3>💌 Birthday Wishes</h3>
            <div id="messageText">Click here for special birthday wishes!</div>
        </div>
        
        <!-- Controls -->
        <div class="controls">
            <button class="btn" onclick="startConfetti()">
                <i class="fas fa-birthday-cake"></i> Party Time!
            </button>
            <button class="btn" onclick="changeTheme()">
                <i class="fas fa-palette"></i> Change Theme
            </button>
            <button class="btn" onclick="downloadPhoto()">
                <i class="fas fa-download"></i> Save Photo
            </button>
            <button class="btn" onclick="sendWish()">
                <i class="fas fa-heart"></i> Send Love
            </button>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <div class="hearts">💖💖💖</div>
            <p>Made with ❤️ PRAKASH </p>
            <p>For the world's best sister - Happy Birthday Didi!</p>
            <p style="margin-top: 15px; font-size: 0.9em; color: #ccc;">
                {% if has_image %}
                📸 Personal photo loaded: 5955.jpg
                {% else %}
                📸 Add 5955.jpg to see personal photo
                {% endif %}
                | Server: Flask | Host: 0.0.0.0:5000
            </p>
        </div>
    </div>
    
    <!-- Canvas for Effects -->
    <canvas id="confettiCanvas" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;display:none;"></canvas>
    
    <script>
        // Birthday Messages
        const messages = {{ messages|tojson }};
        const gifts = {{ gifts|tojson }};
        const surprises = {{ surprises|tojson }};
        const hasImage = {{ has_image|tojson }};
        
        let currentMessage = 0;
        let currentTheme = 0;
        
        // Initialize floating elements
        function initFloatingElements() {
            const container = document.getElementById('floatingElements');
            const emojis = ['🎂', '🎉', '🎁', '✨', '💖', '🎈', '🥳', '🎊'];
            
            for(let i = 0; i < 15; i++) {
                const element = document.createElement('div');
                element.className = 'floating';
                element.textContent = emojis[Math.floor(Math.random() * emojis.length)];
                element.style.left = Math.random() * 100 + 'vw';
                element.style.top = Math.random() * 100 + 'vh';
                element.style.animationDelay = Math.random() * 5 + 's';
                element.style.fontSize = (Math.random() * 2 + 1) + 'em';
                container.appendChild(element);
            }
        }
        
        // Countdown Timer
        function updateCountdown() {
            const now = new Date();
            const target = new Date(now);
            target.setHours(23, 59, 59, 999);
            
            const diff = target - now;
            
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((diff % (1000 * 60)) / 1000);
            
            document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
            document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
            document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
        }
        
        // Change Message
        function changeMessage() {
            currentMessage = (currentMessage + 1) % messages.length;
            const messageBox = document.getElementById('messageText');
            messageBox.textContent = messages[currentMessage];
            
            // Add animation
            messageBox.style.animation = 'none';
            setTimeout(() => {
                messageBox.style.animation = 'pulse 0.5s';
            }, 10);
        }
        
        // Change Photo
        function changePhoto(src, caption) {
            const mainPhoto = document.getElementById('mainPhoto');
            const captionElement = document.getElementById('photoCaption');
            
            // Add fade effect
            mainPhoto.style.opacity = '0.5';
            setTimeout(() => {
                mainPhoto.src = src;
                captionElement.textContent = caption;
                mainPhoto.style.opacity = '1';
            }, 300);
            
            // Update active thumbnail
            document.querySelectorAll('.thumbnail').forEach(thumb => {
                thumb.classList.remove('active');
            });
            event.currentTarget.classList.add('active');
        }
        
        // Show Surprise
        function showSurprise(type) {
            let message = '';
            switch(type) {
                case 'cake':
                    message = '🎂 Cutting the cake! Make a wish Didi!';
                    startConfetti();
                    break;
                case 'gift':
                    message = '🎁 Special gift for you: ' + gifts[Math.floor(Math.random() * gifts.length)];
                    break;
                case 'music':
                    message = '🎵 Playing Happy Birthday song for Didi!';
                    try {
                        const audio = new Audio('https://assets.mixkit.co/music/preview/mixkit-happy-birthday-to-you-443.mp3');
                        audio.play();
                    } catch(e) {
                        console.log('Audio play failed');
                    }
                    break;
                case 'photo':
                    message = '📸 Creating photo album for Didi!';
                    if(hasImage) {
                        // Show photo in fullscreen
                        const img = document.getElementById('mainPhoto');
                        const fullscreen = document.createElement('div');
                        fullscreen.style.cssText = `
                            position: fixed;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 100%;
                            background: rgba(0,0,0,0.9);
                            z-index: 10000;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            cursor: pointer;
                        `;
                        fullscreen.innerHTML = `
                            <img src="${img.src}" style="max-width: 90%; max-height: 90%; border: 5px solid gold; border-radius: 10px;">
                            <div style="position: absolute; top: 20px; right: 20px; color: white; font-size: 2em; cursor: pointer;">×</div>
                        `;
                        fullscreen.onclick = () => fullscreen.remove();
                        document.body.appendChild(fullscreen);
                    }
                    break;
            }
            
            if(message) {
                // Show as notification instead of alert
                showNotification(message);
            }
        }
        
        // Show Notification
        function showNotification(message) {
            const notification = document.createElement('div');
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: rgba(0,0,0,0.8);
                color: white;
                padding: 15px 25px;
                border-radius: 10px;
                border-left: 5px solid gold;
                z-index: 10001;
                animation: slideIn 0.3s ease;
                max-width: 300px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            `;
            
            // Add CSS for animation
            if (!document.getElementById('notificationStyle')) {
                const style = document.createElement('style');
                style.id = 'notificationStyle';
                style.textContent = `
                    @keyframes slideIn {
                        from { transform: translateX(100%); opacity: 0; }
                        to { transform: translateX(0); opacity: 1; }
                    }
                `;
                document.head.appendChild(style);
            }
            
            notification.textContent = message;
            document.body.appendChild(notification);
            
            // Remove after 3 seconds
            setTimeout(() => {
                notification.style.animation = 'slideIn 0.3s ease reverse';
                setTimeout(() => notification.remove(), 300);
            }, 3000);
        }
        
        // Confetti Effect
        function startConfetti() {
            const canvas = document.getElementById('confettiCanvas');
            canvas.style.display = 'block';
            const ctx = canvas.getContext('2d');
            
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            
            const confettiPieces = [];
            const colors = ['#ff6b6b', '#4ecdc4', '#ffe66d', '#ff9ff3', '#54a0ff', '#5f27cd'];
            
            class Confetti {
                constructor() {
                    this.x = Math.random() * canvas.width;
                    this.y = Math.random() * canvas.height - canvas.height;
                    this.size = Math.random() * 10 + 5;
                    this.speedX = Math.random() * 6 - 3;
                    this.speedY = Math.random() * 3 + 5;
                    this.color = colors[Math.floor(Math.random() * colors.length)];
                    this.shape = Math.random() > 0.5 ? 'circle' : 'rect';
                }
                
                update() {
                    this.x += this.speedX;
                    this.y += this.speedY;
                    if (this.y > canvas.height) {
                        this.y = 0;
                        this.x = Math.random() * canvas.width;
                    }
                }
                
                draw() {
                    ctx.fillStyle = this.color;
                    if (this.shape === 'circle') {
                        ctx.beginPath();
                        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                        ctx.fill();
                    } else {
                        ctx.fillRect(this.x, this.y, this.size, this.size);
                    }
                }
            }
            
            // Create confetti
            for (let i = 0; i < 150; i++) {
                confettiPieces.push(new Confetti());
            }
            
            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                for (let i = 0; i < confettiPieces.length; i++) {
                    confettiPieces[i].update();
                    confettiPieces[i].draw();
                }
                
                requestAnimationFrame(animate);
            }
            
            animate();
            
            // Stop after 10 seconds
            setTimeout(() => {
                canvas.style.display = 'none';
            }, 10000);
        }
        
        // Change Theme
        function changeTheme() {
            const themes = [
                'linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab)',
                'linear-gradient(-45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4)',
                'linear-gradient(-45deg, #5f27cd, #341f97, #ee5a24, #feca57)',
                'linear-gradient(-45deg, #00d2d3, #54a0ff, #5f27cd, #c8d6e5)'
            ];
            
            currentTheme = (currentTheme + 1) % themes.length;
            document.body.style.background = themes[currentTheme];
        }
        
        // Download Photo
        function downloadPhoto() {
            if(hasImage) {
                const link = document.createElement('a');
                link.href = '/download_photo';
                link.download = 'birthday_photo_didi.jpg';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                showNotification('📸 Photo download started!');
            } else {
                showNotification('⚠️ Add 5955.jpg to download');
            }
        }
        
        // Send Wish
        function sendWish() {
            const hearts = ['💖', '💕', '💝', '💓', '💗'];
            for(let i = 0; i < 20; i++) {
                setTimeout(() => {
                    const heart = document.createElement('div');
                    heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
                    heart.style.position = 'fixed';
                    heart.style.left = Math.random() * 100 + 'vw';
                    heart.style.top = '100vh';
                    heart.style.fontSize = '2em';
                    heart.style.zIndex = '1000';
                    heart.style.animation = `fall ${Math.random() * 2 + 2}s linear forwards`;
                    
                    document.body.appendChild(heart);
                    
                    // Remove after animation
                    setTimeout(() => heart.remove(), 3000);
                }, i * 100);
            }
            
            // Add CSS for falling animation
            if (!document.getElementById('fallStyle')) {
                const style = document.createElement('style');
                style.id = 'fallStyle';
                style.textContent = `
                    @keyframes fall {
                        to {
                            transform: translateY(-100vh) rotate(360deg);
                            opacity: 0;
                        }
                    }
                `;
                document.head.appendChild(style);
            }
        }
        
        // Initialize everything
        window.onload = function() {
            initFloatingElements();
            updateCountdown();
            setInterval(updateCountdown, 1000);
            
            // Auto-change message every 15 seconds
            setInterval(changeMessage, 15000);
            
            // Auto-show confetti every 45 seconds
            setInterval(startConfetti, 45000);
            
            console.log('🎉 Birthday Website Loaded with Personal Photo!');
            
            // If image exists, add some special effects
            if(hasImage) {
                setTimeout(() => {
                    showNotification('📸 Your personal photo is displayed!');
                }, 1000);
            }
        };
    </script>
</body>
</html>
    ''', 
    messages=BIRTHDAY_DATA['wishes'],
    gifts=BIRTHDAY_DATA['gifts'],
    surprises=BIRTHDAY_DATA['surprises'],
    has_image=HAS_IMAGE)

@app.route('/get_photo')
def get_photo():
    if HAS_IMAGE:
        return send_file(IMAGE_PATH, mimetype='image/jpeg')
    else:
        # Return default image
        return send_file("https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80", 
                        mimetype='image/jpeg')

@app.route('/download_photo')
def download_photo():
    if HAS_IMAGE:
        return send_file(IMAGE_PATH, 
                        mimetype='image/jpeg',
                        as_attachment=True,
                        download_name='birthday_didi_photo.jpg')
    else:
        return "Photo not found", 404

@app.route('/api/data')
def get_data():
    return jsonify(BIRTHDAY_DATA)

@app.route('/health')
def health():
    return jsonify({
        "status": "✅ Running",
        "has_image": HAS_IMAGE,
        "image_path": IMAGE_PATH if HAS_IMAGE else "Not found",
        "server": "Flask",
        "port": 5000,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == '__main__':
    print("\n" + "🎂" * 50)
    print("🎉 PERSONAL BIRTHDAY WEBSITE WITH YOUR PHOTO 🎉")
    print("🎂" * 50)
    
    if HAS_IMAGE:
        print(f"\n✅ Found your photo: {IMAGE_PATH}")
        print("📸 Photo will be displayed on the website!")
    else:
        print(f"\n⚠️  Photo '{IMAGE_PATH}' not found!")
        print("   Place 5955.jpg in current directory")
        print("   Using default image for now")
    
    print("\n✅ Server running at:")
    print("   🌐 http://127.0.0.1:5000")
    print("   📱 http://localhost:5000")
    
    print("\n✨ Features with YOUR Photo:")
    print("   • Your photo in animated frame")
    print("   • Download option")
    print("   • Fullscreen view")
    print("   • Special effects")
    
    print("\n🛑 Press Ctrl+C to stop")
    print("🎂" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
