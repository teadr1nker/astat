header = r'''\documentclass{article}
\usepackage[utf8]{inputenc}

\title{title}
\usepackage[utf8x]{inputenc}
\usepackage[russian]{babel}
\usepackage{graphicx}
\usepackage[top=20mm, left=30mm, right=10mm, bottom=20mm, nohead]{geometry}
\usepackage{indentfirst}
\renewcommand{\baselinestretch}{1.50}
\begin{document}
'''
end = '\end{document}'
class tex:
    def printhead():
        print(header)

    def printend():
        print(end)

    def printline(line):
        print(line.replace('_', '\_') + '\\\\')
