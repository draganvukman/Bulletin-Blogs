from flask import Blueprint, render_template
from app.models import Blog

page_routes = Blueprint('page_routes', __name__)

@page_routes.route('/')
def home():
    # Fetch blogs for each category
    business_blogs = Blog.query.filter_by(category='Business').all()
    health_blogs = Blog.query.filter_by(category='Health').all()
    technology_blogs = Blog.query.filter_by(category='Technology').all()

    return render_template('index.html', 
                           business_blogs=business_blogs,
                           health_blogs=health_blogs,
                           technology_blogs=technology_blogs)

@page_routes.route('/business')
def business():
    # Fetch blogs for business category
    business_blogs = Blog.query.filter_by(category='Business').all()
    return render_template('business.html', business_blogs=business_blogs)

@page_routes.route('/technology')
def technology():
    # Fetch blogs for technology category
    technology_blogs = Blog.query.filter_by(category='Technology').all()
    return render_template('technology.html', technology_blogs=technology_blogs)

@page_routes.route('/health')
def health():
    # Fetch blogs for health category
    health_blogs = Blog.query.filter_by(category='Health').all()
    return render_template('health.html', health_blogs=health_blogs)

@page_routes.route('/authors')
def authors():
    return render_template('authors.html')

@page_routes.route('/contact')
def contact():
    return render_template('contact-us.html')

@page_routes.route('/insert-dummy-data', methods=['GET'])
def insert_dummy_data():
    # Dummy data for blogs
    dummy_blogs = [
        # Technology Blogs
        {
            "title": "The Rise of Artificial Intelligence",
            "content": "Artificial intelligence (AI) is transforming industries worldwide...",
            "category": "Technology",
            "author": "John Doe",
            "imageLink": "images/tech-blog-1.jpeg"
        },
        {
            "title": "The Future of Quantum Computing",
            "content": "Quantum computing is set to revolutionize problem-solving...",
            "category": "Technology",
            "author": "Jane Smith",
            "imageLink": "images/tech-blog-2.jpeg"
        },
        {
            "title": "Cybersecurity in the Modern Era",
            "content": "With increasing cyber threats, cybersecurity is more important than ever...",
            "category": "Technology",
            "author": "Alex Johnson",
            "imageLink": "images/tech-blog-3.jpeg"
        },

        # Health Blogs
        {
            "title": "The Benefits of a Balanced Diet",
            "content": "A balanced diet is crucial for maintaining optimal health...",
            "category": "Health",
            "author": "Emily Davis",
            "imageLink": "images/health-blog-1.webp"
        },
        {
            "title": "Mental Health Awareness",
            "content": "Understanding and supporting mental health is key to a healthy society...",
            "category": "Health",
            "author": "Michael Brown",
            "imageLink": "images/health-blog-2.webp"
        },
        {
            "title": "The Science of Sleep",
            "content": "Quality sleep is fundamental for physical and mental health...",
            "category": "Health",
            "author": "Sarah Wilson",
            "imageLink": "images/health-blog-3.webp"
        },

        # Business Blogs
        {
            "title": "Strategies for Effective Leadership",
            "content": "Strong leadership is the cornerstone of a successful organization...",
            "category": "Business",
            "author": "Chris Martin",
            "imageLink": "images/business-blog-1.avif"
        },
        {
            "title": "The Impact of Globalization on Businesses",
            "content": "Globalization has transformed how businesses operate worldwide...",
            "category": "Business",
            "author": "Sophia White",
            "imageLink": "images/business-blog-2.avif"
        },
        {
            "title": "The Importance of Financial Planning",
            "content": "Sound financial planning is critical for business growth...",
            "category": "Business",
            "author": "David Lee",
            "imageLink": "images/business-blog-3.avif"
        },
    ]

    # Insert dummy data into the database
    for blog_data in dummy_blogs:
        blog = Blog(
            title=blog_data["title"],
            content=blog_data["content"],
            category=blog_data["category"],
            author=blog_data["author"],
            imageLink=blog_data["imageLink"]
        )
        db.session.add(blog)

    # Commit changes to the database
    db.session.commit()

    return jsonify({"message": "Dummy data inserted successfully!"})
