# The MIT License (MIT)
#
# Copyright (c) 2019 Sharad Raj Singh Maurya
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import shutil
import glob
import json
import frontmatter
import commonmark

from jinja2 import Template

collections_metainfo_array = []

with open('config.json') as json_file:
    config_json_data = json.load(json_file)


#  for creating a file
def createFile(path, name, file_content):
    f = open(path + name, "a")
    f.write(file_content)
    f.close()

# for rendering the templates


def render_markdown_and_yml(template_name, content):
    temp = {'page': content}
    # for providing access to collections meta in pages
    config_json_data["site"]["collections"] = collections_metainfo_array
    temp.update({**config_json_data, **temp})
    return Template(open(template_name).read()).render(data=temp)


# for generating collections
def generateCollections():
    all_collections = glob.glob("collections/*/*.md")
    for p in all_collections:
        page = frontmatter.load(p)
        filepath, filename = os.path.split(p)
        page.__setattr__("content", commonmark.commonmark(page.content))

        # for url to the article of that collection
        page["url"] = filepath.replace(
            "collections", "")+"/" + filename.replace(".md", ".html")

        if not os.path.exists("_site"+filepath.replace("collections", "")+"/"):
            os.mkdir("_site"+filepath.replace("collections", "")+"/")
        createFile("_site"+filepath.replace("collections", "")+"/", filename.replace(".md",
                                                                                     ".html"), render_markdown_and_yml("templates/" + page["layout"] + ".html", page))
        print("Generating ",filename.replace(".md", ".html"))                                                                                     
        # For addding this article to collections_metainfo dictionary
        collections_metainfo_array.append(page)
        pass

# for generating the pages which are inside pages folder


def generatePages():
    all_pages = glob.glob("pages/*.md")
    for p in all_pages:
        page = frontmatter.load(p)
        filepath, filename = os.path.split(p)
        page.__setattr__("content", commonmark.commonmark(page.content))
        createFile("_site/", filename.replace(".md", ".html"),
                   render_markdown_and_yml("templates/" + page["layout"] + ".html", page))
        print("Generating ",filename.replace(".md", ".html"))
        pass


def main():
    # Create a new _site directory from scratch.
    if os.path.isdir('_site'):
        shutil.rmtree('_site')
    shutil.copytree('static', '_site')

    # Generate collections
    generateCollections()

    # Generate pages
    generatePages()


if __name__ == '__main__':
    main()
