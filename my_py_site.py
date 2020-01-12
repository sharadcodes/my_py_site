import os,shutil,glob,json
import frontmatter
import commonmark

from jinja2 import Template

with open('config.json') as json_file:
    config_json_data = json.load(json_file)


#  for creating a file
def createFile(path,name,file_content):
    f = open(path + name, "a")
    f.write(file_content)
    f.close()

# for rendering the templates
def render_markdown_and_yml(template_name, content):
    temp = {'page': content}
    temp.update({**config_json_data , **temp})
    return Template(open(template_name).read()).render(data=temp)


# for generating collections
def generateCollections():
    all_collections = glob.glob("collections/*/*.md")
    for p in all_collections:
        page = frontmatter.load(p)
        filepath, filename = os.path.split(p)
        page.__setattr__("content",commonmark.commonmark(page.content))
        if not os.path.exists("_site"+filepath.replace("collections","")+"/"):
            os.mkdir("_site"+filepath.replace("collections","")+"/")
        createFile("_site"+filepath.replace("collections","")+"/", filename.replace(".md", ".html"), render_markdown_and_yml("templates/" + page["layout"] + ".html", page))
        pass


# for generating the pages which are inside pages folder
def generatePages():
    all_pages = glob.glob("pages/*.md")
    for p in all_pages:
        page = frontmatter.load(p)
        filepath, filename = os.path.split(p)
        page.__setattr__("content",commonmark.commonmark(page.content))
        createFile("_site/", filename.replace(".md", ".html"), render_markdown_and_yml("templates/" + page["layout"] + ".html", page))
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