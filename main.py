from ultralytics import YOLO
import cv2
import easyocr
from bntoen import convert_bengali_to_english

def predict(path):
    model = YOLO('./models/best.pt')
    results = model([path])
    print(results)
    # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        # result.show()  # display to screen
        result.save(filename='./cropped/bounded.jpg')  # save to disk
    return cropNameplates(results)


def cropNameplates(results):
    # Load the original image
    image = "./cropped/bounded.jpg"
    img = cv2.imread(image)

    # Extract bounding boxes
    boxes = results[0].boxes.xyxy.tolist()

    # Iterate through the bounding boxes
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box
        # Crop the object using the bounding box coordinates
        ultralytics_crop_object = img[int(y1):int(y2), int(x1):int(x2)]
        # Save the cropped object as an image
        cv2.imwrite('./cropped/cropped_' + str(i) + '.jpg', ultralytics_crop_object)
        return getTheNumber('./cropped/cropped_' + str(i) + '.jpg')

def getTheNumber(path):
    # Initialize the EasyOCR reader with the 'bn' language (Bengali)
    reader = easyocr.Reader(['bn'])
    # Provide the path to the image containing Bengali text
    image_path = path
    # Read the text from the image
    result = reader.readtext(image_path)
    # print(result)
    # Print the extracted text
    res = []
    for detection in result:
        print('detection:', detection[1])
        res.append(detection[1])
    print('Result From Image: ', res)
    return [convert_bengali_to_english(res[1]), res[0]+'\n'+res[1]]



# getTheNumber()




