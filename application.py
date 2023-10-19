6)reg form
form.html

<!DOCTYPE html>
<html>
<head>
<title>Simple Form</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<h1>Simple Form</h1>
<form action="/submit" method="post">
<label for="name">Name:</label>
<input type="text" id="name" name="name" required>
<br>
<label for="email">Email:</label>
<input type="email" id="email" name="email" required>
<br>
<label for="message">Message:</label>
<textarea id="message" name="message" rows="4" cols="50"
required></textarea>
<br>
<br>
<label for="message">Address</label>
<textarea id="message" name="message" rows="10" cols="100"
required></textarea>
<br>
<input type="submit" value="Submit" >
</form>
<marquee>Please fill out the registration form</marquee>
</body>
</html>
styles.css:
body {
font-family: Arial, sans-serif;
margin: 20px;
}
h1 {
text-align: center;
}
form {
max-width: 400px;
margin: 0 auto;
}
label {
display: block;
margin-bottom: 5px;
}
input[type="text"],
input[type="email"],
textarea {
width: 100%;
padding: 8px;
margin-bottom: 10px;
border: 1px solid #ccc;
border-radius: 4px;
}
input[type="submit"] {
background-color: #4CAF50;
color: white;
padding: 10px 15px;
border: none;
border-radius: 4px;
cursor: pointer;
width: 100%;
}
input[type="submit"]:hover {
background-color: #45a049;
}
input:required,
textarea:required {
border-color: #FF0000;
}


7)index.html:

<!DOCTYPE html>
<head>
<title>Simple Calculator</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="calculator">
<input type="text" id="display" disabled>
<div class="buttons">
<button class="operator"
onclick="clearDisplay()">C</button>
<button class="operator"
onclick="backspace()">&larr;</button>
<button class="operator"
onclick="appendOperator('+')">+</button>
<button class="operator"></button>
<button onclick="appendNumber('7')">7</button>
<button onclick="appendNumber('8')">8</button>
<button onclick="appendNumber('9')">9</button>
<button class="operator" onclick="appendOperator('-')">-
</button>
<button onclick="appendNumber('4')">4</button>
<button onclick="appendNumber('5')">5</button>
<button onclick="appendNumber('6')">6</button>
<button class="operator"
onclick="appendOperator('*')">*</button>
<button onclick="appendNumber('1')">1</button>
<button onclick="appendNumber('2')">2</button>
<button onclick="appendNumber('3')">3</button>
<button class="operator"
onclick="appendOperator('/')">/</button>
<button onclick="appendNumber('.')">.</button>
<button onclick="appendNumber('0')">0</button>
<button class="operator"></button>
<button class="operator" onclick="calculate()">=</button>
</div>
</div>
<script src="script.js"></script>
</body>
</html>


styles.css:

body {
font-family: Arial, sans-serif;
line-height: 1.6;
display: flex;
justify-content: center;
align-items: center;
min-height: 100vh;
margin: 0; }
.calculator {
border: 1px solid #ccc;
border-radius: 5px;
width: 250px;
padding: 10px;
}
input {
width: 90%;
font-size: 20px;
padding: 10px;
text-align: right;
margin-bottom: 10px;
}
.buttons {
display: grid;
grid-template-columns: repeat(4, 1fr);
gap: 5px;
}
button {
font-size: 20px;
padding: 10px;
cursor: pointer;
border: none;
border-radius: 5px; }
.operator {
background-color: #007BFF;
color: #fff;
}
script.js:
let display = document.getElementById('display');
let expression = ' ';
function appendNumber(num) {
expression += num;
display.value = expression;
}
function appendOperator(operator) {
if (expression === '') return;
expression += operator;
display.value = expression;
}
function calculate() {
try {
const result = eval(expression);
display.value = result;
expression = result.toString();}
catch (error) {
display.value = 'Error';
expression = '';
}
}
function clearDisplay() {
expression = '';
display.value = '';}
function backspace() {
expression = expression.slice(0, -1);
display.value = expression;}


8)form validation angular js
<html>
<head>
<title>Form Validation</title>
<script type="text/javascript">
function validate(){
var fname=document.getElementById("name");
var usrname=document.getElementById("username");
var password=document.getElementById("password1");
var repassword=document.getElementById("password2");
var address=document.getElementById("address");
var age=document.getElementById("age");
var gender=document.getElementById("gender");
if(fname.value==""||usrname.value==""||address.value==""||age.va
lue==""||password.value==""||repassword.value=="")
{
alert("fill all the details");
return false;
}
else{
return true;
} }
</script>
</head>
<body>
<form onsubmit="return validate()" action="xyz.html"
method="POST">
<center><h3>Registration form<h3>
<table border="4" bordercolor="#7FFFD4" cellspacing="2"
cellpadding="2" width="40%">
<tr>
<td>Full name</td>
<td>:</td>
<td><input type="text" placeholder="Full name" id="name"></td>
</tr>
<tr>
<td>User name</td>
<td>:</td>
<td><input type="text" placeholder="User name"
id="username"></td>
</tr>
<tr>
<td>Password</td>
<td>:</td>
<td><input type="password" placeholder="Password"
id="password1"></td>
</tr>
<tr>
<td>Re Password</td>
<td>:</td>
<td><input type="Password" placeholder="Repassword"
id="password2"></td>
</tr>
<tr>
<td>Address</td>
<td>:</td>
<td><input type="textarea" placeholder="Address"
id="address"></td>
</tr>
<tr>
<td>Age</td>
<td>:</td>
<td><input type="number" label="age" id="age"></td>
</tr>
<tr>
<td>Gender</td>
<td>:</td>
<td style="width: 8%"><input type="radio" label="male"
name="Gender" value="1">male
<input type="radio" label="female" name="Gender"
value="0">female</td>
</tr>
</table>
<br><br>
<input type="submit" name="submit">
</center>
</form>
</body>


9)implement express angular js

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AngularJS Expression</title>
<script
src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angul
ar.min.js"></script>
</head>
<body bgcolor="cyan">
<div ng-app="">
<center>
<p>My first expression: {{ 10 + 5 }}</p>
</center>
</div>
</body>
</html>


10)backend building angular js

<html>
<head>
<script
src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angul
ar.min.js"></script>
<script>
var app=angular.module("myapp",[])
app.controller("myctrl",function($scope){
$scope.s=[{
rollno:"1",
name:"Ushij",
dept:"it",
address:"hyd"
},
{
rollno:"2",
name:"Anu",
dept:"ece",
address:"chennai"
},
{
rollno:"3",
name:"Sanjay",
dept:"mech",
address:"bangalore"
},
{
rollno:"4",
name:"Abhi",
dept:"ece",
address:"mumbai"
},
{
rollno:"5",
name:"Niraj",
dept:"civil",
address:"delhi"
}]
})
</script>
</head>
<body ng-app="myapp">
<div ng-controller="myctrl">
<center>
<table border="4">
<tr>
<td>rollno</td>
<td>name</td>
<td>dept</td>
<td>address</td>
</tr>
<tr ng-repeat="student in s">
<td>{{student.rollno}}</td>
<td>{{student.name}}</td>
<td>{{student.dept}}</td>
<td>{{student.address}}</td>
</tr>
</table>
</center>
</body>
</html>
