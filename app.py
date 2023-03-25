from flask import *
from telegraph import upload_file

app = Flask(__name__)

@app.route('/upload')
def upload():
	media = request.args.get('media')
	try:
		up = upload_file(media)
		return {'status':'sucess','url':f'https://telegra.ph/{up[0]}'}
	except Exception as e:
		return {'status':'error','reson':str(e)}
	
	
if __name__ == "__main__":
	app.run(debug=True)