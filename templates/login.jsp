{% extends "layout.jsp" %}
{% block content %}
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
{% endblock %}