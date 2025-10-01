import streamlit as st
import pandas as pd  # Just an example, could be used for dynamic data later

# --- Page Configuration ---
st.set_page_config(
    page_title="Tripixo - Your Journey Awaits",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    /* General Styling */
    .reportview-container .main {
        color: #333;
        background-color: #f8f9fa; /* Light background */
    }
    .sidebar .sidebar-content {
        background-color: #ffffff; /* White sidebar */
        color: #333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #007bff; /* Primary blue for headings */
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }

    /* Hero Section Specific */
    .hero-section {
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1490604018820-202d603a15dc?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjVsbDF8MHwxfGFsbHwxfHx0cmF2ZWwsYWR2ZW50dXJlLGV4cGxvcmF8fHx8fHx8fDE2NzEyMzA0NjE&ixlib=rb-4.0.3&q=80&w=1080'); /* Using an online image for broader access */
        background-size: cover;
        background-position: center;
        padding: 100px 0;
        text-align: center;
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .hero-section h1 {
        font-size: 3.5em;
        margin-bottom: 10px;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    }
    .hero-section p {
        font-size: 1.5em;
        margin-bottom: 30px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
    }

    /* Card Styling for Destinations/Packages */
    .st-emotion-cache-1r6dmym, .st-emotion-cache-f1gtdg { /* These are Streamlit's div classes for columns */
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        background-color: white;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .st-emotion-cache-1r6dmym:hover, .st-emotion-cache-f1gtdg:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    .stImage > img {
        border-radius: 5px;
        max-height: 200px;
        object-fit: cover;
    }
    .stText {
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

# --- Header & Navigation ---
st.sidebar.image("Tripixo_.png", width=150)  # Assuming you have a logo
st.sidebar.title("Tripixo Navigation")
page = st.sidebar.radio("Go to", ["Home", "Destinations", "Packages", "About Us", "Contact Us"])

# --- Home Page ---
if page == "Home":
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown("<h1>Tripixo - Your Journey Awaits</h1>", unsafe_allow_html=True)
    st.markdown("<p>Discover breathtaking destinations and unforgettable adventures.</p>", unsafe_allow_html=True)
    st.button(
        "Explore Destinations")  # This button won't navigate directly in Streamlit, but you could set it to change the 'page' variable with some JS or state management.
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    st.subheader("Featured Trip Ideas")
    col1, col2 = st.columns(2)
    with col1:
        st.image("Paris.png", caption="Romantic Paris Getaway")
        st.markdown(
            "**Paris:** Explore the city of love, from the Eiffel Tower to charming cafes. Perfect for couples.")
    with col2:
        st.image("Kyoto.jpg", caption="Cultural Kyoto Exploration")
        st.markdown("**Kyoto:** Immerse yourself in ancient temples, serene gardens, and traditional Japanese culture.")

    st.write("---")
    st.subheader("Why Choose Tripixo?")
    st.markdown("""
    *   **Expertly Curated Trips:** Hand-picked destinations and itineraries for unique experiences.
    *   **Personalized Service:** We tailor trips to your dreams and budget.
    *   **24/7 Support:** Travel with peace of mind knowing we're always here for you.
    *   **Sustainable Travel:** Committed to responsible tourism that benefits local communities.
    """)

# --- Destinations Page ---
elif page == "Destinations":
    st.title("Our Top Destinations")
    st.write("Explore the world with Tripixo! Here are some of our most popular travel spots.")

    # Using columns for a grid layout
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("Paris.png", caption="Paris, France")
        st.subheader("Paris, France")
        st.write(
            "The iconic 'City of Love' offers breathtaking architecture, world-class cuisine, and unforgettable romantic experiences. Visit the Eiffel Tower, Louvre Museum, and stroll along the Seine.")

    with col2:
        st.image("Kyoto.jpg", caption="Kyoto, Japan")
        st.subheader("Kyoto, Japan")
        st.write(
            "Step back in time in Japan's cultural capital. Discover ancient temples, serene gardens, traditional geisha districts, and exquisite culinary delights.")

    with col3:
        st.image("Serengeti.jpg", caption="Serengeti, Tanzania")
        st.subheader("Serengeti, Tanzania")
        st.write(
            "Embark on an incredible wildlife safari adventure. Witness the Great Migration, spot the 'Big Five', and experience the raw beauty of the African savanna.")

    st.write("---")
    st.subheader("More Destinations Coming Soon!")
    st.info("We are constantly expanding our portfolio to bring you more incredible places. Stay tuned!")

# --- Packages Page ---
elif page == "Packages":
    st.title("Our Travel Packages")
    st.write("Find the perfect trip for your next adventure with our specially designed packages.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Romantic European Escape")
        st.image("Paris.png", caption="Paris & Rome")
        st.markdown("""
        *   **Duration:** 7 Days / 6 Nights
        *   **Destinations:** Paris, Rome
        *   **Includes:** Flights, 4-star accommodation, city tours, romantic dinner.
        *   **Price:** Starting from $2500 per person
        """)
        if st.button("Book European Escape", key="europe_book"):
            st.success("You've expressed interest in the European Escape! We'll contact you shortly.")

    with col2:
        st.subheader("Southeast Asian Cultural Tour")
        st.image("Bangkok.jpg", caption="Bangkok & Hanoi")  # Placeholder, imagine a relevant image
        st.markdown("""
        *   **Duration:** 10 Days / 9 Nights
        *   **Destinations:** Bangkok, Hanoi, Ha Long Bay
        *   **Includes:** Flights, boutique hotels, cooking classes, guided temple visits.
        *   **Price:** Starting from $2000 per person
        """)
        if st.button("Book Asian Tour", key="asia_book"):
            st.success("You've expressed interest in the Asian Cultural Tour! We'll contact you shortly.")

    st.write("---")
    st.subheader("Custom Packages Available!")
    st.write("Don't see exactly what you're looking for? Contact us to create a tailor-made itinerary just for you.")

# --- About Us Page ---
elif page == "About Us":
    st.title("About Tripixo")
    st.write("---")
    st.image("Tripixo_.png", width=200)  # Re-use logo if desired or use a team photo
    st.subheader("Our Story")
    st.write("""
    Tripixo was founded with a simple yet profound vision: to make the wonders of the world accessible to everyone. We believe that travel is not just about visiting new places, but about creating lasting memories, broadening horizons, and experiencing diverse cultures.
    """)
    st.write("""
    Our team of passionate travel experts has decades of combined experience in designing unforgettable journeys. From thrilling adventures to serene retreats, we meticulously plan every detail so you can focus on enjoying your trip.
    """)
    st.subheader("Our Mission")
    st.markdown("""
    *   To inspire and enable unique travel experiences.
    *   To provide unparalleled service and support.
    *   To promote sustainable and responsible tourism.
    """)

# --- Contact Us Page ---
elif page == "Contact Us":
    st.title("Contact Tripixo")
    st.write("Have questions or ready to plan your next adventure? We'd love to hear from you!")

    st.subheader("Send Us a Message")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message", height=150)

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit Inquiry")
        if submitted:
            if name and email and message:
                st.success(
                    f"Thank you, {name}! Your message has been sent. We will get back to you at {email} shortly.")
                # Here you would typically send this data to an email service, database, or API.
                # For this example, it's just a confirmation.
                st.write(f"**Collected Data:**")
                st.write(f"Name: {name}")
                st.write(f"Email: {email}")
                st.write(f"Message: {message}")
            else:
                st.error("Please fill in all fields.")

    st.write("---")
    st.subheader("Other Ways to Reach Us")
    st.markdown("""
    **Email:** BlackWarrior5521@gmail.com

    **Phone:** 9371065521

    **Address:** Pune 

    **Follow Us:**  
    [Instagram](https://www.instagram.com/tripixo_/) | 
    [Youtube](https://www.youtube.com/@Tripixoo)
    """)

# --- Footer (Optional) ---
st.markdown("---")
st.markdown("<footer>© 2023 Tripixo. All rights reserved.</footer>", unsafe_allow_html=True)
