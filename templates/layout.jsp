<html>
    <head>
        <!-- CSS Source http://materializecss.com/about.html, used under MIT License as given in project files -->

        <!--Import Google Icon Font-->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
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
		<header class="page-header">
			{% if session.username %}
				<a class="btn waves-effect waves-light left" href="/index">
					{{session.username}}
					<i class="material-icons left">perm_identity</i>
				</a>
				<a class="btn waves-effect waves-light right" href="/logout">
					Logout
					<i class="material-icons right">input</i>
				</a>
			{% endif %}
		</header>
		{% block content %}
		{% endblock %}
		<footer class="page-footer blue lighten-5">
			<div>
				<p class="grey-text">Links to resources
					<a class="blue-text text-lighten-1" href="http://materializecss.com/">Materialze CSS</a>
					<a class="blue-text text-lighten-1" href="http://flask.pocoo.org/">Flask</a>
				</p>
			</div>
			<div class="footer-copyright">
				<div>
					<span class="black-text left">Developed by Nitish</span>
					<span class="black-text right">95-733 Internet Technologies. Carnegie Mellon University</span>
					</p>
				</div>
			</div>
		</footer>	                  
	</body>
</html>