index = 0
kirby_body = ["#F3BDCC", "#F6E54C", "#B7E1F7", "#EE7C85", "#ACFCAB", "#D5D5D5", "#F1A072", "#010324"]
kirby_shoes = ["#BA4E54", "#D1752B", "#3A84F3", "#C449A2", "#EF9E38", "#767676", "#BF595C", "#806595"]
kirby_blush = ["#EE91BD", "#E3AD3B", "#92BED2", "#EB5796", "#C7BE72", "#B9B9B9", "#E86E75", "#010324"]
kirby_mouth = ["#D5666E", "#D5666E", "#D5666E", "#D5666E", "#D5666E", "#949494", "#D5666E", "#D5666E"]
kirby_eye1 = ["#03102E", "#03102E", "#03102E", "#03102E", "#03102E", "#03102E", "#03102E", "#EEDF4A"]
kirby_eye2 = ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#EEDF4A"]

def setup():
    size(400, 400)
    background("#F4FFFF")

def draw():
    print(mouse_x, mouse_y)
    background(200)
    global index
    kirby(kirby_body[index], kirby_shoes[index], kirby_blush[index], kirby_mouth[index], kirby_eye1[index], kirby_eye2[index])

def mouse_pressed():
    global index
    index = int(random(0, 8))

def kirby_eye(color1, color2):
    rotate(radians(245))
    fill(color1)
    ellipse(0, 0, 65, 26)
    fill(color2)
    ellipse(16, 0, 22, 15)

def kirby_blush_shape(color):
    rotate(radians(330))
    fill(color)
    ellipse(0, 0, 40, 15)

def kirby(body, shoes, blush, mouth, eyes1, eyes2):
    no_stroke()
    
    #kirby shoes
    fill(shoes)
    push_matrix()
    translate(137, 308)
    rotate(radians(25))
    ellipse(0, 0, 90, 110)
    pop_matrix()
    push_matrix()
    translate(308, 262)
    rotate(radians(300))
    ellipse(0, 0, 90, 110)
    pop_matrix()
    
    #kirby body
    fill(body)
    circle(200, 200, 250)
    
    #kirby left arm
    push_matrix()
    translate(82, 160)
    rotate(radians(285))
    ellipse(0, 0, 70, 100)
    pop_matrix()
    
    #kirby right arm
    push_matrix()
    translate(244, 86)
    rotate(radians(30))
    ellipse(0, 0, 70, 100)
    pop_matrix()
    
    #kirby eyes
    push_matrix()
    translate(150, 160)
    kirby_eye(eyes1, eyes2)
    pop_matrix()
    push_matrix()
    translate(200, 140)
    kirby_eye(eyes1, eyes2)
    pop_matrix()
    
    #kirby blush
    push_matrix()
    translate(136, 210)
    kirby_blush_shape(blush)
    pop_matrix()
    push_matrix()
    translate(245, 166)
    kirby_blush_shape(blush)
    pop_matrix()
    
    #kirby mouth
    push_matrix()
    translate(192, 194)
    rotate(radians(335))
    fill(mouth)
    arc(0, 0, 40, 55, radians(0), radians(180))
    pop_matrix()
    
run_sketch()
