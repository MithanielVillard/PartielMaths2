class Transform:
    def __init__(self, posX, posY, posZ, pitch, yaw, roll):

        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll

    def translate(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def rotate(self, dpitch, dyaw, droll):
        self.pitch += dpitch
        self.yaw += dyaw
        self.roll += droll

    def get_position(self):
        return (self.x, self.y, self.z)
    
    def get_rotation(self):
        return (self.pitch, self.raw, self.yaw)
    
    