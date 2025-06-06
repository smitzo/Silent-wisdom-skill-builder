import datetime
import sqlite3
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
def user_dashboard(category= None):
    with open('current.txt', 'r') as file:
        email = file.read()
        
    print(email)
    # Connect to the SQLite database
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()
    if not category:
        # Query to fetch score and attempts for each category of the user
        cursor.execute("""
            SELECT * FROM gameplay
            WHERE email = ?
        """, (email,))

        # Fetch all rows from the result set
        data = cursor.fetchall()

        # Print the score and attempts for each category
        print("Score and Attempts for User ID", email)
        for row in data:
            print(row)
        
      # Extract category data
        categories = list(set([row[3] for row in data]))

        # Initialize dictionaries to store scores and attempts for each category
        category_scores = {category: [] for category in categories}
        category_attempts = {category: [] for category in categories}

        # Extract scores and attempts for each category
        for row in data:
            category_scores[row[3]].append(row[2])
            category_attempts[row[3]].append(row[1])  # Assuming datetime is in the second column

        # Create plotly figure for individual scores
        fig_scores = go.Figure()

        # Add traces for each category with different colors
        color_palette = px.colors.qualitative.Plotly
        for i, category in enumerate(categories):
            fig_scores.add_trace(go.Box(y=category_scores[category], name=category, marker_color=color_palette[i]))

        # Update layout for individual scores plot
        fig_scores.update_layout(title='Scores Distribution for Each Game',
                                yaxis_title='Score',
                                showlegend=True)

        # Show individual scores plot
        # fig_scores.show()
        pio.show(fig_scores)

        # Create plotly figure for line plot
        fig_line_plot = go.Figure()

        # Add traces for each category with different colors
        for i, category in enumerate(categories):
            fig_line_plot.add_trace(go.Scatter(x=category_attempts[category], y=category_scores[category], mode='lines+markers', name=category, marker_color=color_palette[i]))

        # Update layout for line plot
        fig_line_plot.update_layout(title='Score Progress Over Time',
                                    xaxis_title='Datetime',
                                    yaxis_title='Score',
                                    showlegend=True)

        # Show line plot
        # fig_line_plot.show()
        pio.show(fig_line_plot)
        # Calculate overall performance for each category
        overall_performance = {category: ((sum(scores) / (len(scores)))/ 170) *100 for category, scores in category_scores.items()}

        # Create plotly figure for overall performance
        fig_performance = go.Figure()
        fig_performance.add_trace(go.Bar(x=list(overall_performance.keys()), y=list(overall_performance.values()), name='Overall Performance', marker_color=color_palette))

        # Update layout for overall performance plot
        fig_performance.update_layout(title='Overall Performance for Each Game',
                                    xaxis_title='Game',
                                    yaxis_title='Overall Performance (%)',
                                    showlegend=True)

        # Show overall performance plot
        # fig_performance.show()
        pio.show(fig_performance)
    else:
        cursor.execute("""
            SELECT * FROM gameplay
            WHERE email = ? and category = ?
        """, (email,category))

        # Fetch all rows from the result set
        data= cursor.fetchall()

        # Print the score and attempts for each category
        print("Score and Attempts for User ID", email)
        for row in data:
            print(row)

       # Extract datetime, score, and category data
        datetime_data = [row[1] for row in data]
        scores = [row[2] for row in data]
        category = data[0][3]

        # Convert scores to percentage
        scores_percentage = [(score / 170) * 100 for score in scores]

        # Create plotly figure
        fig = go.Figure()

        # Add trace for score over time
        fig.add_trace(go.Scatter(x=datetime_data, y=scores_percentage, mode='lines+markers', name='Progress'))

        # Update layout
        fig.update_layout(title=f'Learning Progress for {category}',
                        xaxis_title='Datetime',
                        yaxis_title='Progress (%)',
                        showlegend=True,
                        font=dict(family="Arial, sans-serif", size=12, color="black"))

        # Calculate overall progress
        overall_progress = ((sum(scores) / (len(scores)))/ 170) *100

        # Add overall progress annotation
        fig.add_annotation(text=f'Overall Progress: {overall_progress:.2f}%', xref='paper', yref='paper', x=1, y=1, showarrow=False,
                        font=dict(family="Arial, sans-serif", size=14, color="black"), align="right")

        # Show plot
        # fig.show()
        pio.show(fig)

    conn.commit()
    conn.close()

# user_dashboard("arithmatic_modules")