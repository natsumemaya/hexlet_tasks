def normalize_url(url):
    begin_url = url[:8]
    normal = 'https://'
    if begin_url != normal:
        if url[:7] == 'http://':
            return normal + url[7:]
        else:
            return normal + url
    return url


print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('google.com'))     # => 'https://google.com'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'