process.stdin.resume();
process.stdin.setEncoding('utf8');
// 自分の得意な言語で
// Let's チャレンジ！！
var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  lines.push(line);
});
reader.on('close', () => {
 let a = Number(lines[0]);

  let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  console.log(alphabet.substr(0, a));
  
});