from subprocess import call
import os.path
import sys


mdfile = sys.argv[1]
mdfile_name, mdfile_ext = os.path.splitext(mdfile)

print mdfile_name

print mdfile_ext

print os.path.splitext(mdfile)

#extensions = ['pdf', 'html', 'tex']



# md2html
print "converting to html"
call(["pandoc", "-o", "./html/" + mdfile_name + ".html", mdfile])

# md2tex
print "converting to tex"
call(["pandoc", "-o", "./latex/" + mdfile_name + ".tex", mdfile])

# md2pdf
print "converting to pdf"
call(["pandoc", mdfile, "-o", "./pdf/" + mdfile_name + ".pdf"])
