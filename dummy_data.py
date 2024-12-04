from app import db, create_app
from app.models import Blog

db.metadata.clear()

# Create the Flask app and set up the application context
app = create_app()
with app.app_context():
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
            "imageLink": "images/business-blog-1.jpg"
        },
        {
            "title": "The Impact of Globalization on Businesses",
            "content": "Globalization has transformed how businesses operate worldwide...",
            "category": "Business",
            "author": "Sophia White",
            "imageLink": "images/business-blog-2.jpg"
        },
        {
            "title": "The Importance of Financial Planning",
            "content": "Sound financial planning is critical for business growth...",
            "category": "Business",
            "author": "David Lee",
            "imageLink": "images/business-blog-3.jpg"
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
    print("Dummy blog data inserted successfully!")
