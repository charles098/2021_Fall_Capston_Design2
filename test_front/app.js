URL = window.URL || window.webkitURL;

let gumStream; 						//stream from getUserMedia()
let rec; 							//Recorder.js object
let input; 							//MediaStreamAudioSourceNode we'll be recording

// shim for AudioContext when it's not avb. 
let AudioContext = window.AudioContext || window.webkitAudioContext;
let audioContext //audio context to help us record

let recordButton = document.getElementById("recordButton");
let stopButton = document.getElementById("stopButton");
let pauseButton = document.getElementById("pauseButton");

const mic_img = document.querySelector('img');

document.addEventListener("keydown", downHandler); // spacebar 누름
document.addEventListener("keyup", upHandler); // spacebar 뗌


let flag = true;

// spacebar 누름 - 녹음 시작
function downHandler(e){
    if(flag){
        flag = false;
        
        if(e.keyCode == 32){
            console.log('스페이스바를 누르셨습니다. 녹음 시작');

            // 사진 mic_on으로 변경
            mic_img.src = "images/mic_on.png";


            // 녹음 시작
            let constraints = { audio: true, video:false }

            navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
                console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
        
                /*
                    create an audio context after getUserMedia is called
                    sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
                    the sampleRate defaults to the one set in your OS for your playback device
        
                */
                audioContext = new AudioContext();
        
        
                /*  assign to gumStream for later use  */
                gumStream = stream;
                
                /* use the stream */
                input = audioContext.createMediaStreamSource(stream);
        
                /* 
                    Create the Recorder object and configure to record mono sound (1 channel)
                    Recording 2 channels  will double the file size
                */
                rec = new Recorder(input,{numChannels:1})
        
                //start the recording process
                rec.record()
        
                console.log("Recording started");
        
            }).catch(function(err) {
                console.log("error");
            });
        }
    }   
}

// spacebar 뗌 - 녹음 끝
function upHandler(e){
    if(!flag){
        flag = true;

        if(e.keyCode ==  32){
            console.log('스페이스바를 떼셨습니다. 녹음 끝');

            // 사진 mic_off로 변경
            mic_img.src = "images/mic_off.png";


            console.log("stopButton clicked");

            //tell the recorder to stop the recording
            rec.stop();

            //stop microphone access
            gumStream.getAudioTracks()[0].stop();

            //create the wav blob and pass it on to createDownloadLink
            //rec.exportWAV(createDownloadLink);
            rec.exportWAV(blob => {
                console.log(blob);
                var url = URL.createObjectURL(blob);
                var filename = new Date().toISOString();
                var link = document.createElement('a');
                link.href = url;
                link.download = filename + '.wav';
                link.style.display = 'none';
                link.click();
                link.remove();
            })
        }
    }
}

/*
const spawn = require('child_process').spawn; 

const result = spawn('python', ['pyFiles/print.py']); 
//const result = spawn('C:\\Users\\LeeChan\\Anaconda3\\envs\\py37_32\\python', ['test.py']); 

 
result.stdout.on('data', function(data) {
    console.log(data.toString()); 
}); 

result.stderr.on('data', function(data) { 
    console.log(data.toString()); 
});
*/
