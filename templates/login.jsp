<html>
    <head>
        <!-- CSS Source http://materializecss.com/about.html, used under MIT License as given in project files -->

        <!--Import Google Icon Font-->
        <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <!--Import materialize.css-->
        <link type="text/css" rel="stylesheet" href="{{url_for('static', filename='materialize.min.css')}}"  media="screen,projection"/>
        <!--Let browser know website is optimized for mobile-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.1/css/materialize.min.css">
        <title>Tweet Analytics</title>
    </head>
	<body>
	<!--Import jQuery before materialize.js-->
	<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
	<script type="text/javascript" src="{{url_for('static', filename='materialize.min.js')}}"></script>
        <div align="center">
            <div class="card-panel">
                <h5>Please enter your username and password below</h5>
            </div>
            <form action="login" method="POST">
                <div class="row">
				<div class="col l2 offset-l5 s6 offset-s3">
                    <div class="input-field">
                        <i class="material-icons prefix">perm_identity</i>
                        <input id="username" type="text" name="username">
						<label class="active" for="username">Username</label>
                    </div>
					</div>
                </div>
				<div class="row">
						<div class="col l2 offset-l5 s6 offset-s3">		

                    <div class="input-field">
                        <i class="material-icons prefix">visibility_off</i>
                        <label class="active" for="password">Password</label>
						<input id="password" type="password" name="password">
						
                    </div>
					</div>
                </div>
                <div class="card-panel">
                    <button class="btn waves-effect waves-light blue lighten-1" type="submit">
                        Submit
                        <i class="material-icons right">send</i>
                    </button>
                </div>
				</div>
            </form>
        </div>
	<footer class="page-footer blue lighten-5">
		<div>
			<p class="grey-text">Links to resources
				<a class="blue-text text-lighten-1" href="http://materializecss.com/">Materialze CSS</a>
				<a class="blue-text text-lighten-1" href="http://flask.pocoo.org/">Flask</a>
			</p>
		</div>
		<div class="footer-copyright">
			<div>
				<p class="black-text">Developed by Nitish for 95-733 Internet Technologies. Carnegie Mellon University 
				<a class="blue-text text-lighten-1 right" href="/logout">Logout</a>
				</p>
			</div>
		</div>
	</footer>	
    </body>
</html>