from urllib.parse import unquote


class HtmlOutput(object):
    encoding = "utf-8"
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open('output.html', 'w',encoding=self.encoding)

        fout.write("<!DOCTYPE html>")
        fout.write('<html lang="en">')
        fout.write('<head>')
        fout.write('<meta charset="UTF-8">')
        fout.write('<title>Title</title>')
        fout.write('</head>')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        i = 1
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%d</td>" % i)
            # fout.write("<td>%s</td>" % data['url'].encode(self.encoding))
            # fout.write("<td>%s</td>" % data['title'].encode(self.encoding))
            # fout.write("<td>%s</td>" % data['summary'].encode(self.encoding))
            fout.write("<td>%s</td>" % unquote(data['url']))
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            i = i + 1

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

