const spawn = require('child_process').spawn; 

// 음성 받아오기 -> mecab 형태소 분석 -> 증권사로 넘기기 -> 결과 출력 
/*
// 1. 음성 받아오기
const voice = spawn('python', ['./temp/카카오stt.py', 'haha']); 

let voice_result;

voice.stdout.on('data', (data) => {
    console.log(data.toString());
    voice_result = data.toString(); 
});

console.log(voice_result);

//2. mecab 형태소 분석
const mecab = spawn('python', ['mecab.py', voice_result]); 

let mecab_result;

mecab.stdout.on('data', (data) => {
    mecab_result = data.toString();
})

console.log(mecab_result);


/*
//파이썬 파일 실행
const spawn = require('child_process').spawn; 

//const result = spawn('python', ['mecab.py', 'haha']); 
//const result = spawn('C:\\Users\\LeeChan\\Anaconda3\\envs\\py37_32\\python', ['test.py']); 
const result = spawn('python', ['./temp/카카오stt.py', 'haha']); 

result.stdout.on('data', function(data) {
    console.log(data.toString()); 
}); 

result.stderr.on('data', function(data) { 
    console.log(data.toString()); 
});
*/

function STT() {
    const voice = spawn('python', ['./temp/카카오stt.py']);  
    return new Promise((res, rej) => {
        voice.stdout.on('data', data => {
            res(data.toString());
        })
    });
}

function getMecab(corps) {
    const mecab = spawn('python', ['./mecab.py', corps]);
    return new Promise((res, rej) => {
        mecab.stdout.on('data', data => {
            res(data.toString());
        })
    })
}

function reqStock(){
    const stock = spawn('C:\\Users\\LeeChan\\Anaconda3\\envs\\py37_32\\python', ['증권사API.py']); 
    return new Promise((res, rej) => {
        stock.stdout.on('data', data => {
            res(data.toString());
        })
    })
}
  

STT()
    .then(res => getMecab(res))
    .then(res => console.log(res))
    .then(res => reqStock())
    .then(res => {
        console.log(res);
    });


/*
STT()
    .then(res => {
        console.log('STT 진행완료');
        return getMecab(res);}
    ).then(res => {
        console.log(res);
        console.log('NLP 진행완료');
    })
*/


// spawn 동기방식 도움받은 사이트
// https://stackoverflow.com/questions/59107079/how-to-return-value-from-a-child-process-in-a-function