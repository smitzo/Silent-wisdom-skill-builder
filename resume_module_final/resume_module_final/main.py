from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Ellipse
from reportlab.graphics import renderPDF
import sqlite3
import os
from io import BytesIO
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# global variables
# Example usage
output_pdf_path = 'Final_Resume.pdf'

name = ''
age = ''
skills = ''
city = ''
contact = ''
email = ''




# path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = "./resume_module_final/resume_module_final/assets/frame0"

def initialize_global_list():
    global global_list
    global_list = []



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_user_input(en1,en2,en3,en4,en5,en6):
    initialize_global_list()
    global_list.append(en1)
    name = global_list[0]
    global_list.append(en2)
    age = global_list[1]
    global_list.append(en3.split(','))
    skills = global_list[2]
    global_list.append(en4)
    contact = global_list[3]
    global_list.append(en5)
    city = global_list[4]
    global_list.append(en6)
    email = global_list[5]
    
    # print(global_list)





def send_mail(sender,reciever,password,name,pdf_file_path):
    HOST = "smtp-mail.outlook.com"
    PORT = 587
    FROM_EMAIL = sender
    TO_EMAIL = reciever
    PASSWORD = password
    # FROM_EMAIL = "joshismit2812@outlook.com"
    # TO_EMAIL = "ursindhuk@gmail.com"
    # PASSWORD = "Smit@2812"

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = FROM_EMAIL
    message["To"] = TO_EMAIL
    message["Subject"] = "Subject: hello "+ name

    # Add the body of the email
    body = " hello sir ,\n\nThis email is sent from our application .\n\nThanks, sincerely"
    message.attach(MIMEText(body, "plain"))

    # Attach the PDF file
    # pdf_file_path = output_pdf_path
    with open(pdf_file_path, "rb") as attachment:
        pdf_part = MIMEBase("application", "octet-stream")
        pdf_part.set_payload(attachment.read())
        encoders.encode_base64(pdf_part)
        pdf_part.add_header("Content-Disposition", f"attachment; filename=your_file.pdf")
        message.attach(pdf_part)

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
    smtp.quit()


# def create_pdf_with_text( name, age, contact, city, email, category):
#     # Create a new PDF canvas
#     pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=letter)

#     # Set font and size
#     pdf_canvas.setFont("Helvetica", 12)

#     # Add a rectangle at the top of the page (30% of full width)
#     rect_width = letter[0] * 0.3
#     rect_height = letter[1]
#     pdf_canvas.setFillColor(colors.midnightblue)
#     pdf_canvas.setStrokeColor(colors.midnightblue)
#     pdf_canvas.rect(0, 0, rect_width, rect_height, fill=True, stroke=False)

#     # Calculate the position to center the heading "Resume"
#     heading_text = "Resume"
#     heading_width = pdf_canvas.stringWidth(heading_text, "Helvetica-Bold", 60)
#     heading_x = (letter[0] - heading_width) / 2
#     heading_y = rect_height - 30  # Adjust as needed

#     pdf_canvas.setFont("Helvetica-Bold", 30)
#     # Add "Resume" heading at the top
#     pdf_canvas.setFillColor(colors.blue)  # Set text color to white
#     pdf_canvas.drawString(rect_width + 140, heading_y, "RESUME")

#     # Reset text color to black
#     pdf_canvas.setFillColor(colors.black)

#     # Set font and size for the main content
#     pdf_canvas.setFont("Helvetica", 16)

#     # Add text to the canvas with line gaps
#     line_gap = 15
#     content_y = heading_y - 40

#     pdf_canvas.drawString(rect_width + 60, content_y, "Name: {}".format(name))
#     pdf_canvas.drawString(rect_width + 60, content_y - 4 * line_gap, "Age: {}".format(age))
#     pdf_canvas.drawString(rect_width + 60, content_y - 8 * line_gap, "Category: {}".format(", ".join(category)))
#     pdf_canvas.drawString(rect_width + 60, content_y - 12 * line_gap, "City: {}".format(city))
#     pdf_canvas.drawString(rect_width + 60, content_y - 16 * line_gap, "Contact: {}".format(contact))
#     pdf_canvas.drawString(rect_width + 60, content_y - 20 * line_gap, "Email: {}".format(email))

#     # Save the PDF to the specified file path
#     pdf_canvas.save()

#     # send_mail("jamessmit28@outlook.com",email,"Smit@123",name,output_pdf_path)

def calculate_progress(skill_data):
    # Dictionary to store total score for each skill category
    category_scores = {}
    
    # Calculate total score for each skill category
    for entry in skill_data:
        print("entry.....",entry)
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
    c = canvas.Canvas(f"Final_Resume.pdf", pagesize=letter)
    
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
    send_mail("jamessmit28@outlook.com",email,"Smit@123",name,os.getcwd()+"/Final_Resume.pdf")

def get_users_data(email):
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, contact, city, email,category FROM users where email= ?",(email,))
    rows = cursor.fetchone()
    conn.close()
    return rows

def get_gameplay_data(email):
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gameplay where email= ?",(email,))
    rows = cursor.fetchall()
    conn.close()
    return rows

with open('current.txt', 'r') as file:
    email = file.read()

# print(email)
user_data = get_users_data(email)
# print(user_data)
# print(get_gameplay_data(email))
create_pdf_with_text(user_data[0],user_data[1],user_data[2],user_data[3],user_data[4],user_data[5],get_gameplay_data(email))