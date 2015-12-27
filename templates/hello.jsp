{% extends "layout.jsp" %}
{% block content %}
<script>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                alert("{{ message }}")
            {% endfor %}
        {% endif %}
    {% endwith %}
</script>
<div class="card-panel">
	<h5>Hello World!</h5>
	<h4>{% if session.username %} Hi {{session.username}} ! {% endif %}Welcome to the demo twitter app made in Flask</h4>
</div>
<div>
	<p>Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.</p>
	</br>
	<img src="http://flask.pocoo.org/static/logo/flask.png" style="width:300px;height:117px;">
	</br>
	The image is licensed under the “Flask Artwork License”.
	<a href="http://flask.pocoo.org/docs/0.10/license/#flask-artwork-license">Read license text.</a>
</div>
<div class="card-panel">
	<div class="col s2 offset-s4"">
	{% if request.args['message']%}
		</br>
		</br>
		<h5 style="color:red">{{request.args['message']}}</h5>
		</br>
		</br>
	{% endif %}
	{% if "username" in session %}
		<a class="btn waves-effect waves-light blue lighten-1" href="/analysis">
			Enter
			<i class="material-icons right">send</i>
		</a>
	{% else %}
	<a class="btn waves-effect waves-light blue lighten-1" href="/login">
		Login
		<i class="material-icons right">send</i>
	</a>
	{% endif %}
	</div>
	</br></br></br>
	<a href="http://flask.pocoo.org">Click here to learn about Flask</a>
</div>
{% endblock %}

