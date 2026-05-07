import pdfplumber

async def extract_text(file):
    contents = await file.read()

    temp_file = "temp_resume.pdf"

    with open(temp_file, "wb") as f:
        f.write(contents)

    text = ""

    with pdfplumber.open(temp_file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

    return text