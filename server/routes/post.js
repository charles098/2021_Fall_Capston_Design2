const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const spawn = require('child_process').spawn; 

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
    res.sendStatus(200);
    
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
    */
})

module.exports = router;