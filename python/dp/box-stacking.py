class Box:
    def __init__(self, height, width, depth):
        """
        docstring
        """
        self.height = height
        self.width = width
        self.depth = depth

def sort_boxes(boxes):
    n = len(boxes)
    for i in range(0, n):
        for j in range(i+1, n):
            cmp1 = boxes[i].width * boxes[i].depth
            cmp2 = boxes[j].width * boxes[j].depth
            if(cmp1 <= cmp2):
                boxes[i], boxes[j] = boxes[j], boxes[i]

def rotate_boxes(boxes):
    result = [0 for i in range(3*len(boxes))]
    for ind, val in enumerate(boxes):
        result[ind*3] = Box(val.height, min(val.depth, val.width), max(val.depth, val.width))
        result[ind*3+1] = Box(val.width, min(val.depth, val.height), max(val.depth, val.height))
        result[ind*3+2] = Box(val.depth, min(val.height, val.width), max(val.height, val.width))
    return result

def get_max_height(boxes):
    lis = [x.height for x in boxes]
    for i in range(1, len(boxes)):
        for j in range(0, i):
            if(compare_boxes(boxes[i], boxes[j])):
                lis[i] = max(lis[i], lis[j]+boxes[i].height)
    print(lis)
    return max(lis)

def compare_boxes(box1, box2):
    return box1.depth < box2.depth and box1.width < box2.width

boxes = [Box(4,6,7), Box(1,2,3), Box(4,5,6), Box(10,12,32)]

rotated_boxes = rotate_boxes(boxes)
sort_boxes(rotated_boxes)
#print([(x.height, x.width,x.depth) for x in rotated_boxes])
print("Max height = ",get_max_height(rotated_boxes))