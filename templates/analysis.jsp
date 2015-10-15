{% extends "layout.jsp" %}
{% block content %}
<div align="center">
	<div class="card-panel">
		<h5>Hi {{session.username}} ! Please choose an analysis to perform below</h4>
	</div>
	<form action="analysis" method="POST">
	<div class="container">
		<div class="row" align="left">
			<div class="col l4 offset-l4 s6 offset-s3">
				<div class="card-panel">
					<input type="radio" class="with-gap" name="option" id="option1" value="1" checked />
					<label for="option1">#HashTag frequency</label>
					</br>
					</br>
					<input type="radio" class="with-gap" name="option" id="option2" value="2" />
					<label for="option2">Word frequency</label>
					</br>
					</br>
					<input type="radio" class="with-gap" name="option" id="option3" value="3" />
					<label for="option3">Sentiment analysis score for positive tweets</label>
					</br>
					</br>
					<input type="radio" class="with-gap" name="option" id="option4" value="4" />
					<label for="option4">Sentiment analysis score for negative tweets</label>
					</br>
					</br>
					<input type="radio" class="with-gap" name="option" id="option5" value="5" />
					<label for="option5">Sentiment analysis score for happiest US states</label>
				</div>
			</div>
		</div>
		<div class="row">
			<div class="col l4 offset-l4 s6 offset-s3">
				<div class="card-panel">
					<div class="row">
					<h6>How many top N values do you want? (default 10)</h6>
					<div class="input-field col l4 offset-l4 s6 offset-s3">
						<i class="material-icons prefix">mode_edit</i>
						<input id="topn" type="text" name="topn">
						<label class="active" for="topn">N</label>
					</div>
					</div>
					<div class="row">
					<h6>How many live tweets do you want? (default 1000)</h6>
					<div class="input-field col l4 offset-l4 s6 offset-s3">
						<i class="material-icons prefix">mode_edit</i>
						<input id="tweet_count" type="text" name="tweet_count">
						<label class="active" for="tweet_count">Tweets</label>
					</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="card-panel">
		<button class="btn waves-effect waves-light blue lighten-1" type="submit">
			Select
			<i class="material-icons right">send</i>
		</button>
	</div>
	</form>
</div>
{% endblock %}