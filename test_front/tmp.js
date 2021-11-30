const spawn = require('child_process').spawn; 
const nodeID3 = require('node-id3');

text = '지후 누나 보고싶다'
filename = 'haha.mp3'

const result = spawn('python', [__dirname + '/api_codes/kakaoTTS.py', text, filename]);


result.stdout.on('data', function(data) {
    console.log(data.toString()); 
}); 

result.stderr.on('data', function(data) { 
    console.log(data.toString()); 
});

interval = setInterval(() => {
    try{
        nodeID3.read("./ttsFile/haha.mp3");
        clearInterval(interval);
    }
    catch(err){}
}, 100)

//console.log(id3);