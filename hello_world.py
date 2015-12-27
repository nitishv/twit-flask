from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
import twitterstream, tweet_sentiment, happiest_state, top_tags, top_terms
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.secret_key = 'lTIwhEh95uUM8Rbn7mMFS3SsejOrPXVF'
app.config['PERMANENT_SESSION_LIFETIME'] = 300

@app.route('/index')
@app.route('/')
def index():
    return render_template('hello.jsp')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return redirect(url_for('analysis'))
        else:
            error = 'Invalid username/password'
            return render_template('login.jsp', error=error)
    else:
        return render_template('login.jsp')

        
@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if 'username' not in session:
        return render_template('login.jsp')

    if request.method == 'POST':
        option = (int)(request.form['option'])
        session['option'] = option
        
        if request.form['topn']:
            session['topn'] = (int)(request.form['topn'])
        else:
            session['topn'] = 10
            
        if request.form['tweet_count']:
            session['tweet_count'] = (int)(request.form['tweet_count'])
        else:
            session['tweet_count'] = 1000
        
        print "Option", option        
        print "TopN", session['topn']
        print "Tweets", session['tweet_count']
        
        return redirect(url_for('result'))
    else:
        return render_template('analysis.jsp')

@app.route('/result')
def result():
    if 'username' not in session:
        return render_template('login.jsp')
        
    option = session['option']
    n = session['topn']
    if option == 1:
        headers = ['HashTag', 'Frequency']
        results = top_tags.calculate_top_tags(session['tweet_count'], n)
        if not results:
            return redirect(url_for('result'))
        else:
            return render_template('result.jsp', results=results, headers=headers)
    elif option == 2:
        headers = ['Word', 'Frequency']
        results = top_terms.calculate_term_frequency(session['tweet_count'], n)
        if not results:
            return redirect(url_for('result'))
        else:
            return render_template('result.jsp', results=results, headers=headers)
    elif option == 3:
        headers = ['Tweet', 'Score']
        results = tweet_sentiment.calculate_tweet_sentiment('resources/AFINN-111.txt', session['tweet_count'], n, 1)
        if not results:
            return redirect(url_for('result'))
        else:   
            resp = make_response(render_template('result.jsp', results=results, headers=headers))
            resp.headers['Content-Type'] = 'text/html; charset=utf-8'
            return resp
    elif option == 4:
        headers = ['Tweet', 'Score']
        results = tweet_sentiment.calculate_tweet_sentiment('resources/AFINN-111.txt', session['tweet_count'], n, -1)
        if not results:
            return redirect(url_for('result'))
        else:
            return render_template('result.jsp', results=results, headers=headers)
    elif option == 5:
        headers = ['State Code', 'State Name', 'Tweets', 'Score']
        results = happiest_state.get_state_happiness('resources/AFINN-111.txt', session['tweet_count'])
        if not results:
            return redirect(url_for('result'))
        else:
            return render_template('result.jsp', results=results, headers=headers)

def valid_login(user, pwd):
    if user == 'nitish' and pwd == '1234':
        session['username'] = user
        return True
    else:
        return False
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    flash('You have been successfully logged out!')
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    debug = True
    app.run()


