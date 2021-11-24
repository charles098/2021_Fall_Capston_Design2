const express = require('express');
const morgan = require('morgan');
const path = require('path');
const dotenv = require('dotenv');
const nunjucks = require('nunjucks');

dotenv.config();
//const webSocket = require('./routes/socket');
const indexRouter = require('./routes/index');
const postRouter = require('./routes/post');

const app = express();
app.set('port', 8080);
app.set('view engine', 'html');
nunjucks.configure('views', {
  express: app,
  watch: true,
});

app.use(morgan('dev'));
app.use(express.static(path.join(__dirname, 'public')));
app.use('/audio', express.static(path.join(__dirname, 'uploads')));
app.use('/tts', express.static(path.join(__dirname, 'ttsFile'))); 
app.use(express.json());

app.use('/', indexRouter);
app.use('/post', postRouter);
//app.use('/socket', webSocket);

app.use((req, res, next) => {
        const error = new Error(`${req.method} ${req.url} 라우터가 없습니다.`);
        error.status = 404;
        next(error);
});

app.use((err, req, res, next) => {
        res.locals.message = err.message;
        res.locals.error = err;
        res.status(err.status || 500);
        res.render('error');
})

//const server = 
app.listen(app.get('port'), () => {
        console.log(app.get('port'), '번 포트에서 대기중');
})

//webSocket(server);