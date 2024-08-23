<?php
// You can try logging in by guest:guest
if(isset($_GET['username']) && isset($_GET['password'])){
	header('Content-Type: text/plain');
	$username = $_GET['username'];
	$password = $_GET['password'];
	$mysqli = new mysqli("db","user","password","sharifdb");
	$r = $mysqli->query("SELECT * FROM users WHERE username = '{$username}' and password = '{$password}'")->fetch_assoc();
	if($r){
		echo 'Correct!';
	} else {
		echo 'Wrong username or password :(';
	}
	$mysqli->close();
	die();
}

highlight_file(__FILE__);

