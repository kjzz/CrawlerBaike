from urllib import unquote


class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def append_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td style=\"width:20%%;border:1px solid\">%s</td>" % unquote(data['url'].encode('utf-8')))
            fout.write("<td style=\"width:20%%;border:1px solid\">%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td style=\"width:60%%;border:1px solid\">%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

