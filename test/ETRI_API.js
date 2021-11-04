//ETRI API 사용 예제

var fs = require('fs');
var openApiURL = 'http://aiopen.etri.re.kr:8000/WiseASR/Recognition';
var access_key = '36e97828-2f1c-4eef-afd3-3e0768c54360';
var languageCode = 'korean';
var audioFilePath = './audio_file/hello2.wav';
var audioData;
 
var audioData = fs.readFileSync(audioFilePath);
 
var requestJson = {
    'access_key': access_key,
    'argument': {
        'language_code': languageCode,
        'audio': audioData.toString('base64')
    }
};
 
var request = require('request');
var options = {
    url: openApiURL,
    body: JSON.stringify(requestJson),
    headers: {'Content-Type':'application/json; charset=UTF-8'}
};
request.post(options, function (error, response, body) {
    console.log('responseCode = ' + response.statusCode);
    console.log('responseBody = ' + body);
});
