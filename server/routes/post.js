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
})

module.exports = router;