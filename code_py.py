from flask import Flask, render_template, request 
from werkzeug.utils import secure_filename 
#from keras.preprocessing.image import ImageDataGenerator 
import tensorflow as tf 
import numpy as np 
import os
from PIL import Image 
import shutil 
  
upload_folder = 'uploaded/image'
if os.path.exists(upload_folder):
    shutil.rmtree(upload_folder)
os.makedirs(upload_folder)
  
model = tf.keras.models.load_model('Brain tumor classification.h5') 
app = Flask(__name__) 
  
app.config['UPLOAD_FOLDER'] = upload_folder
  
@app.route('/') 
def upload_f(): 
    return render_template('CNN_deploy.html') 
  
def finds(file_path): 
    #img_path = "uploaded"
    image = Image.open(file_path)
    image = image.resize((150,150))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    
    predi = model.predict(image)
    predic = np.argmax(predi)
   
    if predic==0:
        pred = "No tumor"
    elif predic==1:
        pred = "Pituitary tumor"
    elif predic==2:
        pred = "Meningioma tumor"
    elif predic==3:
        pred = "Glioma tumor" 
    return str(pred) 
  
@app.route('/uploader', methods = ['GET', 'POST']) 
def upload_file(): 
    if request.method == 'POST': 
        f = request.files['file'] 
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(file_path) 
        val = finds(file_path) 
        return render_template('pred.html', ss = val) 
  
if __name__ == '__main__': 
    app.run(debug=True)