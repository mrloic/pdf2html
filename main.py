from PyPDF2 import PdfReader

pdf_path = '888901.pdf'
reader = PdfReader(pdf_path)

text_content = ''
for page in reader.pages:
    text_content += page.extract_text()

html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Политика конфиденциальности</title>
</head>
<body>
    <h1>Политика конфиденциальности и обработки персональных данных</h1>
    <pre>{text_content}</pre>
</body>
</html>
"""

html_path = 'privacy_policy_'+pdf_path[:-4]+'.html'
with open(html_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

