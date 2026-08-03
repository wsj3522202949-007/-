---
id: tool-01022
type: tool
area: 库
status: active
tags: [TTS, 协议未明, 本地优先, 英文文档, 本地写作]
title: ayuindia.github.io
summary: 小说转语音/有声书
source: https://github.com/ayuindia/ayuindia.github.io
created: 2026-07-18
updated: 2026-07-18
no: 1022
category: 二、网文 / 长篇 AI 写作系统 库
repo: AYUINDIA/ayuindia.github.io
stars: 0
url: https://github.com/ayuindia/ayuindia.github.io
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AYUINDIA/ayuindia.github.io

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ayuindia/ayuindia.github.io
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：AYUINDIA AI is a student-built smart assistant that helps with study, math solving, subject explanations, GK, coding, creative writing, and safe anime info. It features voice input, chat modes, quizzes, and productivity tools in a futuristic interface, designed to make learning faster, easier, and more interactive for students.
- **本地描述**：AYUINDIA AI is a student-built smart assistant that helps with study, math solving, subject explanations, GK, coding, creative writing, and safe anime info. It features voice input, chat modes, quizzes, and productivity tools in a futuristic interface, designed to make learning faster, easier, and more interactive for students.
- **拉取时间**：2026-07-23 23:08:49

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AYUINDIA ULTRA PRO AI</title>

<!-- FUTURISTIC AI FONT -->
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">

<style>
*{box-sizing:border-box}

body{
  margin:0;
  font-family:Orbitron, Arial, sans-serif;
  color:#e5e7eb;
  overflow-x:hidden;
}

/* ===== FUTURISTIC BACKGROUND ===== */
#bgSlide{
  position:fixed;
  inset:0;
  background-size:cover;
  background-position:center;
  z-index:-3;
  transition:background-image 1s ease-in-out;
  filter:brightness(0.35) contrast(1.2);
}

#bgOverlay{
  position:fixed;
  inset:0;
  background:radial-gradient(circle at 30% 30%,#0ea5e933,#020617ee);
  z-index:-2;
}

/* GRID GLOW EFFECT */
#gridFX{
 position:fixed;
 inset:0;
 background-image:linear-gradient(#0ea5e922 1px,transparent 1px),linear-gradient(90deg,#0ea5e922 1px,transparent 1px);
 background-size:60px 60px;
 z-index:-1;
 animation:gridMove 20s linear infinite;
}

@keyframes gridMove{
 from{transform:translateY(0)}
 to{transform:translateY(60px)}
}

/* ===== HEADER ===== */
header{
  text-align:center;
  padding:40px 20px;
  background:#00000066;
  backdrop-filter: blur(8px);
  box-shadow:0 0 40px #0ea5e955 inset;
}

