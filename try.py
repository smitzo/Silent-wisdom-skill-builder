from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def calculate_progress(skill_data):
    # Dictionary to store total score for each skill category
    category_scores = {}
    
    # Calculate total score for each skill category
    for entry in skill_data:
        email, timestamp, score, category = entry
        if category not in category_scores:
            category_scores[category] = []
        category_scores[category].append(score)
    
    # Calculate progress percentage for each skill category
    progress = {}
    for category, scores in category_scores.items():
        if scores:  # Ensure there are scores for the category
            percentage = ((sum(scores) / len(scores)) / 170) * 100
            progress[category] = percentage
    
    return progress

def create_pdf_with_text(name, age, contact, city, email, category, skill_data):
    skill_dictionary= {"arithmatic_modules":"Critical Thinking","balloon game":"Hand Eye Coordination","memorizing numbers":"Memorizing Ability","digits_sign_learning":"Language Learning Skills","reflex game":"Reflexive Capabilities","keyboard typing speed":"Keyboard Typing","physical fitness": "Physical Fitness"}
    # Convert numeric values to strings
    age = str(age)
    contact = str(contact)
    
    # Calculate progress for each skill category
    progress = calculate_progress(skill_data)
    
    # Create a PDF canvas
    c = canvas.Canvas(f"{name}_resume.pdf", pagesize=letter)
    
    # Set font and font size
    c.setFont("Helvetica-Bold", 24)  # Big and bold font for title
    
    # Draw the title
   # c.drawString(250, 750, "RESUME")  # Adjusted position
    c.setFillColorRGB(0, 0, 137)  # Blue font color
    c.drawString(250, 750, "RESUME")
    c.setFillColorRGB(0, 0, 0)  # Set font color to black

        
    # Add personal information
    c.setFont("Helvetica", 14)
    y = 700  # Adjusted starting y position
    info = [
        ("Name", name),
        ("Age", age),
        ("Contact", contact),
        ("City", city),
        ("Email", email),
        ("Category", category)
    ]
    column_width = 100  # Width of the column
    for label, value in info:
        c.setFillColorRGB(0, 0, 0)  # Set font color to black
        c.drawString(100, y, f"{label}:")
        c.drawString(170, y, f"{value}")
        y -= 20  # Move to the next line
        # Add horizontal line below each line
        c.line(100, y, 500, y)
        y -= 15 # Reduce spacing between rows
    
    y -= 40  # Add some space between personal information and skills
    
    # Add skills title
    c.setFont("Helvetica-Bold", 16)  # Big and bold font for skills title
    c.drawString(100, y, "Skills Progress")
    c.setFillColorRGB(0, 0, 0)  # Reset
    y -= 40  # Move to the next line
    
    # Add skills with progress percentage
    for skill, percentage in progress.items():
        # print(skill)
        if percentage >= 30:  # Only include skills with progress >= 30%
            skill_text = f"{skill_dictionary[skill]}: {round(percentage, 2)}%"
            c.setFont("Helvetica", 14)  # Bold font for skills
            c.drawString(100, y, skill_text)
            y -= 20  # Reduce spacing between skills and subskills
            # Add horizontal line below each skill
            c.line(100, y, 500, y)
            y -= 20  # Reduce spacing between rows
    
    # Save the PDF
    c.save()

# Sample usage:
skill_data = [('joshismit2812@gmail.com', '2024-03-04 17:14:23.372287', 100, 'arithmatic_modules'), ('joshismit2812@gmail.com', '2024-03-04 17:40:04.745449', 100, 'arithmatic_modules'), ('joshismit2812@gmail.com', '2024-03-04 17:43:00.663234', 120, 'arithmatic_modules'), ('joshismit2812@gmail.com', '2024-03-04 18:17:31.202913', 70, 'balloon game'), ('joshismit2812@gmail.com', '2024-03-04 18:18:50.514402', 90, 'balloon game'), ('joshismit2812@gmail.com', '2024-03-04 18:19:49.018759', 110, 'digits_sign_learning'), ('joshismit2812@gmail.com', '2024-03-04 18:21:31.379014', 140, 'digits_sign_learning'), ('joshismit2812@gmail.com', '2024-03-04 18:22:39.897382', 5, 'physical fitness'), ('joshismit2812@gmail.com', '2024-03-04 18:23:41.625396', 14, 'physical fitness'), ('joshismit2812@gmail.com', '2024-03-04 18:24:39.454123', 150, 'reflex game'), ('joshismit2812@gmail.com', '2024-03-04 18:25:31.095167', 150, 'reflex game'), ('joshismit2812@gmail.com', '2024-03-04 18:26:28.183642', 30, 'memorizing numbers'), ('joshismit2812@gmail.com', '2024-03-04 18:27:23.694573', 40, 'memorizing numbers'), ('joshismit2812@gmail.com', '2024-03-04 18:43:27.804365', 0, 'keyboard typing speed'), ('joshismit2812@gmail.com', '2024-03-04 20:48:31.773342', 80, 'arithmatic_modules'), ('joshismit2812@gmail.com', '2024-03-04 20:51:13.626673', 80, 'arithmatic_modules')]
create_pdf_with_text("John Doe", 25, "123-456-7890", "New York", "john@example.com", "Special Abilities Student", skill_data)

