{% extends "layout.jsp" %}
{% block content %}
<div align="center">
	<div class="row">
	<div class="card-panel">
		<h5>The result for the analysis for option {{session.option}} is</h5>
	</div>
	</div>
	<div class="row">
	<div class="card-panel col l4 offset-l4 s6 offset-s3 left">
		<table class="striped" border="1px">
			<tr>
				{% for header in headers %}
					<th>{{header}}</th>
				{% endfor %}
			</tr>
		<tbody>
		{% for result in results %}
			<tr>
				{% for val in result %}
					<td>{{val}}</td>
				{% endfor %}
			</tr>
		{% endfor %}
		</tbody>
		</table>
	</div>
	</div>
	<div class="row">
	<div class="card-panel">
		<a class="btn waves-effect waves-light blue lighten-1" href="/analysis">
			Select another analysis
			<i class="material-icons right">send</i>
		</a>
	</div>
	</div>
</div>
{% endblock %}