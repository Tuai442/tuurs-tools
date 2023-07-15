

import re

def wrap_keywords_with_span(html_code, keywords, config):
    wrapped_code = html_code

    for keyword in keywords:
        pattern = rf'\b{keyword}\b'
        wrapped_code = re.sub(pattern, f'<span class="{config[keyword]}">{keyword}</span>', wrapped_code)

    return wrapped_code



html_code = '''
    function initContactForm() {
        const form = document.createElement('form');
        form.id = 'contact-form';
        form.addEventListener('submit', handleContactFormSubmit);
        document.body.appendChild(form);
    }
'''

keywords = ['function', 'const', 'document']
config = {
    'function': 'keyword-function',
    'const': 'keyword-const',
    'document': 'keyword-document'
}

wrapped_code = wrap_keywords_with_span(html_code, keywords, config)
print(wrapped_code)
