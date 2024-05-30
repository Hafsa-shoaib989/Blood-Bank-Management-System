# Blood Bank Management System

This project is a comprehensive web application developed using Python with the Django Web Framework. It primarily focuses on managing blood donations, requests, patients, and donors. The system is divided into three panels: Patient, Donor, and Admin, each with specific functionalities. One of the key features is the automation system that enables users to quickly check the availability of blood and facilitates donors in donating blood promptly.

## Features

- **User Registration and Interaction:** Allow users to register as patients or donors with detailed information and facilitate blood requests and donations.
- **Donation Management:** Enable donors to submit blood donation requests, with approval required from the admin, and maintain a donation history.
- **Automated Blood Availability Check:** Implement an automated system for users to quickly check the availability of blood when needed.
- **Admin Control:** Provide an administrative panel with the ability to manage donors, patients, blood requests, donations, and blood stocks.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Hafsa-shoaib989/Blood-Bank-Management-System.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

