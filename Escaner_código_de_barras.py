from pyzbar import pyzbar
import cv2

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, image = cap.read()
    if ret:
        codes = pyzbar.decode(image)
        for code in codes:
            (x, y, w, h) = code.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            codeData = code.data.decode("utf-8")
            codeType = code.type
            text = "{} ({})".format(codeData, codeType)
            cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            print("Se encontró {} matrícula: {}".format(codeType, codeData))
        cv2.imshow('Image', image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()