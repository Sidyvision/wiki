import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, 'library-full.json'), encoding='utf-8') as f:
    LIBRARY = json.load(f)
with open(os.path.join(HERE, 'rooms.json'), encoding='utf-8') as f:
    layout = json.load(f)
with open(os.path.join(HERE, 'three.min.js'), encoding='utf-8') as f:
    THREE_SRC = f.read()

ROOMS = layout['rooms']
CORRIDORS = layout['corridors']

LIBRARY_JSON = json.dumps(LIBRARY, ensure_ascii=False)
ROOMS_JSON = json.dumps(ROOMS, ensure_ascii=False)
CORRIDORS_JSON = json.dumps(CORRIDORS, ensure_ascii=False)

TEMPLATE = r"""<title>Citadelle du Sham</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root{
    --stone-void:#0d0906;
    --stone-wall:#4a3524;
    --floor-lit:#d8bd8a;
    --ember:#d97b34;
    --ember-glow:#ffc072;
    --tile-teal:#2f7a6b;
    --tile-teal-dark:#1f4e46;
    --parchment:#f0e4c4;
    --parchment-edge:#d9c294;
    --parchment-shadow:#c4ac7c;
    --ink:#2b2013;
    --ink-soft:#6b5738;
    --accent:#c9702f;
    --font-display:Cambria,"Iowan Old Style","Palatino Linotype","Book Antiqua",Georgia,serif;
    --font-ui:"Avenir Next","Segoe UI","Helvetica Neue",Arial,sans-serif;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden;background:var(--stone-void);
    font-family:var(--font-ui);-webkit-tap-highlight-color:transparent;}
  #app{position:fixed;inset:0;background:var(--stone-void);}
  #game{position:absolute;inset:0;width:100%;height:100%;display:block;touch-action:none;cursor:grab;}
  #game:active{cursor:grabbing;}
  #minimap{position:absolute;top:14px;right:14px;width:150px;height:130px;border-radius:6px;
    background:rgba(13,9,6,.72);border:1px solid rgba(216,189,138,.35);box-shadow:0 4px 18px rgba(0,0,0,.45);}
  #hud{position:absolute;top:14px;left:14px;max-width:min(62vw,560px);color:var(--floor-lit);
    pointer-events:none;text-shadow:0 2px 6px rgba(0,0,0,.8);}
  #breadcrumb{font-family:var(--font-display);font-size:15px;letter-spacing:.06em;text-transform:uppercase;
    color:var(--ember-glow);background:rgba(13,9,6,.55);padding:7px 12px;border-radius:4px;
    border:1px solid rgba(216,189,138,.25);display:inline-block;}
  #hint{margin-top:8px;font-size:12.5px;color:rgba(240,228,196,.85);background:rgba(13,9,6,.5);
    display:inline-block;padding:5px 10px;border-radius:4px;transition:opacity .8s ease;}
  #hint.hidden{opacity:0;}

  #search-wrap{margin-top:10px;pointer-events:auto;}
  #search-toggle{font-family:var(--font-ui);font-size:12.5px;background:rgba(13,9,6,.55);color:var(--floor-lit);
    border:1px solid rgba(216,189,138,.35);padding:6px 12px;border-radius:4px;cursor:pointer;}
  #search-toggle:hover{background:rgba(13,9,6,.78);}
  #search-panel{margin-top:8px;width:300px;max-width:80vw;background:linear-gradient(180deg,var(--parchment),#e7d8ab 97%);
    border:1px solid var(--parchment-edge);border-radius:6px;box-shadow:0 10px 30px rgba(0,0,0,.4);overflow:hidden;}
  #search-panel[hidden]{display:none;}
  #search-input{width:100%;box-sizing:border-box;border:none;border-bottom:1px solid var(--parchment-shadow);
    padding:10px 12px;font-family:var(--font-ui);font-size:14px;background:transparent;color:var(--ink);outline:none;}
  #search-input:focus{background:rgba(201,112,47,.06);}
  #search-results{max-height:260px;overflow-y:auto;}
  .search-result{padding:8px 12px;cursor:pointer;border-bottom:1px solid rgba(107,87,56,.12);}
  .search-result:hover,.search-result:focus-visible{background:rgba(201,112,47,.14);outline:none;}
  .search-result-title{font-family:var(--font-display);font-size:13.5px;color:var(--ink);font-weight:700;}
  .search-result-room{font-size:10.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--ink-soft);margin-top:2px;}
  .search-empty{padding:10px 12px;font-size:12.5px;color:var(--ink-soft);}

  #panel{position:absolute;top:0;right:0;height:100%;width:340px;max-width:88vw;
    background:linear-gradient(180deg,var(--parchment),#e7d8ab 96%);border-left:3px solid var(--parchment-edge);
    box-shadow:-12px 0 30px rgba(0,0,0,.45);color:var(--ink);transform:translateX(0);
    transition:transform .35s ease;display:flex;flex-direction:column;}
  #panel.stowed{transform:translateX(100%);}
  #panel-toggle{position:absolute;top:16px;right:100%;background:var(--parchment);border:1px solid var(--parchment-edge);
    border-right:none;color:var(--ink);font-family:var(--font-display);font-size:13px;letter-spacing:.05em;
    padding:8px 6px;border-radius:6px 0 0 6px;cursor:pointer;writing-mode:vertical-rl;}
  #panel-toggle:focus-visible,.dpad button:focus-visible,#start-btn:focus-visible,.book:focus-visible,
  .xlink:focus-visible,#reader-close:focus-visible,#reader-back:focus-visible,#search-toggle:focus-visible,
  #search-input:focus-visible{
    outline:3px solid var(--ember-glow);outline-offset:2px;}
  #panel-head{padding:20px 20px 12px;border-bottom:1px solid var(--parchment-shadow);}
  #room-name{font-family:var(--font-display);font-size:22px;margin:0 0 6px;color:var(--ink);text-wrap:balance;}
  #room-flavor{margin:0;font-size:13.5px;font-style:italic;color:var(--ink-soft);line-height:1.5;}
  #room-count{margin-top:8px;font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);}
  #book-list{flex:1;overflow-y:auto;padding:10px 14px 24px;}
  .book{border-bottom:1px solid rgba(107,87,56,.18);padding:10px 6px;cursor:pointer;}
  .book:hover .book-title{color:var(--accent);}
  .book-title{font-family:var(--font-display);font-size:14.5px;font-weight:700;color:var(--ink);margin:0;text-wrap:balance;}
  .book-meta{font-size:10.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-soft);margin-top:3px;}
  .book-meta .tag{display:inline-block;margin-right:6px;padding:1px 6px;border-radius:3px;
    background:rgba(47,122,107,.15);color:var(--tile-teal-dark);border:1px solid rgba(47,122,107,.3);}

  #reader{position:absolute;inset:0;z-index:30;display:none;background:rgba(13,9,6,.55);
    align-items:center;justify-content:center;padding:26px;}
  #reader.open{display:flex;}
  #reader-sheet{background:linear-gradient(180deg,var(--parchment),#e7d8ab 97%);max-width:760px;width:100%;
    max-height:88vh;border-radius:4px;box-shadow:0 20px 60px rgba(0,0,0,.55);display:flex;flex-direction:column;
    border:1px solid var(--parchment-edge);}
  #reader-top{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;
    padding:22px 26px 14px;border-bottom:1px solid var(--parchment-shadow);}
  #reader-title{font-family:var(--font-display);font-size:24px;margin:0 0 6px;color:var(--ink);text-wrap:balance;}
  #reader-meta{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--accent);}
  #reader-actions{display:flex;gap:8px;flex-shrink:0;}
  #reader-back,#reader-close{font-family:var(--font-ui);font-size:13px;background:rgba(43,32,19,.08);
    border:1px solid var(--parchment-shadow);color:var(--ink);padding:6px 12px;border-radius:4px;cursor:pointer;}
  #reader-back[hidden]{display:none;}
  #reader-close:hover,#reader-back:hover{background:rgba(43,32,19,.16);}
  #reader-body{overflow-y:auto;padding:20px 26px 32px;font-size:14.5px;line-height:1.7;color:var(--ink);}
  #reader-body h2,#reader-body h3,#reader-body h4,#reader-body h5,#reader-body h6{
    font-family:var(--font-display);color:var(--ink);margin:1.3em 0 .5em;text-wrap:balance;}
  #reader-body p{margin:0 0 1em;}
  #reader-body ul{margin:0 0 1em;padding-left:1.3em;}
  #reader-body blockquote{margin:0 0 1em;padding:.4em 1em;border-left:3px solid var(--accent);
    background:rgba(201,112,47,.08);font-style:italic;color:var(--ink-soft);}
  #reader-body code{background:rgba(43,32,19,.08);padding:1px 5px;border-radius:3px;font-size:.9em;}
  .xlink{color:var(--tile-teal-dark);text-decoration:underline;text-decoration-color:rgba(47,122,107,.4);
    cursor:pointer;font-weight:600;}
  .xlink:hover{color:var(--accent);}
  .xlink-missing{color:var(--ink-soft);border-bottom:1px dotted var(--ink-soft);cursor:default;}

  #start-overlay{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,#241a10,#0f0a06 78%);
    display:flex;align-items:center;justify-content:center;flex-direction:column;text-align:center;
    color:var(--floor-lit);padding:24px;z-index:20;}
  #start-overlay h1{font-family:var(--font-display);font-weight:700;font-size:clamp(28px,6vw,46px);
    letter-spacing:.03em;margin:0 0 10px;color:var(--ember-glow);text-wrap:balance;
    text-shadow:0 4px 24px rgba(217,123,52,.35);}
  #start-overlay p{max-width:500px;margin:0 auto 22px;font-size:15px;line-height:1.6;color:#e9dcc0;}
  #start-btn{font-family:var(--font-display);font-size:16px;letter-spacing:.05em;text-transform:uppercase;
    background:linear-gradient(180deg,var(--ember),#a84f1c);color:#fff3e2;border:1px solid rgba(255,255,255,.2);
    padding:12px 28px;border-radius:5px;cursor:pointer;box-shadow:0 6px 18px rgba(0,0,0,.4);}
  #start-btn:hover{filter:brightness(1.08);}
  #controls-legend{margin-top:20px;font-size:12px;color:#c9b789;display:flex;gap:18px;flex-wrap:wrap;justify-content:center;}
  #controls-legend kbd{background:rgba(240,228,196,.12);border:1px solid rgba(240,228,196,.3);border-radius:3px;
    padding:2px 6px;font-family:var(--font-ui);}
  #start-overlay.hidden{display:none;}
  #loading{position:absolute;inset:0;z-index:25;display:flex;align-items:center;justify-content:center;
    color:var(--floor-lit);font-family:var(--font-display);letter-spacing:.08em;text-transform:uppercase;
    background:var(--stone-void);}
  #loading.hidden{display:none;}

  .dpad{position:absolute;bottom:22px;left:22px;display:none;grid-template-columns:52px 52px 52px;
    grid-template-rows:52px 52px 52px;gap:4px;}
  .dpad.show{display:grid;}
  .dpad button{background:rgba(13,9,6,.6);border:1px solid rgba(216,189,138,.4);color:var(--floor-lit);
    font-size:18px;border-radius:8px;}
  .dpad button:active{background:rgba(217,123,52,.5);}
  #dp-up{grid-column:2;grid-row:1;} #dp-left{grid-column:1;grid-row:2;}
  #dp-right{grid-column:3;grid-row:2;} #dp-down{grid-column:2;grid-row:3;}

  @media (max-width:720px){
    #panel{width:100%;max-width:100%;height:42vh;top:auto;bottom:0;border-left:none;border-top:3px solid var(--parchment-edge);}
    #panel-toggle{top:auto;bottom:16px;right:auto;left:0;writing-mode:horizontal-tb;
      border-radius:6px 6px 0 0;border:1px solid var(--parchment-edge);border-bottom:none;transform:translateY(-100%);}
    #reader{padding:0;}
    #reader-sheet{max-width:100%;max-height:100%;height:100%;border-radius:0;}
  }
  @media (prefers-reduced-motion: reduce){ #hint{transition:none;} #panel{transition:none;} }
</style>

<div id="app">
  <canvas id="game"></canvas>
  <canvas id="minimap" width="150" height="130"></canvas>
  <div id="hud">
    <div id="breadcrumb">Citadelle du Sham</div>
    <div id="hint">Glisse pour orbiter la caméra — WASD/flèches pour marcher</div>
    <div id="search-wrap">
      <button id="search-toggle" type="button" aria-expanded="false">🔍 Chercher une fiche</button>
      <div id="search-panel" hidden>
        <input id="search-input" type="text" placeholder="Titre d'une fiche…" autocomplete="off" />
        <div id="search-results"></div>
      </div>
    </div>
  </div>

  <aside id="panel">
    <button id="panel-toggle" type="button" aria-expanded="true">Bibliothèque</button>
    <div id="panel-head">
      <h2 id="room-name">Grand Hall de la Citadelle</h2>
      <p id="room-flavor">Trois couloirs partent d'ici.</p>
      <div id="room-count"></div>
    </div>
    <div id="book-list"></div>
  </aside>

  <div id="reader">
    <div id="reader-sheet">
      <div id="reader-top">
        <div>
          <h3 id="reader-title">Titre</h3>
          <div id="reader-meta"></div>
        </div>
        <div id="reader-actions">
          <button id="reader-back" type="button" hidden>‹ Précédent</button>
          <button id="reader-close" type="button">Fermer ✕</button>
        </div>
      </div>
      <div id="reader-body"></div>
    </div>
  </div>

  <div class="dpad" id="dpad">
    <button id="dp-up" type="button" aria-label="Avancer">▲</button>
    <button id="dp-left" type="button" aria-label="Gauche">◀</button>
    <button id="dp-right" type="button" aria-label="Droite">▶</button>
    <button id="dp-down" type="button" aria-label="Reculer">▼</button>
  </div>

  <div id="start-overlay">
    <h1>La Citadelle du Sham</h1>
    <p>Une forteresse en 3D bâtie sur le depot-lecture : chaque salle est un répertoire, chaque ouvrage sur les
       étagères une fiche que tu peux lire en entier — et suivre ses renvois vers d'autres fiches. Incarne
       l'émissaire qui l'arpente.</p>
    <button id="start-btn" type="button">Entrer dans la citadelle</button>
    <div id="controls-legend">
      <span><kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> — marcher</span>
      <span>glisser la souris/le doigt — orbiter la caméra</span>
      <span>clic sur un ouvrage — le lire en entier</span>
    </div>
  </div>
  <div id="loading">Construction de la citadelle…</div>
</div>

<script>
__THREE_SRC__
</script>
<script>
(function(){
"use strict";

var LIBRARY = __LIBRARY_JSON__;
var ROOMS = __ROOMS_JSON__;
var CORRIDORS = __CORRIDORS_JSON__;

var TILE = 4;
var WALL_H = 6.2;

var WING_NAMES = { hall:"Grand Hall", rd:"Aile de l'Atelier", doctrinal:"Aile Doctrinale", hermeneutique:"Aile Herméneutique" };
var WING_COLORS = { hall:0xd97b34, rd:0x7fae6a, doctrinal:0xc9702f, hermeneutique:0x3f8fae };
var WING_COLORS_CSS = { hall:"#d97b34", rd:"#7fae6a", doctrinal:"#c9702f", hermeneutique:"#3f8fae" };

var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// ---------- procedural audio (no external files) ----------
var audioCtx = null, masterGain = null, crackleGain = null;
function initAudio(){
  if(audioCtx) return;
  try{
    var AC = window.AudioContext || window.webkitAudioContext;
    if(!AC) return;
    audioCtx = new AC();
    masterGain = audioCtx.createGain(); masterGain.gain.value = 0.5; masterGain.connect(audioCtx.destination);

    var dur = 2, buf = audioCtx.createBuffer(1, audioCtx.sampleRate*dur, audioCtx.sampleRate);
    var data = buf.getChannelData(0);
    for(var i=0;i<data.length;i++) data[i] = (Math.random()*2-1) * (0.25+0.75*Math.random());
    var src = audioCtx.createBufferSource(); src.buffer = buf; src.loop = true;
    var filt = audioCtx.createBiquadFilter(); filt.type='bandpass'; filt.frequency.value=950; filt.Q.value=0.6;
    crackleGain = audioCtx.createGain(); crackleGain.gain.value = 0.05;
    src.connect(filt); filt.connect(crackleGain); crackleGain.connect(masterGain);
    src.start();
  }catch(e){ audioCtx = null; }
}
function playUiBlip(freq){
  if(!audioCtx) return;
  var o = audioCtx.createOscillator(), g = audioCtx.createGain();
  o.type='sine'; o.frequency.value = freq || 660;
  var t0 = audioCtx.currentTime;
  g.gain.setValueAtTime(0.0001, t0);
  g.gain.exponentialRampToValueAtTime(0.16, t0+0.012);
  g.gain.exponentialRampToValueAtTime(0.0001, t0+0.15);
  o.connect(g); g.connect(masterGain);
  o.start(t0); o.stop(t0+0.16);
}
function playFootstep(){
  if(!audioCtx) return;
  var n = Math.floor(audioCtx.sampleRate*0.055);
  var buf = audioCtx.createBuffer(1,n,audioCtx.sampleRate);
  var d = buf.getChannelData(0);
  for(var i=0;i<n;i++) d[i] = (Math.random()*2-1) * Math.pow(1-i/n, 1.6);
  var src = audioCtx.createBufferSource(); src.buffer = buf;
  var filt = audioCtx.createBiquadFilter(); filt.type='lowpass'; filt.frequency.value = 380 + Math.random()*80;
  var g = audioCtx.createGain(); g.gain.value = 0.3;
  src.connect(filt); filt.connect(g); g.connect(masterGain);
  src.start();
}

// ---------- tile grid (same scheme as the 2D prototype, tile-integer keyed) ----------
var floorSet = new Set();
var wallSet = new Set();
var tileWing = new Map();
var tileIsRoom = new Set();

function fillRect(x0,y0,x1,y1,wing,isRoom){
  for(var x=x0;x<=x1;x++){
    for(var y=y0;y<=y1;y++){
      var k = x+","+y;
      floorSet.add(k); tileWing.set(k, wing);
      if(isRoom) tileIsRoom.add(k);
    }
  }
}
ROOMS.forEach(function(r){ fillRect(r.x0,r.y0,r.x1,r.y1,r.wing,true); });
CORRIDORS.forEach(function(c){ fillRect(c.x0,c.y0,c.x1,c.y1,c.wing,false); });

var NEI8 = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]];
var wallList = [];
floorSet.forEach(function(k){
  var p = k.split(","), x=parseInt(p[0],10), y=parseInt(p[1],10);
  NEI8.forEach(function(d){
    var nk = (x+d[0])+","+(y+d[1]);
    if(!floorSet.has(nk) && !wallSet.has(nk)){ wallSet.add(nk); }
  });
});
wallSet.forEach(function(k){ var p=k.split(","); wallList.push([parseInt(p[0],10),parseInt(p[1],10)]); });

function inRoom(room, tx, ty){ return tx>=room.x0 && tx<=room.x1 && ty>=room.y0 && ty<=room.y1; }
function findRoomAt(tx,ty){ for(var i=0;i<ROOMS.length;i++){ if(inRoom(ROOMS[i], tx, ty)) return ROOMS[i]; } return null; }
function findWingAt(tx,ty){ return tileWing.get(Math.round(tx)+","+Math.round(ty)) || null; }

var minX=Infinity,maxX=-Infinity,minY=Infinity,maxY=-Infinity;
ROOMS.forEach(function(r){ minX=Math.min(minX,r.x0); maxX=Math.max(maxX,r.x1); minY=Math.min(minY,r.y0); maxY=Math.max(maxY,r.y1); });

// ---------- three.js scene ----------
var canvas = document.getElementById('game');
var renderer = new THREE.WebGLRenderer({canvas:canvas, antialias:true});
renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.5));
renderer.outputEncoding = THREE.sRGBEncoding;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.35;
var scene = new THREE.Scene();
scene.background = new THREE.Color(0x0d0906);
scene.fog = new THREE.FogExp2(0x0d0906, 0.011);

var camera = new THREE.PerspectiveCamera(56, window.innerWidth/window.innerHeight, 0.1, 400);

scene.add(new THREE.AmbientLight(0x54402a, 1.6));
var hemi = new THREE.HemisphereLight(0x6a5540, 0x0a0704, 0.55);
scene.add(hemi);

function resize(){
  var w = window.innerWidth, h = window.innerHeight;
  renderer.setSize(w,h);
  camera.aspect = w/h; camera.updateProjectionMatrix();
}
window.addEventListener('resize', resize);
resize();

// ---------- procedural textures ----------
function noiseCanvas(size, base, variance, drawExtra){
  var c = document.createElement('canvas'); c.width=c.height=size;
  var cx = c.getContext('2d');
  cx.fillStyle = base; cx.fillRect(0,0,size,size);
  for(var i=0;i<size*size*0.12;i++){
    var x = Math.random()*size, y = Math.random()*size, s = 1+Math.random()*2.4;
    var v = (Math.random()-0.5)*variance;
    cx.fillStyle = 'rgba('+(v>0?'255,255,255':'0,0,0')+','+Math.min(Math.abs(v)/255,0.35)+')';
    cx.fillRect(x,y,s,s);
  }
  if(drawExtra) drawExtra(cx,size);
  return c;
}
function tex(canvas){
  var t = new THREE.CanvasTexture(canvas);
  t.magFilter = THREE.NearestFilter; t.minFilter = THREE.LinearMipmapLinearFilter;
  t.anisotropy = 4;
  return t;
}
var floorTexture = tex(noiseCanvas(96, '#c3a874', 40, function(cx,s){
  cx.strokeStyle = 'rgba(90,68,40,0.35)'; cx.lineWidth=2;
  cx.strokeRect(1,1,s-2,s-2);
}));
var corrTexture = tex(noiseCanvas(96, '#a4906e', 34, function(cx,s){
  cx.strokeStyle = 'rgba(47,122,107,0.4)'; cx.lineWidth=2; cx.strokeRect(1,1,s-2,s-2);
}));
var wallTexture = tex(noiseCanvas(96, '#4a3524', 46, function(cx,s){
  cx.strokeStyle = 'rgba(20,14,8,0.5)'; cx.lineWidth=2;
  for(var i=0;i<4;i++){ cx.beginPath(); cx.moveTo(0,i*s/4); cx.lineTo(s,i*s/4); cx.stroke(); }
}));
var ceilTexture = tex(noiseCanvas(96, '#241a12', 26));

var floorMat = new THREE.MeshLambertMaterial({map:floorTexture});
var corrMat = new THREE.MeshLambertMaterial({map:corrTexture});
var wallMat = new THREE.MeshLambertMaterial({map:wallTexture});
var ceilMat = new THREE.MeshLambertMaterial({map:ceilTexture, side:THREE.BackSide});

// ---------- instanced geometry ----------
var m4 = new THREE.Matrix4();
function buildInstanced(cells, geo, mat, y){
  var mesh = new THREE.InstancedMesh(geo, mat, cells.length);
  for(var i=0;i<cells.length;i++){
    m4.makeTranslation(cells[i][0]*TILE+TILE/2, y, cells[i][1]*TILE+TILE/2);
    mesh.setMatrixAt(i, m4);
  }
  mesh.instanceMatrix.needsUpdate = true;
  return mesh;
}
var roomFloorCells = [], corrFloorCells = [];
floorSet.forEach(function(k){
  var p=k.split(","); var cell=[parseInt(p[0],10),parseInt(p[1],10)];
  if(tileIsRoom.has(k)) roomFloorCells.push(cell); else corrFloorCells.push(cell);
});

var floorGeo = new THREE.BoxGeometry(TILE-0.06, 0.3, TILE-0.06);
var ceilGeo = new THREE.BoxGeometry(TILE-0.02, 0.3, TILE-0.02);
var wallGeo = new THREE.BoxGeometry(TILE, WALL_H, TILE);

scene.add(buildInstanced(roomFloorCells, floorGeo, floorMat, 0.15));
scene.add(buildInstanced(corrFloorCells, floorGeo, corrMat, 0.15));
var allFloorCells = roomFloorCells.concat(corrFloorCells);
scene.add(buildInstanced(allFloorCells, ceilGeo, ceilMat, WALL_H));
scene.add(buildInstanced(wallList, wallGeo, wallMat, WALL_H/2));

// ---------- torches ----------
var torches = [];
ROOMS.forEach(function(r){
  if(r.id==='hall'){
    torches.push({x:r.x0+1.4,y:r.y0+1.4,lit:true},{x:r.x1-1.4,y:r.y1-1.4,lit:true},
                 {x:r.x1-1.4,y:r.y0+1.4,lit:false},{x:r.x0+1.4,y:r.y1-1.4,lit:false});
  } else {
    torches.push({x:r.x0+0.8,y:r.cy,lit:true},{x:r.x1-0.8,y:r.cy,lit:false});
  }
});
CORRIDORS.forEach(function(c,ci){
  torches.push({x:(c.x0+c.x1)/2, y:(c.y0+c.y1)/2, lit:(ci%2===0)});
});
// Only a subset of torches carry a real-time PointLight (WebGL shades every
// surface against every active light each frame, so 55 of them was the main
// cause of lag) — the rest keep their flame mesh (visual only, no light cost).
var torchLights = [];
var flameGeo = new THREE.SphereGeometry(0.22,8,8);
var flameMat = new THREE.MeshBasicMaterial({color:0xffb45c});
torches.forEach(function(t){
  var wx = t.x*TILE+TILE/2, wz = t.y*TILE+TILE/2, wy = WALL_H*0.6;
  var light = null;
  if(t.lit){
    light = new THREE.PointLight(0xffa552, 2.1, TILE*13, 2);
    light.position.set(wx,wy,wz);
    scene.add(light);
  }
  var flame = new THREE.Mesh(flameGeo, flameMat);
  flame.position.set(wx,wy,wz);
  scene.add(flame);
  torchLights.push({light:light, flame:flame, seed:Math.random()*10, wx:wx, wz:wz});
});

// ---------- bookshelves: real, clickable, one spine per fiche ----------
var shelfMat = new THREE.MeshLambertMaterial({color:0x2c1d10});
var spineColors = [0x7a3b2e,0x8a6a2f,0x2f6a5a,0x5a3b7a,0x6a2f3b,0x3b5a2f,0x7a5a2f];
var spineMats = spineColors.map(function(c){ return new THREE.MeshLambertMaterial({color:c}); });
var interactiveGroup = new THREE.Group();
scene.add(interactiveGroup);

ROOMS.forEach(function(r){
  if(r.id==='hall') return;
  var books = LIBRARY[r.key] || [];
  var count = books.length;
  if(count===0) return;
  var perRow = 20;
  var rows = Math.max(1, Math.min(6, Math.ceil(count/perRow)));
  var perRowActual = Math.ceil(count/rows);
  var wallX = r.x0+0.35;
  var wz0 = r.y0+0.9, wz1 = r.y1-0.9;
  var bookIdx = 0;
  for(var row=0; row<rows && bookIdx<count; row++){
    var y = 1.0 + row*1.05;
    var n = Math.min(perRowActual, count-bookIdx);
    var shelf = new THREE.Mesh(new THREE.BoxGeometry(0.5,0.1,(wz1-wz0)*TILE), shelfMat);
    shelf.position.set(wallX*TILE, y-0.42, (r.cy)*TILE);
    scene.add(shelf);
    for(var i=0;i<n;i++,bookIdx++){
      var t = wz0 + (wz1-wz0)*(i+0.5)/n;
      var h = 0.62+((bookIdx*37)%10)/10*0.4;
      var spineMat = spineMats[bookIdx%spineMats.length].clone();
      var spine = new THREE.Mesh(new THREE.BoxGeometry(0.4,h,0.15), spineMat);
      spine.position.set(wallX*TILE+0.05, y+h/2-0.4, t*TILE);
      spine.userData = {dir:r.key, idx:bookIdx};
      scene.add(spine);
      interactiveGroup.add(spine);
    }
  }
});

// ---------- player character (procedural low-poly assassin) ----------
var playerModel = new THREE.Group();
(function buildAssassin(){
  var robeColor = 0x5a4230, robeDark = 0x46331f, hoodColor = 0x211710, capeColor = 0x3a1f14,
      sashColor = 0xd97b34, skinColor = 0xb98a63;
  var robeMat = new THREE.MeshLambertMaterial({color:robeColor});
  var robeDarkMat = new THREE.MeshLambertMaterial({color:robeDark});
  var limbMat = new THREE.MeshLambertMaterial({color:0x6b4e34});
  var hoodMat = new THREE.MeshLambertMaterial({color:hoodColor});
  var capeMat = new THREE.MeshLambertMaterial({color:capeColor, side:THREE.DoubleSide});
  var sashMat = new THREE.MeshLambertMaterial({color:sashColor});
  var skinMat = new THREE.MeshLambertMaterial({color:skinColor});

  var hips = new THREE.Group(); hips.position.set(0,0,0); playerModel.add(hips);

  // torso (flared robe silhouette)
  var torso = new THREE.Mesh(new THREE.CylinderGeometry(0.34,0.5,1.15,14), robeMat);
  torso.position.set(0,0.7,0); hips.add(torso);
  var chestWrap = new THREE.Mesh(new THREE.CylinderGeometry(0.36,0.36,0.16,14), sashMat);
  chestWrap.position.set(0,0.55,0.02); chestWrap.rotation.z = 0.08; hips.add(chestWrap);

  // lower robe skirt (wider, reaches toward knees, gives AC silhouette)
  var skirt = new THREE.Mesh(new THREE.CylinderGeometry(0.5,0.62,0.42,14,1,true), robeDarkMat);
  skirt.position.set(0,0.55,0); hips.add(skirt);

  // head + hood
  var neck = new THREE.Mesh(new THREE.CylinderGeometry(0.13,0.15,0.16,10), skinMat);
  neck.position.set(0,1.36,0); hips.add(neck);
  var head = new THREE.Mesh(new THREE.SphereGeometry(0.23,14,10), skinMat);
  head.position.set(0,1.58,0.01); hips.add(head);
  var hood = new THREE.Mesh(new THREE.ConeGeometry(0.29,0.36,14), hoodMat);
  hood.position.set(0,1.68,-0.02); hood.rotation.x = 0.32; hips.add(hood);
  var hoodBack = new THREE.Mesh(new THREE.SphereGeometry(0.27,12,10,0,Math.PI*2,0,Math.PI*0.62), hoodMat);
  hoodBack.position.set(0,1.66,-0.02); hoodBack.rotation.x = Math.PI; hips.add(hoodBack);

  // cape
  var capeGeo = new THREE.PlaneGeometry(0.62,1.15,1,4);
  var cape = new THREE.Mesh(capeGeo, capeMat);
  cape.position.set(0,0.95,-0.32); cape.rotation.x = 0.18;
  var capePivot = new THREE.Group(); capePivot.position.set(0,1.42,-0.22); capePivot.add(cape);
  cape.position.set(0,-0.47,-0.10);
  hips.add(capePivot);
  playerModel.userData.cape = capePivot;

  // sash tail
  var sash = new THREE.Mesh(new THREE.BoxGeometry(0.12,0.55,0.03), sashMat);
  sash.position.set(0.18,0.15,0.34); sash.rotation.z = -0.15; hips.add(sash);

  function limb(radiusTop,radiusBot,len,mat){
    var geo = new THREE.CylinderGeometry(radiusTop,radiusBot,len,10);
    var mesh = new THREE.Mesh(geo, mat);
    mesh.position.y = -len/2;
    var pivot = new THREE.Group();
    pivot.add(mesh);
    return pivot;
  }
  var armL = limb(0.09,0.075,0.78,limbMat); armL.position.set(0.42,1.28,0);
  var armR = limb(0.09,0.075,0.78,limbMat); armR.position.set(-0.42,1.28,0);
  var handL = new THREE.Mesh(new THREE.SphereGeometry(0.09,10,8), skinMat); handL.position.y=-0.78; armL.children[0].add(handL);
  var handR = new THREE.Mesh(new THREE.SphereGeometry(0.09,10,8), skinMat); handR.position.y=-0.78; armR.children[0].add(handR);
  hips.add(armL); hips.add(armR);

  var legL = limb(0.15,0.12,0.95,limbMat); legL.position.set(0.18,0.95,0);
  var legR = limb(0.15,0.12,0.95,limbMat); legR.position.set(-0.18,0.95,0);
  hips.add(legL); hips.add(legR);

  playerModel.userData.armL = armL; playerModel.userData.armR = armR;
  playerModel.userData.legL = legL; playerModel.userData.legR = legR;
  playerModel.userData.hips = hips;

  playerModel.traverse(function(o){ o.castShadow = false; });
})();
scene.add(playerModel);

// ---------- dust puffs at footfall ----------
var dustTexture = tex((function(){
  var c = document.createElement('canvas'); c.width=c.height=32;
  var cx = c.getContext('2d');
  var g = cx.createRadialGradient(16,16,0,16,16,16);
  g.addColorStop(0,'rgba(216,189,138,0.55)'); g.addColorStop(1,'rgba(216,189,138,0)');
  cx.fillStyle = g; cx.fillRect(0,0,32,32);
  return c;
})());
var dustPool = [];
(function(){
  var mat = new THREE.SpriteMaterial({map:dustTexture, transparent:true, depthWrite:false, opacity:0});
  for(var i=0;i<10;i++){
    var s = new THREE.Sprite(mat.clone());
    s.visible = false; s.userData.life = 0;
    scene.add(s); dustPool.push(s);
  }
})();
function spawnDust(x,z){
  if(reduceMotion) return;
  for(var i=0;i<dustPool.length;i++){
    var s = dustPool[i];
    if(!s.visible){
      s.visible = true; s.position.set(x + (Math.random()-0.5)*0.3, 0.1, z + (Math.random()-0.5)*0.3);
      s.scale.set(0.4,0.4,0.4); s.material.opacity = 0.45; s.userData.life = 0.55;
      return;
    }
  }
}
function updateDust(dt){
  for(var i=0;i<dustPool.length;i++){
    var s = dustPool[i];
    if(!s.visible) continue;
    s.userData.life -= dt;
    if(s.userData.life<=0){ s.visible=false; continue; }
    var k = 1 - s.userData.life/0.55;
    s.scale.set(0.4+k*0.7,0.4+k*0.7,0.4+k*0.7);
    s.material.opacity = 0.45*(1-k);
  }
}

function shortAngleDiff(a,b){
  var d = (b-a) % (Math.PI*2);
  if(d > Math.PI) d -= Math.PI*2;
  if(d < -Math.PI) d += Math.PI*2;
  return d;
}

// ---------- player state ----------
var player = { x:0, z:0, yaw:0.6, pitch:0.42, facing:0, half: TILE*0.24, speed: TILE*1.9, moving:false };

function canStand(x,z){
  var m = player.half;
  var pts = [[x-m,z-m],[x+m,z-m],[x-m,z+m],[x+m,z+m]];
  for(var i=0;i<pts.length;i++){
    var tx = Math.floor(pts[i][0]/TILE), tz = Math.floor(pts[i][1]/TILE);
    var k = tx+","+tz;
    if(wallSet.has(k)) return false;
    if(!floorSet.has(k)) return false;
  }
  return true;
}

// ---------- input ----------
var keys = {};
var KEY_MAP = { ArrowUp:'up', ArrowDown:'down', ArrowLeft:'left', ArrowRight:'right',
  w:'up', s:'down', a:'left', d:'right', W:'up', S:'down', A:'left', D:'right' };
window.addEventListener('keydown', function(e){
  if(document.activeElement && document.activeElement.tagName === 'INPUT') return;
  var dir = KEY_MAP[e.key];
  if(dir){ keys[dir]=true; onFirstMove(); if(!readerOpen) e.preventDefault(); }
  if(e.key === 'Escape' && readerOpen) closeReader();
});
window.addEventListener('keyup', function(e){ var dir = KEY_MAP[e.key]; if(dir) keys[dir]=false; });

var hintEl = document.getElementById('hint');
var firstMoveDone = false;
function onFirstMove(){ if(firstMoveDone) return; firstMoveDone=true; setTimeout(function(){ hintEl.classList.add('hidden'); },1600); }

function bindHold(id, dir){
  var el = document.getElementById(id);
  var on = function(ev){ keys[dir]=true; onFirstMove(); ev.preventDefault(); };
  var off = function(ev){ keys[dir]=false; if(ev) ev.preventDefault(); };
  el.addEventListener('pointerdown', on); el.addEventListener('pointerup', off);
  el.addEventListener('pointerleave', off); el.addEventListener('pointercancel', off);
}
bindHold('dp-up','up'); bindHold('dp-down','down'); bindHold('dp-left','left'); bindHold('dp-right','right');
if(('ontouchstart' in window) || (navigator.maxTouchPoints && navigator.maxTouchPoints>0)){
  document.getElementById('dpad').classList.add('show');
}

// look via drag (pointer events cover mouse + touch); a short low-movement press is a "click" pick
var dragging = false, lastPX=0, lastPY=0, downX=0, downY=0, downT=0;
var raycaster = new THREE.Raycaster();
var pointerNDC = new THREE.Vector2();
var hoveredSpine = null;

function setHover(spine){
  if(hoveredSpine === spine) return;
  if(hoveredSpine) hoveredSpine.material.emissive.setHex(0x000000);
  hoveredSpine = spine;
  if(hoveredSpine){ hoveredSpine.material.emissive.setHex(0x552200); canvas.style.cursor = 'pointer'; }
  else { canvas.style.cursor = dragging ? 'grabbing' : 'grab'; }
}

function pickSpineAt(clientX, clientY){
  var rect = canvas.getBoundingClientRect();
  pointerNDC.x = ((clientX-rect.left)/rect.width)*2-1;
  pointerNDC.y = -((clientY-rect.top)/rect.height)*2+1;
  raycaster.setFromCamera(pointerNDC, camera);
  var hits = raycaster.intersectObjects(interactiveGroup.children, false);
  return hits.length ? hits[0].object : null;
}

canvas.addEventListener('pointerdown', function(e){
  dragging=true; lastPX=e.clientX; lastPY=e.clientY; downX=e.clientX; downY=e.clientY; downT=performance.now();
  canvas.setPointerCapture(e.pointerId);
});
canvas.addEventListener('pointerup', function(e){
  dragging=false; canvas.style.cursor='grab';
  var moved = Math.hypot(e.clientX-downX, e.clientY-downY);
  if(moved < 6 && performance.now()-downT < 500 && !readerOpen){
    var spine = pickSpineAt(e.clientX, e.clientY);
    if(spine){ playUiBlip(); openReader(spine.userData.dir, spine.userData.idx, true); }
  }
});
canvas.addEventListener('pointercancel', function(){ dragging=false; });
canvas.addEventListener('pointermove', function(e){
  if(dragging){
    var dx = e.clientX-lastPX, dy = e.clientY-lastPY;
    lastPX=e.clientX; lastPY=e.clientY;
    if(Math.hypot(e.clientX-downX,e.clientY-downY) > 6){
      player.yaw -= dx*0.0044;
      player.pitch -= dy*0.0032;
      player.pitch = Math.max(0.12, Math.min(1.25, player.pitch));
      setHover(null);
    }
  } else if(!readerOpen){
    setHover(pickSpineAt(e.clientX, e.clientY));
  }
});

// ---------- panel / reader ----------
var panel = document.getElementById('panel');
var panelToggle = document.getElementById('panel-toggle');
var roomNameEl = document.getElementById('room-name');
var roomFlavorEl = document.getElementById('room-flavor');
var roomCountEl = document.getElementById('room-count');
var bookListEl = document.getElementById('book-list');
var breadcrumbEl = document.getElementById('breadcrumb');
var readerEl = document.getElementById('reader');
var readerTitle = document.getElementById('reader-title');
var readerMeta = document.getElementById('reader-meta');
var readerBody = document.getElementById('reader-body');
var readerBack = document.getElementById('reader-back');
var readerClose = document.getElementById('reader-close');
var readerOpen = false;
var readerStack = [];

panelToggle.addEventListener('click', function(){
  var stowed = panel.classList.toggle('stowed');
  panelToggle.setAttribute('aria-expanded', String(!stowed));
});

function escapeHtml(s){
  return String(s).replace(/[&<>"']/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; });
}

var lastRenderedRoomId = null;
function renderRoom(room){
  if(!room || room.id===lastRenderedRoomId) return;
  lastRenderedRoomId = room.id;
  roomNameEl.textContent = room.name;
  roomFlavorEl.textContent = room.flavor;
  if(!room.key){
    roomCountEl.textContent = "";
    bookListEl.innerHTML = "<p style='font-size:13px;line-height:1.6;color:var(--ink-soft);padding:8px 6px;'>Le hall ne conserve aucun ouvrage — engage-toi dans l'un des trois couloirs.</p>";
    return;
  }
  var books = LIBRARY[room.key] || [];
  roomCountEl.textContent = books.length + (books.length>1 ? " ouvrages" : " ouvrage");
  bookListEl.innerHTML = books.map(function(b,i){
    var meta = [];
    if(b.type) meta.push('<span class="tag">'+escapeHtml(b.type)+'</span>');
    if(b.status) meta.push('<span class="tag">'+escapeHtml(b.status)+'</span>');
    return '<div class="book" data-dir="'+escapeHtml(room.key)+'" data-idx="'+i+'" tabindex="0" role="button">'+
      '<p class="book-title">'+escapeHtml(b.title)+'</p><div class="book-meta">'+meta.join('')+'</div></div>';
  }).join('');
  Array.prototype.forEach.call(bookListEl.querySelectorAll('.book'), function(el){
    var open = function(){ playUiBlip(660); openReader(el.getAttribute('data-dir'), parseInt(el.getAttribute('data-idx'),10), true); };
    el.addEventListener('click', open);
    el.addEventListener('keydown', function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); open(); } });
  });
}

function openReader(dirKey, idx, pushStack){
  var entry = (LIBRARY[dirKey]||[])[idx];
  if(!entry) return;
  if(pushStack && readerOpen){ readerStack.push({dir:currentReaderDir, idx:currentReaderIdx}); }
  else if(pushStack){ readerStack = []; }
  currentReaderDir = dirKey; currentReaderIdx = idx;
  readerTitle.textContent = entry.title;
  var metaParts = [];
  if(entry.type) metaParts.push(entry.type);
  if(entry.status) metaParts.push(entry.status);
  readerMeta.textContent = metaParts.join(' · ');
  readerBody.innerHTML = entry.bodyHtml || '<p><em>Fiche vide.</em></p>';
  readerBack.hidden = readerStack.length===0;
  Array.prototype.forEach.call(readerBody.querySelectorAll('.xlink'), function(a){
    a.addEventListener('click', function(){
      playUiBlip(720);
      openReader(a.getAttribute('data-dir'), parseInt(a.getAttribute('data-idx'),10), true);
    });
  });
  readerBody.scrollTop = 0;
  readerEl.classList.add('open');
  readerOpen = true;
}
var currentReaderDir=null, currentReaderIdx=null;
function closeReader(){ readerEl.classList.remove('open'); readerOpen=false; playUiBlip(420); }
readerClose.addEventListener('click', closeReader);
readerBack.addEventListener('click', function(){
  var prev = readerStack.pop();
  if(prev) openReader(prev.dir, prev.idx, false);
  readerBack.hidden = readerStack.length===0;
  playUiBlip(540);
});
readerEl.addEventListener('click', function(e){ if(e.target===readerEl) closeReader(); });

// ---------- search ----------
var searchToggle = document.getElementById('search-toggle');
var searchPanel = document.getElementById('search-panel');
var searchInput = document.getElementById('search-input');
var searchResultsEl = document.getElementById('search-results');
var searchIndex = [];
Object.keys(LIBRARY).forEach(function(dirKey){
  var room = ROOMS.filter(function(r){ return r.key===dirKey; })[0];
  var roomName = room ? room.name : dirKey;
  LIBRARY[dirKey].forEach(function(entry, idx){
    searchIndex.push({dir:dirKey, idx:idx, title:entry.title, room:roomName});
  });
});
function normalizeText(s){
  return s.toLowerCase().normalize('NFD').replace(new RegExp('[\\u0300-\\u036f]','g'),'');
}
var searchIndexNorm = searchIndex.map(function(e){ return {e:e, n:normalizeText(e.title)}; });

function openSearch(){
  searchPanel.hidden = false; searchToggle.setAttribute('aria-expanded','true');
  searchInput.value=''; searchResultsEl.innerHTML=''; searchInput.focus();
}
function closeSearch(){ searchPanel.hidden = true; searchToggle.setAttribute('aria-expanded','false'); }
searchToggle.addEventListener('click', function(){ searchPanel.hidden ? openSearch() : closeSearch(); });

searchInput.addEventListener('input', function(){
  var q = normalizeText(searchInput.value.trim());
  if(!q){ searchResultsEl.innerHTML=''; return; }
  var matches = searchIndexNorm.filter(function(x){ return x.n.indexOf(q)!==-1; }).slice(0,8);
  if(!matches.length){ searchResultsEl.innerHTML = '<div class="search-empty">Aucune fiche trouvée.</div>'; return; }
  searchResultsEl.innerHTML = matches.map(function(m){
    return '<div class="search-result" data-dir="'+escapeHtml(m.e.dir)+'" data-idx="'+m.e.idx+'" tabindex="0">'+
      '<div class="search-result-title">'+escapeHtml(m.e.title)+'</div>'+
      '<div class="search-result-room">'+escapeHtml(m.e.room)+'</div></div>';
  }).join('');
  Array.prototype.forEach.call(searchResultsEl.querySelectorAll('.search-result'), function(el){
    var pick = function(){
      playUiBlip(600);
      openReader(el.getAttribute('data-dir'), parseInt(el.getAttribute('data-idx'),10), true);
      closeSearch();
    };
    el.addEventListener('click', pick);
    el.addEventListener('keydown', function(e){ if(e.key==='Enter'){ pick(); } });
  });
});
searchInput.addEventListener('keydown', function(e){ if(e.key==='Escape'){ closeSearch(); e.stopPropagation(); } });
window.addEventListener('keydown', function(e){
  if(e.key==='/' && !readerOpen && document.activeElement!==searchInput){ e.preventDefault(); openSearch(); }
});

var currentRoomRef = ROOMS[0];
renderRoom(currentRoomRef);

// ---------- start / loading ----------
document.getElementById('loading').classList.add('hidden');
var startOverlay = document.getElementById('start-overlay');
document.getElementById('start-btn').addEventListener('click', begin);
var started = false;
function begin(){ if(started) return; started=true; startOverlay.classList.add('hidden'); initAudio(); lastTime=performance.now(); requestAnimationFrame(loop); }

// ---------- minimap ----------
var mini = document.getElementById('minimap');
var mctx = mini.getContext('2d');
function drawMinimap(){
  mctx.clearRect(0,0,150,130);
  var pad = 8;
  var scale = Math.min((150-pad*2)/(maxX-minX), (130-pad*2)/(maxY-minY));
  function mx(x){ return pad + (x-minX)*scale; }
  function my(y){ return pad + (y-minY)*scale; }
  ROOMS.forEach(function(r){
    mctx.fillStyle = WING_COLORS_CSS[r.wing] || '#888';
    mctx.globalAlpha = r.id===currentRoomRef.id ? 1 : 0.55;
    mctx.fillRect(mx(r.x0), my(r.y0), (r.x1-r.x0)*scale, (r.y1-r.y0)*scale);
  });
  mctx.globalAlpha = 1;
  mctx.fillStyle = '#fff3e2';
  mctx.beginPath(); mctx.arc(mx(player.x/TILE), my(player.z/TILE), 2.6, 0, Math.PI*2); mctx.fill();
  var fx = mx(player.x/TILE) + Math.sin(player.yaw)*7, fy = my(player.z/TILE)+Math.cos(player.yaw)*7;
  mctx.strokeStyle='#fff3e2'; mctx.lineWidth=1.5;
  mctx.beginPath(); mctx.moveTo(mx(player.x/TILE),my(player.z/TILE)); mctx.lineTo(fx,fy); mctx.stroke();
}

// ---------- loop ----------
var lastTime = 0;
var frameCount = 0;
var fwd = new THREE.Vector3(), right = new THREE.Vector3(), up = new THREE.Vector3(0,1,0);
function loop(t){
  var dt = Math.min((t-lastTime)/1000, 0.05);
  lastTime = t;
  frameCount++;
  update(dt, t/1000);
  render(t/1000);
  requestAnimationFrame(loop);
}

var walkPhase = 0;
var lastFootPhase = 0;
function update(dt, time){
  var mdx=0, mdz=0;
  if(!readerOpen){
    fwd.set(-Math.sin(player.yaw), 0, -Math.cos(player.yaw));
    right.set(Math.cos(player.yaw), 0, -Math.sin(player.yaw));
    if(keys.up){ mdx+=fwd.x; mdz+=fwd.z; }
    if(keys.down){ mdx-=fwd.x; mdz-=fwd.z; }
    if(keys.right){ mdx+=right.x; mdz+=right.z; }
    if(keys.left){ mdx-=right.x; mdz-=right.z; }
  }
  player.moving = (mdx!==0 || mdz!==0);
  var len = Math.hypot(mdx,mdz);
  if(len>0){ mdx/=len; mdz/=len; }

  var nx = player.x + mdx*player.speed*dt;
  var nz = player.z + mdz*player.speed*dt;
  if(canStand(nx, player.z)) player.x = nx;
  if(canStand(player.x, nz)) player.z = nz;

  // character faces movement direction, smoothly
  var prevFacing = player.facing;
  if(player.moving){
    var targetFacing = Math.atan2(mdx, mdz);
    player.facing += shortAngleDiff(player.facing, targetFacing) * Math.min(1, dt*10);
  }
  var turnRate = dt>0 ? shortAngleDiff(prevFacing, player.facing)/dt : 0;
  playerModel.position.set(player.x, 0, player.z);
  playerModel.rotation.y = player.facing;

  // walk-cycle limb animation
  if(player.moving) walkPhase += dt * 8.5;
  var swing = (reduceMotion || !player.moving) ? 0 : Math.sin(walkPhase)*0.62;
  var swing2 = (reduceMotion || !player.moving) ? 0 : Math.sin(walkPhase+Math.PI)*0.62;
  playerModel.userData.legL.rotation.x = swing;
  playerModel.userData.legR.rotation.x = swing2;
  playerModel.userData.armL.rotation.x = swing2*0.7;
  playerModel.userData.armR.rotation.x = swing*0.7;
  var bob = (reduceMotion || !player.moving) ? 0 : Math.abs(Math.sin(walkPhase))*0.09;
  playerModel.userData.hips.position.y = bob + (reduceMotion?0:Math.sin(time*1.3)*0.01);
  playerModel.userData.cape.rotation.x = 0.18 + (reduceMotion?0:Math.sin(walkPhase*0.5)*0.05) + (player.moving?0.12:0);
  var targetCapeYaw = reduceMotion ? 0 : Math.max(-0.5, Math.min(0.5, -turnRate*0.12));
  playerModel.userData.cape.rotation.y += (targetCapeYaw - playerModel.userData.cape.rotation.y) * Math.min(1, dt*6);

  // footstep: trigger on each half walk-cycle
  if(player.moving){
    var footPhase = Math.floor(walkPhase/Math.PI);
    if(footPhase !== lastFootPhase){
      lastFootPhase = footPhase;
      playFootstep();
      spawnDust(player.x, player.z);
    }
  }
  updateDust(dt);

  // third-person orbit camera
  var dist = 9.5;
  var camY = 2.0 + dist*Math.sin(player.pitch);
  var horiz = dist*Math.cos(player.pitch);
  var camX = player.x + Math.sin(player.yaw)*horiz;
  var camZ = player.z + Math.cos(player.yaw)*horiz;
  camera.position.set(camX, camY, camZ);
  camera.lookAt(player.x, 1.5, player.z);

  var tx = player.x/TILE, tz = player.z/TILE;
  var room = findRoomAt(tx,tz);
  if(room){
    currentRoomRef = room;
    renderRoom(room);
    breadcrumbEl.textContent = 'Citadelle du Sham › ' + WING_NAMES[room.wing] + (room.key ? (' › ' + room.name) : '');
  } else {
    var wing = findWingAt(tx,tz);
    if(wing) breadcrumbEl.textContent = 'Citadelle du Sham › ' + WING_NAMES[wing] + ' › Couloir';
  }

  var nearestTorchDist = Infinity;
  torchLights.forEach(function(o){
    var f = reduceMotion ? 1 : (0.82 + 0.22*Math.sin(time*6.5 + o.seed) + 0.06*Math.sin(time*17+o.seed));
    if(o.light) o.light.intensity = 2.1*f;
    o.flame.scale.setScalar(0.85*f + 0.3);
    var d = Math.hypot(o.wx-player.x, o.wz-player.z);
    if(d<nearestTorchDist) nearestTorchDist = d;
  });
  if(crackleGain){
    var proximity = Math.max(0, 1 - nearestTorchDist/(TILE*7));
    crackleGain.gain.value = 0.02 + proximity*0.16;
  }
}

function render(){
  renderer.render(scene, camera);
  drawMinimap();
}
})();
</script>
"""

html = TEMPLATE
html = html.replace("__THREE_SRC__", THREE_SRC)
html = html.replace("__LIBRARY_JSON__", LIBRARY_JSON)
html = html.replace("__ROOMS_JSON__", ROOMS_JSON)
html = html.replace("__CORRIDORS_JSON__", CORRIDORS_JSON)

out_path = os.path.join(HERE, 'citadelle-sham.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("written", out_path, len(html), "bytes")
