from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "key"