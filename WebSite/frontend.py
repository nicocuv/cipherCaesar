from flask import Flask, render_template
from WebSite.forms import Message
from WebSite.cipher import gettranslatedmessage, bruteforcetranslation

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['DEBUG'] = True


@app.route('/', methods=('GET', 'POST'))
def index():
    form = Message()
    resultval = ''

    if form.submit.data:
        if form.rAction.data != 'b':
            resultval = gettranslatedmessage(form.rAction.data, str(form.original_text.data), form.key.data)
        else:
            resultval = bruteforcetranslation(form.original_text.data)

    return render_template('index.html', form=form, result=resultval)


if __name__ == "__main__":
    app.run(debug=True)


