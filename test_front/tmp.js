const spawn = require('child_process').spawn; 

const result = spawn('python', ['pyFiles/print.py']); 
//const result = spawn('C:\\Users\\LeeChan\\Anaconda3\\envs\\py37_32\\python', ['test.py']); 


result.stdout.on('data', function(data) {
    console.log(data.toString()); 
}); 

result.stderr.on('data', function(data) { 
    console.log(data.toString()); 
});
