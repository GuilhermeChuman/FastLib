# FastLib

<h2>DEPENDENCIES</h2>
 <p> $ pip install aiomysql </p>
 <p> $ pip install databases </p>
 <p> $ pip install uvicorn </p>
 <p> $ pip install fastapi </p>
 <p> $ pip install python-multipart </p>
 <p> $ pip install pandas </p>

<h2>HOW TO RUN </h2>
 <p> $ python3 -m uvicorn main:app --reload </p>

<h2>HOSTING ON HEROKU</h2>

You can host this aplication on <a href="https://Fwww.heroku.com">Heroku</a> having the Procfile and requirements.txt files and so:

<p> 1. Install Heroku CLI </p>
```
$ curl https://cli-assets.heroku.com/install.sh | sh
```

<p> 2. Login or Create your Heroku account </p>
```
$ heroku login
```

<p> 3. Upload your application </p>
```
$ git add .
$ git commit -m "init heroku"
$ git push heroku main
```
