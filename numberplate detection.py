import cv2
import numpy as np
from skimage.filters import threshold_local
import tensorflow as tf
from skimage import measure
import imutils


def sort_cont(character_contours):
    """
    To sort contours
    """
    i = 0
    boundingBoxes = [cv2.boundingRect(c) for c in character_contours]
    (character_contours, boundingBoxes) = zip(*sorted(zip(character_contours,
                                                          boundingBoxes),
                                                      key=lambda b: b[1][i],
                                                      reverse=False))
    return character_contours


def segment_chars(plate_img, fixed_width):
    """
    extract Value channel from the HSV format
    of image and apply adaptive thresholding
    to reveal the characters on the license plate
    """
    V = cv2.split(cv2.cvtColor(plate_img, cv2.COLOR_BGR2HSV))[2]
    thresh = cv2.adaptiveThreshold(value, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY,
                                   11, 2)
    thresh = cv2.bitwise_not(thresh)
    # resize the license plate region to
    # a canoncial size
    plate_img = imutils.resize(plate_img, width=fixed_width)
    thresh = imutils.resize(thresh, width=fixed_width)
    bgr_thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    # perform a connected components analysis
    # and initialize the mask to store the locations
    # of the character candidates
    labels = measure.label(thresh, neighbors=8, background=0)
    charCandidates = np.zeros(thresh.shape, dtype='uint8')
    # loop over the unique components
    characters = []
    for label in np.unique(labels):
        # if this is the background label, ignore it
        if label == 0:
            continue
        # otherwise, construct the label mask to display
        # only connected components for the current label,
        # then find contours in the label mask
        labelMask = np.zeros(thresh.shape, dtype='uint8')
        labelMask[labels == label] = 255
        cnts = cv2.findContours(labelMask,
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        # ensure at least one contour was found in the mask
        if len(cnts) > 0:
            # grab the largest contour which corresponds
            # to the component in the mask, then grab the
            # bounding box for the contour
            c = max(cnts, key=cv2.contourArea)
            (boxX, boxY, boxW, boxH) = cv2.boundingRect(c)
            # compute the aspect ratio, solodity, and
            # height ration for the component
            aspectRatio = boxW / float(boxH)
            solidity = cv2.contourArea(c) / float(boxW * boxH)
            heightRatio = boxH / float(plate_img.shape[0])
            # determine if the aspect ratio, solidity,
            # and height of the contour pass the rules
            # tests
            keepAspectRatio = aspectRatio < 1.0
            keepSolidity = solidity > 0.15
            keepHeight = heightRatio > 0.5 and heightRatio < 0.95
            # check to see if the component passes
            # all the tests
            if keepAspectRatio and keepSolidity and keepHeight and boxW > 14:
                # compute the convex hull of the contour
                # and draw it on the character candidates
                # mask
                hull = cv2.convexHull(c)
                cv2.drawContours(charCandidates, [hull], -1, 255, -1)
    _, contours, hier = cv2.findContours(charCandidates,
                                         cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        contours = sort_cont(contours)
        # value to be added to each dimension
        # of the character
        addPixel = 4
        for c in contours:
            (x, y, w, h) = cv2.boundingRect(c)
            if y > addPixel:
                y = y - addPixel
            else:
                y = 0
            if x > addPixel:
                x = x - addPixel
            else:
                x = 0
            temp = bgr_thresh[y:y + h + (addPixel * 2),
                   x:x + w + (addPixel * 2)]
            characters.append(temp)
        return character
    else:
        return None


class PlateFinder:
    def __init__(self):
        # minimum area of the plate
        self.min_area = 4500
        # maximum area of the plate
        self.max_area = 30000
        self.element_structure = cv2.getStructuringElement(
            shape=cv2.MORPH_RECT, ksize=(22, 3))

    def preprocess(self, input_img):
        imgBlurred = cv2.GaussianBlur(input_img, (7, 7), 0)
        # convert to gray
        gray = cv2.cvtColor(imgBlurred, cv2.COLOR_BGR2GRAY)
        # sobelX to get the vertical edges
        sobelx = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
        # otsu's thresholding
        ret2, threshold_img = cv2.threshold(sobelx, 0, 255,
                                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        element = self.element_structure
        morph_n_thresholded_img = threshold_img.copy()
        cv2.morphologyEx(src=threshold_img,
                         op=cv2.MORPH_CLOSE,
                         kernel=element)

