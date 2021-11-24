const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const spawn = require('child_process').spawn; 
const WebSocket = require('ws').Server;
const wss = new WebSocket({port: 8000});
const router = express.Router();

try{
    fs.readdirSync('uploads');
} catch(err){
    console.error('uploads 폴더가 없어 uploads 폴더를 생성합니다.');
    fs.mkdirSync('uploads');
}

const upload = multer();

router.post('/uploads', upload.single('soundBlob'), (req, res, next) => {
    let filename = new Date().toISOString();
    filename = filename.replaceAll(':', '_');
    let uploadLocation = __dirname + '/../uploads/' + filename + req.file.originalname;
    fs.writeFileSync(uploadLocation, Buffer.from(new Uint8Array(req.file.buffer)));

    //console.log(req.body.TTSfilename);
    
    filename = filename + '.wav';
    // 업로드 완료

    
    // 프로세스 진행
    function STT() {
        const voice = spawn('python', [__dirname + '/../api_codes/naverCloba.py', filename]);   
        return new Promise((res, rej) => {
            voice.stdout.on('data', data => {
                res(data.toString());
            })
        });
    }
    
    // mecab에서 형태소 분석 후 메뉴얼에 따라 키워드만 넘긴다
    function getMecab(corps) {
        const mecab = spawn('python', [__dirname + '/../api_codes/mecab.py', corps]);
        return new Promise((res, rej) => {
            mecab.stdout.on('data', data => {
                res(data.toString());
            })
        })
    }
    
    function reqStock(tags){
        const stock = spawn('C:\\Users\\LeeChan\\Anaconda3\\envs\\py37_32\\python', [__dirname + '/../api_codes/daeshin/main.py', tags]); 
        return new Promise((res, rej) => {
            stock.stdout.on('data', data => {
                res(data.toString());
            })
        })
    }

    function kakaoTTS(text){
        const text_result = spawn('python', [__dirname + '/../api_codes/kakaoTTS.py', text, req.body.TTSfilename]);
        return new Promise((res, rej) => {
            text_result.stdout.on('data', data => {
                res(data.toString());
                
            })
        })
    }
      
    
    STT()
        .then(res => getMecab(res))
        .then(res => reqStock(res))
        .then(res => kakaoTTS(res))
        .then(res => {
            console.log(res);
            /*
            wss.on('connection', ws => {
                //ws.send("Hello! I an a server");
                ws.on("message", message => {
                    ws.send(res);
                    console.log("Received: %s", message);
                })
            })
            */
        });

    

    
    
    /*
    // 네이버 클로바 api로 STT 실행
    const result = spawn('python', [__dirname + '/../api_codes/naverCloba.py', filename]); 
    //const result = spawn('C:\\Users\\LeeChan\\Anaconda3\\envs\\py37_32\\python', ['test.py']); 
    
    // 정상작동
    result.stdout.on('data', (data) => {
        console.log(data.toString()); 
    }); 

    // 에러
    result.stderr.on('data', data => { 
        console.log(data.toString()); 
    });
    

    resourcePath = "./audio/output.mp3"
    var stream = fs.createReadStream(resourcePath);
    // 2. 잘게 쪼개진 stream 이 몇번 전송되는지 확인하기 위한 count
    var count = 0;
    // 3. 잘게 쪼개진 data를 전송할 수 있으면 data 이벤트 발생 
    stream.on('data', function(data) {
      count = count + 1;
      console.log('data count='+count);
      // 3.1. data 이벤트가 발생되면 해당 data를 클라이언트로 전송
      res.write(data);
      console.log(data)
    });

    // 4. 데이터 전송이 완료되면 end 이벤트 발생
    stream.on('end', function () {
      console.log('end streaming');
      // 4.1. 클라이언트에 전송완료를 알림
      res.end();
    });
    */
   
    res.sendStatus(200);
})

module.exports = router;