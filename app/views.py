import cv2
from PIL import Image

#Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'


#Route to homepage
@app.route("/", methods = ["GET", "POST"])
def index():
    
    #Execute if request get
    if request.method == "GET":
        return render_template("index.html")
    
    #Execute if request post
    if request.method == "POST":
        
                #Get uploaded image
                file_upload = request.files['file_upload']
                filename = file_upload.filename
                
                # Resize and save uploaded image
                uploaded_image = Image.open(file_upload).resize((250, 160))
                uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

                # Resize and save original Image
                original_image = Image.(os.path.join(app.config['EXISTING_FILE'], 'image.jpg')).resize((250,160))
                original_image.save(os.path.join(app.config['EXISTING_FILE'], 'image.jpg'))
                
                # Read uploaded and original image as an array
                original_image = cv2.imread(os.path.join(app.config['EXISTING_FILE'], 'image.jpg'))
                uploaded_image = cv2.imread(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))
                
                # Convert the images to grayscale
                original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
                uploaded_gray = cv2.cvtColor(uploaded, cv2.COLOR_BGR2GRAY)
                
                # Compute the Structural Similarity Index (SSIM) between the two images, ensuring that the difference image is returned
                (score, diff) = ssim(original_gray, uploaded_gray, full=True)
                diff = (diff * 255).astype("uint8")
                
                
                # Calculate threshlod and contours
                thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
                cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                
                
                # loop over the contours
                for c in cnts:
                    # applying contours on image
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(original, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.rectangle(tampered, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    
                    
                #save all output images
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_original.jpg'), original_image)
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_uploaded.jpg'), uploaded_image)
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_diff.jpg'), diff)
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_thresh.jpg'), thresh)
                
                
                return render_template('index.html', pred=str(round(score*100, 2)) + '%' + 'correct')
            
if __name__=='__main__':
    app.run(debug=True)
                
                



    
    
    