.logo{
  font-size:54px;
  font-weight:900;
  letter-spacing:4px;
  background:linear-gradient(90deg,#38bdf8,#a78bfa,#22d3ee);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  text-shadow:0 0 25px #38bdf8aa;
  animation:glowPulse 3s infinite alternate;
}

@keyframes glowPulse{
 from{text-shadow:0 0 10px #38bdf8aa}
 to{text-shadow:0 0 35px #a78bfaaa}
}

nav{
  display:flex;
  flex-wrap:wrap;
  gap:18px;
  justify-content:center;
  padding:14px;
  background:#00000055;
  position:sticky;
  top:0;
  backdrop-filter:blur(6px);
}

nav a{
  color:#93c5fd;
  text-decoration:none;
  font-weight:bold;
  position:relative;
}

nav a::after{
 content:"";
 position:absolute;
 left:0;
 bottom:-4px;
 width:0%;
 height:2px;
 background:#38bdf8;
 transition:.3s;
}

nav a:hover::after{width:100%}

section{
  max-width:1200px;
  margin:auto;
  padding:60px 20px;
}

.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:22px;
}

.card{
  background:#020617dd;
  border-radius:18px;
  padding:24px;
  box-shadow:0 0 30px #0ea5e933, inset 0 0 20px #000;
  transition:.3s;
  position:relative;
  overflow:hidden;
}

.card::before{
 content:"";
 position:absolute;
 inset:0;
 background:linear-gradient(120deg,transparent, #38bdf833, transparent);
 transform:translateX(-100%);
 transition:.6s;
}

.card:hover::before{transform:translateX(100%)}
.card:hover{transform:translateY(-8px) scale(1.02)}

button{
  padding:12px 18px;
  border-radius:12px;
  border:none;
  font-weight:bold;
  background:linear-gradient(90deg,#2563eb,#06b6d4);
  color:white;
  cursor:pointer;
  box-shadow:0 0 15px #38bdf8aa;
}

button:hover{transform:scale(1.05)}

input,select{
  padding:12px;
  border-radius:10px;
  border:1px solid #38bdf855;
  background:#020617;
  color:white;
  width:100%;
}

/* CHAT */
#messages{
  height:320px;
  overflow-y:auto;
  background:#000814;
  border-radius:12px;
  padding:12px;
  font-size:14px;
  margin-bottom:10px;
  box-shadow:inset 0 0 20px #000;
}

.msgUser{color:#93c5fd}
.msgAI{color:#34d399}

footer{
  text-align:center;
  padding:30px;
  background:#00000066;
  backdrop-filter:blur(6px);
}
</style>
</head>

<body>

<div id="bgSlide"></div>
<div id="bgOverlay"></div>
<div id="gridFX"></div>

<audio id="bgMusic" loop>
  <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8a4a1b7f5.mp3?filename=ambient-110397.mp3" type="audio/mpeg">
</audio>

<header>
  <div class="logo">⚡ AYUINDIA AI ⚡</div>
  <p>Futuristic Student Intelligence System</p>
  <button onclick="startMusic()">Start Music</button>
</header>

<nav>
<a href="#chat">AI Chat</a>
<a href="#study">Study</a>
<a href="#math">Math</a>
<a href="#gk">GK</a>
<a href="#anime">Anime</a>
<a href="#upgrade">Upgrade</a>
<a href="#contact">Contact</a>
</nav>

<section id="chat">
<h2>AI Chat — How can I help u?</h2>
<div class="card">
<div id="messages"></div>
<div style="display:flex;gap:8px;">
<input id="userInput" placeholder="Ask anything…" />
<button onclick="sendMsg()">Send</button>
<button onclick="voiceInput()">🎤</button>
</div>
</div>
</section>

<section id="study">
<h2>Subjects Engine</h2>
<div class="grid">
<div class="card">Math • Science • English • History • Geography • Computers</div>
<div class="card">Explains + quizzes + summaries</div>
<div class="card">Student friendly answers</div>
</div>
</section>

<section id="math">
<h2>Math Solver</h2>
<div class="card">
<input id="mathExp" placeholder="12*8+5" />
<button onclick="solveMath()">Solve</button>
<p id="mathOut"></p>
</div>
</section>

<section id="gk">
<h2>GK Mode</h2>
<div class="card">
<button onclick="gkFact()">Generate Fact</button>
<p id="gkOut"></p>
</div>
</section>

<section id="anime">
<h2>Anime Mode</h2>
<div class="card">
<select id="animePick"><option>Naruto</option><option>One Piece</option><option>Dragon Ball</option></select>
<button onclick="animeInfo()">Show</button>
<p id="animeOut"></p>
</div>
</section>

<section id="upgrade">
<h2>Upgrade ₹100/month</h2>
<div class="card">
<button onclick="fakePay()">Upgrade</button>
<p id="payOut"></p>
</div>
</section>

<section id="contact">
<h2>Contact</h2>
<div class="card">
arcade.avanger@gmail.com — Mail us for any glitch or issue
</div>
</section>

<footer>© AYUINDIA AI</footer>

<script>

const imgs=[
"https://images.unsplash.com/photo-1677442136019-21780ecad995",
"https://images.unsplash.com/photo-1620712943543-bcc4688e7485",
"https://images.unsplash.com/photo-1518770660439-4636190af475",
"https://images.unsplash.com/photo-1535223289827-42f1e9919769",
"https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
"https://images.unsplash.com/photo-1507146153580-69a1fe6d8aa1"
];
let bi=0;
function rotateBG(){document.getElementById("bgSlide").style.backgroundImage=`url(${imgs[bi]})`;bi=(bi+1)%imgs.length;}
rotateBG();setInterval(rotateBG,10000);

function startMusic(){document.getElementById("bgMusic").play();}

const brain={hello:"Hey 😄",anime:"Anime mode ready",math:"Use math solver"};
function aiReply(t){t=t.toLowerCase();for(const k in brain){if(t.includes(k)) return brain[k];}if(/\d+[\+\-*\/]/.test(t)){try{return "Answer = "+eval(t);}catch{}}return "Processing…";}

function sendMsg(){
 const inp=userInput.value.trim(); if(!inp) return;
 messages.innerHTML+=`<div class='msgUser'>You: ${inp}</div>`;
 const r=aiReply(inp);
 setTimeout(()=>{messages.innerHTML+=`<div class='msgAI'>AI: ${r}</div>`;messages.scrollTop=messages.scrollHeight;},300);
 userInput.value="";
}
userInput.addEventListener("keydown",e=>{if(e.key==="Enter") sendMsg();});

function voiceInput(){if(!('webkitSpeechRecognition'in window))return;const r=new webkitSpeechRecognition();r.onresult=e=>{userInput.value=e.results[0][0].transcript;sendMsg();};r.start();}
function solveMath(){try{mathOut.innerText="Result: "+eval(mathExp.value);}catch{mathOut.innerText="Invalid";}}
const gk=["Earth has one moon","Water boils at 100°C","India is in Asia"];function gkFact(){gkOut.innerText=gk[Math.floor(Math.random()*gk.length)];}
const animeDB={Naruto:"Ninja story",'One Piece':"Pirates",'Dragon Ball':"Saiyans"};function animeInfo(){animeOut.innerText=animeDB[animePick.value];}
function fakePay(){payOut.innerText="Upgrade activated (demo)";}

</script>

</body>
</html>
16px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 20px rgba(0,247,255,0.3);
}

/* Chat UI */
#chatBox {
  height: 350px;
  overflow-y: auto;
  border: 1px solid #00f7ff;
  padding: 12px;
  border-radius: 10px;
  margin-bottom: 10px;
}

.msg { margin: 8px 0; }
.user { color: #fff; }
.ai { color: #00f7ff; }

#inputRow {
  display: flex;
  gap: 10px;
}

input, select {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  border: none;
}

button.send {
  padding: 12px 18px;
  border-radius: 8px;
  border: none;
  background: #00f7ff;
  color: black;
  cursor: pointer;
}

.logo {
  font-size: 28px;
  text-align: center;
  margin-bottom: 10px;
}

.upgrade {
  font-size: 20px;
  color: #fff;
}

.toolRow{
 display:flex;
 flex-wrap:wrap;
 gap:10px;
 margin-top:10px;
}
</style>
</head>

<body>
<div class="bg-slide"></div>

<header>⚡ AYUINDIA AI ⚡</header>

<nav>
<button onclick="showTab('chat')">Chat</button>
<button onclick="showTab('features')">Features</button>
<button onclick="showTab('subjects')">Subjects</button>
<button onclick="showTab('tools')">Tools</button>
<button onclick="showTab('anime')">Anime</button>
<button onclick="showTab('upgrade')">Upgrade</button>
<button onclick="showTab('contact')">Contact</button>
</nav>

<section id="chat" class="tab card">
<h2>AI Chat</h2>
<div id="chatBox"></div>
<div id="inputRow">
<input id="userInput" placeholder="How can I help u">
<button class="send" onclick="sendMsg()">Send</button>
<button onclick="voiceInput()">🎤</button>
</div>

<div class="toolRow">
<button onclick="setTone('casual')">Casual</button>
<button onclick="setTone('formal')">Formal</button>
<button onclick="setTone('student')">Student</button>
<button onclick="brainTeaser()">Riddle</button>
<button onclick="makeChecklist()">Checklist</button>
<button onclick="makeQuiz()">Quiz</button>
</div>
</section>

<section id="features" class="tab card" style="display:none">
<h2>All AI Features</h2>
<ul>
<li>Natural smart conversation</li>
<li>Casual / formal / student tone</li>
<li>Math solving + steps</li>
<li>Study help all subjects</li>
<li>Worksheet + test maker</li>
<li>Essay / poem / story writer</li>
<li>Code helper</li>
<li>GK & facts</li>
<li>Anime knowledge (safe)</li>
<li>Quiz & riddles</li>
<li>Timetable builder</li>
<li>Checklist generator</li>
<li>Creative ideas & slogans</li>
</ul>
</section>

<section id="subjects" class="tab card" style="display:none">
<h2>Subjects Knowledge</h2>
<p>Math, Science, English, SST, History, Geography, GK, Computer, Biology, Physics, Chemistry basics supported with student-friendly explanations.</p>
</section>

<section id="tools" class="tab card" style="display:none">
<h2>AI Tools</h2>
<div class="toolRow">
<button onclick="studyPlan()">Study Plan</button>
<button onclick="reviseTips()">Revision Tips</button>
<button onclick="writeEssay()">Essay Idea</button>
<button onclick="storyIdea()">Story Idea</button>
<button onclick="projectIdea()">Project Idea</button>
</div>
<p id="toolOut"></p>
</section>

<section id="anime" class="tab card" style="display:none">
<h2>Anime Info Mode</h2>
<select id="animePick">
<option>Naruto</option>
<option>One Piece</option>
<option>Dragon Ball</option>
</select>
<button onclick="animeInfo()">Show</button>
<p id="animeOut"></p>
</section>

<section id="upgrade" class="tab card" style="display:none">
<h2>AYUINDIA ULTRA Upgrade</h2>
<p class="upgrade">₹100 / month</p>
<ul>
<li>Advanced tools unlocked</li>
<li>Extra creative modes</li>
<li>Priority features (demo)</li>
</ul>
<button class="send" onclick="upgradeDemo()">Upgrade Now</button>
<p id="upOut"></p>
</section>

<section id="contact" class="tab card" style="display:none">
<h2>Contact Us</h2>
<p>Mail us for any glitch or issue:</p>
<p><b>arcade.avanger@gmail.com</b></p>
</section>

<script>
let tone='casual';

function showTab(id){
 document.querySelectorAll('.tab').forEach(t=>t.style.display='none');
 document.getElementById(id).style.display='block';
}

function addMsg(text, cls){
 const box=document.getElementById('chatBox');
 const d=document.createElement('div');
 d.className='msg '+cls;
 d.innerText=text;
 box.appendChild(d);
 box.scrollTop=box.scrollHeight;
}

function setTone(t){
 tone=t;
 addMsg('Tone set to '+t,'ai');
}

function styleReply(msg){
 if(tone==='formal') return 'Response: '+msg;
 if(tone==='student') return 'Easy mode → '+msg;
 return msg+' 😄';
}

function solveStepMath(q){
 try{
  if(/^[0-9+\-*/(). ]+$/.test(q)){
    const ans=eval(q);
    return 'Answer = '+ans;
  }
 }catch{}
 return null;
}

function aiBrain(q){
 const m=solveStepMath(q);
 if(m) return m;
 q=q.toLowerCase();
 if(q.includes('hello')) return styleReply('Hey! Ready to help');
 if(q.includes('math')) return styleReply('Send the full sum');
 if(q.includes('study')) return styleReply('Tell subject + chapter');
 if(q.includes('essay')) return styleReply('I can generate essays');
 if(q.includes('story')) return styleReply('Let’s build a story');
 if(q.includes('anime')) return styleReply('Ask anime name');
 return styleReply('Got it — working on it');
}

function sendMsg(){
 const inp=document.getElementById('userInput');
 if(!inp.value) return;
 addMsg(inp.value,'user');
 const r=aiBrain(inp.value);
 setTimeout(()=>addMsg(r,'ai'),300);
 inp.value='';
}

document.getElementById('userInput').addEventListener('keydown',e=>{
 if(e.key==='Enter') sendMsg();
});

function voiceInput(){
 if(!('webkitSpeechRecognition' in window)){
 alert('Voice not supported'); return;
 }
 const rec=new webkitSpeechRecognition();
 rec.lang='en-IN';
 rec.onresult=e=>{
 document.getElementById('userInput').value=e.results[0][0].transcript;
 sendMsg();
 };
 rec.start();
}

function brainTeaser(){
 const r=[
 'I speak without a mouth — what am I? (Echo)',
 'What has keys but no locks? (Keyboard)',
 'What runs but never walks? (Water)'
 ];
 addMsg(r[Math.floor(Math.random()*r.length)],'ai');
}

function makeChecklist(){
 addMsg('Checklist: Study ✔ Revise ✔ Practice ✔ Test ✔','ai');
}

function makeQuiz(){
 addMsg('Quiz: What is 9×7 ?','ai');
}

function studyPlan(){ toolOut.innerText='Study Plan: 40min study + 10min break × 5'; }
function reviseTips(){ toolOut.innerText='Revise using short notes + self quiz'; }
function writeEssay(){ toolOut.innerText='Essay idea: Future of AI in education'; }
function storyIdea(){ toolOut.innerText='Story idea: Student builds super AI'; }
function projectIdea(){ toolOut.innerText='Project: Build mini chatbot website'; }

const animeDB={Naruto:'Ninja journey','One Piece':'Pirate adventure','Dragon Ball':'Saiyan battles'};
function animeInfo(){ animeOut.innerText=animeDB[animePick.value]; }

function upgradeDemo(){ upOut.innerText='Upgrade activated (demo mode)'; }

addMsg('AYUINDIA AI ready — ask anything.','ai');
</script>

</body>
</html>ut.innerText=animeDB[animePick.value];
}

function fakePay(){
 payOut.innerText="ULTRA mode activated (demo)";
}

/* ================= EXTRA STUDENT TOOLS ================= */

function makeChecklist(){
 addAI("Checklist: Study ✔ Revise ✔ Practice ✔ Sleep ✔");
}

function brainTeaser(){
 const teasers=[
 "I speak without a mouth — what am I? (Echo)",
 "What has keys but no locks? (Keyboard)"
 ];
 addAI(teasers[Math.floor(Math.random()*teasers.length)]);
}

</script>
