import turtle

# Khởi tạo màn hình vẽ
screen = turtle.Screen()
screen.title("Vẽ hai sinh vật hoạt hình với tọa độ")
screen.setup(width=720, height=560)
screen.bgcolor("white")

# Khởi tạo bút vẽ
t = turtle.Turtle()
t.speed(800)
t.hideturtle() # Ẩn con rùa để quá trình vẽ mượt mà hơn

def draw_rectangle(x, y, width, height, color):
    """Vẽ một hình chữ nhật với vị trí, kích thước và màu sắc cụ thể."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_parallelogram(x, y, width, height, angle):
    """
    Vẽ một hình bình hành với vị trí, kích thước và góc đã cho.
    (x, y) là tọa độ góc trên bên trái của hình.
    
    Tham số:
    x (int): Tọa độ x của điểm bắt đầu.
    y (int): Tọa độ y của điểm bắt đầu.
    width (int): Chiều rộng của hình bình hành.
    height (int): Chiều cao của hình bình hành.
    angle (int): Góc nghiêng của hình bình hành (tính bằng độ).
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)  # Đặt hướng ban đầu
    
    t.begin_fill()
    
    # Vẽ cạnh đầu tiên
    t.forward(width)
    
    # Quay để vẽ cạnh nghiêng
    t.right(180 - angle)
    
    # Vẽ cạnh nghiêng
    t.forward(height)
    
    # Quay để vẽ cạnh đối diện
    t.right(angle)
    
    # Vẽ cạnh đối diện (bằng chiều rộng)
    t.forward(width)
    
    # Quay để hoàn thành hình
    t.right(180 - angle)
    
    # Vẽ cạnh cuối cùng
    t.forward(height)
    
    t.end_fill()

