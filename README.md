# my_py_site

The world's smallest and lightweight static site and blog generator for Python lovers.

# HIGHLIGHTS
  * YML Front matter is supported
  * Jinja 2 Templates
  * Almost similary to Jekyll
  * Deploy on Ntlify (Just fork and add it to netlify)
  * Compatible with Ntlify CMS
  * Made in India :smile:

[my_py_site](https://github.com/sharadcodes/my_py_site) is the most 
simplest and lightweight static site generator out there, with less than
90 lines of code.

**[my_py_site](https://github.com/sharadcodes/my_py_site) was made in 
just two hours** but the development will go further and enhancements
will be done in the future to make things more easy.

With approx 90 lines of code it becomes the smallest Static Site 
Generator which is capable of generating multiple pages, blogs.

The documentation is going on, although you won't need because it's
that simple.
After cloning or downloading the [repo](https://github.com/sharadcodes/my_py_site) just run
```
pip install -r requirements.txt
python my_py_site.py
```
and the site will be generated.


>Developer: [Sharad Raj](https://sharadcodes.github.io)

---

## [Live Demo](https://mypysite.netlify.com/)

---

# USAGE

**my_py_site** supports multiple blogs and pages, you dont have to do modify the `my_py_site.py` file.

## Configuration file

The contents of this file can be accessed from templates which are inside `templates` directory. You will have to use the **Jinja2** syntax for accessing the data of `config.json` file.

### Example

```json
{
  "site": {
    "title": "My Awesome Site",
    "author": "Sharad Raj"
  },
  "social": [
    {
      "site": "twitter",
      "id": "iamsharadraj"
    },
    {
      "site": "github",
      "id": "sharadcodes"
    }    
  ]
}
```

In the above config you for accessing the value of `title` inside `site` you will do
```python
{{data.site.title}}
```
in the templates. **data** is global and it is needed for accessing the values of `config.json` file

Similarly for looping over an array of objects like `social` you will do
```python
{% for i in data.social %}
  {{ i.site }}
  {{ i.id }}
{% endfor %}
```
[Actual code example](https://github.com/sharadcodes/my_py_site/blob/master/templates/post.html)

**Anything inside `config.json` can be accessed from any of the templates**

## List of collections

All the meta info about files inside the collections folder can be accessed from any page which is inside `pages` folder.
The meta information about files is inside `data.collections` object which is an array of objects. The YML front matter of the page is also available.

### Example

To access list of articles inside `posts` folder you will do
```python
{% for i in data.site.collections %}
  {{i.url}}
  {{i.title}}
  {{i.author}}
  {{i.date or i.datetime}}
{%endfor%}
```

[Actual code example](https://github.com/sharadcodes/my_py_site/blob/master/templates/blog.html)

---

## For any help https://www.codingindian.codes/contact
