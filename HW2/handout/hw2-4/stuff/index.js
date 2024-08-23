#!/usr/bin/env node
const express = require('express')

const app = express()
const flag1 = 'CE441{testflag1}'
const flag2 = 'CE441{testflag2}'
const users = {
	'admin':'secret_password', // Admin password will be changed when deployed
	'alice':'alice',
}

app.use(express.urlencoded({ extended: true }))

app.post('/login',(req,res)=>{
	let username = req.body.username
	let password = req.body.password
	if(username && password){
		if(username !== 'alice' && users[username] == password){
			return res.send(`Logged in! Here's your flag: ${flag1}`)
		}
	}
	res.end('Wrong username or password')
})

app.post('/bonus-login',(req,res)=>{
	let username = req.body.username
	let password = req.body.password
	if(username && password){
		if(username.length < 6 && username !== 'alice' && users[username] == password){
			return res.send(`wow you know nodejs so well: ${flag2}`)
		}
	}
	res.end('Wrong username or password')
})

app.listen(8000)