def draw_triangle(x, y, side, color, angle=0):
    """Vẽ một tam giác đều với vị trí, kích thước và màu sắc cụ thể."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.setheading(angle)
    for _ in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()

def draw_star(x, y, size, color):
    """Vẽ một ngôi sao nhỏ."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_creature(body_x, body_y, body_color, leg_color, spine_color, head_color, eye_color, mouth_color, tail_color, horn_color, is_pink_creature=True):
    """
    Vẽ một sinh vật hoàn chỉnh với các tham số đã cho.
    body_x, body_y là tọa độ góc trên bên trái của thân.
    """
    if is_pink_creature:
        # Vẽ thân (Tọa độ: body_x, body_y)
        body_width = 216
        body_height = 46
        draw_rectangle(body_x, body_y, body_width, body_height, body_color)

        # Vẽ các chân
        leg_width = 20
        leg_height = 44
        leg_dis = 10
        leg_y = body_y - body_height
        leg_x = body_x + body_width / 2 - leg_width * 2 - leg_dis * 1.5
        for i in range(4):
            # Tọa độ chân thứ i: (leg_x, leg_y)
            draw_rectangle(leg_x, leg_y, leg_width, leg_height, leg_color)
            leg_x = leg_x + leg_dis + leg_width

        # Vẽ đầu (Tọa độ: body_x + body_width, body_y)
        head_size = 56
        head_x = body_x + body_width - head_size + 10
        head_y = body_y + head_size
        draw_rectangle(head_x, head_y, head_size, head_size, head_color)

        # Vẽ mắt
        eye_radius = 20
        eye_y = body_y + 30
        
        # Tọa độ mắt trái: (head_x + 20, eye_y)
        t.penup()
        t.goto(head_x + (head_size/2) - 10, eye_y)
        t.pendown()
        t.dot(eye_radius, "white")
        t.goto(head_x + (head_size/2) - 10, eye_y-5)
        t.dot(eye_radius - 8, eye_color)
        
        # Tọa độ mắt phải: (head_x + 50, eye_y)
        t.penup()
        t.goto(head_x + (head_size/2) + 10, eye_y)
        t.pendown()
        t.dot(eye_radius, "white")
        t.goto(head_x + (head_size/2) + 10, eye_y-5)
        t.dot(eye_radius - 8, eye_color)

        # Vẽ miệng là cung tròn cho cả hai sinh vật
        mouth_x = head_x + head_size/4
        mouth_y = head_y - head_size*3/4 + 5
        t.penup()
        t.goto(mouth_x, mouth_y)
        t.pendown()
        t.pensize(2)
        t.color(mouth_color)
        t.setheading(270)
        t.circle(15, 180)
        t.pensize(1)
        
        # Vẽ các chi tiết khác
        # Tọa độ vòng gai lưng: (body_x + 20 + i * 15, body_y)
        for i in range(8):
            draw_triangle(body_x + 20 + i * 15, body_y, 15, spine_color, 0)
        # Tọa độ gai đuôi: (tail_x, tail_y)
        tail_x = body_x
        tail_y = body_y - body_height/2 + 10
        for i in range(4):
            draw_triangle(tail_x - i * 9 - 15, tail_y + 9*i, 13, spine_color, -45)
        # Tọa độ vương miện: (head_x, head_y)
        for i in range(4):
            draw_triangle(head_x + i*14, head_y, 14, "yellow", 0)

    else:
        # Vật bên phải
        # Vẽ thân (Tọa độ: body_x, body_y)
        body_width = 180
        body_height = 40
        draw_rectangle(body_x, body_y, body_width, body_height, body_color)

        # Vẽ các chân
        leg_width = 18
        leg_height = 40
        leg_dis = 10
        leg_y = body_y - body_height
        leg_x = body_x + body_width / 2 - leg_width * 2 - leg_dis * 1.5
        for i in range(4):
            # Tọa độ chân thứ i: (leg_x, leg_y)
            draw_rectangle(leg_x, leg_y, leg_width, leg_height, leg_color)
            leg_x = leg_x + leg_dis + leg_width

        # Vẽ đầu (Tọa độ: body_x + body_width, body_y)
        head_size = 44
        head_x = body_x - 8
        head_y = body_y + head_size
        draw_rectangle(head_x, head_y, head_size, head_size, head_color)

        # Vẽ mắt
        eye_radius = 15
        eye_y = body_y + 25
        
        # Tọa độ mắt trái: (head_x + 20, eye_y)
        t.penup()
        t.goto(head_x + (head_size/2) - 10, eye_y)
        t.pendown()
        t.dot(eye_radius, "white")
        t.goto(head_x + (head_size/2) - 10, eye_y-3)
        t.dot(eye_radius - 6, eye_color)
        
        # Tọa độ mắt phải: (head_x + 50, eye_y)
        t.penup()
        t.goto(head_x + (head_size/2) + 10, eye_y)
        t.pendown()
        t.dot(eye_radius, "white")
        t.goto(head_x + (head_size/2) + 10, eye_y-3)
        t.dot(eye_radius - 6, eye_color)

        # Vẽ miệng là cung tròn cho cả hai sinh vật
        mouth_x = head_x + head_size/4
        mouth_y = head_y - head_size*3/4 + 5
        t.penup()
        t.goto(mouth_x, mouth_y)
        t.pendown()
        t.pensize(2)
        t.color(mouth_color)
        t.setheading(270)
        t.circle(12, 180)
        t.pensize(1)

        # Tọa độ vòng gai lưng: (body_x + 80 + i * 12, body_y)
        for i in range(8):
            draw_triangle(body_x + 80 + i * 12, body_y, 12, spine_color, 0)
        # Tọa độ sừng: (head_x / head_x + head_size - 10, body_y + head_size)
        draw_triangle(head_x, body_y + head_size, 10, horn_color, 0)
        draw_triangle(head_x + head_size - 10, body_y + head_size, 10, horn_color, 0)
        # Tọa độ các ngôi sao: (body_x + 35 + i * 30, body_y - 40)
        for i in range(8):
            draw_star(body_x + 15 + i * 20, body_y - body_height/2, 10, "yellow")
        # Tọa độ đuôi: (body_x + 150, body_y - 40)
        

# Vẽ sinh vật màu hồng
draw_creature(-300, 100, "pink", "hotpink", "deeppink", "pink", "black", "red", "deeppink", None, True)
t.color("black", "pink")
draw_parallelogram(-310, 70, 10, 60, -45)
# Vẽ sinh vật màu xanh
draw_creature(100, 100, "green", "orange", "deeppink", "purple", "blue", "green", "red", "purple", False)
t.color("black", "green")
draw_parallelogram(320, 120, 10, 60, 45)
# Kết thúc chương trình
screen.mainloop()
