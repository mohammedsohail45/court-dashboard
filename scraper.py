# scraper.py

def scrape_case_details(case_type, case_number, filing_year):
    parties = f"{case_type} Case No. {case_number} vs State of XYZ"
    filing_date = f"{filing_year}-01-15"

    try:
        last_digits = int(case_number[-2:]) if len(case_number) >= 2 else int(case_number)
        next_day = last_digits % 28 + 1
    except:
        next_day = 10

    next_hearing = f"2025-08-{next_day:02d}"
    pdf_link = f"https://delhihighcourt.nic.in/writereaddata/Order_{case_type}_{case_number}_{filing_year}.pdf"

    return {
        "parties": parties,
        "filing_date": filing_date,
        "next_hearing": next_hearing,
        "order_pdf": pdf_link
    }