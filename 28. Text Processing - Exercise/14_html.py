article_title = input()
contents = input()

article_title_html = f'<h1>\n\t{article_title}\n</h1>'
contents_html = f'<article>\n\t{contents}\n</article>'

comments = []
while True:
    comment = input()

    if comment == 'end of comments':
        break
    else:
        comments.append(f'<div>\n\t{comment}\n</div>')
        

print(article_title_html)
print(contents_html)
for comment in comments:
    print(comment)