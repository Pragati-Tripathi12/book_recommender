from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# 1. LOAD ARTIFACTS
# Ensure these files are in the 'Notebook/artifacts/' folder
popular_df = pickle.load(open('Notebook/artifacts/final_ratings.pkl', 'rb'))
book_pivot = pickle.load(open('Notebook/artifacts/book_pivot.pkl', 'rb'))
model = pickle.load(open('Notebook/artifacts/model.pkl', 'rb'))

# 2. DATA CLEANING FOR "LEGITIMATE" RATINGS
# We calculate the real average by ignoring the '0' (implicit) ratings
# This prevents popular books from showing '0' stars in the UI
explicit_ratings = popular_df[popular_df['rating'] != 0]
avg_rating_df = explicit_ratings.groupby('title')['rating'].mean().reset_index()
avg_rating_df.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Merge the true averages back into our display dataframe
popular_df = popular_df.merge(avg_rating_df, on='title', how='left')
popular_df['avg_rating'] = popular_df['avg_rating'].fillna(0) # Handle books with ONLY 0s

@app.route('/')
def index():
    # Show Top 50 books by vote count (popularity)
    display_df = popular_df.drop_duplicates('title').sort_values('num_of_ratings', ascending=False).head(50)
    
    return render_template('index.html',
                           book_name=list(display_df['title'].values),
                           author=list(display_df['author'].values),
                           image=list(display_df['image'].values),
                           votes=list(display_df['num_of_ratings'].values),
                           # Round to 1 decimal place for a professional look (e.g., 8.5)
                           rating=[round(x, 1) for x in list(display_df['avg_rating'].values)]
                           )

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input').strip()
    
    # SEARCH HELPER: Find the best match if the user didn't type the full name
    if user_input not in book_pivot.index:
        matches = [title for title in book_pivot.index if user_input.lower() in title.lower()]
        if matches:
            user_input = matches[0]
        else:
            return render_template('index.html', error="Book not found. Please try another!")

    # RECOMMENDATION LOGIC
    index = np.where(book_pivot.index == user_input)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[index, :].values.reshape(1, -1), n_neighbors=6)
    
    data = []
    for i in suggestions[0]:
        item = []
        temp_df = popular_df[popular_df['title'] == book_pivot.index[i]].drop_duplicates('title')
        
        item.extend(list(temp_df['title'].values))
        item.extend(list(temp_df['author'].values))
        item.extend(list(temp_df['image'].values))
        # Include avg_rating for the recommendation page as well
        item.append(round(temp_df['avg_rating'].values[0], 1))
        
        data.append(item)
    
    return render_template('recommend.html', data=data)

# AUTO-COMPLETE API: For the advanced frontend search bar
@app.route('/search_suggestions')
def search_suggestions():
    q = request.args.get('q', '').lower()
    if len(q) < 2: return jsonify([])
    suggestions = [title for title in book_pivot.index if q in title.lower()][:5]
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)