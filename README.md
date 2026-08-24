# Ade's Estate Records

A simple command-line application for managing estate records, member registrations, and dues collection.

## Overview

This project is a Python-based estate management system that allows you to:
- Register new estate members
- Record dues payments
- View unpaid dues for members
- See which members are up-to-date with payments
- Check individual member payment history

Data is stored in a JSON file (`members.txt`) for persistence between sessions.

## Features

- **Member Registration**: Add new members with their first name, last name, and house number
- **Dues Collection**: Record payments for specific months
- **Payment Tracking**: View unpaid dues through a specified month
- **Status Reports**: See which members are fully paid up through a given month
- **Payment History**: Detailed view of a member's payment history
- **Demo Data**: Generate sample data for testing and demonstration

## Installation

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ade_book-keep
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. (Optional) Generate demo data:
   ```bash
   python -m populate_demo
   ```
   This creates sample member records in `members.txt`.

## Usage

Run the application:
```bash
uv run ade-book-keep
```

Or alternatively:
```bash
python main.py
```

### Menu Options

1. **Register member** - Add a new member to the system
2. **Collect dues** - Record a payment for a member
3. **View unpaid dues** - See which members have unpaid dues through a specified month
4. **View up-to-date members** - See members who are current on payments through a specified month
5. **View member payment history** - Detailed payment history for a specific member
6. **Exit** - Quit the application

### Example Workflow

1. Register a new member:
   ```
   Enter first name: John
   Enter last name: Doe
   Enter house number: 101
   ```

2. Collect dues for January:
   ```
   Enter last name: Doe
   Enter house number: 101
   Enter amount paid: 1000
   Enter month: January
   ```

3. View unpaid dues through March:
   ```
   View unpaid dues through which month? March
   ```

## Project Structure

```
ade_book-keep/
├── ade_book_keep/          # Main package
│   ├── __init__.py
│   ├── mtypes.py          # Type definitions
│   ├── register_members.py # Member registration and dues collection
│   ├── utils.py           # Utility functions (data persistence, helpers)
│   └── views.py           # Reporting functions
├── main.py                # Application entry point
├── populate_demo.py       # Demo data generator
├── members.txt            # JSON data file (created automatically)
├── pyproject.toml         # Project configuration
├── README.md              # This file
└── .gitignore
```

## Data Format

Member records are stored as JSON objects in `members.txt` with the following structure:

```json
{
  "member_id": "doehouse-101",
  "first_name": "john",
  "last_name": "doe",
  "house_num": "house-101",
  "date_of_reg": "2026-08-24",
  "payment_status": {
    "January": {
      "status": "Paid",
      "amount_paid": 1000,
      "date_of_payment": "2026-08-24"
    },
    "February": {
      "status": "Unpaid",
      "amount_paid": 0,
      "date_of_payment": null
    }
    // ... other months
  }
}
```

## Development

### Running Tests

Currently, the project doesn't have a formal test suite. You can manually test by:
1. Running the application
2. Using the demo data generator
3. Verifying the functionality through the CLI

### Code Style

The project follows standard Python conventions with type hints for better code clarity and maintainability.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built as part of a learning exercise in Python application development
- Uses Python's standard library for JSON handling and datetime operations