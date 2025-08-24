from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'srisivasakthischool-secret-key-2025'

# Email configuration - UPDATE THESE VALUES
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ranjithpython072@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'amusrjotxbzrunno'
app.config['MAIL_DEFAULT_SENDER'] = 'ranjithpython072@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')


@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route("/gallery")
def gallery():
    image_folder = os.path.join(app.static_folder, "images")
    images = [
        f for f in os.listdir(image_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    images.sort()  # Optional: sorts alphabetically
    return render_template("gallery.html", images=images)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_enquiry', methods=['POST'])
def submit_enquiry():
    try:
        print("=== FORM SUBMISSION DEBUG ===")
        
        # Get form data
        parent_name = request.form.get('parent_name')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        child_name = request.form.get('child_name')
        dob = request.form.get('dob')
        class_seeking = request.form.get('class_seeking')
        previous_school = request.form.get('previous_school')
        comments = request.form.get('comments')
        
        print(f"Parent: {parent_name}, Child: {child_name}, Mobile: {mobile}")
        
        # Validate required fields
        if not all([parent_name, mobile, email, child_name, dob, class_seeking]):
            flash('Please fill in all required fields marked with *', 'error')
            return redirect(url_for('admissions'))
        
        # Create email message for school admin
        admin_subject = f"🎓 New Admission Enquiry - {child_name} ({class_seeking})"
        admin_body = f"""
NEW ADMISSION ENQUIRY - SRI SIVASAKTHI SCHOOL


Submitted: {datetime.now().strftime('%d %B %Y at %I:%M %p')}

PARENT/GUARDIAN INFORMATION:
Name: {parent_name}
Mobile: {mobile}
Email: {email}

CHILD INFORMATION:
Name: {child_name}
Date of Birth: {dob}
Class Seeking: {class_seeking}
Previous School: {previous_school if previous_school else 'Not specified'}

COMMENTS/QUESTIONS:
{comments if comments else 'No additional comments provided'}


ACTION REQUIRED:
Please contact {parent_name} at {mobile} within 24 hours.

Reply to: {email}
Call: {mobile}

Sri Sivasakthi Nursery & Primary School
Admissions Department - Automated System
        """
        
        admin_msg = Message(
            subject=admin_subject,
            recipients=['srisivashakthi.primary@gmail.com'],  # Admin email
            body=admin_body
        )
        
        print("Attempting to send email...")
        
        # Send email to admin
        mail.send(admin_msg)
        
        print("✅ Email sent successfully!")
        
        # Show success message to parent
        flash(f'Thank you {parent_name}! Your admission enquiry for {child_name} has been received successfully. Our admissions team will contact you at {mobile} within 24 hours.', 'success')
        
    except Exception as e:
        print(f"❌ Email error: {str(e)}")
        flash('There was an error processing your enquiry. Please try again or call us directly at +91 98765 43210.', 'error')
    
    return redirect(url_for('admissions'))

if __name__ == '__main__':
    app.run(debug=True)




