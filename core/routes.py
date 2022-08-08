from datetime import datetime
from core.models import ShortUrls
from core import app, db
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for


def generate_short_id(num_of_chars: int):
    """
    Generates a random shortened URL ID of specified number of characters
    Args:
        num_of_chars: Length of shortened URL ID
    Returns:
        Shortened URL ID
    """
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles HTTP method logic for index page.
    Returns:
        Rendered index page
    """
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        # Duplicate shortened ID
        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('Oh no! Please enter different custom id.')
            return redirect(url_for('index'))

        # Empty URL field
        if not url:
            flash('Oh on! The URL is required.')
            return redirect(url_for('index'))

        # Empty custom field; create shortened ID
        if not short_id:
            short_id = generate_short_id(8)

        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.now())
        
        # Push entry to databasese
        db.session.add(new_link)
        db.session.commit()
        
        short_url = request.host_url + short_id
        
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_id>')
def redirect_url(short_id):
    """
    Handles HTTP method logic for specified URL page.
    Args:
        short_id: Shortened URL ID to redirect to
    Returns:
        Rendered target or index page
    """
    # Get database entry of shortened id
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    
    if link:
        return redirect(link.original_url)
    else:
        flash('Oh on! Invalid URL.')
        return redirect(url_for('index'))
